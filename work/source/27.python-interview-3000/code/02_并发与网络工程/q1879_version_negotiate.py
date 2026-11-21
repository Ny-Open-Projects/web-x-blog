# -*- coding: utf-8 -*-
"""协议版本协商: 客户端声明支持集, 服务端选最高共同版本, 谈不拢报错关门。

- 握手帧: 2 字节长度前缀 + JSON, 客户端 HELLO 带版本列表;
- 服务端求交集取 max, 未通过则回错误帧并断开, 客户端转译为 ProtocolError;
- 服务端自己降级到共同版本继续说话, 这就是灰度期两版并存的握手方案。
"""
import json
import socket
import struct
import threading
import time

SERVER_VERSIONS = [1, 2]


class ProtocolError(Exception):
    pass


def send_frame(sock, obj):
    data = json.dumps(obj).encode()
    sock.sendall(struct.pack(">H", len(data)) + data)


def recv_exact(sock, n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("对端断开")
        buf += chunk
    return buf


def recv_frame(sock):
    (n,) = struct.unpack(">H", recv_exact(sock, 2))
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
            hello = recv_frame(conn)
            common = sorted(set(hello.get("v", [])) & set(SERVER_VERSIONS))
            if common:
                chosen = common[-1]            # 最高共同版本
                send_frame(conn, {"ok": chosen})
            else:
                send_frame(conn, {"err": "no-common-version",
                                  "supported": SERVER_VERSIONS})
        except (ConnectionError, json.JSONDecodeError):
            pass
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


def negotiate(port, client_versions):
    sock = socket.create_connection(("127.0.0.1", port), timeout=2.0)
    try:
        send_frame(sock, {"v": client_versions})
        reply = recv_frame(sock)
    finally:
        sock.close()
    if "ok" in reply:
        return reply["ok"]
    raise ProtocolError("协商失败: %s" % reply)


def main():
    srv, port = start_server()

    v = negotiate(port, [1, 2, 3])
    print("客户端 [1,2,3] vs 服务端 [1,2] -> 协商版本 %d" % v)
    assert v == 2, "取最高共同版本"

    v = negotiate(port, [1])
    print("客户端 [1]     vs 服务端 [1,2] -> 协商版本 %d" % v)
    assert v == 1, "旧客户端也能接入"

    try:
        negotiate(port, [4])
        raise AssertionError("无共同版本应失败")
    except ProtocolError as e:
        print("客户端 [4]     vs 服务端 [1,2] ->", e)

    srv.close()
    print("结论: 版本协商三步曲 声明 交集 取最大, 谈不拢用错误帧体面分手")


if __name__ == "__main__":
    main()
