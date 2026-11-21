---
title: [Q636] WebSocket 握手原理:Sec-WebSocket-Accept 的由来
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q636 · WebSocket 握手原理:Sec-WebSocket-Accept 的由来

> 难度:★★★★ | 标签:WebSocket, 握手, Upgrade

**问**:WebSocket 是怎么从 HTTP"升级"出来的?为什么握手里要有个奇怪的 Key?

**答**:WebSocket 复用 HTTP 通道完成协商:客户端发普通 HTTP GET 带 `Upgrade: websocket`、`Connection: Upgrade`、`Sec-WebSocket-Key`(随机 16 字节的 base64);服务端愿意升级就回 101 Switching Protocols,并附 `Sec-WebSocket-Accept = base64(sha1(key + 固定GUID))`。Accept 的作用是防止普通 HTTP 响应被误当 WS 握手(缓存服务器污染/跨协议攻击):客户端校验服务端确实"懂"这个协议而不是盲转发。101 之后同一条 TCP 连接就切换成 WS 帧协议,与 HTTP 再无关系。

```python
# file: code/02_并发与网络工程/q636_ws_handshake.py
import base64
import hashlib
import socket
import threading
import time

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"  # 协议规定的固定魔法串


def ws_accept(key: str) -> str:
    return base64.b64encode(hashlib.sha1((key + GUID).encode()).digest()).decode()


def server(stop: threading.Event, port_box: list, server_log: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            conn.settimeout(3)
            data = b""
            while b"\r\n\r\n" not in data:
                data += conn.recv(4096)
            headers = {}
            for line in data.split(b"\r\n")[1:]:
                if b": " in line:
                    k, v = line.split(b": ", 1)
                    headers[k.decode().lower()] = v.decode()
            key = headers["sec-websocket-key"]
            accept = ws_accept(key)
            server_log.append(key)
            conn.sendall(
                b"HTTP/1.1 101 Switching Protocols\r\n"
                b"Upgrade: websocket\r\n"
                b"Connection: Upgrade\r\n"
                + f"Sec-WebSocket-Accept: {accept}\r\n\r\n".encode()
            )
            print(f"[server] 升级成功, key={key[:12]}... accept={accept[:12]}...")
        except Exception as e:
            print("[server] 握手失败:", repr(e))
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    import os
    stop = threading.Event()
    box: list = []
    log: list = []
    threading.Thread(target=server, args=(stop, box, log), daemon=True).start()
    while not box:
        time.sleep(0.01)

    key = base64.b64encode(os.urandom(16)).decode()
    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(
        f"GET /ws HTTP/1.1\r\nHost: 127.0.0.1\r\n"
        f"Upgrade: websocket\r\nConnection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode()
    )
    resp = b""
    while b"\r\n\r\n" not in resp:
        resp += c.recv(4096)
    status = resp.split(b"\r\n")[0].decode()
    headers = dict(
        l.split(b": ", 1) for l in resp.split(b"\r\n")[1:] if b": " in l
    )
    expect = ws_accept(key)
    print("[client] 响应:", status)
    print("[client] Accept 校验:", "通过" if headers.get(b"Sec-WebSocket-Accept") == expect.encode() else "失败")
    assert headers.get(b"Sec-WebSocket-Accept") == expect.encode()
    c.close()
    stop.set()
```

**追问**:1) 如果服务端不支持 WebSocket 会怎样?——它把 Upgrade 当未知头忽略,返回普通 200/404;客户端发现状态码不是 101 且 Accept 不匹配,就回退到轮询或 SSE 方案,这正是握手设计"可协商"的意义。2) 为什么用「key+固定 GUID 的 SHA1」而不是回显 key?——固定 GUID(258EAFA5-E914-47DA-95CA-C5AB0DC85B11)是协议魔数:只有真正实现 WS 的服务端才算得出正确 Accept,盲转发的缓存/中间层回显不出,客户端借此确认对端懂协议,防跨协议攻击与缓存污染。3) 协商失败怎么降级?——服务端不支持时按普通 HTTP 回应,客户端校验「状态码 101 且 Accept 匹配」,失败回退轮询/SSE(Q639);可协商正是握手设计的意义,生产要准备好降级路径而不是报错完事。4) 生产陷阱?——Nginx 反代没配 proxy_http_version 1.1 与 Upgrade/Connection 头透传,握手在网关层挂;忽略 Sec-WebSocket-Version 校验;101 后的连接仍按 HTTP 解析(应立即切帧协议)。

---
