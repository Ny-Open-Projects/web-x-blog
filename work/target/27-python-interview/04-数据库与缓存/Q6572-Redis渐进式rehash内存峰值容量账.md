---
title: [Q6572] Redis 渐进式 rehash 的内存峰值容量账
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6572 · Redis 渐进式 rehash 的内存峰值容量账

难度：P7 ｜ 标签：Redis / 内存容量规划 / dict 结构

**问**：一个有 5 亿 key 的 Redis 实例，内存水位 70%，运维说还有余量。为什么一次大扩容（比如从 4 亿写入涨到 5 亿）可能触发 OOM？做容量规划时要给 rehash 留多少余量？

**答**：
- **结论**：Redis dict 扩容采用渐进式 rehash，扩容瞬间会同时持有旧表 ht[0] 和新表 ht[1]，单 dict 结构内存峰值可达 1.5-2 倍。5 亿 key 场景，ht[1] 需要一次分配完整的新桶数组（约 2^30 桶 = 80 亿指针 × 8B ≈ 64GB 仅桶数组），分配瞬间可能直接触发 OOM 或阻塞——渐进式只摊薄"搬数据"的成本，不摊薄"分配新表"的瞬时成本。
- **取舍**：rehash 触发阈值是 `used/size >= 1`（且无 BGSAVE/BGRAOWRITE 时扩为 5 倍才扩容）——有 RDB 子进程时延迟扩容避免 COW 放大，但这也意味着写高峰后集中扩容。容量规划上：hash/zset/set 大集合 key 的 `len` 接近 2 的幂边界时预留 ≥50% 水位余量；更稳的做法是应用层拆桶（一个 500 万成员的大 hash 拆成 100 个 5 万成员），把单 dict 峰值从 GB 级压到 MB 级。
- **实战**：容量账公式：`峰值内存 ≈ 稳态内存 × (1 + rehash 放大系数)`，放大系数对大集合取 1（ht[1] 与 ht[0] 同量级），对小 dict 可忽略。上线前用 `redis-cli --bigkeys` + `MEMORY USAGE` 采样，把 top 集合的 rehash 峰值单算进预算。

```python
# 模拟渐进式 rehash 的内存峰值（纯标准库）
# 基线：Python 3.9+

import sys
from math import ceil


def next_power(size: int) -> int:
    """Redis dict 桶数组向上取 2 的幂，且至少 4"""
    return max(4, 1 << (size - 1).bit_length())


def rehash_peak_entries(n_entries: int, entry_bytes: int) -> tuple[int, int]:
    """返回 (稳态内存, rehash 峰值内存)，桶数组每个指针 8B"""
    old_buckets = next_power(n_entries)
    new_buckets = next_power(n_entries + 1) if (n_entries + 1) / old_buckets >= 1 else old_buckets
    stable = n_entries * entry_bytes + old_buckets * 8
    peak = stable + new_buckets * 8  # rehash 期间双表并存
    return stable, peak


def main() -> None:
    entry_bytes = 72  # 每个 dictEntry+key+val 粗估
    n = 5_000_000
    stable, peak = rehash_peak_entries(n, entry_bytes)
    print(f"entries={n:,} stable={stable/2**30:.1f}GB peak={peak/2**30:.1f}GB")
    assert peak > stable, "rehash 峰值必须高于稳态"
    # 拆桶后单 dict 规模缩小 100 倍
    s2, p2 = rehash_peak_entries(n // 100, entry_bytes)
    print(f"拆桶100份: 单dict峰值={p2/2**20:.1f}MB")
    assert p2 / 2**20 < 100  # 单个分桶峰值压进 100MB 内


if __name__ == "__main__":
    main()
```

**追问 1**：渐进式 rehash 期间读写请求会发生什么？
→ 一句话提示：读先查 ht[0] 再查 ht[1]，写只进 ht[1]，每次请求顺带搬一个桶；rehash 期间无法保证遍历语义强一致（scan 可能重复返回）。

**追问 2**：为什么 Redis 在有 BGSAVE 时延迟扩容，这带来什么风险？
→ 一句话提示：扩容加剧 COW 内存翻倍；延迟扩容则把负载堆积到快照结束后集中爆发，高峰写入后容易出现"快照一结束就 OOM"。

## 背诵要点
- 渐进式 rehash 只摊薄搬桶成本，ht[1] 桶数组分配是瞬时的，单 dict 峰值≈2 倍。
- 扩容阈值 used/size≥1（无 bgsave 时 5 倍），大集合拆桶（每桶 ≤10 万成员）比调内存更根本。
- 容量公式：预算内存 = 稳态 × (1 + rehash 放大)，大 hash/zset 放大系数按 1 计。

## 复盘追问
- SCAN 在 rehash 期间为什么可能返回重复 key？提示：游标以 ht[1] 的桶位反向映射回 ht[0]，反向二进制迭代器保证不漏但不保证不重。
- 如果线上已经接近 OOM 又必须扩容，能做什么？提示：先拆大 key 迁移到新实例分片，再考虑 `hash-max-ziplist-entries` 等编码阈值回收内存。
