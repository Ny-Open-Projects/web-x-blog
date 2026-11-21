import socket
import threading
import time


def pump(a: socket.socket, b: socket.socket) -> None:
    try:
        while True:
            data = a.recv(65536)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass


def relay_server(stop: threading.Event, port_box: list) -> None:
    """公网中继: 先连的注册为隧道 (内网侧), 后连的作为公网用户, 配对后双向搬运。"""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    tunnel: list = []
    users: list = []
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        conn.settimeout(1.0)
        try:
            first = conn.recv(64)
            conn.settimeout(None)
        except socket.timeout:
            first = b""
        if first.startswith(b"REG-TUNNEL"):
            tunnel.append(conn)
            print("[relay] 内网侧隧道注册")
        else:
            users.append((conn, first))
            print("[relay] 公网用户进入")
        # 配对: 隧道和用户各有一个即接通
        while tunnel and users:
            t = tunnel.pop(0)
            u, cached = users.pop(0)
            print("[relay] 隧道与用户配对, 开始转发")
            if cached:
                t.sendall(cached)
            threading.Thread(target=pump, args=(u, t), daemon=True).start()
            threading.Thread(target=pump, args=(t, u), daemon=True).start()
    srv.close()


def private_service(stop: threading.Event, relay_port: int) -> None:
    """内网服务: 主动连出, 挂在隧道上提供 echo。"""
    c = socket.create_connection(("127.0.0.1", relay_port))
    c.sendall(b"REG-TUNNEL echo\n")
    try:
        while not stop.is_set():
            data = c.recv(65536)
            if not data:
                break
            c.sendall(b"private-echo:" + data)  # 这里的回复将出现在公网用户侧
    except OSError:
        pass
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=relay_server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    relay_port = box[0]

    threading.Thread(target=private_service, args=(stop, relay_port), daemon=True).start()
    time.sleep(0.2)

    # 公网用户: 连中继即连到内网服务
    user = socket.create_connection(("127.0.0.1", relay_port), timeout=2)
    user.sendall(b"hello-from-public")
    user.settimeout(2)
    print("[user] 收到:", user.recv(64).decode())
    user.close()
    stop.set()
    print("原理: 内网侧的出站连接承载了入站流量, 无需公网 IP 与防火墙开洞")
