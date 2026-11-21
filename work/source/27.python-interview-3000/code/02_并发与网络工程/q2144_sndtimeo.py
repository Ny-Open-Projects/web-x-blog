# -*- coding: utf-8 -*-
"""SO_SNDTIMEO: 发送超时与慢接收者检测。

- 接收侧停摆时, 发送缓冲区灌满, send 阻塞——慢消费者从这里开始显现;
- SO_SNDTIMEO 给每次 send 设上限, 超时返回 EAGAIN, Python 抛 BlockingIOError;
- 实测: 对端不读, 灌到内核缓冲上限后被拦, 字节数即缓冲容量快照。
"""
import socket
import struct
import threading
import time

HOST = "127.0.0.1"


def main():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    port = srv.getsockname()[1]

    def server():
        conn, _ = srv.accept()
        time.sleep(2.5)              # 故意不读: 模拟慢接收者
        conn.close()

    t = threading.Thread(target=server, daemon=True)
    t.start()
    time.sleep(0.15)

    cli = socket.create_connection((HOST, port))
    cli.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
    # 原生 SO_SNDTIMEO: timeval 结构体的秒 + 微秒
    tv = struct.pack("ll", 0, 300000)          # 0.3s
    cli.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, tv)

    chunk = b"x" * 4096
    sent = 0
    t0 = time.monotonic()
    err = None
    try:
        while True:
            sent += cli.send(chunk)
    except OSError as e:
        err = e
    dur = time.monotonic() - t0
    print("对端不读: 成功塞进内核 %d 字节后报错" % sent)
    print("错误类型:", type(err).__name__, err, "| 总耗时 %.2fs" % dur)
    print("语义: 每次 send 至多等 0.3s, 缓冲满即 BlockingIOError")

    # 对照: 对端正常读取, 永远塞得进去
    srv2 = socket.socket()
    srv2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv2.bind((HOST, 0))
    srv2.listen(1)
    port2 = srv2.getsockname()[1]

    def eater():
        conn, _ = srv2.accept()
        deadline = time.monotonic() + 1.5
        while time.monotonic() < deadline:
            conn.recv(65536)
        conn.close()

    t2 = threading.Thread(target=eater, daemon=True)
    t2.start()
    time.sleep(0.15)
    cli2 = socket.create_connection((HOST, port2))
    cli2.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, tv)
    sent2 = 0
    err2 = None
    try:
        while sent2 < 4 * 1024 * 1024:
            sent2 += cli2.send(chunk)
    except OSError as e:
        err2 = e
    print("对端在读: 塞入 %d 字节, 错误: %s" % (sent2, err2))
    cli.close()
    cli2.close()
    srv.close()
    srv2.close()
    t.join(3)
    t2.join(2)


if __name__ == "__main__":
    main()
