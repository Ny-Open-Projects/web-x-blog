import socket
import threading
import time

log: list = []


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        conn.settimeout(2)
        t0 = time.monotonic()
        chunks = []
        try:
            while True:
                data = conn.recv(4096)
                if not data:
                    log.append(f"EOF at {(time.monotonic() - t0) * 1000:.1f}ms")
                    break
                chunks.append((time.monotonic() - t0, len(data), data))
        except socket.timeout:
            pass
        log.append(f"收到 {len(chunks)} 个 recv 分块:")
        for dt, n, payload in chunks:
            log.append(f"  +{dt * 1000:7.1f}ms  {n:3d}B  {payload!r}")
        conn.close()
    srv.close()


def send_experiment(port: int, nodelay: bool, label: str) -> None:
    c = socket.create_connection(("127.0.0.1", port))
    if nodelay:
        c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    log.append(f"--- {label} ---")
    c.sendall(b"a")                      # 三个小写背靠背
    c.sendall(b"b")
    c.sendall(b"c")
    time.sleep(0.3)
    c.shutdown(socket.SHUT_WR)           # 半关闭: 发送 EOF 但保留读
    c.settimeout(0.5)
    try:
        c.recv(10)  # 服务端不回复, 读完即关
    except socket.timeout:
        log.append("(服务端未响应, 半关闭后仍可等待)")
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    send_experiment(port, nodelay=False, label="Nagle 开启")
    send_experiment(port, nodelay=True, label="TCP_NODELAY")

    for line in log:
        print(line)
    print("观察点: 应用层三次 send 不等于三个包; recv 分块是到达边界不是发送边界")
    stop.set()
