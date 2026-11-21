import selectors
import socket
import threading
import time


def echo_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    sel = selectors.DefaultSelector()
    sel.register(srv, selectors.EVENT_READ, data="listener")
    conns = {}
    while not stop.is_set():
        for key, events in sel.select(timeout=0.2):
            if key.data == "listener":
                conn, addr = key.fileobj.accept()
                conn.setblocking(False)
                conns[conn.fileno()] = conn
                sel.register(conn, selectors.EVENT_READ, data="client")
                print(f"[mux] 新连接 fd={conn.fileno()}, 后端={type(sel).__name__}")
            else:
                conn = key.fileobj
                try:
                    data = conn.recv(1024)
                    if not data:
                        raise ConnectionError
                    conn.sendall(b"mux-echo:" + data)
                except (ConnectionError, OSError):
                    sel.unregister(conn)
                    conns.pop(conn.fileno(), None)
                    conn.close()
                    print("[mux] 连接关闭并注销")
    for c in conns.values():
        c.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=echo_server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)

    clients = [socket.create_connection(("127.0.0.1", box[0]), timeout=2) for _ in range(3)]
    for i, c in enumerate(clients):
        c.sendall(f"msg-{i}".encode())
        c.settimeout(1)
        print(f"client{i} 收到:", c.recv(64).decode())
    for c in clients:
        c.close()
    time.sleep(0.3)
    stop.set()
    print("单个线程 + 单个多路复用器服务了 3 个客户端连接")
