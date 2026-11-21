import socket
import threading
import time


def pump(src: socket.socket, dst: socket.socket, label: str, stats: dict) -> None:
    """单向搬运 + EOF 半关闭传播。"""
    try:
        while True:
            data = src.recv(65536)
            if not data:
                break
            stats[label] = stats.get(label, 0) + len(data)
            dst.sendall(data)
    except OSError:
        pass
    finally:
        try:
            dst.shutdown(socket.SHUT_WR)  # EOF 传播: 通知对端读完了
        except OSError:
            pass


def handle_client(client: socket.socket, backend_addr: tuple, stats: dict) -> None:
    try:
        backend = socket.create_connection(backend_addr, timeout=2)
    except OSError as e:
        print(f"[proxy] 后端不可达: {e}")
        client.close()
        return
    t1 = threading.Thread(target=pump, args=(client, backend, "up", stats))
    t2 = threading.Thread(target=pump, args=(backend, client, "down", stats))
    t1.start(); t2.start()
    t1.join(); t2.join()
    backend.close()
    client.close()
    print(f"[proxy] 连接结束 up={stats.get('up', 0)}B down={stats.get('down', 0)}B")


def proxy_server(stop: threading.Event, port_box: list, backend_addr: tuple) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    stats: dict = {}
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(conn, backend_addr, stats),
                         daemon=True).start()
    srv.close()


def backend_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            conn.settimeout(2)
            data = conn.recv(1024)
            conn.sendall(b"backend-echo:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    pb: list = []
    bb: list = []
    threading.Thread(target=backend_server, args=(stop, bb), daemon=True).start()
    while not bb:
        time.sleep(0.01)
    threading.Thread(target=proxy_server, args=(stop, pb, ("127.0.0.1", bb[0])),
                     daemon=True).start()
    while not pb:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", pb[0]), timeout=2)
    c.sendall(b"via-proxy")
    c.settimeout(2)
    print("[client] 经代理收到:", c.recv(64).decode())
    c.shutdown(socket.SHUT_WR)  # 半关闭: 验证 EOF 传播
    c.close()
    stop.set()
