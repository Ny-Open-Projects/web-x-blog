---
title: "[Q6718] COUNT(*) 的代价与近似计数"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6718 · COUNT(*) 的代价与近似计数

难度：P6 ｜ 标签：COUNT、索引扫描、采样估算、容量账

基线：Python 3.12；MySQL 8.0 / PostgreSQL 15 概念对照；纯 Python 演示采样估计误差。

**问**：后台列表页要显示"共 238 万条"，运营大屏每隔 10 秒刷新一次总数。直接 `SELECT COUNT(*)` 在千万级表上要 4 秒，加缓存又总是旧值。为什么 InnoDB 的 `COUNT(*)` 不能像 MyISAM 那样 O(1)？近似计数能用在什么场景、误差怎么控？

**答**：
- **结论**：InnoDB 支持 MVCC，不同事务看到的行数不同，**没有一个全局准确的当前行数**可以常数时间返回；`COUNT(*)` 只能扫一个最小的二级索引逐行计数（不回表，但仍要扫全部索引记录）。MyISAM 没有 MVCC，表级元数据直接存行数，所以 O(1)。PostgreSQL 同理，`COUNT(*)` 要全表/全索引扫描，`reltuples` 只是统计估算值。
- **取舍**：精确计数 = 全扫，成本随数据量线性增长；近似计数（采样、统计信息、HyperLogLog/计数表）误差可控但结果会跳。列表页显示"约 238 万"完全可接受；财务对账、分页总页数（影响能不能翻到）必须精确或改用游标分页。缓存计数要接受 TTL 内的旧值。
- **实战**：① 分页改用 keyset/游标，绕开 `COUNT(*)` 和深翻页；② 大屏用统计表/增量计数（写时 +1、删时 -1）并定期对账；③ 需要估算时按页采样（`TABLESAMPLE`/随机主键区间）并给出置信区间；④ 给 `COUNT(*)` 加超时与降级，别让它拖垮连接池。

```python
import random


def estimate_by_sample(population: int, sample_pages: int, page_size: int) -> tuple[int, float]:
    """按页采样：返回估计总数与相对误差（示意，假设页内分布均匀）。"""
    rng = random.Random(7)
    total_sampled = 0
    for _ in range(sample_pages):
        # 每页实际行数围绕 page_size 波动
        total_sampled += max(1, int(rng.gauss(page_size, page_size * 0.05)))
    avg_per_page = total_sampled / sample_pages
    pages = population / page_size
    estimate = int(avg_per_page * pages)
    error = abs(estimate - population) / population
    return estimate, error


if __name__ == "__main__":
    population = 23_800_000
    for pages in (10, 100, 1000):
        est, err = estimate_by_sample(population, pages, 1000)
        print(f"采样 {pages:>4} 页 -> 估计 {est:,} 相对误差 {err:.2%}")
    print("结论：采样页数越多误差越小；展示场景可用，对账场景必须精确")
```

**追问一**：为什么 `COUNT(1)`、`COUNT(*)`、`COUNT(id)` 在 InnoDB 里性能差不多，但语义有差别？
→ 解析：`COUNT(*)` 和 `COUNT(1)` 都统计行数，优化器选最小的二级索引扫描；`COUNT(id)` 统计 `id` 非 NULL 的行数，若 `id` 是主键也等价，但若列可空则语义不同（不统计 NULL）。性能差异主要来自选哪个索引，不来自括号里写什么。

**追问二**：用 Redis 计数器维护总数，删除时减一，为什么会越用越不准？
→ 解析：写入成功但 Redis 更新失败、事务回滚、批量导入绕过应用层、重复消费等都会让计数漂移；Redis 不是事实源。必须定期用数据库精确值校正（对账 job），并把计数当成"可接受的近似"而不是真相。
