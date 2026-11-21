---
title: [Q644] 抓包思路:不引第三方库观察 TCP 行为
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q644 · 抓包思路:不引第三方库观察 TCP 行为

> 难度:★★★☆ | 标签:抓包, TCP 观察, 排障

**问**:不能装 tcpdump 的环境里,怎么用 socket 本身观察连接行为?

**答**:四个层次:1) 应用层日志——收发数据的字节量、时间戳、分块边界,能还原大部分粘包/延迟问题;2) socket 状态——getsockopt 拿 SO_ERROR、TCP_INFO(Linux)看 RTT/重传;3) 对端行为探测——故意半关闭/不发数据,观察对端反应(是否依赖假设);4) 环境对照——同一代码分别打回环与真实网关,差异即中间设备行为(如代理缓冲)。配合 /proc/net/tcp(Linux)或 netstat 可以看到连接队列与状态机位置。真正的 tcpdump/wireshark 用于最终确证,思路是"先应用层缩小范围,再抓包确证"。

```python
# file: code/02_并发与网络工程/q644_observe_stream.py
import socket
import threading
import time

log: list = []


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        conn.settimeout(2)
        t0 = time.monotonic()
        chunks = []
        try:
            while True:
                data = conn.recv(4096)
                if not data:
                    log.append(f"EOF at {(time.monotonic() - t0) * 1000:.1f}ms")
                    break
                chunks.append((time.monotonic() - t0, len(data), data))
        except socket.timeout:
            pass
        log.append(f"收到 {len(chunks)} 个 recv 分块:")
        for dt, n, payload in chunks:
            log.append(f"  +{dt * 1000:7.1f}ms  {n:3d}B  {payload!r}")
        conn.close()
    srv.close()


def send_experiment(port: int, nodelay: bool, label: str) -> None:
    c = socket.create_connection(("127.0.0.1", port))
    if nodelay:
        c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    log.append(f"--- {label} ---")
    c.sendall(b"a")                      # 三个小写背靠背
    c.sendall(b"b")
    c.sendall(b"c")
    time.sleep(0.3)
    c.shutdown(socket.SHUT_WR)           # 半关闭: 发送 EOF 但保留读
    c.settimeout(0.5)
    try:
        c.recv(10)  # 服务端不回复, 读完即关
    except socket.timeout:
        log.append("(服务端未响应, 半关闭后仍可等待)")
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    send_experiment(port, nodelay=False, label="Nagle 开启")
    send_experiment(port, nodelay=True, label="TCP_NODELAY")

    for line in log:
        print(line)
    print("观察点: 应用层三次 send 不等于三个包; recv 分块是到达边界不是发送边界")
    stop.set()
```

**追问**:1) recv 分块边界能对上 send 边界吗?——不能,流式协议里 recv 只保证"有数据就返回",Nagle/路径 MTU/接收缓冲都会重切块;任何依赖"一次 send 对应一次 recv"的代码都是错的。2) 应用层日志要记哪些字段才够定位?——时间戳(monotonic+墙上时钟双记)、方向、字节数、读写分块边界、对端地址、socket 状态;分块边界能直接还原 Nagle/粘包/中间设备缓冲现象,是最廉价的「抓包替代品」。3) 不装工具还能拿到什么内核信息?——getsockopt(SO_ERROR) 看挂起错误;Linux TCP_INFO 拿 RTT/重传/拥塞窗口,应用层直接输出这条连接的网络质量;/proc/net/tcp 或 netstat 看连接状态与队列;macOS 用 TCP_CONNECTION_INFO,常数与结构不同要分支。4) 生产陷阱?——只在开发机回环验证(无中间设备,问题全隐藏);对照实验一次改多个变量;诊断日志本身把磁盘打满,变成新事故。

---
