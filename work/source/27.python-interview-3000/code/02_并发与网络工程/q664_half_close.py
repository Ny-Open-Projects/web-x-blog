import socket
import threading
import time


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
            # 读到 EOF (对端 shutdown WR) 才认为请求结束
            request = b""
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[server] 收到 EOF: 请求体结束, 开始响应")
                    break
                request += data
            conn.sendall(b"response-based-on-" + request)
            # 服务端也半关闭: 发完响应关闭写方向, 再等对端关闭
            conn.shutdown(socket.SHUT_WR)
            conn.close()
        except OSError:
            pass
    srv.close()


def client_half_close(port: int) -> None:
    c = socket.create_connection(("127.0.0.1", port))
    c.sendall(b"stream-request")
    c.shutdown(socket.SHUT_WR)   # 只关写: 保留读能力
    print("[client] 已 shutdown WR, 仍可读响应")
    c.settimeout(2)
    print("[client] 响应:", c.recv(64).decode())
    c.close()


def client_full_close(port: int) -> None:
    """对照组: 直接 close, 响应可能永远收不到。"""
    c = socket.create_connection(("127.0.0.1", port))
    c.sendall(b"full-close-request")
    c.close()  # 双向拆除: 服务端的响应发往已死连接
    print("[client] full close: 响应通道已毁")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]
    client_half_close(port)   # 正确姿势
    time.sleep(0.1)
    client_full_close(port)   # 反例
    time.sleep(0.1)
    stop.set()
