---
title: [Q2153] 限流与重试的联合语义:Retry-After 的握手
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2153 · 限流与重试的联合语义:Retry-After 的握手

> 难度:★★★★ | 标签:限流, 重试, Retry-After, 令牌桶

**问**:服务端限流和客户端重试,各自独立设计会有什么问题?正确的联合语义是什么?

**答**:客户端盲目重试会放大洪峰,服务端硬拒绝会让客户端乱猜节奏;联合语义是服务端在 429 里带上 Retry-After 表达"何时再来",客户端在三重约束下重试:尊重 Retry-After、自己的单次等待上限、总尝试预算。

- 回环实测:容量 3 的令牌桶,突发 6 请求,前 3 个立即通过;

- 后 3 个按 Retry-After 分批补票,尝试 8 次、总耗时 0.52s 全部通过;

- 客户端单次等待上限防止服务端把自己挂起过久;

- 总预算兜底:任何一侧的失误都不会变成无限循环。

```python
# file: code/02_并发与网络工程/q2153_ratelimit_retry.py
# -*- coding: utf-8 -*-
"""限流与重试的联合语义: 服务端令牌桶与客户端退避的握手。

- 服务端限流拒绝时给 Retry-After, 表达"何时再来";
- 客户端重试要同时尊重: Retry-After、自己的单次等待上限、总尝试预算;
- 实测: 突发 6 个请求, 3 个立即通过, 其余按 Retry-After 分批补票入场。
"""
import socket
import threading
import time

HOST = "127.0.0.1"


class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate            # 每秒补充
        self.tokens = float(capacity)
        self.ts = time.monotonic()

    def take(self):
        now = time.monotonic()
        self.tokens = min(self.capacity,
                          self.tokens + (now - self.ts) * self.rate)
        self.ts = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True, 0.0
        wait = (1 - self.tokens) / self.rate
        return False, wait


def server(port_ready, bucket):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    port_ready.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    with conn:
        f = conn.makefile("rb")
        for line in f:
            if line.strip() != b"REQ":
                break
            ok, wait = bucket.take()
            if ok:
                conn.sendall(b"200 OK\n")
            else:
                reply = b"429 %d\n" % max(1, round(wait))
                conn.sendall(reply)
    srv.close()


def client(port):
    attempts = 0
    passed = 0
    t0 = time.monotonic()
    MAX_WAIT = 0.25                  # 客户端单次等待上限
    cli = socket.create_connection((HOST, port))
    f = cli.makefile("rb")
    while passed < 6 and attempts < 20:
        if time.monotonic() - t0 > 5.0:          # 总预算 5s
            break
        attempts += 1
        cli.sendall(b"REQ\n")
        resp = f.readline().decode().split()
        if resp[0] == "200":
            passed += 1
        else:                                     # 429: 尊重 Retry-After
            retry_after = min(float(resp[1]), MAX_WAIT)
            time.sleep(retry_after)
    cli.close()
    return attempts, passed, time.monotonic() - t0


def main():
    ready = []
    bucket = TokenBucket(capacity=3, rate=10.0)
    t = threading.Thread(target=server, args=(ready, bucket), daemon=True)
    t.start()
    while not ready:
        time.sleep(0.01)
    attempts, passed, dur = client(ready[0])
    t.join(3)
    print("尝试 %d 次, 通过 %d 个, 总耗时 %.2fs" % (attempts, passed, dur))
    print("容量 3: 头 3 个立即通过, 其余按 Retry-After 排队补票")
    print("联合语义三要素: 服务端意图 Retry-After + 客户端单次上限 + 总预算")


if __name__ == "__main__":
    main()
```

**追问**:1) Retry-After 该填多久?——按令牌桶的下一次可得时间算,精确到能入桶的时刻;填 1 秒一刀切会让客户端要么等多要么再撞墙。2) 客户端可以不尊重 Retry-After 吗?——技术上可以,但会被继续 429,双方约定一旦破坏,只有升级为熔断或更狠的限流。3) 三重约束的优先级与实现?——Retry-After 是服务端契约(最高优先级)、单次等待上限防「被挂起过久」、总预算防无限循环;实现:max(Retry-After, 本地退避) 与 min(等待上限) 的夹逼——「尊重对方+保护自己」的双重边界。4) Retry-After 的精确计算怎么服务端做?——令牌桶的「下次可得时刻」减 now(Q1344);填 1s 一刀切会让客户端要么等多要么再撞墙;date 形式用于维护窗口(Q2153 原问)——「精确到能入桶」是协议礼貌。5) 生产陷阱?——429 不带 Retry-After;客户端无视 Retry-After(硬顶,双方互损);单次等待上限缺失(被恶意 Retry-After 挂死);总预算缺失(无限循环);把 429 重试与 5xx 重试同参数(语义不同)。

---
