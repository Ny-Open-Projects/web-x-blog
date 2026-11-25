---
title: [Q6656] Redis 热 key 本地兜底容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6656 · Redis 热 key 本地兜底容量账

难度：P6-P7 | 标签：Redis、热点、容量规划

**问**：大促期间某商品详情 key QPS 打到 12 万，全落在 Cluster 的一个分片上。加分片没用（单 key 无法再拆），本地兜底缓存的容量与一致性账怎么算？

**答**：结论：单 key 热点本质是"key 的请求无法水平分摊"，唯一出路是**把读推回应用进程**：本地缓存承接热 key 的绝大部分读，Redis 只兜底 miss。两笔账：① 进程内存账：本地缓存条目数×单条字节数×进程数，热 key 场景只需缓存 top-N 个 key（常是几十个），几 MB 就够，而不是全量 key；② 一致性账：本地 TTL 换 Redis 压力，TTL=1-5s 的陈旧度是否可接受由业务定，配合失效广播（Q6531）可压到亚秒级。同时要防"本地缓存本身变成新热点问题"——命中率统计与主动过期要 O(1)。

实战要点：
1. 热 key 识别走两路：Redis 侧 `--hotkeys`/LFU 计数，应用侧按 key 维度的 QPS 直方图，双源对齐防误判。
2. 本地兜底只放"读多改少"数据；库存类强一致数据不能进本地缓存（可用本地缓存放"是否售罄"布尔位）。
3. 降级联动：Redis 不可用时本地缓存 + 过期数据可短暂续命（serve-stale），但要打上降级标记。

```python
"""热 key 本地兜底：容量账 + TTL 兜底缓存（标准库，可运行）"""
import time
from collections import OrderedDict


def hot_key_budget(per_key_bytes: int, top_n: int,
                   process_count: int) -> float:
    """本地兜底内存账：只需缓存 top-N 热 key"""
    total = per_key_bytes * top_n * process_count
    return total / 1024 / 1024


print("本地兜底内存(MB):",
      hot_key_budget(per_key_bytes=2 * 1024, top_n=50, process_count=16))


class LocalGuard:
    """TTL + serve-stale 的热 key 兜底缓存"""

    def __init__(self, ttl: float, max_entries: int = 100) -> None:
        self.ttl = ttl
        self.max_entries = max_entries
        self.data: OrderedDict[str, tuple[float, str]] = OrderedDict()
        self.hits = self.stale_hits = 0

    def get(self, key: str):
        item = self.data.get(key)
        if item is None:
            return None
        expire_at, value = item
        if time.monotonic() < expire_at:
            self.hits += 1
            return value
        self.stale_hits += 1      # 过期但可 serve-stale 兜底
        return value + "(stale)"

    def put(self, key: str, value: str) -> None:
        self.data[key] = (time.monotonic() + self.ttl, value)
        self.data.move_to_end(key)
        while len(self.data) > self.max_entries:
            self.data.popitem(last=False)


g = LocalGuard(ttl=2.0)
g.put("item:9527", "detail-json")
print(g.get("item:9527"), "| hits:", g.hits)
```

**追问 1**：为什么"把热 key 复制到多个分片（key 加后缀）"只对部分场景有效？
**提示**：多副本读可分摊，但写更新要同步 N 份，且应用要随机挑副本；对纯读详情有效，对计数类无效。

**追问 2**：本地 TTL 2 秒 + 16 个进程，最坏陈旧窗口是多少？
**提示**：约等于 TTL（广播失效可压到广播延迟），但每次发布/扩容新进程冷启动会集中回源，要预热。

## 背诵要点
- 单 key 热点加不了分片，唯一解是把读推进程内本地缓存，Redis 只兜 miss。
- 本地兜底内存账 = top-N 条 × 单条字节 × 进程数，热 key 场景通常几 MB 足够。
- 陈旧度窗口≈本地 TTL，强一致数据（库存余量）禁入本地缓存。

## 复盘追问
- 事前如何用压测证明"12 万 QPS 落单分片"是热 key 而不是容量不足？
- 如果本地缓存命中率掉到 50%，Redis 分片还扛得住吗？兜底与分片容量的联合水位线怎么定？
