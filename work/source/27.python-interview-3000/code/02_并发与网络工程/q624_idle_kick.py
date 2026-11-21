import socket
import threading
import time

IDLE_TIMEOUT = 0.6
SCAN_INTERVAL = 0.2

sessions: dict = {}  # conn -> {"last_seen": ts, "name": str}
sessions_lock = threading.Lock()
kicked: list = []


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)

    def reaper() -> None:  # 巡检线程: 回收空闲连接
        while not stop.is_set():
            now = time.monotonic()
            with sessions_lock:
                dead = [c for c, s in sessions.items() if now - s["last_seen"] > IDLE_TIMEOUT]
            for c in dead:
                with sessions_lock:
                    info = sessions.pop(c, None)
                if info:
                    kicked.append(info["name"])
                    print(f"[reaper] 踢除空闲连接: {info['name']}")
                    c.close()
            time.sleep(SCAN_INTERVAL)

    threading.Thread(target=reaper, daemon=True).start()

    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        with sessions_lock:
            sessions[conn] = {"last_seen": time.monotonic(), "name": f"conn{id(conn) % 1000}"}
        threading.Thread(target=serve_conn, args=(conn,), daemon=True).start()
    srv.close()


def serve_conn(conn: socket.socket) -> None:
    conn.settimeout(0.1)
    try:
        while True:
            try:
                data = conn.recv(128)
                if not data:
                    break
                with sessions_lock:
                    if conn in sessions:
                        sessions[conn]["last_seen"] = time.monotonic()
                if data.strip() == b"PING":
                    conn.sendall(b"PONG")
                else:
                    conn.sendall(b"echo:" + data)
            except socket.timeout:
                continue
    except OSError:
        pass
    finally:
        with sessions_lock:
            sessions.pop(conn, None)
        conn.close()


def client(port: int, name: str, heartbeat: bool, duration: float) -> None:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    t0 = time.monotonic()
    while time.monotonic() - t0 < duration:
        if heartbeat:
            c.sendall(b"PING")
            c.settimeout(0.3)
            try:
                c.recv(16)
            except socket.timeout:
                pass
        time.sleep(0.2)
    try:
        c.close()
    except OSError:
        pass
    print(f"[{name}] 结束 (heartbeating={heartbeat})")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)
    port = box[0]
    # 客户端 A 持续心跳存活; 客户端 B 静默 → 被踢
    ta = threading.Thread(target=client, args=(port, "A-active", True, 1.2))
    tb = threading.Thread(target=client, args=(port, "B-silent", False, 1.2))
    ta.start(); tb.start()
    ta.join(); tb.join()
    time.sleep(0.3)
    print("被踢名单:", kicked)
    stop.set()
