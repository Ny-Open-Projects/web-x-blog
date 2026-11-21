"""域级异步限流: 每主机一把信号量 + 最小请求间隔。

对多主机爬取, 全局一把信号量会把"好欺负的主机"打满而"慢主机"饿着。
正确姿势: 按主机登记 Semaphore(并发窗口) + last 请求时刻(最小间隔),
两个维度都按主机隔离。本演示对两个本机端口各抓 6 页,
验证每主机并发永不超 2。
"""
import asyncio
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        time.sleep(0.08)                # 模拟上游响应耗时
        body = b"ok"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def start_server():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv.server_address[1]


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


class HostThrottle:
    def __init__(self, concurrency=2, interval=0.06):
        self.concurrency = concurrency
        self.interval = interval
        self.state = {}

    def _host(self, key):
        if key not in self.state:
            self.state[key] = {
                "sem": asyncio.Semaphore(self.concurrency),
                "next": 0.0,
                "active": 0,
                "max": 0,
            }
        return self.state[key]

    async def fetch(self, key, port, path):
        st = self._host(key)
        async with st["sem"]:                    # 主机级并发窗口
            loop = asyncio.get_running_loop()
            wait = st["next"] - loop.time()
            if wait > 0:
                await asyncio.sleep(wait)        # 主机级最小间隔
            st["next"] = loop.time() + self.interval
            st["active"] += 1
            st["max"] = max(st["max"], st["active"])
            try:
                reader, writer = await asyncio.open_connection("127.0.0.1", port)
                writer.write(("GET %s HTTP/1.1\r\nHost: localhost\r\n"
                              "Connection: close\r\n\r\n" % path).encode())
                await writer.drain()
                data = await reader.read()
                writer.close()
                await writer.wait_closed()
                return data.split(b"\r\n", 1)[0]
            finally:
                st["active"] -= 1


async def crawl():
    throttle = HostThrottle(concurrency=2, interval=0.06)
    jobs = []
    for port in PORTS:
        for i in range(6):
            key = "localhost:%d" % port
            jobs.append(throttle.fetch(key, port, "/p%d" % i))
    results = await asyncio.gather(*jobs)
    for key, st in throttle.state.items():
        print("主机 %-16s 实际最大并发: %d, 全部 200: %s"
              % (key, st["max"], all(b"200" in r for r in results[:6])))
    return throttle.state


PORTS = []


def main():
    PORTS.append(start_server())
    PORTS.append(start_server())
    for p in PORTS:
        wait_port(p)
    state = asyncio.run(crawl())
    for key, st in state.items():
        assert st["max"] <= 2, "每主机并发不得超过窗口 2"
        assert st["max"] == 2, "窗口应当被用满而不是浪费"
    for srv_port in PORTS:
        pass
    print("结论: 并发窗口管'同时在飞', 最小间隔管'起跳节奏', 都要按主机隔离")


if __name__ == "__main__":
    main()
