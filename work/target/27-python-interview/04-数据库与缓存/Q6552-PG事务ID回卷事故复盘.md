---
title: [Q6552] PG 事务 ID 回卷事故：xid 冻结与长事务卡死
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6552 · PG 事务 ID 回卷事故：xid 冻结与长事务卡死

难度：P7 | 标签：PostgreSQL、XID 回卷、autovacuum、事故复盘

**问**：一条"数据库将在 1000 万个事务后拒绝写入"的告警是什么意思？为什么一个三天没提交的事务能把整个库逼向停写？anti-wraparound vacuum 到底在做什么？

**答**：
- **结论**：PG 的事务 ID 是 32 位环，写操作都会消耗 xid，用完即回卷——回卷后老数据会被"当成未来的事务"产生数据错乱，所以 PG 选择在逼近时宁可停写。解法是冻结（freeze）：autovacuum 把足够老的行 xmin 改写为 FrozenXID，这些行永久退出比较。关键账目：回卷风险由"最老未冻结行的 xmin"到下一个 xid 的环形距离决定，不是总消耗量——冻结掉最老的一张表，预算立刻恢复。
- **取舍**：freeze 是写放大（要改写整行），autovacuum 会主动提速，代价是 IO 争抢；调大 autovacuum_freeze_max_age 只是把危险推后。真正的敌人是长事务：它把冻结线（horizon）钉死在自己开启的位置，horizon 之后的行谁也冻不了，预算持续下降直到 kill 长事务。
- **实战**：巡检三件事：① `pg_postmaster_start_time` 之外看 `age(datfrozenxid)` 最大的库；② `pg_stat_activity` 里 duration 最高的未提交事务（这也是长事务锁雪崩的同一个元凶）；③ 备表均匀写入——单表超大时 freeze 一次要扫全表，拆表让冻结增量进行。

```python
"""PostgreSQL 事务 ID 回卷：回卷空间由「最老未冻结 xmin」决定，而非总消耗量。"""
XID_LIMIT = 2**32          # xid 是 32 位环，超过 2^32 即回卷
FROZEN = XID_LIMIT - 1000  # FrozenTransactionId 标记（冻结行不再参与比较）

# 表 -> 该表最老未冻结行的 xmin（按提交顺序编号）
tables = {
    "orders_2019": 2_700_000_000,
    "orders_2023": 3_100_000_000,
    "orders_today": 3_219_900_000,
    "audit_log": 3_219_999_500,
}
next_xid = 3_220_000_000

def wrap_distance(older: int, newer: int) -> int:
    """环形距离：older 在 newer 之前多少个事务（处理回绕）。"""
    return (newer - older) % XID_LIMIT

def remaining_budget(unfrozen: dict) -> int:
    oldest = min(unfrozen.values())
    return wrap_distance(oldest, next_xid)

budget = remaining_budget(tables)
print(f"剩余回卷空间 {budget / 1e6:.1f} 百万事务，"
      f"瓶颈在 {min(tables, key=tables.get)}")

# anti-wraparound vacuum 冻结最老的表：xmin 改写为 FrozenXID，预算立即恢复
recovered = dict(tables)
victim = min(recovered, key=recovered.get)
recovered.pop(victim)
budget2 = remaining_budget(recovered)
print(f"冻结 {victim} 后剩余空间恢复到 {budget2 / 1e6:.1f} 百万事务")

# 长事务把冻结线（horizon）钉死：vacuum 只能冻结 xmin 早于 horizon 的行
stale_backend_xmin = 2_750_000_000    # 一个挂了三天未提交的事务
horizon = stale_backend_xmin
freezable = {t: x for t, x in recovered.items() if x < horizon}
if freezable:
    for t in freezable:
        recovered.pop(t)
    print(f"horizon 之前可冻结 {list(freezable)}，预算推进到 "
          f"{remaining_budget(recovered) / 1e6:.1f} 百万事务")
else:
    stuck = remaining_budget(recovered)
    print(f"horizon={horizon} 之前的行已全部冻结；最老未冻结行（"
          f"{min(recovered, key=recovered.get)}）在 horizon 之后，冻不了")
    print(f"预算卡死在 {stuck / 1e6:.1f} 百万事务并随 next_xid 持续下降——kill 长事务立刻解锁")

# 紧迫度分级：剩余 < 2 亿事务开始告警，< 1000 万事务 PG 拒绝新写入
remain = remaining_budget(recovered)
level = "正常" if remain >= 200_000_000 else ("告警" if remain >= 10_000_000 else "拒绝写入")
print(f"剩余 {remain / 1e6:.1f} 百万事务 -> {level}"
      "；跌破 1000 万 PG 将强制单用户模式 vacuum")
```

**追问链**：
1. 追问一层：为什么是"写操作"消耗 xid，只读查询不算？——只有写入（含删除/更新）才分配真实 xid 并留下 xmin；纯 SELECT 不占回卷预算，所以"读多写少"的库回卷风险天然低。
2. 追问二层：replication slot 为什么也会加剧回卷？——延迟订阅者让 vacuum 不能清理死元组、同样推迟冻结推进；这和复制槽把 pg_wal 撑爆是同一族问题：slot 是"我还要旧数据"的承诺，承诺不收回，清理就无法前进。

**背诵要点**：
1. xid 是 32 位环；冻结（FrozenXID）让老行退出比较，回卷风险看最老未冻结 xmin。
2. 长事务钉死 horizon，vacuum 冻结无法推进，预算持续下降直至停写。
3. 巡检三件套：age(datfrozenxid)、超长未提交事务、超大单表的冻结成本。

**复盘追问**：
1. 库拒绝写入、日志刷 "wraparound" 告警，第一动作是什么？（找 `pg_stat_activity` 里最老的未提交事务并 kill，让 horizon 前进，随后立刻手动触发 anti-wraparound vacuum）
2. 为什么"把 autovacuum 关掉降负载"在这个场景是自毁？（freeze 是唯一的预算恢复手段，关掉 autovacuum 等于坐等回卷，宁可限流也要让 freeze 跑完）
