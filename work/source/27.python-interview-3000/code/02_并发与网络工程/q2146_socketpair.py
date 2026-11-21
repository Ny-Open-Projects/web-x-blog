# -*- coding: utf-8 -*-
"""socketpair: 本机双工管道, 线程与子进程的私有通道。

- os.socketpair 返回一对已连接的匿名 AF_UNIX/AF_LOCAL 套接字;
- 双向全双工, 无端口无名字, 是线程间和 fork 后父子间的自带管道;
- 比普通 pipe 强在双向且有字节流语义, 比 TCP 少一整套协议栈。
"""
import os
import socket
import threading
import time


def echo_worker(sock, stats):
    """工作线程: 从自己的那一端收, 原样回, 直到对端半关闭。"""
    sock.settimeout(3.0)
    try:
        for _ in range(3):
            data = sock.recv(1024)
            stats.append((time.monotonic(), data))
            sock.sendall(b"echo:" + data)
        while sock.recv(1024):        # 半关闭后 recv 回 b'', 循环退出
            pass
    except socket.timeout:
        pass
    finally:
        sock.close()


def main():
    parent_sock, child_sock = socket.socketpair(socket.AF_UNIX,
                                                socket.SOCK_STREAM)
    print("socketpair fd: parent=%d child=%d" %
          (parent_sock.fileno(), child_sock.fileno()))

    stats = []
    t = threading.Thread(target=echo_worker, args=(child_sock, stats))
    t.start()

    for msg in (b"ping-1", b"ping-2", b"ping-3"):
        t0 = time.monotonic()
        parent_sock.sendall(msg)
        reply = parent_sock.recv(1024)
        print("发出 %-8s 收到 %-16s RTT %.3fms" %
              (msg.decode(), reply.decode(),
               (time.monotonic() - t0) * 1000))

    parent_sock.shutdown(socket.SHUT_WR)     # 半关闭: 通知对端没有更多数据
    t.join(3)
    print("对端收到 EOF 后自行退出, join 正常返回")
    parent_sock.close()

    for ts, data in stats:
        print("工作线程收到:", data.decode())
    print("双向各走一遍: 全双工成立, 无端口无路由, 延迟最低")
    print("fork 后父子各持一端, 就是最经典的进程内 IPC 用法")


if __name__ == "__main__":
    main()
