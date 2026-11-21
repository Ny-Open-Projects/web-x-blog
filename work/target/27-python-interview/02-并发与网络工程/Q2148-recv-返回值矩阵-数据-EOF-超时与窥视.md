---
title: [Q2148] recv 返回值矩阵:数据、EOF、超时与窥视
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2148 · recv 返回值矩阵:数据、EOF、超时与窥视

> 难度:★★☆ | 标签:recv, EOF, MSG_PEEK, 超时

**问**:recv 这个调用有几种结局?分别该怎么处理?

**答**:四种:返回数据(可能少于请求量)、返回 b''(对端关闭)、抛 socket.timeout(超时)、抛 OSError(真故障);矩阵齐了,连接管理才不慌。

- 实测部分读:send 2 字节,recv(4) 立即返回 2 字节,不会硬等凑满;

- MSG_PEEK 窥视不消费,同一份数据第二次 recv 原样拿到;

- 静默期超时抛 socket.timeout,耗时与设定一致;

- 对端 shutdown 写半边后 recv 连续返回 b'',这是 EOF 信号而非错误。

```python
# file: code/02_并发与网络工程/q2148_recv_matrix.py
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
```

**追问**:1) b'' 后再 recv 会怎样?——继续返回 b'',不会抛错;协议层把它当关闭信号跳出读循环。2) MSG_PEEK 的典型用途?——嗅探首字节决定走明文还是 TLS(如 STARTTLS 端口复用),以及探测包类型再决定缓冲区大小。3) 四种结局的处理矩阵怎么落成代码结构?——数据→业务;EOF(b'')→正常关闭(跳出读循环,Q664);timeout→视场景(继续等/心跳检查);OSError→分类(Q1311)后断连——「结局即分支」,switch 化的读循环比 if-else 堆叠可测。4) MSG_PEEK 的典型应用与风险?——嗅探首字节决定协议分支(明文 vs TLS,STARTTLS 端口复用);探测包类型定缓冲大小;风险:peek 后忘记正常读(数据滞留),peek+超时的组合在不同平台行为差异——peek 是探针不是读取。5) 生产陷阱?——把 b'' 当错误(正常关连被当故障重试);partial read 当错误(正常);timeout 无限重抛不推进(假死循环);MSG_PEEK 后缓冲处理错位;recv 大小设太大(内存)或太小( syscall 频繁)。

---
