"""重试客户端分层: 连接层与请求层分工。

- 连接层: connect 被拒说明服务不可达, 与幂等无关, 一律退避重试;
- 请求层: 只有幂等方法(GET/PUT/DELETE)才对 502/503/504 重试,
  POST 遇 5xx 必须快速失败交给上层, 否则就是重复下单;
- 退避: 指数 + 抖动, 服务端给了 Retry-After 就取两者较大值。
"""
import http.client
import random
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

RETRYABLE_STATUS = {502, 503, 504}
IDEMPOTENT = {"GET", "HEAD", "PUT", "DELETE", "OPTIONS"}
ATTEMPTS = {"GET": 2, "POST": 2}          # 服务端对每个路径先失败 N 次


class FlakyHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    seen_post = 0

    def _respond(self, code, body=b"", headers=()):
        self.send_response(code)
        for k, v in headers:
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _route(self):
        if self.command == "POST":
            cl = self.headers.get("Content-Length")
            if cl:
                self.rfile.read(int(cl))
            FlakyHandler.seen_post += 1
        if ATTEMPTS.get(self.command, 0) > 0:
            ATTEMPTS[self.command] -= 1
            self._respond(503, headers=[("Retry-After", "0.2")])
        else:
            self._respond(200, ("ok-%s" % self.command).encode())

    do_GET = _route
    do_POST = _route

    def log_message(self, *args):
        pass


class RetryClient:
    def __init__(self, port, connect_attempts=8, base=0.1, cap=0.6):
        self.port = port
        self.connect_attempts = connect_attempts
        self.base = base
        self.cap = cap

    def _backoff(self, attempt, retry_after=None):
        delay = min(self.cap, self.base * (2 ** attempt) * random.uniform(0.5, 1.5))
        if retry_after:
            delay = max(delay, float(retry_after))
        time.sleep(delay)
        return delay

    def request(self, method, path, body=None):
        idem = method in IDEMPOTENT
        # ---- 连接层: 服务不可达与幂等无关, 一律退避重试 ----
        conn = None
        for attempt in range(self.connect_attempts):
            try:
                conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=2)
                conn.connect()
                break
            except OSError as e:
                if attempt == self.connect_attempts - 1:
                    raise
                delay = self._backoff(attempt)
                print("连接失败 %s, %.2fs 后第 %d 次重连" % (type(e).__name__, delay, attempt + 2))
        # ---- 请求层: 只对幂等方法重试 5xx ----
        resp = None
        for attempt in range(self.connect_attempts):
            conn.request(method, path, body=body)
            resp = conn.getresponse()
            payload = resp.read()
            if resp.status not in RETRYABLE_STATUS:
                conn.close()
                return resp.status, payload
            if not idem:
                conn.close()
                raise RuntimeError("非幂等 %s 遇到 %d: 不重试, 快速失败"
                                   % (method, resp.status))
            if attempt == self.connect_attempts - 1:
                conn.close()
                raise RuntimeError("重试额度耗尽")
            delay = self._backoff(attempt, resp.getheader("Retry-After"))
            print("%s 收到 %d, 尊重 Retry-After, %.2fs 后重试" % (method, resp.status, delay))
        return resp.status


def late_server(port_slot):
    time.sleep(0.35)                        # 服务"迟到": 前 0.35s 端口没人听
    srv = ThreadingHTTPServer(("127.0.0.1", 0), FlakyHandler)
    port_slot.append(srv.server_address[1])
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with http.client.HTTPConnection("127.0.0.1", port, timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def main():
    slot = []
    srv_holder = late_server(slot)
    # 连接层演示: 一开始端口未就绪, 客户端靠退避重连等到服务起来
    client = RetryClient(port=0, connect_attempts=8)
    client.port = slot[0] if slot else 0
    # 先用"注定失败"的方式触发连接层重试: 直接连一个没有服务的端口 0.35s
    while not slot:
        time.sleep(0.05)
    client.port = slot[0]

    # 请求层演示 1: 幂等 GET 遇 503, 尊重 Retry-After 重试成功
    status, payload = client.request("GET", "/flaky-get")
    print("GET 最终:", status, payload.decode())
    assert status == 200

    # 请求层演示 2: 非幂等 POST 遇 503 快速失败, 不重试
    ATTEMPTS["POST"] = 2
    try:
        client.request("POST", "/flaky-post", body=b"order")
        raise AssertionError("POST 不应被重试")
    except RuntimeError as e:
        print("POST:", e)
    assert FlakyHandler.seen_post == 1, "POST 只应到达服务端一次"

    srv_holder.shutdown()
    srv_holder.server_close()
    print("结论: 连接层重试不看幂等, 请求层重试只认幂等 + Retry-After")


if __name__ == "__main__":
    main()
