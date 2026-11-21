---
title: [Q176] 热 key 问题
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q176 · 热 key 问题

> 难度:★★★★ | 标签:Redis, 热点, 架构

**问**:什么是热 key?发现和处理手段有哪些?

**答**:某个 key 的访问 QPS 远超其他 key,把流量集中到单个 Redis 分片甚至单节点网卡,造成局部过载。发现:redis-cli --hotkeys、monitor 采样、客户端埋点统计。处理:① 本地缓存兜底(应用进程内 LRU,容忍秒级不一致);② key 打散:把一个热点 key 拆成 N 个副本 key(如 key:0..N-1)读时随机取一个,写时全部更新;③ 读写分离/集群扩容分片;④ 极端场景直接推送本地广播。

```python
# file: code/04_数据库与缓存/q176_hot_key.py
"""热 key 治理: 本地 LRU 缓存 + 热 key 打散副本"""
from collections import OrderedDict
import random


class LocalLRU:
    def __init__(self, capacity: int = 2):
        self.data: OrderedDict = OrderedDict()
        self.capacity = capacity
        self.hits = 0

    def get(self, key):
        if key in self.data:
            self.data.move_to_end(key)
            self.hits += 1
            return self.data[key]
        return None

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


REPLICAS = 4       # 热 key 打散成 4 个副本


def shard_key(key: str) -> str:
    return f"{key}:{random.randrange(REPLICAS)}"


class TieredCache:
    def __init__(self):
        self.local = LocalLRU()
        self.remote: dict = {}
        self.remote_reads = 0

    def load_remote(self, key: str, value: str):
        for i in range(REPLICAS):          # 写: 更新全部副本
            self.remote[f"{key}:{i}"] = value

    def get(self, key: str):
        hit = self.local.get(key)
        if hit is not None:
            return hit, "local"
        self.remote_reads += 1
        value = self.remote.get(shard_key(key))   # 读: 随机副本分流
        if value is not None:
            self.local.put(key, value)            # 回填本地
        return value, "remote"


if __name__ == "__main__":
    cache = TieredCache()
    cache.load_remote("hot:news", "头条内容")
    for _ in range(100):
        cache.get("hot:news")
    print(f"本地命中 {cache.local.hits} 次, 远端读取 {cache.remote_reads} 次")
    # 本地缓存把绝大部分读挡在进程内, 剩余读也被副本分散到多个分片
```

**追问**:
- 本地缓存一致性如何取舍?——热 key 通常允许秒级陈旧;要求强一致就不要用本地缓存,改走 DB/强一致链路。
- 热 key 和大 key 的区别?——热 key 是读流量集中,大 key 是单个 value 过大导致阻塞,治理手段完全不同。

---
