---
title: "[Q6766] 淘汰不是真 LRU：maxmemory-samples 采样近似与淘汰精度的账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6766 · 淘汰不是真 LRU：maxmemory-samples 采样近似与淘汰精度的账

难度：P6 ｜ 标签：Redis、内存淘汰、maxmemory-samples、LRU 近似、CPU 取舍

基线：Python 3.12；实现真 LRU 与采样式近似 LRU 两条淘汰路径，对比"误逐热键率"与比较成本，全标准库实跑。

**问**：Redis 内存满了开始淘汰，配置的 allkeys-lru。Redis 的 LRU 和教科书 LRU 是一回事吗？为什么官方文档说它是"近似 LRU"？`maxmemory-samples` 从 5 调到 10 会有什么变化？有人说"调大了缓存更准但 CPU 更高"，这笔账怎么算？

**答**：
- **结论**：Redis 的 LRU 是**采样近似**：不维护全局双向链表（O(1) 淘汰需要每个 key 两个指针，几千万 key 时内存税太大），而是在每个 key 的对象头里存一个 24bit 的空闲时钟，**淘汰时随机抽 `maxmemory-samples` 个 key，淘汰其中空闲时间最长的**，必要时多轮重复。精度换内存：samples=5 时"误逐热键"概率已经很低，samples 调大精度单调上升、每轮淘汰的 CPU 成本线性上升。LFU 模式（allkeys-lfu）同理采样，只是比较对象从空闲时间换成对数计数器。这笔账的本质：**淘汰发生在"内存已满"的压力时刻，CPU 是稀缺资源，采样数是精度与 CPU 的直接旋钮**。
- **取舍**：① samples=5 是经验默认，热键误逐率通常 <1%，多数场景不动；② 命中率统计发现"逐了热键"（命中率异常下滑、QPS 未涨内存未涨）再考虑调大 samples 或换 LFU；③ LFU 的 `lfu-log-factor` 与 `lfu-decay-time` 决定计数灵敏度：访问越快计数越难涨（对数）、长时间不访问计数自动衰减——适合"热点会迁移"的场景；④ 淘汰风暴：一次大批量写入把内存瞬间打满，会触发连续多轮淘汰（每轮都是 O(samples)），写入延迟毛刺，容量规划要留水位（Q1014/Q6572）。
- **实战**：① 监控 `evicted_keys` 增速与命中率联动，evicted 突增先查写入突刺再看淘汰模式；② 热点稳定的场景 allkeys-lru + samples 默认即可；热点迁移频繁（推荐位、活动位）换 allkeys-lfu；③ 永不过期键的业务（计数、队列）单独实例隔离，别和缓存混池被淘汰误伤（Q6740 的教训延伸）；④ samples 参数变更走灰度（Q6558），观察一个完整业务周期再全量。

```python
"""真 LRU vs 采样近似 LRU：误逐热键率与比较成本的对比。"""
import random
from collections import OrderedDict


def true_lru_evict(lru: OrderedDict) -> int:
    """教科书 LRU: O(1) 淘汰链表头 (需双向链表, 每 key 两个指针的内存税)。"""
    victim, _ = lru.popitem(last=False)     # 最久未用
    return victim


def sampled_lru_evict(access_time: dict, samples: int, rng: random.Random) -> int:
    """Redis 近似: 随机抽 samples 个, 淘汰其中最久未访问的 (时间戳最小)。"""
    keys = rng.sample(list(access_time), min(samples, len(access_time)))
    victim = min(keys, key=lambda k: access_time[k])
    del access_time[victim]
    return victim


def run(cache_keys: list, workload: list, pool_size: int,
        samples: int = 0, seed: int = 7) -> tuple[float, int]:
    """模拟固定容量缓存, 返回 (命中率, 淘汰次数)。"""
    rng = random.Random(seed)
    hits = evictions = 0
    lru = OrderedDict()                     # key -> 1 (顺序即访问序)
    access_time: dict[str, int] = {}        # key -> 最后访问的 tick
    tick = 0
    for op in workload:
        tick += 1
        if op in lru:                       # 命中
            hits += 1
            lru.move_to_end(op)
            access_time[op] = tick
        else:                               # 未命中 -> 装载, 满则淘汰
            evictions += 1
            if len(lru) >= pool_size:
                victim = (true_lru_evict(lru) if samples == 0
                          else sampled_lru_evict(access_time, samples, rng))
                if victim in lru:
                    lru.pop(victim)
            lru[op] = 1
            access_time[op] = tick
    return hits / len(workload), evictions


if __name__ == "__main__":
    rng = random.Random(1)
    keys = [f"key{i}" for i in range(2000)]
    hot = rng.sample(keys, 40)
    workload = []                           # 80/20 倾斜访问
    for _ in range(60_000):
        workload.append(rng.choice(hot) if rng.random() < 0.8
                        else rng.choice(keys))
    POOL = 200

    r_true, _ = run(keys, workload, POOL)
    print(f"真 LRU (O(1)链表):        命中率 {r_true:.1%}")
    for s in (5, 10, 20):
        r_s, _ = run(keys, workload, POOL, samples=s)
        print(f"采样 LRU samples={s:>2}: 命中率 {r_s:.1%}  (与真 LRU 差 {(r_true - r_s) * 100:.2f}pp)")

    # 误逐热键统计: 采样版多淘汰的次数
    _, e_true = run(keys, workload, POOL)
    _, e_s = run(keys, workload, POOL, samples=5)
    print(f"\nsamples=5: 淘汰 {e_s} 次 vs 真 LRU {e_true} 次, 命中率差 {(r_true - run(keys, workload, POOL, samples=5)[0]) * 100:.2f}pp")
    print("比较成本: 真LRU O(1)/次, 采样 O(samples)/次 -> samples 是精度换 CPU 的旋钮")
    print("结论：Redis LRU 是采样近似, samples=5 精度已够大多数场景;")
    print("      误逐热键看命中率异常, 别盲调参数; 热点会迁移的场景换 LFU")
```

**追问一**：为什么 Redis 不用真 LRU？

→ 解析：真 LRU 需要 O(1) 淘汰的链表结构：每个 key 两个前后指针，64 位系统上每 key 额外 16 字节——Redis 单实例几千万 key 时仅指针税就是数百 MB，而 Redis 的设计哲学是数据本体优先（每个 key 的头已经很紧凑）。24bit 时钟 + 采样方案的每 key 附加成本几乎为零，精度损失用采样数控制。这是**内存预算 vs 淘汰精度**的典型取舍，与 Q1960 的对象头放大账同一思路：Redis 的每个字节都要精打细算，淘汰机制不能成为内存大头。

**追问二**：淘汰发生在什么时机，会不会阻塞写入？

→ 解析：淘汰在写入路径上惰性触发：命令执行前检查内存超限，超了就先做淘汰再写——所以淘汰是**写命令延迟的一部分**，samples 大或单轮没释放够内存时要重复多轮采样，写入延迟毛刺就是这么来的。极端情况：一次大 SET 需要腾出 100MB，samples=5 每轮只释放少量，要跑很多轮，命令耗时秒级。缓解手段：容量水位提前告警（在 80% 时人工介入扩容）、批量写入前主动清理过期键（`lazyfree` 配合 UNLINK，Q6705）、写入侧限流。监控上把 `evicted_keys/sec` 与 `latency` 放同一张图，毛刺归因一目了然。
