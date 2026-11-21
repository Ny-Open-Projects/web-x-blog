---
title: [Q1344] 429 与 Retry-After:服务端的礼貌拒绝
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1344 · 429 与 Retry-After:服务端的礼貌拒绝

> 难度:★★★☆ | 标签:429, Retry-After, 限流

**问**:限流触发时,只返回状态码 429 够吗?客户端该怎么配合?

**答**:429 只告诉客户端"被拒了",Retry-After 才告诉它"什么时候再来"——前者是判决,后者是出路。服务端按客户端粒度维护令牌桶,拒绝时计算"下次有令牌的最早时刻",换算成 Retry-After 秒数(或 HTTP-date);客户端的礼貌姿势是:收到 429 严格按 Retry-After 等待后重试,而不是立刻硬顶。配合失败会发生什么?客户端硬重试 × 服务端限流 = 请求全变成无效流量,双方都在消耗资源处理注定失败的事。下面的演示同一个限流服务,粗鲁客户端与礼貌客户端的行为对比:粗鲁的一堆 429,礼貌的全员 200 且总请求数更少。

```python
# file: code/02_并发与网络工程/q1344_429_retry_after.py
import http.client
import math
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

RATE = 5.0
BURST = 5


class RateLimitedApp(BaseHTTPRequestHandler):
    bucket = {"tokens": BURST, "last": time.monotonic()}
    lock = threading.Lock()

    def do_GET(self):
        with RateLimitedApp.lock:
            now = time.monotonic()
            b = RateLimitedApp.bucket
            b["tokens"] = min(BURST, b["tokens"] + (now - b["last"]) * RATE)
            b["last"] = now
            if b["tokens"] >= 1:
                b["tokens"] -= 1
                self.send_response(200)
                self.send_header("Content-Length", "2")
                self.end_headers()
                self.wfile.write(b"ok")
                return
            wait = (1 - b["tokens"]) / RATE
        self.send_response(429)
        self.send_header("Retry-After", str(math.ceil(wait * 10) / 10))
        self.send_header("Content-Length", "8")
        self.end_headers()
        self.wfile.write(b"throttle")

    def log_message(self, *args):
        pass


def burst(port: int, n: int) -> list:
    out = []
    for _ in range(n):
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("GET", "/")
        resp = conn.getresponse()
        resp.read()
        out.append((resp.status, resp.getheader("Retry-After")))
        conn.close()
    return out


def main() -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), RateLimitedApp)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    RateLimitedApp.bucket.update(tokens=BURST, last=time.monotonic() - 10)

    rude = burst(port, 10)
    rude_429 = sum(1 for s, _ in rude if s == 429)
    print(f"粗鲁客户端: 连发 10 个 -> {rude_429} 个 429, "
          f"Retry-After 样例 {next((ra for s, ra in rude if s == 429), None)}s")

    time.sleep(1.2)                    # 桶回满
    RateLimitedApp.bucket.update(tokens=BURST, last=time.monotonic() - 10)

    polite = []
    for _ in range(10):
        out = burst(port, 1)[0]
        if out[0] == 429:
            time.sleep(float(out[1]))  # 严格按 Retry-After 等待
            out = burst(port, 1)[0]
        polite.append(out[0])
    print(f"礼貌客户端: 10 次业务请求 -> 429 出现 {polite.count(429)} 次, 最终 200 {polite.count(200)} 个")
    assert polite == [200] * 10
    assert rude_429 >= 4
    print("结论: 429+Retry-After 是限流的完整契约, 服务端给判决也给出路, 客户端照办")


if __name__ == "__main__":
    main()
```

**追问**:1) Retry-After 用秒数还是 HTTP-date?——秒数适合"相对时长"(过载恢复类),date 适合"确定时刻"(计划内维护窗口);两者都合法,秒数对客户端时钟不敏感,优先用。2) 客户端的礼貌姿势的完整规则?——收到 429 严格按 Retry-After 等(没有就退避+抖动);重试同样受重试预算约束(Q1306);连续 429 要降速率而不是硬顶——「限流是协作协议」:服务端给出路,客户端守规则,任何一方违约都是互损。3) 秒数与 date 怎么选(见原问的展开)?——秒数对客户端时钟不敏感,过载恢复类首选;date 适合计划维护窗口(精确时刻);实现端注意 Retry-After 可能在代理层被剥掉,客户端要处理「429 无 Retry-After」的退让路径。4) 生产陷阱?——服务端限流响应不带 Retry-After(客户端只能盲试);客户端把 429 当 5xx 重试(语义全错,限流是「稍后再来」不是「我坏了」);限流指标与 Retry-After 计算脱节(告诉客户端 10s 后再来,10s 后照样满额被拒);全局 429 与按租户 429 混用,告警归因失真。

---
