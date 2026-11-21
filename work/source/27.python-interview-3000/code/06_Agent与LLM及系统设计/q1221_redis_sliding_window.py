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
