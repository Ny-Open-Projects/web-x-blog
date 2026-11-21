# -*- coding: utf-8 -*-
"""综合设计: 迷你服务治理台。

- 一个回环 HTTP 服务: 健康端点、令牌桶限流的业务端点、指标端点;
- 客户端: 代理绕行 + 健康探测指数回退 + 尊重 Retry-After 的突发;
- 收尾: 优雅停机与最终指标对账, 把本篇的治理件串成一条链。
"""
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import build_opener, ProxyHandler
from urllib.error import HTTPError

metrics = {"requests_total": 0, "rejected_total": 0, "in_flight": 0}
lock = threading.Lock()
bucket = {"tokens": 3.0, "cap": 3.0, "rate": 10.0, "ts": time.monotonic()}


def take_token():
    with lock:
        now = time.monotonic()
        bucket["tokens"] = min(bucket["cap"],
                               bucket["tokens"] +
                               (now - bucket["ts"]) * bucket["rate"])
        bucket["ts"] = now
        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True, 0
        return False, (1 - bucket["tokens"]) / bucket["rate"]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _json(self, code, payload, extra=None):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._json(200, {"status": "ok"})
        elif self.path == "/work":
            with lock:
                metrics["requests_total"] += 1
                metrics["in_flight"] += 1
            ok, wait = take_token()
            with lock:
                metrics["in_flight"] -= 1
            if ok:
                self._json(200, {"done": True})
            else:
                with lock:
                    metrics["rejected_total"] += 1
                self._json(429, {"done": False},
                           {"Retry-After": str(max(1, round(wait)))})
        elif self.path == "/metrics":
            with lock:
                self._json(200, dict(metrics))
        else:
            self._json(404, {"error": "not found"})


def wait_ready(opener, base, timeout=3.0):
    interval = 0.05
    t0 = time.monotonic()
    while time.monotonic() - t0 < timeout:
        try:
            r = opener.open(base + "/health", timeout=0.5)
            if r.status == 200:
                return time.monotonic() - t0
        except Exception:
            pass
        time.sleep(interval)
        interval = min(0.4, interval * 2)      # 探测回退
    raise RuntimeError("服务未就绪")


def burst(opener, base, n=6):
    ok = rejected = 0
    for _ in range(n):
        try:
            r = opener.open(base + "/work", timeout=1.0)
            if r.status == 200:
                ok += 1
        except HTTPError as e:
            if e.code == 429:
                rejected += 1
                wait = min(float(e.headers.get("Retry-After", "1")), 0.25)
                time.sleep(wait)               # 尊重 Retry-After, 有上限
                try:                           # 补一次尝试
                    r2 = opener.open(base + "/work", timeout=1.0)
                    if r2.status == 200:
                        ok += 1
                except HTTPError:
                    pass
    return ok, rejected


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_address[1]
    base = "http://127.0.0.1:%d" % port
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    opener = build_opener(ProxyHandler({}))    # 绕过环境代理
    ready_in = wait_ready(opener, base)
    print("服务就绪, 探测耗时 %.2fs" % ready_in)

    ok, rejected = burst(opener, base)
    print("突发 6 请求: 通过 %d, 429 %d (按 Retry-After 分批入场)" %
          (ok, rejected))

    m = json.loads(opener.open(base + "/metrics", timeout=1).read())
    print("指标端点:", m)
    server.shutdown()                          # 优雅停机: 停止 accept
    server.server_close()
    t.join(3)
    print("停机完成, 线程存活:", t.is_alive())


if __name__ == "__main__":
    main()
