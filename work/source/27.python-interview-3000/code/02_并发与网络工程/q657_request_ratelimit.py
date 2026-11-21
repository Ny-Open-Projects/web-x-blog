import socket
import threading
import time


class TokenBucket:
    def __init__(self, rate: float, burst: int) -> None:
        self.rate = rate          # 每秒补充令牌
        self.burst = burst        # 桶容量
        self.tokens = float(burst)
        self.last = time.monotonic()

    def take(self) -> bool:
        now = time.monotonic()
        self.tokens = min(self.burst, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def retry_after(self) -> float:
        return max(0.0, (1 - self.tokens) / self.rate)


class RateLimitServer:
    def __init__(self) -> None:
        self.buckets: dict = {}

    def check(self, key: str) -> tuple:
        bucket = self.buckets.setdefault(key, TokenBucket(rate=5, burst=5))
        if bucket.take():
            return True, 0.0
        return False, bucket.retry_after()


def server(stop: threading.Event, port_box: list, limiter: RateLimitServer) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        try:
            conn.settimeout(2)
            data = conn.recv(1024)
            key = addr[0]
            ok, retry = limiter.check(key)
            if ok:
                conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 3\r\n\r\nok\n")
            else:
                body = f"rate limited, retry after {retry:.2f}s".encode()
                conn.sendall(
                    b"HTTP/1.1 429 Too Many Requests\r\n"
                    + f"Retry-After: {retry:.0f}\r\n".encode()
                    + f"Content-Length: {len(body)}\r\n\r\n".encode() + body
                )
        except OSError:
            pass
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    limiter = RateLimitServer()
    threading.Thread(target=server, args=(stop, box, limiter), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    print("突发 8 个请求 (rate=5/s, burst=5):")
    for i in range(8):
        c = socket.create_connection(("127.0.0.1", port), timeout=2)
        c.sendall(b"GET /api HTTP/1.1\r\nHost: x\r\n\r\n")
        c.settimeout(2)
        resp = c.recv(1024)
        status = resp.split(b"\r\n")[0].decode()
        c.close()
        print(f"  req{i}: {status}")
        time.sleep(0.02)

    time.sleep(0.5)  # 等令牌回填
    c = socket.create_connection(("127.0.0.1", port), timeout=2)
    c.sendall(b"GET /api HTTP/1.1\r\nHost: x\r\n\r\n")
    print("0.5s 后:", c.recv(64).split(b"\r\n")[0].decode())
    c.close()
    stop.set()
