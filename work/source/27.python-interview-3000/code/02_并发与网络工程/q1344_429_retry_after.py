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
