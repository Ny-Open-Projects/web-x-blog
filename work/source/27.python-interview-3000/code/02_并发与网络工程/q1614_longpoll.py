"""长轮询: 挂起请求与准实时推送。

没有 WebSocket 时, 长轮询是 HTTP 上的准实时方案:
- 客户端 GET /poll?wait=3, 服务端"握着"请求不回, 直到有消息或超时;
- 消息一到, 立刻唤醒挂起的请求返回, 延迟 = 事件延迟而非轮询间隔;
- 对比短轮询: 没消息也要白跑 N 次; 长轮询空转期只有一条挂起的连接。
"""
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Channel:
    def __init__(self):
        self.event = threading.Event()
        self.message = None
        self.lock = threading.Lock()

    def send(self, msg):
        with self.lock:
            self.message = msg
            self.event.set()            # 唤醒所有挂起的 poll

    def poll(self, wait):
        got = self.event.wait(wait)     # 请求在这里"挂起"
        with self.lock:
            if got:
                msg, self.message = self.message, None
                self.event.clear()
            else:
                msg = None
        return got, msg


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    channel = None

    def _respond(self, code, body):
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parts = urllib.parse.urlsplit(self.path)
        qs = urllib.parse.parse_qs(parts.query)
        if parts.path == "/poll":
            wait = float(qs.get("wait", ["2"])[0])
            got, msg = Handler.channel.poll(wait)
            body = ("msg=%s" % msg).encode() if got else b"timeout"
            self._respond(200, body)
        elif parts.path == "/send":
            Handler.channel.send(qs.get("m", ["x"])[0])
            self._respond(200, b"sent")
        else:
            self._respond(404, b"not found")

    def log_message(self, *args):
        pass


def main():
    Handler.channel = Channel()
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    result = {}

    def poller():
        t0 = time.monotonic()
        resp = opener.open("http://127.0.0.1:%d/poll?wait=3" % port, timeout=10)
        result["body"] = resp.read().decode()
        result["latency"] = time.monotonic() - t0
        resp.close()

    t = threading.Thread(target=poller)
    t.start()
    time.sleep(0.3)                     # 先让 poll 挂起
    opener.open("http://127.0.0.1:%d/send?m=hello" % port, timeout=2).close()
    t.join(timeout=5)

    print("长轮询返回:", result["body"], "| 延迟 %.2fs" % result["latency"])
    assert result["body"] == "msg=hello"
    assert result["latency"] < 1.5, "消息到达应立刻唤醒, 而不是等满超时"

    # 空闲期: 没有消息, 请求按 wait 超时返回
    t0 = time.monotonic()
    resp = opener.open("http://127.0.0.1:%d/poll?wait=0.5" % port, timeout=10)
    body = resp.read().decode()
    resp.close()
    idle = time.monotonic() - t0
    print("空闲轮询返回:", body, "| 耗时 %.2fs" % idle)
    assert body == "timeout" and 0.4 < idle < 1.2, "空闲期应按 wait 挂到超时"

    srv.shutdown()
    srv.server_close()
    print("结论: 长轮询 = 服务端挂住请求 + 事件到达即唤醒, 延迟与空转都最优")


if __name__ == "__main__":
    main()
