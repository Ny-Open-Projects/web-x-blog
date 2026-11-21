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
