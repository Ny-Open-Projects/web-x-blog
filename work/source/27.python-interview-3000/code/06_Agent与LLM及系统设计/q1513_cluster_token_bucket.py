"""令牌桶集群版桩:模拟 Redis 原子脚本串行执行,支持突发余票与多节点竞争。"""
import threading


class RedisStub:
    """单线程互斥的 Redis 桩:execute 保证脚本原子性,等价 Lua 脚本语义。"""

    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def eval(self, script, keys, args):
        with self.lock:                      # Redis 单线程执行 Lua 天然原子
            return script(self.data, keys, args)


def token_bucket_script(capacity, refill_per_sec):
    """返回脚本闭包:按流逝时间补充令牌,再判断是否扣得起。"""
    def script(data, keys, args):
        now, want = args
        state = data.setdefault(keys[0], {"tokens": float(capacity), "ts": now})
        elapsed = max(0.0, now - state["ts"])
        state["tokens"] = min(float(capacity), state["tokens"] + elapsed * refill_per_sec)
        state["ts"] = now
        if state["tokens"] >= want:
            state["tokens"] -= want
            return 1, round(state["tokens"], 2)
        return 0, round(state["tokens"], 2)
    return script


class ClusterRateLimiter:
    """集群限流门面:所有节点打到同一个 Redis 桩,全局只有一份桶状态。"""

    def __init__(self, redis, capacity, refill_per_sec):
        self.redis = redis
        self.script = token_bucket_script(capacity, refill_per_sec)

    def allow(self, key, cost=1.0, now=0.0):
        ok, left = self.redis.eval(self.script, [key], [now, cost])
        return {"ok": bool(ok), "remaining": left}


if __name__ == "__main__":
    rds = RedisStub()
    limiter = ClusterRateLimiter(rds, capacity=10, refill_per_sec=0.5)

    results = [limiter.allow("api", 1.0, now=0) for _ in range(12)]
    assert [r["ok"] for r in results[:10]] == [True] * 10
    assert results[10]["ok"] is False and results[10]["remaining"] == 0.0, "第 11 发被集群态拒绝"

    later = limiter.allow("api", 1.0, now=2.0)       # 2 秒补回 1 个
    assert later["ok"] is True and later["remaining"] == 0.0
    burst = limiter.allow("api", 5.0, now=2.0)       # 不足 5 票
    assert burst["ok"] is False and burst["remaining"] == 0.0

    other = limiter.allow("api-b", 10.0, now=0)      # 另一个 key 独立满桶
    assert other["ok"] is True and other["remaining"] == 0.0

    # 多线程并发扣同一 key:桩内互斥保证总量不超发
    rds2 = RedisStub()
    lim2 = ClusterRateLimiter(rds2, capacity=20, refill_per_sec=0.0)
    granted = []
    def worker():
        for _ in range(30):
            r = lim2.allow("k", 1.0, now=0)
            if r["ok"]:
                granted.append(1)
    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(granted) == 20, "并发下恰好放行容量 20 次 实际 " + str(len(granted))
    print("集群令牌桶通过:10 桶 12 发拒 1 时间补票 key 隔离 4 线程 120 请求仅放 20")
