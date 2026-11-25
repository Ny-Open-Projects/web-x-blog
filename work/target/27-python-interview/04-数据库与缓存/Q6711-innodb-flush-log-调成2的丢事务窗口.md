---
title: "[Q6711] innodb_flush_log_at_trx_commit 调成 2 的丢事务窗口"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6711 · innodb_flush_log_at_trx_commit 调成 2 的丢事务窗口

难度：P6 ｜ 标签：持久化、redo log、双一配置、事故复盘

基线：Python 3.12；MySQL 8.0 InnoDB；纯 Python 模拟三种刷盘档位的丢失窗口。

**问**：为了扛住大促写入，DBA 把 `innodb_flush_log_at_trx_commit` 从 1 改成 2，QPS 涨了 40%。三个月后机房一路电源抖动，实例重启后财务对账少了 1.8 万笔已返回成功的支付。参数 2 到底承诺了什么？为什么"已经 commit 成功"还会丢？

**答**：
- **结论**：这个参数控制的是 redo log 从 **log buffer → OS page cache → 磁盘** 的刷盘时机，不是"事务是否提交成功"。`=1` 每次 commit 都 `fsync`，提交返回即落盘；`=2` 每次 commit 只 `write()` 到 OS page cache，由后台每秒 `fsync`；`=0` 连 `write` 都交给后台线程每秒做。所以 `=2` 下"commit 成功"只保证数据交给了操作系统，**OS 崩溃/断电**会丢掉最近约 1 秒的已提交事务；`=0` 连 mysqld 进程崩溃都会丢。
- **取舍**：`=1` 是金融级默认，代价是每次提交一次 fsync（NVMe 上约 0.1-1ms，高并发下被组提交摊薄）；`=2` 用"最多丢 1 秒"换掉绝大部分 fsync，适合可重放、可从上游补的数据（日志、埋点、可重算的宽表）；`=0` 只在纯缓存/可全量重建场景考虑。**关键不是选哪个档，而是业务能不能承受对应窗口的丢失并补齐**。
- **实战**：① 支付、账务、订单状态一律 `=1`，并配 `sync_binlog=1`（"双一"），否则 binlog 与 redo 的落盘顺序还会在崩溃恢复时制造主从不一致；② 允许丢窗口的业务必须在上游留**可重放源**（消息队列/本地消息表），重启后按时间窗补；③ 参数变更走容量评审与故障演练，别只压测 QPS；④ 监控 `Innodb_os_log_pending_fsyncs` 与提交延迟，确认 `=1` 下的组提交确实在攒批。

```python
def lost_on_crash(
    flush_mode: int, crash_kind: str, tx_per_sec: int, sec_since_flush: float
) -> int:
    """返回崩溃瞬间可能丢失的已提交事务数（示意模型）。"""
    if crash_kind == "mysqld" and flush_mode in (1, 2):
        return 0                      # mode 2 已 write 到 OS 缓存，进程崩溃不丢
    if flush_mode == 1:
        return 0                      # 双一下 page cache 也已落盘
    # mode 0/2：最近一个后台刷盘周期内的事务还在 log buffer 或 page cache
    return int(tx_per_sec * min(sec_since_flush, 1.0))


if __name__ == "__main__":
    tx_sec, since = 5000, 0.6
    for mode in (0, 1, 2):
        loss_mysqld = lost_on_crash(mode, "mysqld", tx_sec, since)
        loss_os = lost_on_crash(mode, "os", tx_sec, since)
        print(f"mode={mode}: mysqld 崩溃丢 {loss_mysqld} 笔, OS 崩溃丢 {loss_os} 笔")
    print("结论：mode=2 的 commit 成功 ≠ 落盘，断电窗口约 1 秒")
```

**追问一**：既然 `=1` 每次提交都 fsync，为什么高并发下还能有很高 QPS？
→ 解析：靠**组提交（group commit）**：多个并发事务的 redo 在 fsync 前合并成一次系统调用，一次刷盘确认一批事务，fsync 次数被摊薄。所以 `=1` 的吞吐取决于并发度与 `binlog_group_commit_sync_delay` 等参数，而不是"每个事务一次磁盘 IO"。

**追问二**：只把 `innodb_flush_log_at_trx_commit` 设成 1，`sync_binlog` 仍是默认 100，会有什么问题？
→ 解析：redo 已落盘但 binlog 可能还在 page cache，崩溃后 redo 重放出的数据与 binlog 不一致：主库有、从库没有，或基于 binlog 的恢复缺事务。金融链路要"双一"；至少要让 binlog 的落盘策略与业务的可恢复承诺匹配。
