---
title: [Q616] Nagle 算法与 TCP_NODELAY:小包延迟从哪来
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q616 · Nagle 算法与 TCP_NODELAY:小包延迟从哪来

> 难度:★★★☆ | 标签:TCP_NODELAY, Nagle, 延迟

**问**:交互式服务为什么都要设置 TCP_NODELAY?Nagle 算法到底在优化什么?

**答**:Nagle 算法为了减少网络中的小包,规定"有未确认的小段在途时,后续小数据先攒着,等 ACK 或攒满 MSS 才发"。它优化带宽利用率,代价是延迟:与对端延迟确认(delayed ACK,最多等 40ms+)相互作用时,第二个小写可能被扣住几十毫秒,这就是"写一个字节等一下"的经典延迟来源。SSH/游戏/推送等交互式协议一律设置 TCP_NODELAY 禁用 Nagle;批量传输(文件下载)则不必关,攒包反而有利。验证方法是观察"背靠背两次小写"的到达间隔。

```python
# file: code/02_并发与网络工程/q616_nagle.py
import socket
import threading
import time

arrivals: dict = {}  # conn_id -> [到达时刻]


def server(stop: threading.Event, results: dict) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    results["port"] = srv.getsockname()[1]
    srv.settimeout(0.2)
    conn_id = 0
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        conn_id += 1
        cid = conn_id
        t0 = time.monotonic()
        arrivals[cid] = []
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # 收到第一个包后延迟 100ms 再响应, 模拟应用处理 + 触发对端延迟确认
        data1 = conn.recv(1)
        arrivals[cid].append(time.monotonic() - t0)
        time.sleep(0.1)
        conn.sendall(b"R1")
        data2 = conn.recv(1)
        arrivals[cid].append(time.monotonic() - t0)
        conn.sendall(b"R2")
        results[f"gap{cid}"] = arrivals[cid][1] - arrivals[cid][0]
        conn.close()
    srv.close()


def client(port: int, nodelay: bool) -> float:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    if nodelay:
        c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    c.sendall(b"A")      # 第一个小写
    time.sleep(0.01)     # 确保两个写在时间上错开
    c.sendall(b"B")      # 第二个小写: Nagle 开启时可能被扣住
    c.recv(2)
    c.recv(2)
    c.close()
    return 0.0


if __name__ == "__main__":
    stop = threading.Event()
    results: dict = {}
    t = threading.Thread(target=server, args=(stop, results), daemon=True)
    t.start()
    while "port" not in results:
        time.sleep(0.01)
    port = results["port"]

    client(port, nodelay=False)
    gap_nagle = results.get("gap1", 0)
    client(port, nodelay=True)
    gap_fast = results.get("gap2", 0)
    print(f"Nagle 开启: 第二包延迟到达 gap={gap_nagle * 1000:.0f}ms")
    print(f"NODELAY:    第二包立即到达 gap={gap_fast * 1000:.0f}ms")
    stop.set()
    t.join()
    print("结论: 交互式协议应设置 TCP_NODELAY, 批量传输无所谓")
```

**追问**:1) 设置 NODELAY 后小包一定变多吗?——应用层自己攒包(如日志聚合)比依赖 Nagle 更可控,NODELAY 只是把"何时发"的决定权从内核拿回应用。2) Nagle 与延迟确认为什么会互相卡住?——发送端 Nagle 等 ACK 才放行下一个小包,接收端 delayed ACK 又故意推迟(最多 40ms+),两边互相等,形成经典的 40ms 延迟尖刺;这是「发送端想攒、接收端想拖」的组合症,关任何一边都能解。3) 内核还有哪些开关影响小包行为?——TCP_QUICKACK 关闭接收端延迟确认;TCP_CORK 与 NODELAY 相反、强制攒到 MSS 再发(适合「响应头+体一起发」);NODELAY 只影响发送方向,接收方向由对端策略决定。4) 生产陷阱?——内网 RPC 框架默认不开 NODELAY,P99 平白多出 40ms 尖刺且只在跨机复现;把关 Nagle 当万能(批量传输关了反而更碎);以为 NODELAY 立即作用于已在途的数据。

---
