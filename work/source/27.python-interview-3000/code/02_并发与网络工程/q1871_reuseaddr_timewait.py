# -*- coding: utf-8 -*-
"""SO_REUSEADDR 与 TIME_WAIT: 先关的一方进 TIME_WAIT, 重绑必须带选项。

- 谁先主动关闭, 谁持有 TIME_WAIT: 服务端先关连接, 服务端口进入 TIME_WAIT;
- TIME_WAIT 未过期时, 不带 SO_REUSEADDR 重绑同端口会 EADDRINUSE;
- 带 SO_REUSEADDR 则允许重绑, 这就是重启服务的标配选项。
"""
import errno
import socket
import threading
import time


def main():
    # 第一步: 建立连接, 服务端先关闭, 制造服务端侧 TIME_WAIT
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]

    cli = socket.socket()
    cli.connect(("127.0.0.1", port))
    conn, _ = srv.accept()

    conn.close()                               # 服务端先关 -> 服务端口 TIME_WAIT
    cli.close()
    srv.close()
    print("连接已由服务端先关闭, 该端口立刻处于 TIME_WAIT 窗口内")

    # 第二步: 不带 SO_REUSEADDR 立即重绑 -> EADDRINUSE
    s2 = socket.socket()
    try:
        s2.bind(("127.0.0.1", port))
        s2.close()
        print("警告: 本机允许无选项重绑, TIME_WAIT 语义较弱")
        no_reuse_rejected = False
    except OSError as e:
        no_reuse_rejected = True
        print("无选项重绑被拒: errno=%d %s" % (e.errno, errno.errorcode.get(e.errno)))
        assert e.errno == errno.EADDRINUSE

    # 第三步: 带 SO_REUSEADDR 重绑成功
    s3 = socket.socket()
    s3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s3.bind(("127.0.0.1", port))
    s3.listen(1)
    print("SO_REUSEADDR 重绑同一端口成功")
    s3.close()

    # 复用被拒时才谈得上演示价值; 若本机语义弱, 也已验证选项无害
    print("无选项被拒: %s" % no_reuse_rejected)
    print("结论: TIME_WAIT 是给主动关闭方的; REUSEADDR 是重启服务的救命选项")


if __name__ == "__main__":
    main()
