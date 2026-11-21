import socket
import statistics
import threading
import time


def tcp_ping(host: str, port: int, count: int = 10, timeout: float = 1.0) -> dict:
    samples: list = []
    fails = 0
    for _ in range(count):
        t0 = time.monotonic()
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            s.close()
            samples.append((time.monotonic() - t0) * 1000)
        except OSError:
            fails += 1
        time.sleep(0.05)
    if not samples:
        return {"ok": False, "fails": fails}
    samples.sort()
    jitter = statistics.pstdev(samples)
    return {
        "ok": True, "fails": fails, "min": samples[0],
        "avg": statistics.mean(samples),
        "p95": samples[int(len(samples) * 0.95) - 1],
        "max": samples[-1], "jitter": jitter,
    }


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(16)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
            conn.close()  # 只做握手, 立即关闭
        except socket.timeout:
            continue
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    r = tcp_ping("127.0.0.1", port, count=20)
    print(f"TCP ping 127.0.0.1:{port} × 20:")
    print(f"  min={r['min']:.2f}ms avg={r['avg']:.2f}ms "
          f"p95={r['p95']:.2f}ms max={r['max']:.2f}ms 抖动={r['jitter']:.2f}ms")
    print(f"  失败 {r['fails']} 次")
    assert r["ok"] and r["avg"] < 50

    r2 = tcp_ping("127.0.0.1", 1, count=3, timeout=0.2)
    print("探测未监听端口:", r2)
    stop.set()
    print("结论: 无 ICMP 权限时, TCP connect 采样是应用视角的连通性/质量基线")
