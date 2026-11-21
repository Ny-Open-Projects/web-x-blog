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
