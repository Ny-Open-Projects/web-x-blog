---
title: "[Q6725] random_page_cost=4 在 SSD 上为什么会选错计划"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6725 · random_page_cost=4 在 SSD 上为什么会选错计划

难度：P7 ｜ 标签：PostgreSQL、代价模型、random_page_cost、SSD

基线：Python 3.12；PostgreSQL 12+ 默认 `random_page_cost=4.0`、`seq_page_cost=1.0`；纯 Python 模拟代价比较。

**问**：同一套 SQL，在机械盘时代走索引，迁到全闪存后反而开始走全表扫，慢了三倍。`EXPLAIN` 的代价估算显示 seq scan 更便宜。磁盘明明更快了，为什么优化器反而更保守？

**答**：
- **结论**：PG 的代价模型用 `seq_page_cost=1.0` 表示顺序读一页的相对成本，`random_page_cost=4.0` 表示随机读一页是顺序读的 4 倍——这是**机械盘寻道**的经验值。SSD/NVMe 的随机读延迟远低于此，真实倍率常在 1.1-1.5。默认值会让优化器高估索引扫描的随机 IO 成本，从而偏好顺序全表扫。把 `random_page_cost` 调到接近 1.1-2.0，索引计划才会被正确评估。
- **取舍**：这个参数是**全局/会话级**的粗粒度旋钮，不是精确模型。调太低会让嵌套循环 + 索引回表看起来极便宜，planner 可能选出"百万次随机回表"的计划，在并发下把 IOPS 打满；调太高则大表永远全扫。正确做法是结合 `effective_cache_size`（告诉 planner 有多少页常驻缓存）一起调，并对关键查询用 `pg_hint_plan` 或改写兜底，而不是只改一个数。
- **实战**：① 用 `EXPLAIN (ANALYZE, BUFFERS)` 对比估算代价与实际耗时，估算低但实际慢说明模型失配；② 在只读副本上做 A/B：`SET random_page_cost=1.1` 跑基准，确认计划稳定后再改全局；③ 监控 `pg_stat_statements` 的计划翻转，参数变更后重点看嵌套循环的 `loops`；④ 云盘/本地 NVMe 可设 1.1，网络存储（EBS 级）建议 2.0 左右，别照搬。

```python
"""简化代价模型：比较 seq scan 与 index scan 在不同 random_page_cost 下的选择。"""
from dataclasses import dataclass


@dataclass
class CostModel:
    seq_page_cost: float = 1.0
    random_page_cost: float = 4.0
    cpu_tuple_cost: float = 0.01


def seq_scan_cost(pages: int, rows: int, m: CostModel) -> float:
    return pages * m.seq_page_cost + rows * m.cpu_tuple_cost


def index_scan_cost(index_pages: int, matched_rows: int, heap_pages: int,
                    m: CostModel) -> float:
    # 索引页顺序读 + 匹配行按主键随机回表
    return (index_pages * m.seq_page_cost
            + matched_rows * m.random_page_cost
            + matched_rows * m.cpu_tuple_cost)


def choose(pages: int, rows: int, index_pages: int, matched: int,
           m: CostModel) -> tuple[str, float, float]:
    seq = seq_scan_cost(pages, rows, m)
    idx = index_scan_cost(index_pages, matched, pages, m)
    return ("seq_scan" if seq < idx else "index_scan"), seq, idx


if __name__ == "__main__":
    # 100 万行、每页 100 行 -> 1 万页；命中 1% 即 1 万行
    pages, rows, index_pages, matched = 10_000, 1_000_000, 200, 10_000
    for rpc in (4.0, 2.0, 1.5, 1.1):
        m = CostModel(random_page_cost=rpc)
        plan, seq, idx = choose(pages, rows, index_pages, matched, m)
        print(f"random_page_cost={rpc:>4}  seq={seq:>9.1f}  idx={idx:>9.1f}  -> {plan}")
    print("结论：SSD 上默认 4.0 让索引计划显得贵；调到 1.1-2.0 才接近真实 IO 成本")
```

**追问一**：把 `random_page_cost` 调到 1.1 后，为什么有些查询反而变慢了？
→ 解析：索引计划变便宜后，planner 可能选嵌套循环 + 逐行回表，`loops` 很大时随机 IO 总量反而超过一次顺序全扫；并发下还会把 buffer pool 里其他热页挤掉。SSD 的"单次随机读快"不等于"海量随机读总成本低"，要看总页数和缓存命中率。

**追问二**：`effective_cache_size` 和 `random_page_cost` 是什么关系？
→ 解析：前者告诉 planner "有多少页可能已在 OS/共享缓存里"，影响它估计索引访问中有多少是 cache hit（不计 IO 成本）；后者是未命中时的随机读单价。只调 `random_page_cost` 而不调 `effective_cache_size`，等于假设缓存很小，索引仍然显得贵。两者要一起按机器内存配置。
