# -*- coding: utf-8 -*-
"""能力标志位协商: 位图求交集, 协商结果直接驱动消息编码路径。

- 客户端上报能力位图, 服务端回自己的支持集与客户端的交集;
- 协商结果不是摆设: 有 COMPRESS 位走压缩编码, 没有就走明文;
- 使用未协商的能力是协议违规, 必须显式拒绝。
"""
import json
import socket
import struct
import threading
import time

CAPS = {"COMPRESS": 1, "ENCRYPT": 2, "RESUME": 4, "MULTIPLEX": 8}
SERVER_CAPS = CAPS["COMPRESS"] | CAPS["RESUME"] | CAPS["MULTIPLEX"]  # 不支持 ENCRYPT


def cap_names(mask):
    return [name for name, bit in CAPS.items() if mask & bit]


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


def encode_payload(payload, agreed):
    if agreed & CAPS["COMPRESS"]:
        return "Z:" + payload[::-1]            # 假压缩: 反转示意
    return "P:" + payload


def decode_payload(wire, agreed):
    mode, _, body = wire.partition(":")
    if mode == "Z":
        if not agreed & CAPS["COMPRESS"]:
            raise ProtocolViolation("未协商 COMPRESS 却收到压缩消息")
        return body[::-1]
    return body


class ProtocolViolation(Exception):
    pass


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
            agreed = hello["caps"] & SERVER_CAPS
            send_frame(conn, {"caps": agreed})
            wire = recv_frame(conn)["wire"]
            payload = decode_payload(wire, agreed)
            send_frame(conn, {"decoded": payload,
                              "features": cap_names(agreed)})
        except (ConnectionError, KeyError, json.JSONDecodeError) as e:
            print("  服务端会话异常退出:", repr(e))
        except ProtocolViolation as e:
            print("  服务端拒绝协议违规:", e)
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


def session(port, client_caps, payload):
    sock = socket.create_connection(("127.0.0.1", port), timeout=2.0)
    try:
        send_frame(sock, {"caps": client_caps})
        agreed = recv_frame(sock)["caps"]
        send_frame(sock, {"wire": encode_payload(payload, agreed)})
        return agreed, recv_frame(sock)
    finally:
        sock.close()


def main():
    srv, port = start_server()

    agreed, reply = session(port, CAPS["COMPRESS"] | CAPS["ENCRYPT"], "hello")
    print("客户端能力 %s -> 协商 %s, 回声 %r"
          % (cap_names(CAPS["COMPRESS"] | CAPS["ENCRYPT"]),
             cap_names(agreed), reply["decoded"]))
    assert agreed == CAPS["COMPRESS"], "ENCRYPT 未获支持, 只协商出 COMPRESS"
    assert reply["decoded"] == "hello"
    assert reply["features"] == ["COMPRESS"]

    agreed2, reply2 = session(port, 15, "full-featured")
    print("客户端能力 %s -> 协商 %s"
          % (cap_names(15), cap_names(agreed2)))
    assert agreed2 == SERVER_CAPS
    assert reply2["decoded"] == "full-featured"
    assert "ENCRYPT" not in reply2["features"]

    # 协议违规: 服务端没协商 COMPRESS, 客户端硬发压缩报文
    sock = socket.create_connection(("127.0.0.1", port), timeout=2.0)
    sock.settimeout(2.0)
    try:
        send_frame(sock, {"caps": CAPS["ENCRYPT"]})    # 只声明 ENCRYPT
        agreed = recv_frame(sock)["caps"]
        assert agreed == 0, "ENCRYPT 与服务端无交集"
        send_frame(sock, {"wire": "Z:ollex"})          # 却发压缩编码
        reply = recv_frame(sock)
        raise AssertionError("违规帧不应被接受: %r" % reply)
    except ConnectionError:
        print("违规使用未协商能力: 服务端拒绝并终止会话")
    finally:
        sock.close()

    srv.close()
    print("结论: 能力位图是握手期的契约, 协商结果直接长在编解码代码路径上")


if __name__ == "__main__":
    main()
