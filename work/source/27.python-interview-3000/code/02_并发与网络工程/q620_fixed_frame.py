import socket
import threading
import time

FRAME = 16  # 每条消息固定 16 字节, 不足补 \x00


def encode(msg: str) -> bytes:
    raw = msg.encode()
    assert len(raw) <= FRAME, f"消息超过 {FRAME} 字节"
    return raw.ljust(FRAME, b"\x00")


def recv_fixed(sock: socket.socket, n: int) -> bytes:
    buf = b""
    while len(buf) < n:          # recv 可能短读, 必须循环补齐
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("对端关闭")
        buf += chunk
    return buf


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
            while True:
                frame = recv_fixed(conn, FRAME)  # 一次一帧, 天然无粘包
                if not frame.strip(b"\x00"):
                    break
                msg = frame.rstrip(b"\x00").decode()
                print(f"[server] 完整收到一帧: {msg!r}")
                conn.sendall(encode("ack:" + msg))
        except (ConnectionError, OSError):
            pass
        finally:
            conn.close()
    srv.close()


def client(port: int) -> None:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    # 三帧数据一次 send 出去: 服务端仍按帧精确切分 → 粘包被协议化解
    payload = encode("frame-1") + encode("frame-2") + encode("frame-3")
    c.sendall(payload)
    for _ in range(3):
        print("[client] 收到应答:", recv_fixed(c, FRAME).rstrip(b"\x00").decode())
    c.sendall(encode(""))
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)
    client(box[0])
    stop.set()
