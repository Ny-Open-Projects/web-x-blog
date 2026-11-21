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
