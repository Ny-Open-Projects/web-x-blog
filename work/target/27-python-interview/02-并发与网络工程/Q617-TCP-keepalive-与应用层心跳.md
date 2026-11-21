---
title: [Q617] TCP keepalive 与应用层心跳
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q617 · TCP keepalive 与应用层心跳

> 难度:★★★☆ | 标签:keepalive, 心跳, 存活检测

**问**:TCP 自带 keepalive,为什么应用还要自己做心跳?

**答**:TCP keepalive 探测的是"连接路径还通不通",默认 2 小时才启动,且中间的 NAT/防火墙/LB 只看有没有应用数据,空闲连接照样被掐;应用层心跳则是自定义频率的"业务级活性",能同时验证对端进程活着、鉴权仍有效、NAT 映射未过期。工程实践:心跳间隔取 NAT 超时的 1/3~1/2(常见 30~60s),连续 N 次未收到 pong 判定断线并触发重连;keepalive 作为兜底保留(把 idle 时间调小)。两者是互补而不是二选一。

```python
# file: code/02_并发与网络工程/q617_heartbeat.py
import socket
import sys
import threading
import time


def enable_keepalive(sock: socket.socket) -> None:
    """设置内核级 keepalive 作为兜底 (参数平台相关)。"""
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    if sys.platform == "darwin":
        TCP_KEEPALIVE = 0x10
        sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, 60)  # 空闲 60s 开始探测
    elif sys.platform.startswith("linux"):
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3)


def server(stop: threading.Event) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    server.port = srv.getsockname()[1]  # type: ignore[attr-defined]
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        enable_keepalive(conn)
        conn.settimeout(2)
        while True:
            try:
                data = conn.recv(64)
            except socket.timeout:
                continue  # 心跳间隔内的静默是正常的
            if not data or data == b"PING":
                if data == b"PING":
                    conn.sendall(b"PONG")
                    continue
                break
            conn.sendall(b"echo:" + data)
        conn.close()
    srv.close()


def client_with_heartbeat(port: int) -> None:
    c = socket.socket()
    enable_keepalive(c)
    c.connect(("127.0.0.1", port))
    c.settimeout(1)

    def heartbeat() -> None:
        while not c._closed:  # 简化判断, 生产用状态标志
            try:
                c.sendall(b"PING")
                pong = c.recv(4)
                if pong != b"PONG":
                    print("心跳异常, 触发重连逻辑")
            except OSError:
                return
            time.sleep(0.05)

    hb = threading.Thread(target=heartbeat, daemon=True)
    hb.start()
    c.sendall(b"hello")
    print("业务响应:", c.recv(64).decode())
    time.sleep(0.2)  # 期间心跳在跑
    c.close()
    hb.join(timeout=1)


if __name__ == "__main__":
    stop = threading.Event()
    t = threading.Thread(target=server, args=(stop,), daemon=True)
    t.start()
    while not hasattr(server, "port"):
        time.sleep(0.01)
    client_with_heartbeat(server.port)  # type: ignore[attr-defined]
    stop.set()
    print("keepalive 兜底 + 应用心跳主动, 双层检测就绪")
```

**追问**:1) 心跳应该由哪一端发起?——一般客户端发起(它最关心连接可用性且数量多),服务端只做超时判定与踢除;两端都发会浪费带宽,只服务端发则无法及时发现单向断连。2) 为什么心跳判定不能依赖阻塞 recv?——recv 没数据就一直挂着,应用失去「该收到了却没收到」的判定权;要么独立定时器/selector 超时,要么 settimeout 把超时控制拿回应用层,判定与读取必须解耦。3) keepalive 三参数怎么调?——Linux 上 setsockopt(SOL_TCP, TCP_KEEPIDLE/TCP_KEEPINTVL/TCP_KEEPCNT) 把默认 2h 改成秒级;macOS 常数名不同(TCP_KEEPALIVE),跨平台代码要按平台分支,这也是「兜底交给内核」的实现成本。4) 生产陷阱?——心跳计时用 time.time,NTP 回拨让差值变负、死连接长期不被清理(计时一律 time.monotonic);心跳与业务消息抢同一发送锁,慢业务把心跳饿死,对端误判断线;重连风暴无抖动(见 Q623)。

---
