---
title: [Q1872] connect/bind/recv 错误实验台:三种 errno 各有各的病因
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1872 · connect/bind/recv 错误实验台:三种 errno 各有各的病因

> 难度:★★★ | 标签:errno, 排障, socket

**问**:Connection refused、Address already in use、ENOTCONN,这三个错误各自的病因和排查方向是什么?

**答**:ECONNREFUSED 是对方给的:目标端口无人监听,内核直接回 RST,客户端立刻失败——注意它和 connect 超时不同,refused 是 '明确拒绝',超时是 '路上丢了',排查方向完全不同。

- EADDRINUSE 是自己的锅:本地地址端口被占,bind 阶段失败;要么是另一个进程占着,要么是 TIME_WAIT 没带 SO_REUSEADDR;

- ENOTCONN 是顺序错误:没建立连接就 recv,这类错误说明状态机写漏了分支;

- 实验台用 errno 模块把错误码显式断言:61/48/57,错误分类写进告警规则,排障时一眼定位层面。

好习惯:网络层异常按 errno 分类打点,refused 计数、timeout 计数、reset 计数分开,告警才有语义。

```python
# file: code/02_并发与网络工程/q1872_errno_lab.py
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
```

**追问**:1) ECONNREFUSED 为什么比 connect 超时 '好'?——refused 意味着路由通、主机活、只是端口没人听,重试有意义;超时可能是网络黑洞,重试只是放大流量,两者的重试策略应该不同。2) 「refused 比超时好」的重试策略差异怎么落地?——refused(路由通、端口没人听):短退避重试(服务可能在启动);超时(黑洞):先降频探测(重试只是放大流量),要查网络;错误分类驱动重试策略(Q1311 分诊表的工程化落地)。3) errno 分类怎么进告警规则?——ECONNREFUSED 归服务部署告警;EADDRINUSE 归配置/部署;ENOTCONN 归代码缺陷(状态机漏分支);错误码显式断言(实验台的做法)推广到生产日志:分类计数器让「错误类型分布」可观测。4) 生产陷阱?——所有 OSError 一个 except(分类全丢);把 EADDRINUSE 重试(端口占用重试无意义,要人工/部署介入);ENOTCONN 当网络问题排查(是顺序 bug);refused 与 timeout 合并成「连接失败」指标(归因混乱)。


---
