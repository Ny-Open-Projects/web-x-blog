# -*- coding: utf-8 -*-
"""connect/bind/recv 错误实验台: 三种最常见的 socket errno, 各有各的病因。

- ECONNREFUSED: 目标端口无人监听, 内核直接回 RST, 立刻失败而非超时;
- EADDRINUSE: 本地地址端口已被占用, bind 阶段失败;
- ENOTCONN: 未建立连接就 recv, 操作顺序错误的典型。
"""
import errno
import socket


def free_tcp_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()                                  # 关闭后端口短暂无人监听
    return port


def main():
    # ECONNREFUSED: 连一个没人监听的端口
    dead_port = free_tcp_port()
    try:
        socket.create_connection(("127.0.0.1", dead_port), timeout=1.0)
        raise AssertionError("不应连上")
    except OSError as e:
        print("连接无监听端口: %s errno=%d %s"
              % (type(e).__name__, e.errno, errno.errorcode.get(e.errno)))
        assert isinstance(e, ConnectionRefusedError)
        assert e.errno == errno.ECONNREFUSED

    # EADDRINUSE: 两个 socket 绑同一地址端口
    a = socket.socket()
    a.bind(("127.0.0.1", 0))
    port = a.getsockname()[1]
    b = socket.socket()
    try:
        b.bind(("127.0.0.1", port))
        raise AssertionError("重复 bind 不应成功")
    except OSError as e:
        print("重复 bind: %s errno=%d %s"
              % (type(e).__name__, e.errno, errno.errorcode.get(e.errno)))
        assert e.errno == errno.EADDRINUSE

    # ENOTCONN: 未连接就 recv
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        c.recv(10)
        raise AssertionError("未连接 recv 不应成功")
    except OSError as e:
        print("未连接 recv: %s errno=%d %s"
              % (type(e).__name__, e.errno, errno.errorcode.get(e.errno)))
        assert e.errno == errno.ENOTCONN

    a.close()
    b.close()
    c.close()
    print("结论: 拒绝是对方给的, 占用是自己的锅, 未连接是顺序错误")


if __name__ == "__main__":
    main()
