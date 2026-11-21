---
title: [Q6503] MVCC 膨胀:autovacuum 调参实例与 dead tuple 监控
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6503 · MVCC 膨胀:autovacuum 调参实例与 dead tuple 监控

> 难度:★★★ | 标签:PostgreSQL, MVCC, 运维

**问**：一张高频更新的订单状态表，半年后查询越来越慢、磁盘涨了 3 倍，VACUUM 也在跑但没回收。这道题考 MVCC 膨胀的机理：autovacuum 为什么"跑了但没用"，你怎么调参和监控？

**答**：结论：PG 的 UPDATE/DELETE 不原地改数据，而是写新元组、旧元组变 dead tuple，靠 autovacuum 回收。膨胀的两大根因：一是 autovacuum 触发阈值按比例（`scale_factor`）算，大表要攒几十万 dead tuple 才启动，永远追不上更新速率；二是长事务/复制槽持住 xmin，vacuum 再勤也不敢回收"新事务还看得见"的旧版本。"VACUUM 在跑但空间没还"多半是回收了行版本但没到 truncate 阶段，或者被长事务卡住。

调参与监控实战：
- 大表把 per-table 比例阈值改绝对值：`ALTER TABLE orders SET (autovacuum_vacuum_scale_factor = 0, autovacuum_vacuum_threshold = 50000);` 高频表再压 `autovacuum_vacuum_cost_delay = 0`（或全局调低 cost limit）让它敢跑快点；`autovacuum_max_workers` 上调前要认清 worker 共享 cost budget。
- 监控三指标：`pg_stat_user_tables` 的 `n_dead_tup / n_live_tup`（死活比 > 0.2 告警）、`last_autovacuum`（长时间未 vacuum 的表点名）、`pg_replication_slots` 的 `active=false` 且 `restart_lsn` 长期不动（泄漏槽，最隐蔽的膨胀元凶）。
- 事故复盘：一张 2 亿行表膨胀到 800GB，根因是某个逻辑复制槽停用未删，xmin 卡了 40 天，全库 vacuum 全部空转。删槽后 vacuum 一夜回收 60%。教训：膨胀排查先查 xmin horizon（`SELECT min(pg_xact_commit_timestamp(xmin)) ...` 或简单看 slot），再谈调参；已膨胀到位的表 autovacuum 只能止血，收缩要 `pg_repack`（在线）或 VACUUM FULL（锁全表，慎用）。

```python
# 基线:Python 3.9+ 标准库 + psycopg(可选);核心巡检逻辑纯标准库可运行
import subprocess

SQL = """
SELECT relname, n_live_tup, n_dead_tup,
       round(n_dead_tup::numeric / greatest(n_live_tup,1), 2) AS dead_ratio,
       last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC LIMIT 5;
"""

def top_bloated_tables(psql_path: str = "psql", dsn: str = "db") -> list[str]:
    """输出死元组占比最高的表;psql 不可用时降级为内置示例数据。"""
    try:
        out = subprocess.run(
            [psql_path, dsn, "-At", "-F", "|", "-c", SQL],
            capture_output=True, text=True, timeout=10, check=True,
        ).stdout.strip().splitlines()
        rows = [line.split("|") for line in out if line]
    except (OSError, subprocess.SubprocessError):
        rows = [["orders", "50000000", "14000000", "0.28", "2026-11-10 03:00"]]  # 降级示例
    alerts = []
    for name, live, dead, ratio, last_av in rows:
        if float(ratio) > 0.2:
            alerts.append(f"[WARN] {name}: dead_ratio={ratio} last_autovacuum={last_av}")
    return alerts or ["OK: 无超阈值膨胀表"]

if __name__ == "__main__":
    for line in top_bloated_tables():
        print(line)
```

**追问**：
- 一层追问：为什么热更新表还推荐fillfactor 调到 70~80？——把页留出空闲空间，让 HOT（Heap-Only Tuple）更新不写新索引项；fillfactor 太满是索引膨胀和 IO 放大的隐藏推手。
- 二层追问：`VACUUM` 与 `VACUUM FULL` 的本质区别？——前者标记空间可复用（不还 OS、不排他锁），后者重写整表换回磁盘但持 ACCESS EXCLUSIVE；生产收缩首选 pg_repack，它用触发器+交换表模拟在线 FULL。
- 三层追问：怎么区分"autovacuum 没跑"和"跑了没用"？——看 `pg_stat_user_tables.last_autovacuum`（没跑→阈值/cost 限制）与 `pg_stat_activity` 里 vacuum 是否长期 active 却无进度（被长事务/锁挡住→查 xmin horizon）。
