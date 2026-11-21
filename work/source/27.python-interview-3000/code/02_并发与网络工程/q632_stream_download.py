import socket
import threading
import time

TOTAL = 1024 * 1024  # 1MB 模拟大文件


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            conn.close()
            return
        data += chunk
    conn.sendall(
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/octet-stream\r\n"
        + f"Content-Length: {TOTAL}\r\n\r\n".encode()
    )
    sent = 0
    block = b"\xab" * 65536
    while sent < TOTAL:
        n = min(65536, TOTAL - sent)
        conn.sendall(block[:n])
        sent += n
    conn.close()


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


def stream_download(port: int, chunk_size: int = 131072) -> None:
    c = socket.create_connection(("127.0.0.1", port), timeout=5)
    c.sendall(b"GET /file HTTP/1.1\r\nHost: x\r\n\r\n")
    # 读头部
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += c.recv(4096)
    head, body = buf.split(b"\r\n\r\n", 1)
    total = int(dict(
        l.split(b": ", 1) for l in head.split(b"\r\n")[1:] if b": " in l
    )[b"Content-Length"])
    received = len(body)
    t0 = time.perf_counter()
    last_report = 0
    while received < total:
        chunk = c.recv(chunk_size)
        if not chunk:
            break
        received += len(chunk)
        pct = received * 100 // total
        if pct >= last_report + 25:  # 每 25% 报告一次进度
            speed = received / max(time.perf_counter() - t0, 1e-9) / 1024
            print(f"  进度 {pct:3d}%  已收 {received / 1024:.0f}KB  {speed:.0f}KB/s")
            last_report = pct
    c.close()
    print(f"下载完成: {received} / {total} 字节校验 {'通过' if received == total else '失败'}")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    stream_download(box[0])
    stop.set()
