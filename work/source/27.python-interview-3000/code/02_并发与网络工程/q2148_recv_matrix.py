# -*- coding: utf-8 -*-
"""recv 返回值矩阵: 数据、EOF、超时与 MSG_PEEK。

- recv 有四种结局: 返回数据、返回 b'' (对端关闭)、抛 timeout、抛错误;
- b'' 是 EOF 信号, 不是错误, 忘记区分就会把正常关连当故障;
- MSG_PEEK 窥视不消费, 用于先探类型再决定读多少。
"""
import socket
import threading
import time

HOST = "127.0.0.1"


def main():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    port = srv.getsockname()[1]

    cli = socket.create_connection((HOST, port))
    conn, _ = srv.accept()

    # 1. 部分数据: recv(4) 只读到 2 字节
    conn.send(b"ab")
    time.sleep(0.15)
    part = cli.recv(4)
    print("recv(4) 只有 2 字节 -> %r (部分读, 无阻塞到凑满)" % part)

    # 2. MSG_PEEK: 窥视不消费
    conn.send(b"cdef")
    time.sleep(0.15)
    peek = cli.recv(4, socket.MSG_PEEK)
    again = cli.recv(4)
    print("MSG_PEEK 得到 %r, 再 recv 又得到 %r (窥视不消费)" %
          (peek, again))

    # 3. 超时: 对端安静
    cli.settimeout(0.3)
    t0 = time.monotonic()
    try:
        cli.recv(4)
        print("意外: 安静期居然有数据")
    except socket.timeout as e:
        print("安静期 recv -> socket.timeout, 耗时 %.2fs" %
              (time.monotonic() - t0))

    # 4. EOF: 对端 shutdown 写半边
    conn.shutdown(socket.SHUT_WR)
    eof = cli.recv(4)
    eof2 = cli.recv(4)
    print("对端半关闭后 recv -> %r, 再 recv -> %r (EOF 信号)" %
          (eof, eof2))

    cli.close()
    conn.close()
    srv.close()
    print("处理口诀: 有数据用数据, b'' 做关闭, timeout 做重试, 其他错误做告警")


if __name__ == "__main__":
    main()
