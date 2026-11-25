---
title: "[Q6820] updated_at 维护契约与增量同步漏行：谁负责刷时间戳"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6820 · updated_at 维护契约与增量同步漏行：谁负责刷时间戳

难度：P6 ｜ 标签：updated_at、增量同步、ON UPDATE、触发器、ORM 钩子、时区口径、批量更新尖峰

基线：SQLite 3.45（触发器模拟 MySQL ON UPDATE CURRENT_TIMESTAMP）；实测漏刷导致的增量拉取漏行与时区口径事故，全标准库实跑。

**问**：数仓按 `updated_at > 上次水位` 从业务库增量拉数据，运营反馈"改了状态但报表就是看不到"。排查发现那条 UPDATE 语句压根没 set updated_at——它依赖"应用框架会自动刷"的传说。updated_at 到底该谁维护？ON UPDATE、触发器、ORM 钩子三种机制怎么选？为什么批量 UPDATE 会让增量同步流量尖峰？还有哪些口径坑？

**答**：

- **结论**：增量同步的正确性完全建立在一条契约上：**任何行变更必刷 updated_at**。这条契约不能靠"开发者记得写"（应用层 UPDATE 漏 set 就是漏单，实测：漏刷的行在 `WHERE updated_at > 水位` 拉取结果里消失），必须由机制强制，三选一：① **DB 默认值 `ON UPDATE CURRENT_TIMESTAMP`**（MySQL）——DB 引擎保证，任何路径的 UPDATE 都刷，最可靠；② **触发器**（MySQL 手写 / PG 触发器 / SQLite 触发器模拟）——同样 DB 级保证，灵活但要管理触发器本身的演进；③ **ORM 钩子/中间件**（SQLAlchemy `onupdate`、Django auto_now）——应用内所有走 ORM 的写都被覆盖，但**绕过 ORM 的脚本/直连 SQL 全部漏刷**，是三选一里最弱的。时区是第二杀手：`datetime('now')` 是 UTC、本地时间是 +8，水位线与写入值口径混用，增量要么全漏要么全重拉。
- **取舍**：三种机制的取舍本质是"覆盖面 vs 演进成本"。DB 级机制（①②）覆盖面 100%，代价是行为对应用不可见（测试时要注意 updated_at 自动变化）且跨库迁移要逐库重建；ORM 钩子演进最顺但覆盖面 = ORM 使用率。决策规则：**表上有增量同步/审计需求的，用 DB 级机制**（①优先，PG 用触发器）；ORM 钩子作为辅助打点。批量 UPDATE 还有第二个坑：5 万行同时被触发器刷新，updated_at 挤在同一秒，增量水位跳变，下游一次性拉 5 万行形成流量尖峰——水位推进要配合"分批更新 + 批间 sleep"，或下游按 updated_at 分段拉取。还有 DELETE 语义：updated_at 拉不到已删除的行，增量同步要配软删除（deleted 标记 + updated_at）或单独的删除流。
- **实战**：一次报表漏数事故：运营在管理后台改了订单状态（该接口是老代码，原生 SQL 直写，没刷 updated_at），数仓水位后的拉取永远跳过它，次日报表对不上账。修复链：订单表 updated_at 加 `ON UPDATE CURRENT_TIMESTAMP`（存量行为审计后统一刷一次）；全库扫描直写 SQL 的路径，收编进 ORM；水位拉取加对账——按主键范围校验"最大 id 处的 updated_at 不早于水位"，不一致即告警；时区统一 UTC 存储、下游展示转换。上线后漏单归零。规范沉淀：**凡是要被增量消费的表，updated_at 是契约字段，建表评审必须回答"谁保证它被刷"**。

下面用 SQLite 触发器模拟 ON UPDATE，实测漏行、修复与批量尖峰。

```python
# Q6820 updated_at 维护契约与增量同步漏行: ON UPDATE / 触发器 / 应用层
import sqlite3

def make_db(with_trigger):
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE orders(
        id INTEGER PRIMARY KEY, status TEXT, updated_at TEXT)""")
    if with_trigger:                       # 模拟 MySQL ON UPDATE CURRENT_TIMESTAMP
        conn.execute("""CREATE TRIGGER touch_updated_at AFTER UPDATE ON orders
                        BEGIN
                          UPDATE orders SET updated_at = datetime('now','localtime')
                          WHERE id = NEW.id;
                        END""")
    conn.executemany("INSERT INTO orders VALUES(?, ?, ?)",
                     [(1, "new", "2026-11-25 09:00:00"),
                      (2, "new", "2026-11-25 09:00:00")])
    return conn

# [1] 应用层 UPDATE 漏刷 updated_at → 增量同步按 updated_at 拉取会漏行
conn = make_db(False)
conn.execute("UPDATE orders SET status='paid' WHERE id=1")   # 忘记 set updated_at
cursor_ts = "2026-11-25 09:00:00"
pulled = conn.execute("SELECT id FROM orders WHERE updated_at > ?",
                      (cursor_ts,)).fetchall()
print(f"[1] 漏刷 updated_at: 行 1 已变更但增量拉取结果 {pulled} → 漏单")
assert pulled == []

# [2] 触发器自动维护: 任何 UPDATE 都刷新 updated_at, 增量不再漏
conn_t = make_db(True)
conn_t.execute("UPDATE orders SET status='paid' WHERE id=1")
row = conn_t.execute("SELECT status, updated_at FROM orders WHERE id=1").fetchone()
pulled = conn_t.execute("SELECT id FROM orders WHERE updated_at > ?",
                        (cursor_ts,)).fetchall()
print(f"[2] 触发器维护: status={row[0]}, updated_at={row[1]}; 增量拉取 {pulled}")
assert pulled == [(1,)]

# [3] 批量 UPDATE 的副作用: 触发器逐行触发, 大批量会把 updated_at 打成同一时刻簇
conn_t.executemany("INSERT INTO orders VALUES(?, ?, ?)",
                   [(i, "new", "2026-11-25 09:00:00") for i in range(3, 503)])
conn_t.execute("UPDATE orders SET status='paid' WHERE id > 2")   # 500 行
cluster = conn_t.execute(
    "SELECT count(*) FROM orders WHERE updated_at > '2026-11-25 09:00:00'").fetchone()[0]
print(f"[3] 批量 UPDATE 触发器: {cluster} 行 updated_at 同时刷新 → 同步流量尖峰")
assert cluster == 501

# [4] 应用层约定 vs 数据库兜底: 应用层写法必须 lint 级强制
def app_update(conn, oid, status, set_ts=True):
    sql = "UPDATE orders SET status=?"
    args = [status]
    if set_ts:      # 口径必须与 cursor 一致: 混用 UTC('now')与本地是增量同步第二杀手
        sql += ", updated_at=datetime('now','localtime')"
    sql += " WHERE id=?"
    args.append(oid)
    return conn.execute(sql, args).rowcount

conn4 = make_db(False)
conn4.executemany("INSERT INTO orders VALUES(?, ?, ?)",
                  [(9, "new", "2026-11-25 09:00:00")])
app_update(conn4, 9, "paid", set_ts=True)
pulled = conn4.execute("SELECT id FROM orders WHERE updated_at > ?",
                       (cursor_ts,)).fetchall()
print(f"[4] 应用层显式刷新: 增量拉取 {pulled}; 契约靠 review 不可靠, 靠 ORM 钩子/DB 默认值兜底")
assert pulled == [(9,)]
print("    → 实测 增量同步的正确性完全依赖 updated_at 写入纪律: 应用漏刷必漏单, 兜底三选一 ON UPDATE/触发器/ORM 钩子")
```

**追问一**：为什么 updated_at 做水位线天生不可靠，binlog 订阅好在哪里？—— updated_at 水位有三个先天缺陷：① 依赖写入纪律（本卡主旨）；② 同一秒内多行变更无法保证拉取顺序与提交顺序一致（水位推进可能跳过并发写）；③ 删除行永远拉不到。binlog 订阅（CDC）在存储层捕获变更，不依赖应用契约、含 DELETE、顺序就是提交顺序——所以严肃数仓同步都走 CDC（Debezium/canal），updated_at 水位只适合低要求场景或兜底对账。但 CDC 也有代价：部署与位点管理、DDL 演进处理、全量初始化。两者常组合：CDC 做主通道，updated_at 做对账校验。

**追问二**：水位线推进的"恰好一次"怎么保证？拉取到一半崩溃怎么办？—— 水位拉取的标准模式是"拉取快照 → 处理 → 一起原子提交新水位"：把"处理结果落库/发送"与"水位推进"放进同一事务（或本地消息表），崩溃后重放同一水位区间（下游幂等消费 upsert）。如果下游不幂等，就要用两阶段水位（新水位先写成 pending，处理完才转正式）。另一个细节：水位用 `>=` 而不是 `>` 边界会重复拉一批（幂等消费吸收），用 `>` 则可能漏同秒行——配合主键复合水位 `(updated_at, id)` 可以把边界钉死，这也是 Q2749 复合游标分页的同款原理。

## 背诵要点

- 契约：任何行变更必刷 updated_at，靠"开发者记得"必漏单；强制三选一：ON UPDATE（MySQL 首选）> 触发器 > ORM 钩子（绕过 ORM 全漏）。
- 两个口径杀手：时区混用（UTC vs 本地）、批量 UPDATE 把 updated_at 打成同一秒簇（下游流量尖峰）。
- updated_at 水位拉不到 DELETE、不保提交顺序；严肃同步走 CDC，updated_at 做对账；水位与处理结果要原子提交。

## 复盘追问

- "改了状态但报表看不到"，你的排查顺序？（先确认该行的 updated_at 是否随 UPDATE 变化；再对账水位区间 SQL 复现；最后追写入路径是否绕过 ORM——三层分别对应契约、消费端、写入端）
- 为什么管理后台的老接口最容易漏刷 updated_at？（老代码直写 SQL 绕过 ORM 钩子；且该接口写于"契约"建立之前——所以契约建立时要做一次全库写入路径审计）
