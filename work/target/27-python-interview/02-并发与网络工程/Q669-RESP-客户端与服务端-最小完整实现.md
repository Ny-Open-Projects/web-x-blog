---
title: [Q669] RESP 客户端与服务端:最小完整实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q669 · RESP 客户端与服务端:最小完整实现

> 难度:★★★☆ | 标签:RESP, Redis, 协议实现

**问**:不引 redis 库,用标准库实现一个能跑 SET/GET/DEL/PING 的 Redis 风格服务端和客户端,核心代码路径是什么?

**答**:服务端:accept→读字节流→RespParser 喂数据→每解析出一个命令数组就 dispatch(内存 dict 执行)→把结果用 RESP 编码写回。客户端:命令编码为 bulk 数组发送,同步读一个回复解析。整个协议层就是 Q667 编码 + Q668 解析的组合,加上一个 dispatch 表。注意服务端要处理"一次 recv 带来多条命令"(管道预备)和连接关闭的清理。这个实现正是理解 redis-py 底层的捷径。

```python
# file: code/02_并发与网络工程/q669_resp_client.py
import socket
import threading
from q668_resp_parser import RespParser, RespError, _INCOMPLETE  # 复用解析器


def encode_bulk(data: bytes) -> bytes:
    if data is None:
        return b"$-1\r\n"
    return b"$" + str(len(data)).encode() + b"\r\n" + data + b"\r\n"


def encode_command(*args: str) -> bytes:
    out = b"*" + str(len(args)).encode() + b"\r\n"
    for a in args:
        out += encode_bulk(a.encode())
    return out


store: dict = {}


def dispatch(cmd: list) -> bytes:
    """语义层: 命令 → RESP 回复。"""
    name = cmd[0].decode().upper()
    if name == "PING":
        return b"+PONG\r\n"
    if name == "SET" and len(cmd) >= 3:
        store[cmd[1]] = cmd[2]
        return b"+OK\r\n"
    if name == "GET" and len(cmd) >= 2:
        return encode_bulk(store.get(cmd[1]))
    if name == "DEL" and len(cmd) >= 2:
        return b":1\r\n" if store.pop(cmd[1], None) is not None else b":0\r\n"
    return f"-ERR unknown command {name}\r\n".encode()


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=serve_conn, args=(conn,), daemon=True).start()
    srv.close()


def serve_conn(conn: socket.socket) -> None:
    parser = RespParser()
    conn.settimeout(2)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            for cmd in parser.feed(data):  # 一次可能解析出多条命令 (管道)
                if isinstance(cmd, list):
                    conn.sendall(dispatch(cmd))
    except (OSError, ValueError):
        pass
    finally:
        conn.close()


class RespClient:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.create_connection((host, port), timeout=2)
        self.sock.settimeout(2)
        self.parser = RespParser()
        self.pending: list = []  # 未消费的回复队列

    def command(self, *args: str):
        self.sock.sendall(encode_command(*args))
        return self._read_reply()

    def _read_reply(self):
        while not self.pending:
            data = self.sock.recv(4096)
            if not data:
                raise ConnectionError("closed")
            self.pending.extend(self.parser.feed(data))
        reply = self.pending.pop(0)
        if isinstance(reply, RespError):
            raise reply
        return reply


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)

    c = RespClient("127.0.0.1", box[0])
    print("PING:", c.command("PING"))
    print("SET:", c.command("SET", "name", "redis-mini"))
    print("GET:", c.command("GET", "name"))
    print("GET missing:", c.command("GET", "nope"))
    print("DEL:", c.command("DEL", "name"))
    print("DEL again:", c.command("DEL", "name"))
    try:
        c.command("BOGUS")
    except RespError as e:
        print("错误传播:", e)
    c.sock.close()
    stop.set()
```

**追问**:1) 这套同步客户端改造成异步要动哪里?——只换传输层(recv 换成 await reader.read,发送不变),协议编解码层零改动,这也是协议与传输解耦的价值。2) 服务端 dispatch 要注意什么?——单命令异常要回 -ERR 而不是崩掉处理循环;dispatch 用 dict 查表,未注册命令回 unknown command;写回要循环 send 补齐半写。3) 协议层与传输层的解耦怎么体现?——RespParser/编码器不 import socket,输入输出都是 bytes 与结构;换 asyncio/WS 传输零改动——demo 的分层就是 redis-py 的分层方式,也是「协议可测性」的来源。4) 生产陷阱?——一次 recv 带来多条命令只处理第一条;连接关闭没清理会话状态(泄漏);回复类型与语义不匹配(SET 成功应回简单字符串 OK 而不是 bulk)。

---
