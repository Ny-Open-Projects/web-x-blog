---
title: [Q638] WebSocket 心跳 ping/pong 与关闭握手
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q638 · WebSocket 心跳 ping/pong 与关闭握手

> 难度:★★★☆ | 标签:WebSocket, ping pong, 关闭

**问**:WS 协议层的 ping/pong 和关闭流程是怎么设计的?

**答**:ping(opcode 0x9)/pong(0xA)是协议级控制帧:任何一端可发 ping,对端必须尽快回 pong 且载荷原样带回,这解决了"TCP 连接在但进程假死/中间设备掐空闲连接"的检测问题——比应用层自定义心跳更统一(浏览器端 JS 都能被动响应)。关闭用 opcode 0x8 的 close 帧载荷携带状态码(1000 正常、1001 端点离开、1011 服务器内部错误),双方各发一次、先到先停:发起方发 close 后等待对端 close 回执再断 TCP,保证双方状态一致。握手时序同样要注意:服务端读完客户端的 Upgrade 请求必须回 101(带 Sec-WebSocket-Accept),客户端等不到回包就阻塞到 socket 超时。

```python
# file: code/02_并发与网络工程/q638_ws_ping_pong.py
import base64
import hashlib
import os
import socket
import struct
import threading
import time

WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def ws_accept(key: str) -> bytes:
    """RFC 6455: Accept = base64(sha1(key + GUID))。"""
    return base64.b64encode(hashlib.sha1((key + WS_GUID).encode()).digest())


def encode_frame(payload: bytes, opcode: int, mask: bool = False) -> bytes:
    first = 0x80 | opcode
    mask_bit = 0x80 if mask else 0
    ln = len(payload)
    if ln < 126:
        header = bytes([first, mask_bit | ln])
    else:
        header = bytes([first, mask_bit | 126]) + struct.pack("!H", ln)
    if mask:
        key = os.urandom(4)
        return header + key + bytes(b ^ key[i % 4] for i, b in enumerate(payload))
    return header + payload


def recv_frame(sock: socket.socket) -> tuple:
    def recv(n):
        buf = b""
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("closed")
            buf += chunk
        return buf

    b1, b2 = recv(2)
    opcode = b1 & 0x0F
    length = b2 & 0x7F
    if length == 126:
        (length,) = struct.unpack("!H", recv(2))
    mask_key = recv(4) if b2 >> 7 else None
    payload = recv(length)
    if mask_key:
        payload = bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload))
    return opcode, payload


def server(stop: threading.Event, port_box: list) -> None:
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
            # 完成 HTTP 握手: 读完整请求头后必须回 101, 客户端才能进帧收发
            conn.settimeout(3)
            buf = b""
            while b"\r\n\r\n" not in buf:
                buf += conn.recv(4096)
            ws_key = ""
            for line in buf.split(b"\r\n"):
                if line.lower().startswith(b"sec-websocket-key:"):
                    ws_key = line.split(b":", 1)[1].strip().decode()
            conn.sendall(
                b"HTTP/1.1 101 Switching Protocols\r\n"
                b"Upgrade: websocket\r\n"
                b"Connection: Upgrade\r\n"
                b"Sec-WebSocket-Accept: " + ws_accept(ws_key) + b"\r\n\r\n"
            )
            while True:
                opcode, payload = recv_frame(conn)
                if opcode == 0x9:                       # ping → 必须回 pong
                    print(f"[server] ping 载荷 {payload!r} → pong")
                    conn.sendall(encode_frame(payload, 0xA))
                elif opcode == 0x8:                     # close → 回 close 再断
                    code = struct.unpack("!H", payload[:2])[0] if len(payload) >= 2 else 1005
                    print(f"[server] 收到关闭帧 状态码={code} → 回执并断开")
                    conn.sendall(encode_frame(payload[:2], 0x8))
                    break
                else:
                    conn.sendall(encode_frame(payload, 0x1))
        except (ConnectionError, OSError):
            pass
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(b"GET /ws HTTP/1.1\r\nHost: x\r\nUpgrade: websocket\r\n"
              b"Connection: Upgrade\r\nSec-WebSocket-Key: aGVsbG8=\r\n"
              b"Sec-WebSocket-Version: 13\r\n\r\n")
    resp = b""
    while b"\r\n\r\n" not in resp:
        resp += c.recv(4096)
    print("[client] 握手:", resp.split(b"\r\n")[0].decode())

    c.sendall(encode_frame(b"hb-1", 0x9, mask=True))   # 心跳 ping
    opcode, payload = recv_frame(c)
    print(f"[client] 收到 opcode={opcode} pong={payload!r}")
    assert opcode == 0xA and payload == b"hb-1"

    c.sendall(encode_frame(struct.pack("!H", 1000), 0x8, mask=True))  # 正常关闭
    opcode, payload = recv_frame(c)
    print(f"[client] 收到关闭回执 opcode={opcode} 状态码={struct.unpack('!H', payload)[0]}")
    c.close()
    stop.set()
```

**追问**:1) ping 间隔怎么定?——浏览器端无法主动发 ping,只能依赖服务端;服务端一般 30s 一 ping,连续 2 次无 pong 判死;间隔过短浪费流量,过长则死连接占用资源时间变长。2) close 握手为什么设计成两次?——发起方发 close 后要等对端 close 回执再断 TCP,保证双方都把没发完的数据发完、状态一致;等待有超时上限,超时就硬拆,不能无限等——这是「先到先停」的完整语义。3) 协议心跳与应用心跳怎么分工?——ping/pong 在帧层、任何实现都应响应(浏览器被动支持),探「协议栈活着」;业务心跳可携带序列号/鉴权状态;服务端典型 30s 一 ping、连续 2 次无 pong 判死,间隔过短浪费流量过长拖慢发现。4) 生产陷阱?——自研服务端不回 pong(浏览器等价端会判你死);close 用保留段状态码(0-999)导致对端解析异常;pong 与大消息共用发送队列被队头阻塞,慢消费者被误判死——控制帧要优先发送。

---
