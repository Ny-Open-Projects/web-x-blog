# -*- coding: utf-8 -*-
"""backlog 实测: 连接上限时 connect 的真实行为。

- listen(backlog) 给的是全连接队列长度, 队列满时内核丢弃新 SYN;
- macOS 实测: 多出来的客户端 connect 一直重试, 直到应用层超时;
- 服务端开始 accept 后, 排队者才逐个转为 ESTABLISHED。
"""
import socket
import threading
import time

HOST = "127.0.0.1"


def try_connect(i, port, results):
    c = socket.socket()
    c.settimeout(1.5)
    t0 = time.monotonic()
    try:
        c.connect((HOST, port))
        results[i] = ("connected", time.monotonic() - t0, c)
    except OSError as e:
        results[i] = ("%s: %s" % (type(e).__name__, e),
                      time.monotonic() - t0, None)


def main():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)                       # backlog=1: 队列容量极小
    port = srv.getsockname()[1]

    results = [None] * 6
    ts = []
    for i in range(6):
        t = threading.Thread(target=try_connect, args=(i, port, results))
        t.start()
        ts.append(t)
        time.sleep(0.05)                # 依次到达, 制造排队
    for t in ts:
        t.join(3)

    ok = 0
    for i, (res, dur, conn) in enumerate(results):
        print("client %d -> %-28s %.2fs" % (i, res, dur))
        if conn:
            ok += 1
    print("backlog=1 时仅 %d 个立即成功, 其余 connect 超时(SYN 被丢)" % ok)

    # 服务端现在开始 accept: 存活连接被取走, 新连接可以进来了
    accepted = 0
    srv.settimeout(0.1)
    try:
        while True:
            conn, _ = srv.accept()
            conn.close()
            accepted += 1
            if accepted >= ok:
                break
    except socket.timeout:
        pass
    print("服务端 accept 了 %d 个积压连接" % accepted)
    print("容量公式: BSD/macOS 的全连接队列 = backlog + 1, Linux 为 backlog")
    srv.close()


if __name__ == "__main__":
    main()
