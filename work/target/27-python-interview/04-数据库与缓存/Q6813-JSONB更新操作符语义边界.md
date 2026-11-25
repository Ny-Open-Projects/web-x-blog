---
title: "[Q6813] JSONB 更新操作符：jsonb_set、||、json_patch 的语义边界"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6813 · JSONB 更新操作符：jsonb_set、||、json_patch 的语义边界

难度：P6 ｜ 标签：JSONB、jsonb_set、json_patch、浅合并、深合并、原子读改写、竞态

基线：PG 12+ 的 jsonb_set / || / jsonb_pretty；代码用 SQLite 3.45 的 json 函数（json_set / json_patch / json_remove）复刻语义，全标准库实跑。

**问**：配置表用 JSONB 存嵌套配置，更新时同事用 `doc || '{"retry": {"max": 5}}'`，上线后发现 `backoff` 字段悄悄消失；另一处"读出 JSON、Python 里改完、写回"，并发下更新互相覆盖。JSONB 的更新到底该用哪个操作符？`||` 和 `jsonb_set`、`jsonb_set` 和 `json_patch` 各差在哪？为什么读改写会丢更新？

**答**：

- **结论**：三个操作符三种语义，混用就丢字段。① **`jsonb_set(doc, path, value)`**：单路径精确覆盖，路径不存在时按 `create_missing` 决定是否新建；数组下标越界的行为各家引擎不一致（PG 报错或忽略、SQLite 静默忽略），**更新"没生效"也不报错**是常见事故；② **`||`（拼接操作符）**：**浅合并**——同名顶层键整块替换，嵌套子键不会递归合并，`{"retry":{"max":3,"backoff":1.5}} || {"retry":{"max":5}}` 的结果是 `{"retry":{"max":5}}`，backoff 直接消失；③ **`json_patch(doc, patch)`**：RFC 7396 深合并，嵌套对象逐键合并、`null` 值删除键。而"读出-改完-写回"是两次独立语句，中间有竞态窗口：两个并发事务都读到旧值、各自写回，后写覆盖先写，静默丢更新。
- **取舍**：选型规则一句话——改一个叶子用 jsonb_set，合并多字段且要保留未提及的嵌套键用 json_patch，**永远不要用 `||` 合并含嵌套对象的文档**（顶层标量场景 `||` 才安全）。读改写必须单语句原子完成：`UPDATE ... SET doc = jsonb_set(doc, '$.n', (doc->>'n')::int + 1)` 让"读"发生在 UPDATE 表达式内部，与写同事务无窗口；复杂逻辑（JSON 里做不了的业务判断）才允许应用层读改写，但必须配乐观锁版本号或 `SELECT ... FOR UPDATE`。数组越界、类型不匹配（对数组用对象路径）这些静默失败面，上线前必须用真实样例验证每个 UPDATE 的行为。
- **实战**：一次灰度配置平台事故，两个服务并发更新同一配置文档的不同字段：服务 A 用 `||` 更新顶层 `timeout`（顺带把 `retry` 整块替换成旧值），服务 B 读改写更新 `retry.max`——两小时后 `backoff` 与 A 的新 timeout 同时丢失，故障复盘对不上任何一次"删除"操作。修复：配置更新收敛为"字段级 patch 接口"，内部统一 `json_patch` + 单语句原子写；文档加 `rev` 版本号，`WHERE rev = ?` 乐观锁兜底；CI 里为每个 JSONB 更新语句配行为快照测试（对样例文档跑 UPDATE 断言结果）。之后同类事故归零。

下面用 SQLite 的 JSON 函数复刻三种更新语义，并演示读改写竞态。

```python
# Q6813 JSONB 更新操作符语义: jsonb_set / || / #- 用 sqlite json 函数复刻
import sqlite3, json

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE cfg(id INTEGER PRIMARY KEY, doc TEXT)")
conn.execute("INSERT INTO cfg VALUES(1, ?)",
             ('{"timeout": 30, "retry": {"max": 3, "backoff": 1.5}, "tags": ["a", "b"]}',))

def show(sql, label):
    v = conn.execute(sql).fetchone()[0]
    print(f"[{label}] {v}")
    return v

# [1] jsonb_set: 单路径覆盖, 路径不存在默认创建
v = show("""SELECT json_set(doc, '$.timeout', 60) FROM cfg WHERE id=1""", "1 json_set")
assert '"timeout":60' in v.replace(" ", "")
v = show("""SELECT json_set(doc, '$.rate_limit.qps', 100) FROM cfg WHERE id=1""", "1b 深路径创建")
assert '"rate_limit":{"qps":100}' in v.replace(" ", "")

# [2] || 浅合并 vs json_patch 深合并 (RFC 7396)
# 注: sqlite 没有 PG 的 jsonb || 操作符, 用 dict | dict 复刻其浅合并语义
import json as _json
doc = _json.loads(conn.execute("SELECT doc FROM cfg WHERE id=1").fetchone()[0])
v2 = _json.dumps(doc | {"retry": {"max": 5}})          # PG jsonb || 即浅合并
print(f"[2a || 浅合并(复刻)] {v2}")
assert '"backoff"' not in v2.replace(" ", ""), "|| 同名键整块替换, backoff 丢失"
v = show("""SELECT json_patch(doc, json('{"retry":{"max":5}}')) FROM cfg WHERE id=1""",
         "2b json_patch 深合并")
assert '"max":5' in v.replace(" ", "") and '"backoff":1.5' in v.replace(" ", "")
print("    → 实测 || 把 retry 整块替换(丢 backoff); 深合并必须 json_patch")

# [3] json_remove: 删键与删数组元素
v = show("""SELECT json_remove(doc, '$.tags[0]') FROM cfg WHERE id=1""", "3 删数组首元素")
assert '["b"]' in v.replace(" ", "")

# [4] 数组越界: json_set 到不存在下标 → 静默忽略, 不报错也不生效
v = show("""SELECT json_set(doc, '$.tags[5]', 'x') FROM cfg WHERE id=1""", "4 越界静默忽略")
assert 'null' not in v and '"x"' not in v, "越界下标被静默忽略, 原文档不变"
print("    → 实测 更新'没生效'也没报错: JSON 数组越界各引擎行为不一, 上线前必须用样例验证")

# [5] 原子读改写: 单语句 JSON 表达式, 无竞态窗口
final = conn.execute("""
  UPDATE cfg SET doc = json_set(doc, '$.timeout', json_extract(doc, '$.timeout') + 10)
  WHERE id=1 RETURNING doc
""").fetchone()[0]
assert '"timeout":40' in final.replace(" ", "")
print(f"[5] 单语句原子读改写: timeout 30→40 OK")

# [6] 反例: 应用层读-改-写的竞态窗口 (确定性交错模拟两个并发更新)
def read_modify_write(reader):
    doc = json.loads(conn.execute("SELECT doc FROM cfg WHERE id=1").fetchone()[0])
    doc["timeout"] += 1                       # 读到旧值后本地 +1
    conn.execute("UPDATE cfg SET doc=? WHERE id=1", (json.dumps(doc),))
    return doc["timeout"]

conn.execute("UPDATE cfg SET doc = json_set(doc, '$.timeout', 70) WHERE id=1")
a_read = 70; b_read = 70                       # A、B 几乎同时读到 70
conn.execute("UPDATE cfg SET doc=? WHERE id=1", (json.dumps({"timeout": a_read + 1}),))  # A 写回 71
conn.execute("UPDATE cfg SET doc=? WHERE id=1", (json.dumps({"timeout": b_read + 1}),))  # B 写回 71 (覆盖 A)
after = conn.execute("SELECT json_extract(doc,'$.timeout') FROM cfg WHERE id=1").fetchone()[0]
print(f"[6] 两线程读改写交错: 都读到 70 各 +1, 最终 {after} (应 72, 丢 1 次)")
assert after == 71, "后写覆盖先写, A 的更新丢失"
print("    → 实测 JSONB 读改写必须单语句(json_set 表达式); || 浅合并、json_patch 深合并、数组越界静默忽略各有语义")
```

**追问一**：JSONB 更新的 GIN 索引与写放大有什么关系？—— jsonb 上建 GIN 索引（`jsonb_path_ops` 或默认）后，**任何** jsonb 更新在存储层都是"新文档整体重写"（PG 的 jsonb 是 TOAST 大对象，改一个字节也要重写整个文档），GIN 里被该文档包含的每个键值对都要更新索引项。热点配置行的更新频率 × 文档大小 = 写放大，监控上表现为 WAL 量暴涨。缓解：高频小字段从 JSONB 提升为独立列（生成列可兼顾索引），低频大文档才留 JSONB；GIN 只索引真正用于检索的键（`jsonb_path_ops` 更省）。

**追问二**：`jsonb_set` 只能改一个路径，要一次改多个路径怎么办？嵌套调用有什么坑？—— 多路径用嵌套：`jsonb_set(jsonb_set(doc, '$.a', 1), '$.b', 2)`，从内向外逐层生效。坑有二：一是嵌套两层以上可读性崩塌，改用 `jsonb_strip_nulls(json_patch(doc, '{"a":1,"b":2}'))` 更清晰；二是两个路径修改同一子树时嵌套顺序影响结果（外层 set 会覆盖内层对同一子树的修改），团队规范建议"一个 UPDATE 只表达一次合并意图"，复杂多路径拆成显式的 json_patch 文档。另外 PG 15+ 可用 MERGE 语句表达"读改写"意图，语义比嵌套 set 更直白。

## 背诵要点

- 三种语义：`jsonb_set` 单路径覆盖、`||` 浅合并（嵌套键整块替换会丢字段）、`json_patch` RFC 7396 深合并。
- 读改写必须单语句（UPDATE 表达式内 json_set + json_extract），应用层读改写必配乐观锁版本号。
- JSON 数组越界各引擎行为不一且可能静默不生效；每个 JSONB 更新语句上线前用样例验证。

## 复盘追问

- backoff 字段"消失"但没有任何 DELETE，你怎么定位到 `||` 浅合并？（对配置文档做历史版本 diff，找到替换发生时刻的更新语句；用样例文档在测试库重放该语句复现字段丢失）
- 为什么"读出改完写回"在低并发下也可能丢更新？（窗口大小取决于业务耗时而非并发量；慢请求窗口更长，且两个不同服务的更新没有任何协调，后写覆盖先写）
