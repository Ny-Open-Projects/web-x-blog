---
title: "[Q6794] GTID 换主后的位点恢复：relay log 重放如何做到不丢不重"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6794 · GTID 换主后的位点恢复：relay log 重放如何做到不丢不重

难度：P7 ｜ 标签：MySQL、GTID、主从切换、relay log、auto_position、幂等重放、RPO

基线：MySQL 5.7/8.0 异步与半同步复制；Python 3.12 用 GTID 集合差分与幂等应用模拟换主恢复，全标准库实跑。

**问**：主库在凌晨宕机，三台从库的 `gtid_executed` 分别是 1-100、1-108、1-110（主库执行到 110）。运维想"挑延迟最小的"直接提升，这一步错在哪？提升之后其余从库怎么接回去——`MASTER_AUTO_POSITION=1` 到底补的是哪一段？relay log 里没应用完的事务在重启后重放，会不会把同一笔业务做两遍？

**答**：

- **结论**：GTID 把"复制位点"从文件偏移换成了**事务集合**，于是换主变成三步集合运算。第一步**选主**：不是选"延迟最小"的，而是选 `gtid_executed` **最全**的那台（110 那台）；延迟是时间维度，集合才是数据维度，两者不一致时以集合为准。第二步**追平**：确认所有候选的 `gtid_executed` 差集，能追的用 `WAIT_FOR_EXECUTED_GTID_SET` 等到追平再切，追不平就明确记录 RPO（这几个事务永久丢失），而不是假装没丢。第三步**接回**：从库设 `MASTER_AUTO_POSITION=1`，它把 `主库.gtid_executed - 自己.gtid_executed` 作为要拉取的集合，只补差集。**"不重"来自 SQL 线程在应用每个事务前检查该 GTID 是否已在 `gtid_executed` 里**——在就跳过，所以 relay log 重放、重复拉取、切主后重连都是幂等的（幂等粒度是事务，不是行）。
- **取舍**：`relay_log_recovery=ON` 在崩溃重启时**丢弃未应用的 relay log，按已执行集合重新向主库要**——用一次网络重传换"绝不重复应用"的确定性，绝大多数生产环境应开。半同步（`AFTER_SYNC`）能把 RPO 压到 0，代价是提交延迟多一个网络往返、且超时会静默退化为异步（要监控 `Rpl_semi_sync_master_status`）。组复制（MGR）把选主与追平做成共识协议，代价是多数派可用性与流控复杂度。没有一种方案能同时给"零丢失 + 任意节点可写 + 低延迟"，换主流程必须把"能丢多少"写成明确参数。
- **实战**：一次机房断电后，运维按"延迟最小"提升了 1-108 那台，丢了 2 笔已对用户返回成功的订单，第二天对账才发现。复盘改了切换手册：① 切换前脚本强制输出三台的 `gtid_executed` 并取**并集上界**，选包含最多事务的节点；② 对仍存活的旧主执行 `WAIT_FOR_EXECUTED_GTID_SET`，超时则记录差集并告警；③ 提升后对新主执行 `RESET MASTER` 前必须先 `SET GLOBAL gtid_purged` 为执行集合，否则新主 binlog 的起点与集合对不上，挂上来的从库会报 "The slave is connecting using CHANGE MASTER TO MASTER_AUTO_POSITION = 1, but the master has purged binary logs"。

下面用集合差分 + 幂等应用把"补差集"和"重放不重"跑一遍。

```python
# GTID 换主: 集合差分补缺 + 重复重放的幂等性
class Replica:
    def __init__(self, name, executed):
        self.name = name
        self.executed = set(executed)
        self.rows = {g: f"row-{g}" for g in executed}
        self.applied = 0
        self.skipped = 0

    def apply(self, events):
        """events: [(gtid, payload)]; 已在 executed 中的直接跳过。"""
        for gid, payload in events:
            if gid in self.executed:
                self.skipped += 1
                continue
            self.executed.add(gid)
            self.rows[gid] = payload
            self.applied += 1


PRIMARY_EVENTS = [(g, f"row-{g}") for g in range(1, 111)]
A = Replica("old-primary", range(1, 111))
B = Replica("replica-lagging", range(1, 101))
C = Replica("replica-mid", range(1, 109))
D = Replica("replica-full", range(1, 111))

print("[1] 选主看集合不看延迟:")
for r in (B, C, D):
    print(f"    {r.name}: executed 上界 {max(r.executed)}, 缺 {sorted(A.executed - r.executed)}")
best = max((B, C, D), key=lambda r: len(r.executed))
print(f"    → 实测 应提升 {best.name}(集合最全), 而不是延迟最小的 B")
assert best is D and len(D.executed) == 110

# B 挂到新主 D: auto_position 只补差集
missing = sorted(D.executed - B.executed)
print(f"[2] B 接回 D, auto_position 计算差集: {missing}")
B.apply([(g, f"row-{g}") for g in missing])
print(f"    B 后: executed={len(B.executed)}, rows={len(B.rows)}, applied={B.applied}, skipped={B.skipped}")
assert B.executed == D.executed and len(B.rows) == 110

# relay log 崩溃重放: 同一批事务再来一次
before = len(B.rows)
B.apply(PRIMARY_EVENTS)
print(f"[3] relay log 全量重放 110 条: rows {before} -> {len(B.rows)}, "
      f"applied={B.applied}, skipped={B.skipped}")
assert len(B.rows) == 110, "重放不得产生重复行"
assert B.skipped >= 100
print("    → 实测 GTID 已存在即跳过, 重放幂等, 不重")

# 异步复制下的 RPO: 旧主已 ack 但 B 未收到的那段, 提升 B 就真丢了
LOST = sorted(A.executed - C.executed)
print(f"[4] 若误提升 C: 永久丢失 {LOST} 共 {len(LOST)} 笔, rows={len(C.rows)}")
assert len(LOST) == 2 and len(C.rows) == 108
print("    → 实测 不丢的前提是选集合最全的节点 + 追平, 不是'看起来延迟小'")
```

**追问一**：GTID 模式下为什么 `sql_slave_skip_counter` 用不了？要跳过一条坏事务怎么办？—— 位点复制里"跳过 N 个事件"有明确含义；GTID 复制里事务是原子的集合元素，跳事件会让 GTID 集合出现空洞，后续 `auto_position` 计算的差集永远补不上。正确做法是**注入空事务**：`SET GTID_NEXT='uuid:n'; BEGIN; COMMIT; SET GTID_NEXT='AUTOMATIC';`——把这个 GTID 标记为"已执行但无副作用"，集合连续了，但**数据与主库永久不一致**。所以它只适用于"这条事务在本库确实无意义"（比如只改了一个本库不存在的表），跳过写事务必须配合对账与补数，不能当成常规运维手段。

**追问二**：`RESET MASTER` 在切换时为什么危险？什么时候必须做？—— `RESET MASTER` 会清空本机 binlog 并把 `gtid_executed` 重置为空（除非先设 `gtid_purged`），如果在一台还有业务写入的节点上执行，等于把"我已经执行过哪些事务"的记忆抹掉，从库挂上来会重复拉取、重复应用或直接报 GTID 缺口。它只应出现在"把副本提升为主库、且已经用 `SET GLOBAL gtid_purged` 把执行集合写回"的受控步骤里，且执行前必须确认该节点不再作为任何人的从库。更稳的做法是压根不用 `RESET MASTER`，用 `gtid_purged` + 新的 server_uuid 规划好 binlog 起点。

## 背诵要点

- 换主选 `gtid_executed` 最全的节点，不是延迟最小的；差集 = 新主集合 − 本机集合，`MASTER_AUTO_POSITION=1` 只补差集。
- 不重的机制是 SQL 线程应用前查 `gtid_executed`，已存在就跳过；幂等粒度是事务，relay log 重放天然安全。
- `relay_log_recovery=ON` 丢弃未应用 relay log 重新拉取；`sql_slave_skip_counter` 在 GTID 下无效，只能注入空事务且会造成永久不一致。

## 复盘追问

- 三台从库延迟分别是 0.1s、0.5s、2s，为什么不能挑 0.1s 的那台提升？（延迟是时间，`gtid_executed` 是数据；落后 2s 的可能是网络抖但集合更全，必须比集合）
- relay log 里还有 500 个未应用事务时崩溃重启，为什么不会重复写业务表？（`relay_log_recovery` 丢弃重拉 + GTID 已执行集合检查；两道保险各自独立生效）
