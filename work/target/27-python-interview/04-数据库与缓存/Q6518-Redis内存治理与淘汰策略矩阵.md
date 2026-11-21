---
title: [Q6518] Redis 内存治理：淘汰策略矩阵与大实例拆解
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6518 · Redis 内存治理

> 难度:★★☆ | 标签:Redis, 淘汰策略, 容量

**问**：maxmemory 打满后 Redis 的行为取决于淘汰策略——八种策略各自淘汰谁，缓存场景该配哪个、为什么 allkeys-lru 有坑？内存碎片率怎么看，「单个 2GB 大 key 删除把主线程卡 1 秒」怎么治（lazy-free 与拆桶）？

**答**：策略矩阵（按数据类别分组）：**易失组**（只淘汰带 TTL 的 key）：volatile-lru/lfu/random/ttl——适合缓存与持久数据混存（配置/分布式锁不设 TTL 就不被误杀）；**全量组**：allkeys-lru/lfu/random——纯缓存实例首选 allkeys-lfu（热 key 保护优于 lru，长尾扫描友好）；**noeviction**（默认）：写报错——适合「内存即真相」的实例（分布式锁/队列），打满宁可拒绝写。`allkeys-lru` 的坑：LRU 是**近似抽样淘汰**（默认采 5 key），冷数据突发访问会污染（污染型访问驱逐热数据），lfu 缓解。大 key 治理：**lazy-free**（`UNLINK` 替代 `DEL`，删除异步化；`lazyfree-lazy-expire` 配置）+ **拆桶**（2GB 列表拆成 512 个 4MB 桶，读写按 hash 分桶）。碎片：`mem_fragmentation_ratio > 1.5` 触发告警，原因多是大 key 频繁增删（allocator 空洞）+ 不重启不归还，治本靠 key 生命周期设计。

```python
# demo 用纯 Python 模拟 LRU/LFU 抽样淘汰与拆桶读写（无 Redis 也可跑通语义）
import hashlib, random, time, collections

def evict_sampled(keys: list[str], score: dict, n_sample: int = 5) -> str:
    """近似淘汰：随机抽 n 个、按 score 最差者出局（Redis 惯例 pool 实现）。"""
    sample = random.sample(keys, min(n_sample, len(keys)))
    return min(sample, key=lambda k: score[k])       # LRU: score=访问时间；LFU: score=频次

def demo_lru_pollution():
    """LRU 污染：冷数据突发批量访问 → 抽样池全是冷 key → 热 key 被误杀。"""
    keys = {f"hot{i}": time.time() for i in range(3)}          # 热 key 刚访问过
    keys.update({f"cold{i}": time.time() for i in range(100)})  # 冷 key 批量刚访问（污染）
    victim = evict_sampled(list(keys), keys)                    # 抽 5 个全是 cold 区
    print("被驱逐:", victim, "—— 抽样池大概率没含 hot，热 key 存活但池被冷 key 占据")
    # LFU 口径：频次低的冷 key 被逐出，热 key 频次高存活——污染型访问保护更好

class ShardedList:
    """大 key 拆桶：单 key 2GB → N 桶 × 每桶小，删除 O(桶数×桶大小) 可控。"""
    def __init__(self, buckets: int = 16):
        self.buckets: list[collections.deque] = [collections.deque() for _ in range(buckets)]
    def push(self, item: str):
        h = int(hashlib.md5(item.encode()).hexdigest(), 16)
        self.buckets[h % len(self.buckets)].append(item)
    def delete_all(self):
        """逐桶 UNLINK 语义：每桶删除时长有界，主线程不卡 1s。"""
        removed = 0
        for b in self.buckets:
            removed += len(b); b.clear()      # Redis: UNLINK bucket_i（异步释放）
        return removed

if __name__ == "__main__":
    random.seed(1)
    demo_lru_pollution()
    big = ShardedList(16)
    for i in range(100000):
        big.push(f"item-{i}")
    n = big.delete_all()
    print(f"拆桶删除 {n} 条：16 桶 × 每桶 O(6250) —— 单次卡顿降为 1/16")
    # 运维口径：mem_fragmentation_ratio = used_memory_rss/used_memory，
    # >1.5 告警、>2 危险（allocator 空洞）；activedefrag 开启后在线整理（CPU 换内存）。
```

**追问**：1) volatile-ttl 的实际用途？——「快到期的先死」：业务按 TTL 长短编码重要性（短 TTL=可再生数据），打满时优先牺牲可再生缓存，保护设置了长 TTL 的会话类数据。2) lazy-free 有什么代价？——异步线程释放内存期间，该内存不可复用（RSS 短暂虚高）、引用计数竞争；大 key 频繁 UNLINK 时观察 `lazyfree_pending_objects` 积压。3) 怎么发现大 key？——`redis-cli --bigkeys`（抽样扫描）/ RDB 分析工具离线全量；生产口径：定期 RDB 分析 + `MEMORY USAGE key` 抽查，写代码阶段就限制集合类型长度（拆桶阈值内建在封装层）。

## 背诵要点
1. 策略矩阵：纯缓存 allkeys-lfu；混存 volatile-*（不误杀无 TTL 持久数据）；锁/队列 noeviction 宁拒勿杀。
2. LRU 是近似抽样（默认 5）：冷数据突发访问污染抽样池，LFU 缓解。
3. 大 key 治理：UNLINK/lazy-free 异步释放 + 拆桶（单操作时长有界）；碎片率 >1.5 告警。

## 复盘追问
1. 为什么「缓存与锁共用一个实例 + allkeys-lru」是事故配置？（提示：锁 key 无 TTL 但 allkeys 会杀它 → 分布式锁失效并发重复执行；锁/缓存必须分实例或分策略）
2. activedefrag 什么时候不该开？（提示：CPU 紧张实例（它抢主线程 CPU）；frag 不严重时白耗——看指标再开）
