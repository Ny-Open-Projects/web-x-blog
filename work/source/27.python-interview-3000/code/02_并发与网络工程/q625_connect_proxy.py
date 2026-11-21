import socket
import threading
import time


def pump(a: socket.socket, b: socket.socket) -> None:
    """双向盲转发: 任一方向结束就拆除两端。"""
    try:
        while True:
            data = a.recv(65536)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


def proxy_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            client_conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(client_conn,), daemon=True).start()
    srv.close()


def handle_client(client: socket.socket) -> None:
    client.settimeout(2)
    request = b""
    while b"\r\n\r\n" not in request:
        chunk = client.recv(4096)
        if not chunk:
            client.close()
            return
        request += chunk
    line = request.split(b"\r\n")[0].decode()
    print(f"[proxy] 收到: {line}")
    if not line.startswith("CONNECT"):
        client.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
        client.close()
        return
    host, port = line.split()[1].rsplit(":", 1)
    try:
        remote = socket.create_connection((host, int(port)), timeout=2)
    except OSError as e:
        client.sendall(f"HTTP/1.1 502 Bad Gateway\r\n\r\n".encode())
        client.close()
        print(f"[proxy] 连目标失败: {e}")
        return
    client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
    print(f"[proxy] 隧道建立: {host}:{port}, 进入盲转发")
    t = threading.Thread(target=pump, args=(client, remote), daemon=True)
    t.start()
    pump(remote, client)  # 反向在当前线程; 任一方向结束即整体拆除
    t.join(timeout=1)


def echo_target(stop: threading.Event, port_box: list) -> None:
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
            data = conn.recv(1024)
            conn.sendall(b"target-echo:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    proxy_box: list = []
    target_box: list = []
    tp = threading.Thread(target=proxy_server, args=(stop, proxy_box), daemon=True)
    tt = threading.Thread(target=echo_target, args=(stop, target_box), daemon=True)
    tp.start(); tt.start()
    while not (proxy_box and target_box):
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", proxy_box[0]))
    c.sendall(f"CONNECT 127.0.0.1:{target_box[0]} HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n".encode())
    c.settimeout(2)
    resp = c.recv(1024)
    print("[client] 代理响应:", resp.split(b"\r\n")[0].decode())
    c.sendall(b"hello-via-tunnel")
    print("[client] 隧道内响应:", c.recv(1024).decode())
    c.close()
    stop.set()
