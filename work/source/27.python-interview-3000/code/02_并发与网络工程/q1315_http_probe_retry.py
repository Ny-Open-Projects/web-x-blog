import http.client
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class FlakyApp(BaseHTTPRequestHandler):
    hits = {"n": 0}
    lock = threading.Lock()

    def do_GET(self):
        with self.lock:
            FlakyApp.hits["n"] += 1
            n = FlakyApp.hits["n"]
        if self.path == "/health" and n <= 2:
            self.send_response(503)
            self.send_header("Retry-After", "1")
            self.end_headers()
            self.wfile.write(b"warming up")
        elif self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"no route")

    def log_message(self, *args):
        pass


def classify(status: int) -> tuple:
    if 200 <= status < 300:
        return "healthy", False
    if status in (429, 503):
        return "throttled", True     # 尊重 Retry-After 退避重试
    if 500 <= status < 600:
        return "server_error", True
    return "client_error", False     # 4xx 重试无意义


def probe(host: str, port: int, path: str, max_attempts: int = 3) -> dict:
    attempts = []
    verdict = None
    for i in range(1, max_attempts + 1):
        conn = http.client.HTTPConnection(host, port, timeout=2)
        try:
            conn.request("GET", path)
            resp = conn.getresponse()
            body = resp.read()
            status = resp.status
            retry_after = resp.getheader("Retry-After")
        finally:
            conn.close()
        kind, retryable = classify(status)
        attempts.append(status)
        print(f"  第 {i} 次探测: {status} -> {kind}")
        if not retryable:
            verdict = kind
            break
        if i < max_attempts:
            wait = float(retry_after) if retry_after else 0.1
            time.sleep(min(wait, 0.1))   # 演示加速, 真实应尊重原值
    if verdict is None:
        verdict = "unhealthy_after_retries"
    return {"path": path, "attempts": attempts, "verdict": verdict}


def main() -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), FlakyApp)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    print("/health 前 2 次 503:")
    r1 = probe("127.0.0.1", port, "/health")
    print(f"结论: {r1['verdict']}, 共尝试 {len(r1['attempts'])} 次")
    assert r1["verdict"] == "healthy"

    print("/missing 路径 404:")
    r2 = probe("127.0.0.1", port, "/missing")
    print(f"结论: {r2['verdict']}, 只尝试 {len(r2['attempts'])} 次就放弃")
    assert r2["verdict"] == "client_error" and len(r2["attempts"]) == 1
    srv.shutdown()


if __name__ == "__main__":
    main()
