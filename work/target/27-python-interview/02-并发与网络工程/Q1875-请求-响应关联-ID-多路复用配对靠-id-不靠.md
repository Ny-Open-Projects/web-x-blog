---
title: [Q1875] 请求/响应关联 ID:多路复用配对靠 id 不靠顺序
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1875 · 请求/响应关联 ID:多路复用配对靠 id 不靠顺序

> 难度:★★★ | 标签:关联 ID, 多路复用, 协议设计

**问**:单条连接上并发发多个请求,响应乱序回来,怎么把响应配对到正确的请求?

**答**:每帧携带唯一关联 ID:请求方生成 req_id,响应方原样带回,客户端按 id 把响应分发到对应的等待者——顺序是巧合,id 才是契约。

- 帧格式 4 字节长度前缀加 JSON,reader 线程独立收帧、按 id 查表、set Event 并填结果,收发彻底解耦;

- 演示服务端故意倒序回包,到达顺序 r3、r2、r1,但每个请求都拿到自己的响应,配对零误差;

- id 生成要防碰撞:自增序号 + 前缀即可,跨进程时用 uuid;连接重建后 id 重新计数或带会话前缀。

HTTP/2 的 stream id、数据库驱动的 statement id、消息队列的 correlation-id,全是这一招。

```python
# file: code/02_并发与网络工程/q1875_correlation_id.py
# -*- coding: utf-8 -*-
"""请求/响应关联 ID: 单连接上并发请求的配对靠 id 不靠顺序。

- 帧格式 4 字节长度前缀 + JSON, 请求携带唯一 req_id;
- 服务端故意乱序回包(倒序), 证明配对与到达顺序无关;
- 客户端 reader 线程按 id 分发到等待中的 Event, 主线程按 id 收割结果。
"""
import json
import socket
import struct
import threading
import time


def send_frame(sock, obj):
    data = json.dumps(obj).encode()
    sock.sendall(struct.pack(">I", len(data)) + data)


def recv_exact(sock, n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("对端断开")
        buf += chunk
    return buf


def recv_frame(sock):
    (n,) = struct.unpack(">I", recv_exact(sock, 4))
    return json.loads(recv_exact(sock, n).decode())


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def start_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)

    def handle(conn):
        try:
            conn.settimeout(3.0)
            reqs = [recv_frame(conn) for _ in range(3)]    # 先收齐三个请求
            for req in reversed(reqs):                     # 倒序回包: 顺序不可依赖
                time.sleep(0.03)
                send_frame(conn, {"id": req["id"],
                                  "payload": "resp:" + req["payload"]})
        except (ConnectionError, OSError):
            pass                                           # 客户端收完即走
        conn.close()

    def loop():
        srv.settimeout(3.0)
        while True:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            threading.Thread(target=handle, args=(conn,), daemon=True).start()

    threading.Thread(target=loop, daemon=True).start()
    port = srv.getsockname()[1]
    wait_port(port)
    return srv, port


def main():
    srv, port = start_server()
    sock = socket.create_connection(("127.0.0.1", port))
    sock.settimeout(3.0)

    pending = {}                                       # id -> {"event":, "result":}
    arrival_order = []

    def reader():
        while True:
            try:
                resp = recv_frame(sock)
            except (ConnectionError, OSError):
                break
            arrival_order.append(resp["id"])           # 到达顺序由 reader 记录
            slot = pending.get(resp["id"])
            if slot:
                slot["result"] = resp["payload"]
                slot["event"].set()

    threading.Thread(target=reader, daemon=True).start()

    reqs = [("r1", "alpha"), ("r2", "beta"), ("r3", "gamma")]
    for rid, payload in reqs:                          # 先全部发出再收割
        pending[rid] = {"event": threading.Event(), "result": None}
        send_frame(sock, {"id": rid, "payload": payload})

    for rid, payload in reqs:
        slot = pending[rid]
        assert slot["event"].wait(timeout=2.0), "每个请求都应收到响应"
        print("%s <- %s (期望 resp:%s)" % (rid, slot["result"], payload))
        assert slot["result"] == "resp:" + payload, "id 配对必须准确"
    sock.close()
    srv.close()
    print("响应到达顺序:", arrival_order, "-> 服务端是倒序回的")
    assert arrival_order == ["r3", "r2", "r1"], "到达顺序与配对无关"
    print("结论: 关联 ID 是多路复用的钥匙, 顺序是巧合, id 才是契约")


if __name__ == "__main__":
    main()
```

**追问**:1) 请求发出去了但响应永远不来怎么办?——等待必须带超时,超时后把 slot 从表里摘除并给调用方明确错误;响应晚到时查无此人,丢弃并计数,这就是 '孤儿响应' 监控的来源。2) 孤儿响应的完整处置链?——等待带超时→超时摘除 slot(防表膨胀)→给调用方明确错误;响应晚到查无此人→丢弃+计数(孤儿响应率指标);孤儿率高说明「响应丢失或乱序严重」,是链路质量信号——slot 生命周期管理是配对协议的工程核心。3) req_id 的生成与作用域怎么设计?——单连接内自增+连接前缀;跨进程 uuid;重建连接后重新计数或带会话前缀(防旧连接的迟响应污染新连接的表)——id 作用域与 slot 表的作用域必须一致。4) 生产陷阱?——等待无超时(响应丢失=调用方永久挂起);slot 不摘除(表膨胀);reader 线程异常无人收割(收发解耦的收尾);按到达顺序配对(顺序是巧合,见原问);req_id 碰撞(自增溢出/多连接前缀缺失)。


---
