---
title: "[Q6205] Django JSONField：查询路径翻译与索引的现实"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6205 · Django JSONField：查询路径翻译与索引的现实

难度：P6 ｜ 标签：Django、JSONField、双下划线路径、表达式索引、GIN、查询成本

**问**：`Model.objects.filter(meta__tags__0="python")` 这种双下划线路径是怎么翻译成 SQL 的？为什么 JSONField 查询默认全表扫、加索引比普通列复杂得多？`meta__tags__0` 与 `meta__tags__contains` 的语义差在哪？把关系型数据塞进 JSON 什么时候是合理的？

**答**：
结论：双下划线路径逐段翻译成 JSON 路径表达式：dict 键翻译成 `-> 'key'`（取 JSON 值），list 下标翻译成 `-> 0`，最后一段常用 `->>` 取文本值（或 `#>>` 组合路径）；PostgreSQL 上形如 `meta -> 'tags' ->> 0 = 'python'`。语义细节：`__0` 是"数组第 0 个元素等于 X"，`__contains` 是"JSON 片段包含"（Postgres 的 `@>` 操作符），前者要求精确位置、后者是包含判定，误用会查错集。索引现实：JSON 列默认无索引，任何路径查询都是**全表展开比对**；可加速手段有二——PostgreSQL 的 GIN 索引（`jsonb_path_ops`，支持 `@>` 包含查询）与**表达式索引**（对具体路径 `CREATE INDEX ON t ((meta->'tags'->>0))`，只加速这一条路径）。MySQL 的 JSON 支持更弱：没有 JSON 索引，只能靠生成列（generated column）+ 普通索引。

取舍：a) 高频过滤/JOIN 字段放真实列，JSON 留给"真正无 schema 的扩展属性"；b) 确定要按 JSON 路径过滤时：先估算该路径查询频率，低频直接扫（加 LIMIT 也快），高频建表达式索引（路径写死在索引里，改路径要重建索引）；c) `contains`（GIN 可加速）优先于任意路径等值（不可索引）；d) Django 的 `KeyTextTransform`/`KeyTransform` 可以显式控制 `->>` 与 `->` 的文本/JSON 取值差异（`->>` 返回文本、`->` 返回 JSON，类型比较陷阱常在这）；e) JSON 字段做了结构迁移时（键改名），表达式索引要同步重建，且 `meta->'old_key'` 的旧查询静默返回空——JSON 没有 schema 约束，键改名等于对所有索引路径的静默破坏。

实战：事故形态是"用户偏好存 JSONField，运营后台按 `meta__city` 过滤导出全表用户，MySQL 上无索引全表扫拖垮主库；把 city 提为生成列+索引后查询从 40s 到 80ms，同时把 city 加入写入路径的模型层校验"。下面模拟路径翻译与无索引扫描成本。

```python
import json

ROWS = [
    {"id": 1, "meta": {"tags": ["python", "web"], "vip": True}},
    {"id": 2, "meta": {"tags": ["ops"]}},
    {"id": 3, "meta": {"tags": ["python", "ml"], "vip": True}},
    {"id": 4, "meta": {"note": "no tags key"}},
]


def resolve(doc, path):
    cur = doc
    for part in path.split("__"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        elif isinstance(cur, dict):
            cur = cur[part]
        else:
            raise TypeError("scalar has no children")
    return cur


scans = 0


def filter_json(rows, path, value):
    global scans
    hits = []
    for row in rows:
        scans += 1                      # 无索引：每条全量展开比对
        try:
            if resolve(row["meta"], path) == value:
                hits.append(row["id"])
        except (KeyError, IndexError, TypeError, ValueError):
            pass                        # 结构缺失/路径不通 = 不命中，不报错
    return hits


hits = filter_json(ROWS, "tags__0", "python")
print("[1] data__tags__0 = 'python' 命中:", hits)
print("[2] 无索引扫描次数:", scans, "/", len(ROWS), "（每行都要展开 JSON）")

print("[3] SQL 翻译: meta__tags__0 -> meta->'tags'->>0",
      "（Postgres 表达式索引 CREATE INDEX ON t ((meta->'tags'->>0))）")
print("[4] 有表达式索引后命中 rows 直取，扫描次数: 1")
```

**追问一**：`->` 与 `->>` 的差异会在什么查询里制造静默 bug？—— `->` 返回 JSON 类型（`'30'` 的 JSON 值是 JSON 字符串），`->>` 返回文本。用 `meta__age__gt=30` 时 Django 会把值参数化为 JSON 比较还是文本比较取决于最后一层 transform：若误取 JSON 字符串与数字比较，PostgreSQL 抛类型错误或永假；若数字存成 JSON 字符串，`->>`后 `'30'` 与整数 30 比较不等——查出来 0 行且无报错。排障方法是 `queryset.query` 打印 SQL 看最后一个 transform 是 `->` 还是 `->>`，写入侧用模型层校验保证类型一致。

**追问二**：JSONField 什么场景是合理选型、什么场景是坑？—— 合理：真正的扩展属性（第三方接入的原始 payload 存档、稀疏可选字段、版本化配置快照），特征是"读整块、偶尔按 contains 找、schema 由外部决定"。坑：被当成"懒得建表"的垃圾桶——高频过滤列、多表关联主键、需要强约束的状态字段塞进 JSON，会同时失去索引、外键约束、ORM 关联与迁移保护。判据一句话：**写进 JSON 的数据要不要被高效查询或约束？要 → 提列；只读存档 → JSON。**

## 背诵要点
- 双下划线路径翻译为 JSON 路径：键 `->`、下标 `->0`、末层 `->>`取文本；`__0` 精确位置 vs `__contains` 包含判定。
- JSON 列默认全表扫；加速靠 GIN（`@>` contains）或表达式索引（路径写死，改路径需重建）。
- `->` 返回 JSON 值、`->>` 返回文本，类型比较陷阱导致静默 0 行；高频过滤字段提真实列。

## 复盘追问
- meta__age__gt=30 返回 0 行且不报错，先查什么？（-> 与 ->> 的取值差异，JSON 字符串与数字比较）
- 运营按 JSON 字段导出全表拖垮主库，怎么落地修复？（高频字段提列/生成列+索引，写入侧加校验）
