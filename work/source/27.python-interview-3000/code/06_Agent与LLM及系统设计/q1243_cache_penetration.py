"""缓存三大问题:空值缓存 + singleflight 互斥重建 + TTL 抖动。"""
import random, threading, time


class Cache:
    def __init__(self):
        self.kv, self.db_calls = {}, 0
        self.mu = threading.Lock()
        self.inflight = {}                       # singleflight 登记

    def get_with_guard(self, key, loader, bloom=None, null_ttl=0.05):
        if bloom is not None and not bloom(key):
            return "blocked_by_bloom"
        if key in self.kv:
            v = self.kv[key]
            return v if v is not None else "null_cached"
        owner, waiter = False, None
        with self.mu:                            # 互斥重建
            if key in self.inflight:
                waiter = self.inflight[key]
            else:
                waiter = threading.Event()
                self.inflight[key] = waiter
                owner = True
                self.db_calls += 1
        if not owner:
            waiter.wait(timeout=1)
            v = self.kv.get(key)
            return v if v is not None else "null_cached"
        v = loader(key)
        self.kv[key] = v                          # None 也缓存:防穿透
        with self.mu:
            self.inflight.pop(key, None)
        waiter.set()
        return v if v is not None else "null_cached"


def jittered_ttl(base=60, jitter=10):
    return base + random.uniform(0, jitter)       # 防雪崩:过期时间抖动


if __name__ == "__main__":
    cache = Cache()
    bloom = lambda k: not k.startswith("ghost")
    loader = lambda k: None if k == "item-x" else {"id": k}

    outs = [cache.get_with_guard("item-x", loader, bloom) for _ in range(5)]
    print("穿透防护(过布隆但 DB 无此行):", outs, "DB 调用:", cache.db_calls)
    assert outs[0] == "null_cached" and cache.db_calls == 1, "空值缓存后不再打 DB"
    assert cache.get_with_guard("ghost-1", loader, bloom) == "blocked_by_bloom", "布隆直接拦下不存在的 key"

    # 击穿:50 线程同时打同一未缓存 key
    cache2 = Cache()
    results = []
    def worker():
        results.append(cache2.get_with_guard("hot-key", lambda k: "data", None))
    ts = [threading.Thread(target=worker) for _ in range(50)]
    for t in ts: t.start()
    for t in ts: t.join()
    print("击穿防护: 50 并发重建,DB 调用 =", cache2.db_calls)
    assert cache2.db_calls == 1 and results.count("data") == 50

    ttls = [round(jittered_ttl(), 1) for _ in range(3)]
    print("TTL 抖动:", ttls, "-> 大批 key 不再同时过期")
    assert len(set(ttls)) == 3
