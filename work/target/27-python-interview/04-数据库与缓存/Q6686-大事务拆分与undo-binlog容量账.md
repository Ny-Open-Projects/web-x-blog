---
title: [Q6686] 大事务拆分与 undo/binlog 增长容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6686 · 一个事务改 500 万行：undo 膨胀、binlog 洪峰与拆分账

难度：P6 ｜ 标签：容量规划、大事务、批量更新
基线：MySQL 8.0（undo 表空间可 truncate）；PG 15（ vacuum 长事务压制）。

**问**：运营要求把 500 万行的历史订单状态批量更新。同事写了个单事务 `UPDATE ... WHERE ...`，跑起来后磁盘水位 10 分钟涨了 30%、从库延迟飙到 1 小时、期间全库其他更新都变慢。这个"大事务"的容量账里都有哪些增长项？怎么拆？

**答**：**结论**：单事务改 N 行时，账上有四个增长项：① **undo/回滚日志**——为旧行版本全量留副本，500 万行旧值全部挂在一个事务的 undo 链上，事务不提交不能清理；② **binlog**——事务提交才整体写盘，单事务 binlog 可以到数 GB，主从复制的单线程回放（默认）让从库延迟近似等于主库执行时长；③ **锁与 MVCC**——行锁持有到提交，期间所有并发更新要么等锁，要么为一致性读回溯超长 undo 链，全库变慢；④ **内存**——change buffer/redo 刷盘压力集中爆发。容量账的产出物：**每批行数上限 = 允许的从库延迟窗口 ÷ 单行回放耗时**，通常一事务 1000-10000 行、批次间 sleep 让从库追平。

**取舍**：拆分的粒度由两个约束反推：太小的批次（100 行）事务开销占比高、总时长拉长；太大的批次（10 万+行）回到大事务的所有问题。此外 PG 与 MySQL 的差异：PG 的长事务压住的是 **vacuum**（死元组不能回收，表膨胀），所以 PG 上拆分之外还要保证事务别跨"vacuum 周期"；MySQL 则还要 `innodb_max_undo_log_size` 与 truncate 的配合。批处理实现务必用**可恢复游标**（按主键区间推进）而不是 `LIMIT` offset——offset 会越扫越慢。

**实战**：分批更新的账与可恢复实现：

```python
# 大事务拆分的容量账 + 按主键区间的可恢复批处理（标准库演示）
ROWS, BATCH, ROW_REPLAY_MS = 5_000_000, 5_000, 0.02

single_replay_s = ROWS * ROW_REPLAY_MS / 1000
print(f"单事务：从库回放 {single_replay_s/3600:.1f} 小时（单线程复制）")
batch_tx_s = BATCH * ROW_REPLAY_MS / 1000
batches = ROWS // BATCH
gap_s = 2.0  # 批间让从库追平的间隔
wall_h = batches * (batch_tx_s + gap_s) / 3600
lag_s = batch_tx_s  # 单批延迟上界
print(f"拆成 {batches:,} 批：每批 {batch_tx_s:.1f}s，"
      f"从库延迟上界 {lag_s:.0f}s，总时长 {wall_h:.1f}h")

# undo 膨胀账：旧值行均 200B
undo_gb = ROWS * 200 / 1e9
print(f"单事务 undo 峰值 ~{undo_gb:.1f} GB；拆分后只保留单批 "
      f"{BATCH*200/1e6:.0f} MB 在途")

def update_by_range(conn, table, batch=BATCH):
    """按主键区间推进，崩溃后从 last_pk 续跑。"""
    last_pk = 0
    total = 0
    while True:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT id FROM {table} WHERE id > %s ORDER BY id LIMIT %s",
                (last_pk, batch))
            ids = [r[0] for r in cur.fetchall()]
            if not ids:
                break
            cur.execute(
                f"UPDATE {table} SET status=%s WHERE id BETWEEN %s AND %s",
                ("archived", ids[0], ids[-1]))
        conn.commit()          # 每批独立提交
        last_pk = ids[-1]      # 断点：重启从此续跑
        total += len(ids)
        if total % (batch * 20) == 0:
            print(f"进度 {total:,} 行，断点 id={last_pk}")
    return total

class FakeCursor:   # 演示替身，无真实 DB
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def execute(self, *a): pass
    def fetchall(self): return []

class FakeConn:
    def cursor(self): return FakeCursor()
    def commit(self): pass

print("演示 run：", update_by_range(FakeConn(), "orders") or "0 行（演示环境）")
```

**追问 1**：为什么 binlog 单事务大会放大从库延迟？并行复制（MTS）能解决吗？
提示：默认从库单线程回放 relay log，单事务不可拆；MySQL 5.7+ 的 WRITESET 并行复制能把不冲突事务并行回放，但单个大事务内部仍然串行——所以拆事务是唯一解。

**追问 2**：PG 上同样的批量更新，除了拆批还要做什么？
提示：拆批之外控制死元组产生速率（批间给 autovacuum 留窗口）、监控 `pg_stat_activity` 里最长事务；必要时 `VACUUM (ANALYZE)` 收尾并观察表膨胀率。

**追问 3**：批间 sleep 2 秒是怎么定出来的？有没有更动态的做法？
提示：静态值来自"从库回放速率与主库批次速率的配比"；动态做法是监控 `Seconds_Behind_Master`，延迟超阈值就暂停下一批——把从库延迟做成批处理器的反馈信号。

## 背诵要点
1. 大事务四增长项：undo 全量旧值、binlog 提交洪峰、行锁持有时长、redo/内存压力；从库单线程回放使延迟≈主库执行时长。
2. 拆分公式：每批 1000-10000 行，批间给从库追平窗口；用主键区间游标推进保证可恢复，禁 offset 分页。
3. PG 与 MySQL 差异：PG 长事务压 vacuum 致表膨胀，MySQL 超 undo 上限靠 truncate——两者都要防"事务跨清理周期"。

## 复盘追问
1. 这次批量更新前有没有做行数估算与从库延迟推演？复盘后"批量写操作"是否需要走变更工单带容量账？
2. 从库延迟 1 小时期间，读从库的业务看到了什么不一致？读写分离层有没有延迟感知的降级？
