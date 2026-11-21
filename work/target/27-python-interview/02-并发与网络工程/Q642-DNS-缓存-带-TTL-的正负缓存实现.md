---
title: [Q642] DNS 缓存:带 TTL 的正负缓存实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q642 · DNS 缓存:带 TTL 的正负缓存实现

> 难度:★★★☆ | 标签:DNS 缓存, TTL, 性能

**问**:为什么要在应用层做 DNS 缓存?怎么设计 TTL 与故障兜底?

**答**:libc getaddrinfo 一般不缓存,热路径每请求一次解析既慢(毫秒级)又给 DNS 服务器压力,解析故障还会放大成全站不可用。应用层缓存设计:条目存 (地址列表, 过期时刻),TTL 尊重 DNS 应答但设上下限(如 5s~300s,防 0 TTL 打爆和超长 TTL 切换迟钝);负缓存(解析失败的域名)短 TTL(如 10s),挡住对不存在域名的攻击;故障兜底——DNS 服务器不可用时过期条目再宽限使用(stale-while-revalidate 思想)。注意缓存要线程安全且地址列表是只读快照。

```python
# file: code/02_并发与网络工程/q642_dns_cache.py
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
```

**追问**:1) 服务要"DNS 切换后快速摘除坏节点"怎么办?——把 TTL 下限调小(如 5s)+ 主动健康检查摘除(Q643),而不是指望调大缓存换稳定,缓存换不来故障转移。2) TTL 上下限与正负缓存的设计依据?——正缓存尊重应答 TTL 但设下限(防 0 TTL 打爆自身)与上限(防故障切换迟钝);负缓存短 TTL(如 10s)挡「查询不存在域名」的攻击;stale-while-revalidate:DNS 故障时过期条目宽限使用,牺牲新鲜度换可用性。3) 缓存的线程安全与多实例一致性?——条目存不可变元组快照,单实例读写靠锁或 CPython 原子 dict 操作;多进程各自缓存会有切换时间差,真正快的故障转移靠健康检查摘除(Q643)兜底,缓存只做加速。4) 生产陷阱?——把瞬时故障的空结果缓存满 TTL,全站不可用直到过期;刷新缓存在热路径同步做,解析挂了拖死请求;缓存对象返回可变引用被调用方污染。

---
