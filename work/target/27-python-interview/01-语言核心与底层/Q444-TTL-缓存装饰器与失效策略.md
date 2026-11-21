---
title: [Q444] TTL 缓存装饰器与失效策略
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q444 · TTL 缓存装饰器与失效策略

> 难度:★★★★ | 标签:缓存, 装饰器

**问**:lru_cache 没有 TTL 也没有主动失效,如何自己实现一个带过期时间的缓存装饰器?

**答**:核心结构:参数做 key、(写入时间, 值) 做 value;读时惰性判断过期,写时若超容量就按最旧时间淘汰一条(简化版 LRU)。失效入口暴露 cache_clear;时钟必须用 time.monotonic 防止系统时间回拨把 TTL 算负。并发场景下 CPython 的 dict 单操作原子性不能覆盖「检查再写」的复合操作,严格场景要加锁;另外 key 必须可哈希且把 kwargs 排序归一,否则同样参数不同顺序会各存一份。

```python
# file: code/01_语言核心与底层/q444_ttl_cache.py
import functools
import time

def ttl_cache(ttl=1.0, maxsize=128):
    def deco(func):
        store = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            hit = store.get(key)
            if hit and now - hit[0] < ttl:
                return hit[1]                 # 命中未过期
            value = func(*args, **kwargs)
            if len(store) >= maxsize:
                oldest = min(store, key=lambda k: store[k][0])
                store.pop(oldest)             # 淘汰最旧
            store[key] = (now, value)
            return value

        wrapper.cache_clear = store.clear     # 主动失效入口
        return wrapper
    return deco

CALLS = {"n": 0}

@ttl_cache(ttl=0.05)
def slow_square(x):
    CALLS["n"] += 1
    time.sleep(0.01)
    return x * x

if __name__ == "__main__":
    print(slow_square(4), slow_square(4))     # 第二次命中
    print("calls:", CALLS["n"])
    time.sleep(0.08)                          # 超过 TTL
    print(slow_square(4))
    print("calls after ttl:", CALLS["n"])
```

**追问**:1) 为什么计时用 monotonic 而不是 time.time?——time.time 是墙钟,可能被 NTP 调整回拨,导致刚写入的缓存立刻「过期」或永不过期;monotonic 保证只前进。2) 这个实现与严格 LRU 的差距?——淘汰按「最旧写入」而非「最近访问」,读命中不刷新时间戳,热点数据可能被误淘汰;命中时写回 store[key]=(now, value) 一行即升级为 LRU-TTL。3) 并发竞态在哪一步?——「读命中判断→回源→写缓存」复合操作非原子,并发 miss 造成同一 key 多次回源(缓存击穿);dict 单操作原子不覆盖复合操作,严格场景加锁或 single-flight。4) 生产陷阱?——key 含不可哈希参数直接 TypeError;kwargs 不归一让同义参数各存一份;闭包持有大结果对象导致内存滞留,必须暴露 cache_clear 并在测试与进程退役时调用。
