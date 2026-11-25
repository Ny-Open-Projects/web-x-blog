---
title: "[Q6755] 主从延迟追不上：SQL 线程单线程回放的瓶颈与并行复制"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6755 · 主从延迟追不上：SQL 线程单线程回放的瓶颈与并行复制

难度：P7 ｜ 标签：MySQL、主从复制、并行复制 MTS、延迟追赶

基线：Python 3.12；用离散事件模拟单线程回放与按表分片的 MTS（LOGICAL_CLOCK）追赶速度。

**问**：大促后主库写入了 200 万行 binlog，从库 `Seconds_Behind_Master` 顶在 40 分钟不动。IO 线程早已把 relay log 拉完了，卡在 SQL 线程回放。为什么 SQL 线程慢？并行复制（MTS）为什么能加速？开了 `replica_parallel_workers=8` 就一定快 8 倍吗？

**答**：
- **结论**：MySQL 复制分 IO 线程（拉 binlog 到 relay log）与 SQL 线程（回放）。旧架构 SQL 线程**单线程**，主库上并行执行的 8 个事务，到从库变成串行，回放吞吐 ≈ 单事务耗时倒数，写入高峰自然积压。并行复制（5.7 LOGICAL_CLOCK / 8.0 WRITESET）的思路是：同一时钟周期内主库上**不冲突**的事务可以并行回放，冲突的仍串行。加速比取决于事务间的**冲突率**——热点行/同一张表的连续事务并行不了，8 个 worker 可能只跑出 2~3 倍；单表大批量 UPDATE（无主键时 Q6738 更糟）就是典型瓶颈。
- **取舍**：① 临时扩 worker 数只对"冲突率低"的流量有效，写热点集中在少数表时收益趋零；② WRITESET 并行度更高（按行哈希判冲突），但要求主库 `binlog_transaction_dependency_tracking=WRITESET`，且依赖主库 CPU 换吞吐；③ 追赶期可以暂停从库上的读流量与备份任务，把 IO 与 CPU 让给 SQL 线程；④ 治本是把"高峰单点写入"削峰（批量写合并 Q2220、热点行拆分 Q2242）。
- **实战**：① 看积压要看两段：`relay_log` 落地速度（IO 线程）与回放速度（SQL 线程），分段定位；② 大事务是延迟的放大器——200 万行的批量 UPDATE 是一个事务，MTS 也无法拆它，拆批提交（Q896）优先级最高；③ 追赶完成后把 worker 数回调，避免常驻内存开销；④ 从库延迟导致的读旧数据问题（Q897/Q1704）与追赶是两件事，别混为一谈。

```python
"""单线程回放 vs MTS：按冲突率模拟追赶时间。"""
import collections

TX_MS = 12          # 单事务回放耗时
TOTAL_TX = 60_000   # 主库高峰写入的事务数


def simulate(txs: list[tuple[str, ...]], workers: int) -> tuple[float, int]:
    """txs 按主库提交序给出 (表, 行) 集合；同表同轮次必须串行。
    返回 (总耗时 ms, 真实并行轮次数)。"""
    if workers == 1:
        return TX_MS * len(txs), len(txs)
    t, i, rounds = 0.0, 0, 0
    while i < len(txs):
        rounds += 1
        busy_tables: set[str] = set()
        picked = 0
        j = i
        while j < len(txs) and picked < workers:
            tables = set(txs[j])
            if tables & busy_tables:          # 与本轮已选事务冲突 -> 跳过等待
                j += 1
                continue
            busy_tables |= tables
            picked += 1
            j += 1
        t += TX_MS                            # 一轮耗时 = 单事务耗时
        i = j
    return t, rounds


if __name__ == "__main__":
    # 冲突率低的负载：事务分散在 8 张表
    low = [(f"t{k % 8}",) for k in range(TOTAL_TX)]
    # 冲突率高的负载：8 成事务都打同一张热表
    hot = [("hot",) if k % 10 < 8 else (f"t{k % 7}",) for k in range(TOTAL_TX)]

    for name, txs in (("冲突低", low), ("冲突高", hot)):
        base, _ = simulate(txs, 1)
        print(f"[{name}] 单线程: {base/1000/60:.1f} 分钟")
        for w in (4, 8):
            t, r = simulate(txs, w)
            print(f"   workers={w}: {t/1000/60:.1f} 分钟 | 加速 {base/t:.1f}x "
                  f"| 有效轮次 {r:,}")
    print("\n结论：MTS 的加速上限受冲突率钳制；热点单表事务再多 worker 也并不起来")
    print("      追赶顺序：先拆大事务(单事务无法并行) -> 再调 worker -> 最后削峰写入")
```

**追问一**：为什么主库能并行执行、从库却只能按提交序回放？

→ 解析：binlog 里事务是**按提交顺序**写入的，从库必须复现同样的提交序才能保证复制后的数据与主库一致（尤其涉及外键、同行的依赖时）。主库的并行执行由锁与 MVCC 保障正确性，这些信息不会完整传给从库；LOGICAL_CLOCK 只是给"同一时刻可并行的窗口"打标，WRITESET 补充了行级依赖信息，让从库敢于在窗口内并行。并行度本质是"在保持提交序语义的前提下能安全打乱多少"，冲突越多可打乱越少。

**追问二**：`Seconds_Behind_Master` 显示 0 就一定没延迟吗？

→ 解析：不一定。它是从库 SQL 线程与 IO 线程之间的事件时间差，IO 线程拉取受阻时这个值可能失真；主库瞬间没写入时，积压处理完的空窗期也会显示 0。更可靠的观测是用 Q2781 说的"自报延迟有水分"思路：应用侧写入一个带时间戳的心跳表，在从库读出来算真实差值；或对比主从 binlog 位点差。追赶完成与否要用业务可感知的指标（新写入多久能读到）确认，不能只看一个自报数字。
