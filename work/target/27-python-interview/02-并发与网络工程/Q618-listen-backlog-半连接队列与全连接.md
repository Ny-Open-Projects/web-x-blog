---
title: [Q618] listen backlog:半连接队列与全连接队列
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q618 · listen backlog:半连接队列与全连接队列

> 难度:★★★★ | 标签:backlog, 三次握手, 容量

**问**:listen(128) 里的 128 是什么?突发流量下它怎么影响建连成功率?

**答**:backlog 限制的是全连接队列(已完成三次握手、等待 accept 的连接)长度,半连接队列(SYN_RCVD)主要由 `net.ipv4.tcp_max_syn_backlog` 与 `tcp_syncookies` 约束;而 `net.core.somaxconn` 约束的是**全连接 accept 队列**上限,生效值为 min(backlog, somaxconn)。队列满之后的行为:Linux 默认丢弃 SYN(客户端表现为 connect 超时或重传),macOS 可能回 RST——所以压测看到"connect 超时"首先要怀疑 accept 速度跟不上而不是带宽。应用层要点:accept 循环不能被业务逻辑阻塞;队列长度的合理值 = 峰值 QPS × accept 延迟;ss/netstat -lnt 中 LISTEN 的 Recv-Q 是当前全连接队列长度、Send-Q 是队列上限,两者都是瞬时值;累计溢出要看 `netstat -s` / `nstat` 的 ListenOverflows、ListenDrops。

```python
# file: code/02_并发与网络工程/q618_backlog.py
import socket
import threading
import time


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(2)  # 故意设小 backlog, 模拟 accept 瓶颈
    port = srv.getsockname()[1]
    print(f"服务端 listen(2), 暂不 accept")

    clients: list = []
    results: list = []
    lock = threading.Lock()

    def try_connect(i: int) -> None:
        c = socket.socket()
        c.settimeout(2.0)
        t0 = time.monotonic()
        try:
            c.connect(("127.0.0.1", port))
            ok = True
        except (OSError, socket.timeout) as e:
            ok = False
            err = repr(e)
        dt = time.monotonic() - t0
        with lock:
            results.append((i, ok, dt, err if not ok else ""))
        if ok:
            clients.append(c)

    threads = [threading.Thread(target=try_connect, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ok_n = sum(1 for _, ok, *_ in results if ok)
    print(f"10 个并发连接, backlog=2 且未 accept: 成功 {ok_n} 个")
    for i, ok, dt, err in results[:4]:
        print(f"  conn{i}: ok={ok} 耗时={dt * 1000:.0f}ms {err}")

    print("开始 accept 排空队列")
    srv.settimeout(1.0)
    accepted = 0
    try:
        while True:
            conn, _ = srv.accept()
            accepted += 1
            conn.close()
    except socket.timeout:
        pass
    for c in clients:
        c.close()
    print(f"排队中的连接被依次 accept: {accepted} 个")
    srv.close()


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么 accept 很快但队列还是溢出?——accept 消费的是 ESTABLISHED,但握手本身要占内核时间;洪峰下 SYN 重传也会挤占半连接队列,必要时开 syncookies 并加连接级限流(见 Q656)。2) 应用层怎么观测队列溢出?——ss -lnt 看 LISTEN 的 Recv-Q(当前全连接队列长度)与 Send-Q(上限);netstat -s 里「times the listen queue of a socket overflowed」计数增长就是溢出实锤,配合 accept 线程 CPU 定位消费慢。3) 生效值由哪些参数共同决定?——全连接队列生效值是 min(listen 的 backlog, net.core.somaxconn),只改应用层 backlog 不调 sysctl 常常白调;半连接队列由 tcp_max_syn_backlog 与 syncookies 约束,两者别混为一谈。4) 生产陷阱?——accept 循环里做 DNS/DB 等阻塞调用拖慢消费,队列恒满;压测 connect 超时被误判为带宽问题;backlog 调大只是延缓,真正要修的是 accept 速度。

---
