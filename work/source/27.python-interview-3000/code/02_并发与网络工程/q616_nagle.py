import socket
import threading
import time

arrivals: dict = {}  # conn_id -> [到达时刻]


def server(stop: threading.Event, results: dict) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    results["port"] = srv.getsockname()[1]
    srv.settimeout(0.2)
    conn_id = 0
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        conn_id += 1
        cid = conn_id
        t0 = time.monotonic()
        arrivals[cid] = []
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # 收到第一个包后延迟 100ms 再响应, 模拟应用处理 + 触发对端延迟确认
        data1 = conn.recv(1)
        arrivals[cid].append(time.monotonic() - t0)
        time.sleep(0.1)
        conn.sendall(b"R1")
        data2 = conn.recv(1)
        arrivals[cid].append(time.monotonic() - t0)
        conn.sendall(b"R2")
        results[f"gap{cid}"] = arrivals[cid][1] - arrivals[cid][0]
        conn.close()
    srv.close()


def client(port: int, nodelay: bool) -> float:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    if nodelay:
        c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    c.sendall(b"A")      # 第一个小写
    time.sleep(0.01)     # 确保两个写在时间上错开
    c.sendall(b"B")      # 第二个小写: Nagle 开启时可能被扣住
    c.recv(2)
    c.recv(2)
    c.close()
    return 0.0


if __name__ == "__main__":
    stop = threading.Event()
    results: dict = {}
    t = threading.Thread(target=server, args=(stop, results), daemon=True)
    t.start()
    while "port" not in results:
        time.sleep(0.01)
    port = results["port"]

    client(port, nodelay=False)
    gap_nagle = results.get("gap1", 0)
    client(port, nodelay=True)
    gap_fast = results.get("gap2", 0)
    print(f"Nagle 开启: 第二包延迟到达 gap={gap_nagle * 1000:.0f}ms")
    print(f"NODELAY:    第二包立即到达 gap={gap_fast * 1000:.0f}ms")
    stop.set()
    t.join()
    print("结论: 交互式协议应设置 TCP_NODELAY, 批量传输无所谓")
