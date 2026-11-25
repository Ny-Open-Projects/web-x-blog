---
title: "[Q6722] work_mem 不够：排序落盘为什么让查询慢十倍"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6722 · work_mem 不够：排序落盘为什么让查询慢十倍

难度：P6 ｜ 标签：PostgreSQL、work_mem、外部排序、执行计划

基线：Python 3.12；PostgreSQL 12+ `EXPLAIN (ANALYZE, BUFFERS)` 的 `Sort Method: external merge`；纯 Python 模拟多路归并。

**问**：一条带 `ORDER BY` 的报表 SQL 在测试库 200ms，生产 4s。`EXPLAIN ANALYZE` 里 Sort 节点显示 `Sort Method: external merge  Disk: 184320kB`，而 `work_mem` 是 4MB。多花的内存到底省在哪？为什么调大 `work_mem` 有时反而让整机更慢？

**答**：
- **结论**：`work_mem` 是**每个排序/哈希节点**可用的内存上限，不是每个连接。超出后 PG 把数据分成若干有序的 run 落盘，再做多路归并（`external merge`），代价从 O(n log n) 的内存比较变成"写盘 + 多次顺序读 + 归并比较"。4MB 装不下 180MB 结果，就会产生几十个 run，归并轮数和对临时文件的读放大一起上去。调大 `work_mem` 让排序留在内存里，通常能把 4s 拉回几百毫秒。
- **取舍**：`work_mem` 是**每节点、每连接**分配，一个复杂查询可能有多个 Sort/Hash 节点并发占用；100 个连接 × 64MB 就能把内存打爆，触发 OOM 或 swap，整机反而更慢。正确做法是：全局保持保守（如 4-16MB），对少数报表会话 `SET LOCAL work_mem`；同时优化 SQL 减少排序量（去掉不必要的 `SELECT *`、用索引顺序替代排序、先过滤再排序）。
- **实战**：① 用 `EXPLAIN (ANALYZE, BUFFERS)` 看 `Sort Method` 与 `Disk:` 数值，`external merge` 就是落盘信号；② 观察 `pg_stat_database.temp_bytes` 的增长，它是落盘总量的实例级指标；③ 大报表走只读副本或独立分析库，别和交易库抢内存；④ `work_mem` 调到刚好覆盖常见排序量即可，不要按最大查询配。

```python
"""模拟外部排序：内存批次 -> 多个有序 run -> 多路归并。"""
import heapq
import random


def make_runs(values: list[int], work_mem_rows: int) -> list[list[int]]:
    """每个 run 是能装进 work_mem 的一段，段内排好序后落盘。"""
    runs = []
    for start in range(0, len(values), work_mem_rows):
        chunk = sorted(values[start:start + work_mem_rows])
        runs.append(chunk)              # 真实 PG 这里会写临时文件
    return runs


def merge_runs(runs: list[list[int]]) -> list[int]:
    """多路归并：每取一个元素要比较 k 个 run 的堆顶。"""
    return list(heapq.merge(*runs))


def simulate(rows: int, work_mem_rows: int) -> tuple[int, int, int]:
    values = [random.randrange(10**6) for _ in range(rows)]
    runs = make_runs(values, work_mem_rows)
    merged = merge_runs(runs)
    assert merged == sorted(values)
    # 落盘字节按 8 字节/行估算；归并轮数按 log_k(n) 近似
    spilled_bytes = rows * 8 * 2       # 写一次 + 读一次
    return len(runs), spilled_bytes, len(merged)


if __name__ == "__main__":
    rows = 200_000
    for work_mem_rows in (5_000, 25_000, 200_000):
        runs, spilled, out = simulate(rows, work_mem_rows)
        print(f"work_mem={work_mem_rows:>7} 行 -> run 数={runs:>3}, "
              f"临时读写≈{spilled / 1024 / 1024:.1f}MB, 输出={out}")
    print("结论：run 数随 work_mem 线性下降；装得下时 run=1，完全不落盘")
```

**追问一**：`work_mem` 调大后 `Sort Method` 变成 `quicksort`，但查询没快多少，可能是什么原因？
→ 解析：排序不是瓶颈。要看 `EXPLAIN ANALYZE` 各节点的 `actual time` 占比：如果时间在 Seq Scan 或 Hash Join 的批次上，排序只是最后一环。也可能是结果集被上层 `LIMIT` 截断前已经物化，或者瓶颈在网络传输/客户端反序列化。

**追问二**：为什么 `work_mem` 是按节点分配，而不是按查询或按连接分配？
→ 解析：PG 的执行器是节点流水线，每个 Sort/HashAgg/HashJoin 节点独立申请内存，同一查询里多个节点可能同时持有内存。按节点算是为了简单和并行安全，但也意味着"一个查询的内存占用 ≈ 节点数 × work_mem"，容量规划必须按最坏查询估算，而不是按连接数乘。
