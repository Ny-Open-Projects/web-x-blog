import socket
import struct
import threading
import time

HEADER = struct.Struct("!I")  # 4 字节大端长度前缀


def frame(msg: str) -> bytes:
    raw = msg.encode()
    return HEADER.pack(len(raw)) + raw


def recv_exact(sock: socket.socket, n: int) -> bytes:
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(min(65536, n - len(buf)))
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
                head = recv_exact(conn, HEADER.size)
                (length,) = HEADER.unpack(head)
                if length > 10 * 1024 * 1024:
                    raise ValueError("超长帧, 防恶意攻击")
                payload = recv_exact(conn, length)
                print(f"[server] 收到 {length} 字节: {payload.decode()!r}")
                conn.sendall(frame("ack:" + payload.decode()))
        except (ConnectionError, ValueError, OSError) as e:
            print(f"[server] 连接结束: {e}")
        finally:
            conn.close()
    srv.close()


def client(port: int) -> None:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    # 多包合并发送 + 模拟半包: 把一个帧拆成两段发送
    data = frame("message-1") + frame("message-2")
    one = frame("message-3")
    c.sendall(data + one[:3])      # message-3 的头部只发一半
    time.sleep(0.05)
    c.sendall(one[3:])             # 剩余部分后到
    for _ in range(3):
        (length,) = HEADER.unpack(recv_exact(c, HEADER.size))
        print("[client] 应答:", recv_exact(c, length).decode())
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
