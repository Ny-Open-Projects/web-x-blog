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
