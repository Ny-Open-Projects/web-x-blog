import socket
import threading
import time


def probe_connect(host: str, port: int, timeout: float) -> None:
    t0 = time.monotonic()
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        print(f"connect {host}:{port} 成功 {(time.monotonic() - t0) * 1000:.0f}ms")
        s.close()
    except socket.timeout:
        print(f"connect 超时 ({timeout}s): SYN 无响应 → 宕机/防火墙丢包/队列满")
    except ConnectionRefusedError:
        print(f"connect refused: 端口未监听 (与超时是不同病)")
    except OSError as e:
        print(f"connect 失败: {e!r}")


def probe_read_timeout(port: int, timeout: float) -> None:
    """服务端接受连接但永不回复 → read 超时。"""
    c = socket.create_connection(("127.0.0.1", port), timeout=1)
    connect_ms = 0  # 连接秒成
    c.settimeout(timeout)
    t0 = time.monotonic()
    try:
        c.sendall(b"GET /slow HTTP/1.1\r\n\r\n")
        c.recv(1024)
    except socket.timeout:
        print(f"read 超时 ({timeout}s): connect 只用 {connect_ms}ms 但数据不来 → "
              f"对端处理慢/死锁, 卡了 {(time.monotonic() - t0) * 1000:.0f}ms")
    c.close()


def silent_server(stop: threading.Event, port_box: list) -> None:
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
        # 故意不回复不关闭: 制造 read 超时现场
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=silent_server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    print("--- 场景 1: 回环端口未监听 ---")
    probe_connect("127.0.0.1", 1, timeout=0.5)   # 1 号端口通常 refused
    print("--- 场景 2: 不可路由地址 → connect 超时 ---")
    probe_connect("10.255.255.1", 81, timeout=0.5)
    print("--- 场景 3: 假死服务 → read 超时 ---")
    probe_read_timeout(box[0], timeout=0.5)
    stop.set()
    print("结论: 先分清超时发生在哪个阶段, 病因清单完全不同")
