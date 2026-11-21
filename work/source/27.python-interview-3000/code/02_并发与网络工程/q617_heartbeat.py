import socket
import sys
import threading
import time


def enable_keepalive(sock: socket.socket) -> None:
    """设置内核级 keepalive 作为兜底 (参数平台相关)。"""
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    if sys.platform == "darwin":
        TCP_KEEPALIVE = 0x10
        sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, 60)  # 空闲 60s 开始探测
    elif sys.platform.startswith("linux"):
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3)


def server(stop: threading.Event) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    server.port = srv.getsockname()[1]  # type: ignore[attr-defined]
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        enable_keepalive(conn)
        conn.settimeout(2)
        while True:
            try:
                data = conn.recv(64)
            except socket.timeout:
                continue  # 心跳间隔内的静默是正常的
            if not data or data == b"PING":
                if data == b"PING":
                    conn.sendall(b"PONG")
                    continue
                break
            conn.sendall(b"echo:" + data)
        conn.close()
    srv.close()


def client_with_heartbeat(port: int) -> None:
    c = socket.socket()
    enable_keepalive(c)
    c.connect(("127.0.0.1", port))
    c.settimeout(1)

    def heartbeat() -> None:
        while not c._closed:  # 简化判断, 生产用状态标志
            try:
                c.sendall(b"PING")
                pong = c.recv(4)
                if pong != b"PONG":
                    print("心跳异常, 触发重连逻辑")
            except OSError:
                return
            time.sleep(0.05)

    hb = threading.Thread(target=heartbeat, daemon=True)
    hb.start()
    c.sendall(b"hello")
    print("业务响应:", c.recv(64).decode())
    time.sleep(0.2)  # 期间心跳在跑
    c.close()
    hb.join(timeout=1)


if __name__ == "__main__":
    stop = threading.Event()
    t = threading.Thread(target=server, args=(stop,), daemon=True)
    t.start()
    while not hasattr(server, "port"):
        time.sleep(0.01)
    client_with_heartbeat(server.port)  # type: ignore[attr-defined]
    stop.set()
    print("keepalive 兜底 + 应用心跳主动, 双层检测就绪")
