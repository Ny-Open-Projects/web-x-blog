---
title: [Q1871] SO_REUSEADDR 与 TIME_WAIT:先关方持锁,重启必带选项
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1871 · SO_REUSEADDR 与 TIME_WAIT:先关方持锁,重启必带选项

> 难度:★★☆ | 标签:SO_REUSEADDR, TIME_WAIT, 运维

**问**:服务重启时经常报 Address already in use,过一会儿又能起,这是为什么?

**答**:谁先主动关闭连接,谁进入 TIME_WAIT 并持有端口约 1-4 分钟;演示让服务端先关,该端口立刻处于 TIME_WAIT 窗口,此时不带 SO_REUSEADDR 重绑会 EADDRINUSE,带选项则立即成功。

- TIME_WAIT 的存在是为了让迷路的老报文自然消亡,避免污染新连接,它不是 bug 是保护;

- SO_REUSEADDR 允许绑定处于 TIME_WAIT 的本地端口,这是重启服务的标配选项,但 '标配' 不等于乱用:监听 socket 与已连接 socket 的语义要分清;

- SO_REUSEPORT 是另一回事:多个 socket 同时 bind 同一端口做负载均衡,内核按哈希分发,别和 REUSEADDR 混为一谈。

线上排查:netstat 看 TIME_WAIT 数量,海量 TIME_WAIT 通常是本端高频短连接,该上连接池或长连接了。

```python
# file: code/02_并发与网络工程/q1871_reuseaddr_timewait.py
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
```

**追问**:1) 服务端大量 TIME_WAIT 有什么办法?——让对端先关闭(改协议时序)、开启 tcp_tw_reuse 类内核选项、或干脆复用连接;强杀进程用 SO_LINGER on+0 跳过 TIME_WAIT 是最后手段,代价是对端看到 RST。2) 「谁先关谁持锁」的协议设计含义?——服务端先关(短连接)把 TIME_WAIT 集中在服务端监听端口(可被 REUSEADDR 重绑);客户端先关把 TIME_WAIT 分散到客户端临时端口(占池,Q1319);协议里「谁主动关闭」是要显式设计的时序决策。3) tcp_tw_reuse 与 SO_REUSEADDR 的层次?——REUSEADDR 是 socket 层(允许 bind TIME_WAIT 地址,监听侧);tcp_tw_reuse 是内核层(出站连接复用 TIME_WAIT 四元组,需时间戳);客户端侧端口耗尽靠后者,服务端重启靠前者——层次混用是常见误解。4) 生产陷阱?——REUSEADDR 当万能(不能让两个活跃进程同监听,那是 REUSEPORT);SO_LINGER on+0 跳 TIME_WAIT(对端 RST,最后手段,见原问);客户端临时端口耗尽被误判为服务端问题;TIME_WAIT 大量堆积直接调内核参数而不优化连接复用。


---
