import socket
import threading
import time


class DnsCache:
    def __init__(self, min_ttl: float = 5.0, max_ttl: float = 300.0,
                 neg_ttl: float = 10.0) -> None:
        self._cache: dict = {}   # host -> (expiry, addrinfo or None)
        self._lock = threading.Lock()
        self.min_ttl, self.max_ttl, self.neg_ttl = min_ttl, max_ttl, neg_ttl
        self.stats = {"hit": 0, "miss": 0, "stale": 0, "neg": 0}

    def resolve(self, host: str, port: int = 80) -> list:
        now = time.monotonic()
        with self._lock:
            entry = self._cache.get(host)
            if entry:
                expiry, data = entry
                if expiry > now:
                    self.stats["hit" if data else "neg"] += 1
                    if data:
                        return data
                    raise socket.gaierror(8, "negative cached: 域名不存在")
                # 过期: 暂存旧值做故障兜底
                stale = data
            else:
                stale = None
            self.stats["miss"] += 1
        # 解析在锁外做, 避免长时间持锁
        try:
            infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
            with self._lock:
                self._cache[host] = (now + self.min_ttl, infos)  # 简化: 统一 min_ttl
            return infos
        except socket.gaierror:
            with self._lock:
                if stale:  # DNS 故障但有过期值 → 宽限使用
                    self.stats["stale"] += 1
                    self._cache[host] = (now + self.min_ttl, stale)
                    return stale
                self._cache[host] = (now + self.neg_ttl, None)  # 负缓存
                self.stats["neg"] += 1
            raise


if __name__ == "__main__":
    cache = DnsCache(min_ttl=1.0)

    def timed(label: str, fn) -> None:
        t0 = time.perf_counter()
        try:
            fn()
            print(f"{label}: {(time.perf_counter() - t0) * 1000:.2f}ms")
        except socket.gaierror as e:
            print(f"{label}: 解析失败 {e} ({(time.perf_counter() - t0) * 1000:.2f}ms)")

    timed("首次解析 localhost", lambda: cache.resolve("localhost"))
    timed("缓存命中", lambda: cache.resolve("localhost"))
    timed("缓存命中", lambda: cache.resolve("localhost"))
    timed("负缓存不存在的域", lambda: cache.resolve("no-such-host.invalid"))
    try:
        cache.resolve("no-such-host.invalid")
    except socket.gaierror:
        print("再次访问不存在的域: 直接命中负缓存, 未发起真实解析")
    time.sleep(1.1)
    timed("TTL 过期后重新解析", lambda: cache.resolve("localhost"))
    print("统计:", cache.stats)
