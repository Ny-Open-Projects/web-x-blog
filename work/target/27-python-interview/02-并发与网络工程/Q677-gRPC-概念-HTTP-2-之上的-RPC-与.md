---
title: [Q677] gRPC 概念:HTTP/2 之上的 RPC 与 stub
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q677 · gRPC 概念:HTTP/2 之上的 RPC 与 stub

> 难度:★★★☆ | 标签:gRPC, RPC, HTTP2

**问**:gRPC 的调用在协议层长什么样?它比 REST+JSON 快在哪?

**答**:gRPC 把"调用本地函数"映射到网络:客户端 stub(由 .proto 生成的强类型代码)把方法名+消息体编码后发往服务器,格式是 HTTP/2 帧内嵌 LENGTH-PREFIXED 消息(5 字节前缀:1 字节压缩标志+4 字节长度+protobuf 消息),路径是 /package.Service/Method,元数据走 HTTP/2 headers,状态码走 trailers。快在三点:HTTP/2 多路复用(一连接并发多调用)、protobuf 二进制编码(体积/解析远小于 JSON)、以及四种流模式(unary/server-stream/client-stream/bidi)。生成 stub 的价值是接口即契约,跨语言类型安全。

```python
# file: code/02_并发与网络工程/q677_rpc_stub.py
"""不依赖 gRPC 库, 用 JSON 模拟 unary RPC 的骨架: schema + stub + 服务端 dispatch。"""
import json
import socket
import struct
import threading

SCHEMA = {
    "user.UserService/GetUser": {
        "request": {"user_id": int},
        "response": {"user_id": int, "name": str},
    },
    "user.UserService/ListUsers": {
        "request": {"limit": int},
        "response_stream": True,
    },
}


def encode_frame(obj: dict) -> bytes:
    """gRPC 消息帧: 1 字节压缩标志 + 4 字节大端长度 + 载荷 (此处用 JSON 代 protobuf)。"""
    body = json.dumps(obj).encode()
    return struct.pack("!BI", 0, len(body)) + body


def read_frame(sock: socket.socket) -> dict:
    def recv(n: int) -> bytes:
        buf = b""
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("closed")
            buf += chunk
        return buf

    _flag, length = struct.unpack("!BI", recv(5))
    return json.loads(recv(length))


class Server:
    def __init__(self) -> None:
        self.methods = {
            "user.UserService/GetUser": self.get_user,
        }

    def get_user(self, req: dict) -> tuple:
        if not isinstance(req.get("user_id"), int):
            return None, "INVALID_ARGUMENT user_id must be int"
        return {"user_id": req["user_id"], "name": f"user-{req['user_id']}"}, None


def serve(sock: socket.socket) -> None:
    srv = Server()
    try:
        while True:
            req = read_frame(sock)  # 请求: {"method": ..., "payload": ...}
            method = req["method"]
            handler = srv.methods.get(method)
            if handler is None:
                resp = {"status": "UNIMPLEMENTED"}
            else:
                result, err = handler(req["payload"])
                resp = {"payload": result, "status": err or "OK"}
            sock.sendall(encode_frame(resp))
    except (ConnectionError, json.JSONDecodeError):
        pass
    finally:
        sock.close()


def server(stop: threading.Event, port_box: list) -> None:
    l = socket.socket()
    l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l.bind(("127.0.0.1", 0))
    l.listen(4)
    port_box.append(l.getsockname()[1])
    l.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = l.accept()
        except socket.timeout:
            continue
        threading.Thread(target=serve, args=(conn,), daemon=True).start()
    l.close()


class Stub:
    """客户端存根: 调用像本地方法。"""

    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.create_connection((host, port), timeout=2)
        self.sock.settimeout(2)

    def call(self, method: str, payload: dict) -> dict:
        self.sock.sendall(encode_frame({"method": method, "payload": payload}))
        return read_frame(self.sock)


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)

    stub = Stub("127.0.0.1", box[0])
    print("正常调用:", stub.call("user.UserService/GetUser", {"user_id": 42}))
    print("参数错误:", stub.call("user.UserService/GetUser", {"user_id": "x"}))
    print("未知方法:", stub.call("user.UserService/DeleteAll", {}))
    stub.sock.close()
    stop.set()
```

**追问**:1) gRPC 的四种流模式分别适合什么?——unary 普通请求响应;server-stream 推送/大结果分页;client-stream 批量上传聚合;bidi 双向实时(聊天/协同),HTTP/2 的 stream 机制是它们统一的地基。2) trailers 是什么、状态码为什么走 trailer?——HTTP/2 响应可分首部+DATA+尾首部;gRPC 把 grpc-status/grpc-message 放 trailer,消息先流、状态后到,流式响应中途失败也能带状态送达;REST 没有这个通道。3) 四种流模式的背压与死锁?——server-stream 靠 HTTP/2 流控天然背压;client-stream 批量上传要分块+确认点;bidi 两端独立读写要防「互相等」(约定谁先关发送方向);流式消息处理不能阻塞读循环。4) 生产陷阱?——两端 max message size 不一致,大消息 RESOURCE_EXHAUSTED;keepalive 参数与服务端不一致被 GOAWAY;L4 负载均衡让长连接粘滞单实例,要客户端 LB(Q643)或 L7。

---
