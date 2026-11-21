import hashlib
import os
import socket
import sys
import tempfile
import threading
import time

BODY = os.urandom(2 * 1024 * 1024)  # 2MB 文件


def serve_file(conn: socket.socket, path: str, size: int) -> None:
    head = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {size}\r\n"
        "Content-Type: application/octet-stream\r\n\r\n"
    ).encode()
    conn.sendall(head)  # 头用普通发送
    conn.setblocking(True)  # sendfile 绕过 socket 超时机制,必须阻塞模式
    fd = os.open(path, os.O_RDONLY)
    try:
        offset = 0
        while offset < size:
            try:
                ret = os.sendfile(conn.fileno(), fd, offset, size - offset)
            except BlockingIOError:
                time.sleep(0.01)  # 缓冲区满,让内核排空后重试
                continue
            if isinstance(ret, tuple):
                sent, offset = ret
            else:
                sent = ret
                offset += sent
            if sent == 0:
                break
    finally:
        os.close(fd)


def server(stop: threading.Event, port_box: list, path: str) -> None:
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
            conn.settimeout(3)
            while b"\r\n\r\n" not in conn.recv(4096):
                pass
            serve_file(conn, path, len(BODY))
        except (OSError, ConnectionError) as e:
            print(f"[server] 传输中断: {e!r}")
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(BODY)
        path = f.name
    try:
        stop = threading.Event()
        box: list = []
        threading.Thread(target=server, args=(stop, box, path), daemon=True).start()
        while not box:
            time.sleep(0.01)

        c = socket.create_connection(("127.0.0.1", box[0]), timeout=5)
        c.sendall(b"GET /file HTTP/1.1\r\nHost: x\r\n\r\n")
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += c.recv(4096)
        head, body = buf.split(b"\r\n\r\n", 1)
        t0 = time.perf_counter()
        while len(body) < len(BODY):
            chunk = c.recv(1024 * 1024)
            if not chunk:
                break
            body += chunk
        c.close()
        dt = time.perf_counter() - t0
        ok = hashlib.sha1(body).hexdigest() == hashlib.sha1(BODY).hexdigest()
        first = head.split(b"\r\n")[0].decode(errors="replace")
        print(f"状态: {first}, 收到 {len(body)} 字节, "
              f"哈希{'一致' if ok else '不一致'}, {dt * 1000:.0f}ms "
              f"({len(BODY) / dt / 1024 / 1024:.0f} MB/s)")
    finally:
        os.unlink(path)
        stop.set()
