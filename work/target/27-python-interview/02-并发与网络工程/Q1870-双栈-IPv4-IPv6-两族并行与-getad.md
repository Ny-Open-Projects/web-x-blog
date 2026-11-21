---
title: [Q1870] 双栈 IPv4/IPv6:两族并行与 getaddrinfo 选路
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1870 · 双栈 IPv4/IPv6:两族并行与 getaddrinfo 选路

> 难度:★★★ | 标签:IPv6, 双栈, getaddrinfo

**问**:服务要同时支持 IPv4 和 IPv6,是开两个 socket 还是开一个?

**答**:AF_INET 与 AF_INET6 是两个平行世界,端口号相同也不互通,演示里 v4 socket 连 v6 监听直接被拒。

- 姿势一:两族各一个 socket 各自 bind,代码直白,端口可以共用;

- 姿势二:一个 AF_INET6 socket 设 IPV6_V6ONLY=0,内核把 v4 连接映射为 v4-mapped 地址,一把监听服务两族;macOS 与 Linux 默认值不同,必须显式设置;

- 地址解析统一走 getaddrinfo,它返回的列表按优先级排序,客户端遍历列表逐个尝试是标准写法(Happy Eyeballs 的基础)。

演示在本机 ::1 与 127.0.0.1 各起回声服务,各自回声正确,跨族连接按预期失败。

```python
# file: code/02_并发与网络工程/q1870_dual_stack.py
# -*- coding: utf-8 -*-
"""双栈 IPv4/IPv6: 两个协议族各自监听, getaddrinfo 选路, ::1 与 127.0.0.1 并存。

- AF_INET 与 AF_INET6 是两个平行世界, 端口号相同也不互通;
- 双栈服务的两种姿势: 各族一个 socket, 或 AF_INET6 设 IPV6_V6ONLY=0 一把抓;
- getaddrinfo 是地址族无关的入口, 遍历返回列表逐个尝试是标准写法。
"""
import socket
import threading
import time


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def start_echo(family, bind_addr):
    srv = socket.socket(family, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if family == socket.AF_INET6:
        srv.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
    srv.bind((bind_addr, 0))
    srv.listen(5)

    def serve():
        srv.settimeout(0.2)
        while True:
            try:
                conn, addr = srv.accept()
            except socket.timeout:
                continue
            conn.settimeout(2.0)

            def pump(c, a):
                try:
                    data = c.recv(1024)
                    c.sendall(b"echo-v4:" + data if c.family == socket.AF_INET
                              else b"echo-v6:" + data)
                except OSError:
                    pass
                c.close()

            threading.Thread(target=pump, args=(conn, addr), daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    return srv


def main():
    addrinfos = socket.getaddrinfo("localhost", None, proto=socket.IPPROTO_TCP)
    families = sorted({ai[0] for ai in addrinfos})
    print("localhost 解析出的地址族:", families)

    srv4 = start_echo(socket.AF_INET, "127.0.0.1")
    port4 = srv4.getsockname()[1]
    assert wait_port(port4), "v4 回环应可连"

    srv6 = None
    v6_ok = False
    if socket.has_ipv6:
        try:
            srv6 = start_echo(socket.AF_INET6, "::1")
            port6 = srv6.getsockname()[1]
            c6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            c6.settimeout(2.0)
            c6.connect(("::1", port6))
            c6.sendall(b"hi6")
            resp6 = c6.recv(1024)
            local6 = c6.getsockname()          # 关闭前取, 关闭后调会 EBADF
            c6.close()
            print("v6 回环: %s (本地地址 %s)" % (resp6.decode(), local6))
            v6_ok = True
        except OSError as e:
            print("本机不支持 IPv6 回环, 跳过:", e)

    c4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c4.settimeout(2.0)
    c4.connect(("127.0.0.1", port4))
    c4.sendall(b"hi4")
    resp4 = c4.recv(1024)
    c4.close()
    print("v4 回环: %s" % resp4.decode())
    assert resp4 == b"echo-v4:hi4"

    # 两个世界互不通行
    if srv6 is not None:
        try:
            cx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cx.settimeout(1.0)
            cx.connect(("127.0.0.1", srv6.getsockname()[1]))
            cx.close()
            raise AssertionError("v4 socket 不应连上 v6 监听")
        except OSError as e:
            print("跨族连接被拒绝:", e)
            assert resp6 == b"echo-v6:hi6"
            print("结论: 同一端口号, 两族各自为政, 双栈服务就是两把监听或一把 V6ONLY=0")
    else:
        print("结论: 双栈概念成立, 本机缺 IPv6 回环时 v4 路径同样成立")

    srv4.close()
    if srv6:
        srv6.close()


if __name__ == "__main__":
    main()
```

**追问**:1) V6ONLY=0 的映射有什么坑?——v4 连接在应用里看到的是 ::ffff:x.x.x.x 形式的 v4-mapped 地址,ACL 与日志按字符串前缀匹配会漏;安全敏感的监听建议 V6ONLY=1 双 socket,语义更清晰。2) V6ONLY=0 的 v4-mapped 地址对 ACL 的影响?——v4 连接看到 ::ffff:x.x.x.x,按字符串前缀匹配 ACL(如拒绝 192.168.)会漏 mapped 形式;安全监听建议 V6ONLY=1 双 socket,语义清晰;日志与监控同样要归一化 mapped 地址。3) getaddrinfo 的客户端遍历怎么写才健壮?——按返回顺序逐个尝试(独立超时),记住 last-good(Q1312);服务器侧用 AI_PASSIVE+通配地址绑定;客户端 v6 不通时的回退延迟是双栈常见性能坑(Q641)——双栈的「解析选路」比「socket 开几个」更容易出事。4) 生产陷阱?——V6ONLY 默认值平台差异没显式设置(macOS/Linux 不同);端口冲突(两族同一端口只在一族 bind);v4-mapped 地址进 ACL;解析结果只用第一个地址(无故障转移);IPv6-only 环境没测试(双栈代码在 v6-only 网络上翻车)。


---
