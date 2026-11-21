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


def encode_frame(payload: bytes, opcode: int = 0x1, mask: bool = False) -> bytes:
    first = 0x80 | opcode  # FIN=1
    length = len(payload)
    header = bytes([first])
    mask_bit = 0x80 if mask else 0
    if length < 126:
        header += bytes([mask_bit | length])
    elif length < 65536:
        header += bytes([mask_bit | 126]) + struct.pack("!H", length)
    else:
        header += bytes([mask_bit | 127]) + struct.pack("!Q", length)
    if mask:
        key = os.urandom(4)
        masked = bytes(b ^ key[i % 4] for i, b in enumerate(payload))
        return header + key + masked
    return header + payload


def decode_frame(sock: socket.socket) -> tuple:
    def recv(n: int) -> bytes:
        buf = b""
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("closed")
            buf += chunk
        return buf

    b1, b2 = recv(2)
    fin = b1 >> 7
    opcode = b1 & 0x0F
    masked = b2 >> 7
    length = b2 & 0x7F
    if length == 126:
        (length,) = struct.unpack("!H", recv(2))
    elif length == 127:
        (length,) = struct.unpack("!Q", recv(8))
    mask_key = recv(4) if masked else None
    payload = recv(length)
    if masked:
        payload = bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload))
    return fin, opcode, payload


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
                fin, opcode, payload = decode_frame(conn)
                if opcode == 0x8:
                    conn.sendall(encode_frame(b"", opcode=0x8))
                    break
                print(f"[server] 帧 fin={fin} opcode={opcode} 载荷={payload.decode()!r}")
                conn.sendall(encode_frame(payload, opcode=opcode))  # 服务端不掩码
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

    c.sendall(encode_frame(b"hello", mask=True))           # 客户端必须掩码
    c.sendall(encode_frame(b"x" * 200, mask=True))         # 触发 2 字节扩展长度
    _, _, echo1 = decode_frame(c)
    _, _, echo2 = decode_frame(c)
    print("[client] 回显1:", echo1.decode())
    print(f"[client] 回显2: {len(echo2)} 字节, 内容正确={echo2 == b'x' * 200}")
    c.sendall(encode_frame(b"", opcode=0x8))               # 关闭帧
    c.close()
    stop.set()
