---
title: [Q1866] TCP_NODELAY 延迟实测方法论:回环上的真相
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1866 · TCP_NODELAY 延迟实测方法论:回环上的真相

> 难度:★★★ | 标签:TCP_NODELAY, RTT, 测量方法

**问**:想实测 TCP_NODELAY 的效果,为什么在 127.0.0.1 上测不出差别?正确的测法是什么?

**答**:Nagle 的机制是 '有未确认小段在途时,后续小写先攒着',它需要真实的 ACK 往返才有攒包窗口;回环 ACK 立即返回,第二写永远不会被扣住,实测 on/off 中位 RTT 都是 0.05ms 量级,毫无差别。

- 正确做法是到真实网络或注入延迟的链路上测,观察 '背靠背两次小写再读' 的 RTT 是否出现 40ms 量级台阶——那是 Nagle 与延迟确认互相作用的指纹;

- 无论在哪测,TCP_NODELAY 都要用 getsockopt 读回验证:Darwin 读回的是位掩码(开启时为 4),Linux 读回 1/0,非零即生效,写了没生效是常见事故;

- 测量用中位数与 p99 而不是平均值,尾部抖动会被长尾请求淹没。

结论性纪律:交互式服务(SSH、游戏、推送)一律开 NODELAY;批量传输不必关,攒包反而有利。

```python
# file: code/02_并发与网络工程/q1866_nodelay_rtt.py
# -*- coding: utf-8 -*-
"""TCP_NODELAY 延迟实测方法论: 回环上的真相与设置读写验证。

- 回环 ping-pong RTT 实测: 127.0.0.1 往返约 0.1ms, ACK 立即返回;
- 回环上 nodelay on/off 中位数无差异: Nagle 需要真实网络 RTT 才有"攒包"窗口;
- TCP_NODELAY 必须用 getsockopt 读回验证, 写了没生效是常见事故;
- 教学点: 在错误环境做延迟实验, 会得出错误结论。
"""
import socket
import threading
import time


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def start_echo_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)

    def serve():
        srv.settimeout(0.2)
        while True:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            conn.settimeout(3.0)

            def pump(c):
                try:
                    while True:
                        data = c.recv(4096)
                        if not data:
                            break
                        c.sendall(data)
                except OSError:
                    pass
                c.close()

            threading.Thread(target=pump, args=(conn,), daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    port = srv.getsockname()[1]
    wait_port(port)
    return port


def pingpong_rtt(port, nodelay, rounds=200, wwr=False):
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY,
                 1 if nodelay else 0)
    readback = c.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
    # Darwin 读回的是位掩码(开启时为 4), Linux 读回 1/0, 非零即生效
    assert (readback != 0) == nodelay, "TCP_NODELAY 设置必须读回验证"
    c.settimeout(3.0)
    rtts = []
    for _ in range(rounds):
        t0 = time.perf_counter()
        if wwr:
            c.sendall(b"a")
            c.sendall(b"b")               # 背靠背两次小写, Nagle 的经典靶子
            got = b""
            while len(got) < 2:           # 两次回包可能被服务端一次读完合并发出
                got += c.recv(2 - len(got))
            assert got == b"ab"
        else:
            c.sendall(b"p")
            assert c.recv(1) == b"p"
        rtts.append(time.perf_counter() - t0)
    c.close()
    rtts.sort()
    return rtts[len(rtts) // 2], rtts[int(len(rtts) * 0.99)]


def main():
    port = start_echo_server()
    print("本机回环 ping-pong 实测, 每组 200 轮:")
    medias = {}
    for nodelay in (False, True):
        med, p99 = pingpong_rtt(port, nodelay, 200, wwr=False)
        medias[nodelay] = med
        print("  nodelay=%-5s 中位 RTT %.3fms  p99 %.3fms" % (nodelay, med * 1000, p99 * 1000))
    assert medias[True] < 0.002, "回环 nodelay 开启时 RTT 应在毫秒内"
    assert medias[False] < 0.002, "回环上关闭 nodelay 也不该慢"

    print("背靠背两写一读(触发 Nagle 攒包的模式):")
    for nodelay in (False, True):
        med, p99 = pingpong_rtt(port, nodelay, 100, wwr=True)
        print("  nodelay=%-5s 中位 RTT %.3fms  p99 %.3fms" % (nodelay, med * 1000, p99 * 1000))

    print("结论: 回环 ACK 即时, Nagle 无在途小段可攒, on/off 无差异;")
    print("      真实网络上第二写才会被扣 40ms+, 这就是交互式服务必开 NODELAY 的原因")


if __name__ == "__main__":
    main()
```

**追问**:1) 开 NODELAY 会不会制造小包风暴?——应用层一次写一个字节才会;正确姿势是应用层聚合写(攒够一次 write),传输层再开 NODELAY,两头各管各的。2) Nagle 的攒包窗口为什么依赖真实 RTT?——「有未确认小段在途」需要 ACK 往返时间窗口,回环 ACK 立即返回,窗口恒为零;40ms 台阶是 Nagle×延迟确认(DARWIN/Linux 的 delayed ack)的相互作用指纹(Q616 完整链)——「实验环境的选择」本身就是结论的一部分。3) getsockopt 验证为什么是必须动作?——写 setsockopt 不代表生效(Darwin 读回位掩码、Linux 读回 1/0,语义平台相关);写了没生效(权限/时机/选项不支持)是常见事故;「写→读回→断言」三步是 socket 选项实验的通用模板(Q1600 同源)。4) 生产陷阱?——回环测延迟下结论(错误环境);NODELAY 写了没验证(没生效);NODELAY 与应用层攒包对立(应两头配合,见原问);用平均值报告 RTT(尾部被淹没,用中位数+P99)。


---
