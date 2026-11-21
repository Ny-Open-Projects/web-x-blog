---
title: [Q2916] ping-pong 延迟测量:应用层 RTT 实测方法
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2916 · ping-pong 延迟测量:应用层 RTT 实测方法

> 难度:★★ | 标签:RTT, 延迟测量, TCP_NODELAY

**问**:想知道一条 TCP 链路的真实延迟,为什么不能只 ping 一次?该怎么测?

**答**:发一个 ping、收一个 pong,perf_counter 包住这一来一回就是一次 RTT,然后重复几百次看分布——单次测量毫无意义,分布才是真相。实测回环 300 次:min 0.055ms、p50 0.100ms,亚毫秒级是回环的本色;p95 0.603ms、max 3.586ms,尾部抖动来自内核调度,客户端与服务端同进程时还会混入 GIL 切换噪声,本例把切换间隔调小来压噪声,而"测真实链路要把对端放进独立进程"本身就是测量结论之一。还有两条测量卫生:两端都开 TCP_NODELAY,不然 Nagle 会把 pong 攒到下一个包,测出来的是 Nagle 超时不是网络延迟;注意预热效应,前 20 次均值 0.058ms 而稳态 0.441ms,最先几次的样本要单独看待。

- perf_counter 是单调高精度时钟,time.time 会跳;

- 分桶直方图比一串数字更直观,一眼看出延迟集中在哪个量级;

- 对端负载变化会让分布整体漂移,测量时要记录当时的服务端状态。

```python
# file: code/02_并发与网络工程/q2916_pingpong_latency.py
# -*- coding: utf-8 -*-
"""ping-pong 延迟测量: 应用层 RTT 的实测方法。

- 一发一收算一次 RTT: perf_counter 包住 sendall + recv;
- TCP_NODELAY 两端都开: 不然 Nagle 会把 pong 攒到下个包;
- 统计 min/p50/p95/p99/max + 分桶直方图, 并观察前若干次的预热效应。
"""
import socket
import statistics
import sys
import threading
import time

ROUNDS = 300


def serve(port, done):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(4)
    srv.settimeout(0.1)
    while not done.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        conn.settimeout(3)
        try:
            while True:
                data = conn.recv(64)
                if not data:
                    break
                conn.sendall(b"pong\n")         # 立刻回, 不攒
        except OSError:
            pass
        finally:
            conn.close()
    srv.close()


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


if __name__ == "__main__":
    # 客户端与服务端同进程: RTT 尾部会混入 GIL 调度噪声, 这本身是测量结论
    sys.setswitchinterval(0.001)
    done = threading.Event()
    tmp = socket.socket()
    tmp.bind(("127.0.0.1", 0))
    port = tmp.getsockname()[1]
    tmp.close()
    t = threading.Thread(target=serve, args=(port, done), daemon=True)
    t.start()
    assert wait_port(port)

    sock = socket.create_connection(("127.0.0.1", port), timeout=3)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.settimeout(3)

    rtts = []
    for i in range(ROUNDS):
        t1 = time.perf_counter()
        sock.sendall(b"ping\n")
        buf = b""
        while not buf.endswith(b"\n"):
            chunk = sock.recv(64)
            if not chunk:
                raise ConnectionError("server closed")
            buf += chunk
        rtts.append(time.perf_counter() - t1)
    sock.close()
    done.set()
    t.join(timeout=3)

    lat = sorted(rtts)
    ms = [x * 1000 for x in lat]

    def pct(p):
        return ms[min(len(ms) - 1, int(round(p * (len(ms) - 1))))]

    buckets = {"<0.1ms": 0, "0.1-0.2": 0, "0.2-0.5": 0, "0.5-1": 0, ">=1ms": 0}
    for x in ms:
        if x < 0.1:
            buckets["<0.1ms"] += 1
        elif x < 0.2:
            buckets["0.1-0.2"] += 1
        elif x < 0.5:
            buckets["0.2-0.5"] += 1
        elif x < 1.0:
            buckets["0.5-1"] += 1
        else:
            buckets[">=1ms"] += 1

    warmup = statistics.mean(ms[:20])
    steady = statistics.mean(ms[-100:])
    print("%d 次 RTT: min=%.3f p50=%.3f p95=%.3f p99=%.3f max=%.3f ms"
          % (ROUNDS, ms[0], pct(0.50), pct(0.95), pct(0.99), ms[-1]))
    print("分布:", buckets)
    print("预热效应: 前 20 次均值 %.3fms -> 后 100 次均值 %.3fms"
          % (warmup, steady))
    assert len(rtts) == ROUNDS
    assert pct(0.50) < 2.0, "回环 RTT 中位数应在毫秒以内"
    assert ms[-1] < 100, "回环 RTT 尾部受 GIL 调度影响也不该到 100ms"
    print("要点: p50 亚毫秒是回环本色, 尾部抖动来自 GIL 与内核调度,"
          " 测真实 RTT 应把对端放进独立进程")
```

**追问**:1) 为什么不用 ICMP ping?——ICMP 反映网络层,应用层 RTT 还包含协议处理和调度开销,线上关心的是后者。2) 样本数取多少?——看目标分布的尾部有多 rare,想看清万分位就得万级样本,300 次只够看 p95 量级。3) 底层机制:为什么两端都要 TCP_NODELAY?——客户端 ping 与服务端 pong 都是小包,Nagle 在任一端开启都可能把 pong 扣住等 ACK,与对端 delayed ACK 互等(见 Q616)测出 40ms 级假延迟;NODELAY 让每次写立即出网,RTT 才反映真实链路。4) 生产陷阱?——用 time.time 计时被 NTP 跳变污染,测量钟一律 perf_counter;预热样本混进统计,冷启动污染 min;客户端与服务端同进程,GIL 切换噪声进尾部被误判成网络抖动;单次测量下结论。

---
