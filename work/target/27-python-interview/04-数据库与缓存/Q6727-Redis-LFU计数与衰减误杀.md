---
title: "[Q6727] Redis LFU 的两个旋钮：counter 概率递增与衰减误杀"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6727 · Redis LFU 的两个旋钮：counter 概率递增与衰减误杀

难度：P6 ｜ 标签：Redis、LFU、maxmemory-policy、热点淘汰

基线：Python 3.12；Redis 4.0+ `allkeys-lfu`、`lfu-log-factor`、`lfu-decay-time`；纯 Python 模拟 8 位计数器。

**问**：把缓存策略从 `allkeys-lru` 换成 `allkeys-lfu` 后，一个大促期间的老热点 key 在活动结束后仍长期占着内存，新热点反而频繁被淘汰。明明它有访问计数，为什么 LFU 没把它换下去？`lfu-decay-time` 调大调小分别会发生什么？

**答**：
- **结论**：Redis 的 LFU 不是简单计数，而是 **8 位对数计数器 + 时间衰减**。计数器满值 255，递增是**概率性**的：`p = 1 / ((counter - 5) * lfu_log_factor + 1)`，所以一个 key 要到很高频才会涨到高值，避免一次突发把计数打满。衰减由 `lfu-decay-time` 控制：每 N 分钟（默认 1）计数器减 1。若 `lfu-decay-time` 调得过大（或为 0 表示不衰减），老热点的计数几乎不降，会**长期霸占**内存，新热点进不来；调得过小，计数掉得快，LFU 退化成近似 LRU，抗突发能力消失。
- **取舍**：LFU 适合"热点稳定、长尾明显"的缓存；对"短期活动型热点"不友好，因为历史计数有惯性。`lfu-log-factor` 越大，计数增长越慢，区分度越高但也越难爬到高位。两者都要按访问分布调，不能照默认值一把梭。
- **实战**：① 用 `OBJECT FREQ key` 观察真实计数器，别凭感觉调参；② 活动型业务把 `lfu-decay-time` 调小（如 1-5 分钟）让旧热点快速退场；③ 极端热点用本地缓存或单独实例隔离，别和长尾抢同一个淘汰池；④ 切策略前用 `redis-cli --lfu` 或采样做回放，比较命中率而不是只看理论。

```python
"""模拟 Redis LFU：概率递增 + 按分钟衰减。"""
import random

MAX_COUNTER = 255


def touch(counter: int, log_factor: int = 10, rng: random.Random | None = None) -> int:
    if counter >= MAX_COUNTER:
        return MAX_COUNTER
    rng = rng or random
    p = 1.0 / ((counter - 5) * log_factor + 1) if counter > 5 else 1.0
    return counter + 1 if rng.random() < p else counter


def decay(counter: int, minutes: int, decay_time: int = 1) -> int:
    if decay_time <= 0:
        return counter
    return max(0, counter - minutes // decay_time)


def run(accesses: int, minutes_since: int, decay_time: int,
        rng: random.Random) -> int:
    c = 0
    for _ in range(accesses):
        c = touch(c, rng=rng)
    return decay(c, minutes_since, decay_time)


if __name__ == "__main__":
    rng = random.Random(7)
    old_hot = run(2000, minutes_since=120, decay_time=1000, rng=rng)
    old_hot_fast = run(2000, minutes_since=120, decay_time=1, rng=rng)
    new_hot = run(200, minutes_since=0, decay_time=1, rng=rng)
    print(f"老热点(不衰减) freq={old_hot:>3}")
    print(f"老热点(1分钟衰减) freq={old_hot_fast:>3}")
    print(f"新热点 freq={new_hot:>3}")
    print("老热点不衰减时仍高于新热点 -> 新热点先被淘汰")
    print("把 lfu-decay-time 调小后老热点退场，新热点才能留下")
```

**追问一**：为什么 LFU 的计数器要到 255 才封顶，而不是用 16 位精确计数？
→ 解析：Redis 用 24 位存 `lru/lfu` 元数据（与 LRU 时钟复用同一字段），只能挤出 8 位给计数。对数递增让 8 位也能表达很宽的频率范围（从个位数到百万级访问），代价是精度粗、需要概率递增避免饱和。

**追问二**：LFU 下 `OBJECT FREQ` 读到的值和实际访问次数为什么对不上？
→ 解析：它是**衰减后的对数值**，不是累计次数。概率递增意味着访问 100 次可能只涨 5-10 点；时间衰减又会周期性减 1。它表达的是"近期相对热度"，用于淘汰排序，不适合当业务计数使用。
