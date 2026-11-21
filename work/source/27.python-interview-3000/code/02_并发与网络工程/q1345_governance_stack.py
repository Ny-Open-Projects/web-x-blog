import http.client
import random
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class FlakyDep(BaseHTTPRequestHandler):
    state = {"n": 0}
    lock = threading.Lock()

    def do_GET(self):
        with FlakyDep.lock:
            FlakyDep.state["n"] += 1
            n = FlakyDep.state["n"]
        if n <= 4:
            self.send_response(500)
            self.send_header("Content-Length", "5")
            self.end_headers()
            self.wfile.write(b"down")
        else:
            body = f'value-{n}'.encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, *args):
        pass


class GovernedClient:
    def __init__(self, host: str, port: int) -> None:
        self.host, self.port = host, port
        self.fails = 0
        self.open_until = 0.0
        self.cache = "stale-bootstrap"   # 模拟进程启动时预热的一份陈旧值
        self.rnd = random.Random(1345)
        self.events = []

    def _http_get(self, timeout: float = 0.5) -> str:
        conn = http.client.HTTPConnection(self.host, self.port, timeout=timeout)
        try:
            conn.request("GET", "/")
            resp = conn.getresponse()
            body = resp.read().decode()
            if resp.status != 200:
                raise RuntimeError(f"HTTP {resp.status}")
            return body
        finally:
            conn.close()

    def get(self, key: str) -> tuple:
        now = time.monotonic()
        if now < self.open_until:
            self.events.append(f"{key}: 熔断打开 -> 返回 STALE {self.cache}")
            return "STALE", self.cache
        budget_end = now + 1.0                       # 总预算 1s
        attempt = 0
        while True:
            try:
                value = self._http_get()
                self.fails = 0
                self.cache = value
                src = "LIVE-RETRY" if attempt else "LIVE"
                self.events.append(f"{key}: {src} {value}")
                return src, value
            except Exception as exc:
                self.fails += 1
                attempt += 1
                if self.fails >= 3:
                    self.open_until = time.monotonic() + 0.4
                    self.fails = 0     # 打开后清零: 冷却后的失败从新窗口计数
                    self.events.append(f"{key}: 连续失败 -> 熔断 OPEN 0.4s")
                    return "STALE", self.cache
                if time.monotonic() + 0.1 > budget_end:
                    self.events.append(f"{key}: 预算耗尽({type(exc).__name__}) -> 降级")
                    return "STALE", self.cache
                backoff = self.rnd.uniform(0.02, 0.08) * (2 ** (attempt - 1))
                time.sleep(backoff)                  # full jitter 退避


def main() -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), FlakyDep)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    cli = GovernedClient("127.0.0.1", port)
    src1, v1 = cli.get("req-1")
    print(f"req-1: {src1} {v1}(依赖刚坏, 重试 3 次连败 -> 熔断打开)")
    src2, v2 = cli.get("req-2")
    print(f"req-2: {src2} {v2}(冷却期内直接走缓存)")
    src3, v3 = cli.get("req-3")
    print(f"req-3: {src3} {v3}(仍被熔断拦截)")
    time.sleep(0.45)                   # 等熔断冷却
    src4, v4 = cli.get("req-4")
    print(f"req-4: {src4} {v4}(依赖恢复, 重试转绿, 缓存刷新)")

    assert src1 == "STALE" and src2 in ("STALE",)
    assert src3 == "STALE"
    assert src4 in ("LIVE", "LIVE-RETRY") and v4.startswith("value-")
    print("--- 治理时间线 ---")
    for e in cli.events:
        print(" ", e)
    srv.shutdown()


if __name__ == "__main__":
    main()
