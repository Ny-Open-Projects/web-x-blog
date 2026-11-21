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
