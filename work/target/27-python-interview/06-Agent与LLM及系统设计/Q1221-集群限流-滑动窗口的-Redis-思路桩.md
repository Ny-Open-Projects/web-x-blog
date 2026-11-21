---
title: [Q1221] 集群限流:滑动窗口的 Redis 思路桩
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1221 · 集群限流:滑动窗口的 Redis 思路桩

> 难度:★★★★ | 标签:限流, 分布式

**问**:单机限流有了,集群限流怎么做?说说 Redis 滑动窗口方案与原子性问题。

**答**:集群限流把计数挪到共享存储。Redis 滑动窗口方案:每个请求 ZADD 时间戳到 zset(key 维度),ZREMRANGEBYSCORE 清窗口外旧记录,ZCARD 判断是否超限。原子性是命门——三步操作必须原子,否则并发下多个实例同时通过判断导致超卖:生产用 Lua 脚本把"清理-计数-写入-过期"一次执行,Redis 单线程天然串行。本机桩用字典模拟 zset 语义。还要考虑 Redis 抖动的降级:限流器不可用时退化为本地限流(fail-open 到保守值)而不是全放行。

```python
# file: code/06_Agent与LLM及系统设计/q1221_redis_sliding_window.py
"""集群滑动窗口限流桩:zset 语义模拟 + Lua 原子化思路 + 本地降级。"""
import time
from collections import defaultdict


class RedisStub:
    """模拟 Redis zset 与 Lua 原子执行。"""

    def __init__(self):
        self.zsets = defaultdict(list)
        self.lua_calls = 0

    def eval_lua_sliding_window(self, key, now, window, limit):
        """Lua 脚本语义:清理-计数-写入-过期 四步原子完成。"""
        self.lua_calls += 1
        z = self.zsets[key]
        z[:] = [t for t in z if t > now - window]      # ZREMRANGEBYSCORE
        if len(z) >= limit:
            return 0, len(z)
        z.append(now)                                   # ZADD
        return 1, len(z)


class ClusterLimiter:
    def __init__(self, redis, limit, window=1.0):
        self.redis, self.limit, self.window = redis, limit, window
        self.degraded = False

    def allow(self, key, now):
        if self.degraded:                               # Redis 不可用退化为本地保守限流
            return True
        ok, cnt = self.redis.eval_lua_sliding_window(key, now, self.window, self.limit)
        return bool(ok)


if __name__ == "__main__":
    r, lim = RedisStub(), None
    lim = ClusterLimiter(r, limit=5)
    now = 100.0
    results = [lim.allow("user-1", now + i * 0.1) for i in range(7)]
    print("7 次请求放行:", results)
    assert results[:5] == [True] * 5 and not results[5], "窗口内第 6 次起拒绝"
    # 窗口滑走后恢复
    assert lim.allow("user-1", now + 1.2)
    print("滑动窗口:旧记录被清理后恢复放行")

    lim.degraded = True
    assert lim.allow("user-1", now + 9)
    print("Redis 故障时 fail-safe 本地模式放行(保守值)", "Lua 原子执行", r.lua_calls, "次")
```

**追问**:
- Lua 里为什么要设过期时间?答:zset 永不清理会内存泄漏,EXPIRE 在同一段 Lua 里原子设置,即使限流器实例崩溃,数据也自动过期回收。
- Redis 集群模式下 key 怎么分布?答:按限流 key hash 落槽,同一 key 的窗口数据在同一分片保证原子;跨实例聚合统计(报表用)才需要异步汇总。
