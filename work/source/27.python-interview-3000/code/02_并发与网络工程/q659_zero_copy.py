import os
import socket
import tempfile
import threading
import time

SIZE = 4 * 1024 * 1024  # 4MB


def serve_one(port_box: list, ready: threading.Event) -> socket.socket:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port_box.append(srv.getsockname()[1])
    ready.set()
    conn, _ = srv.accept()
    return conn


def send_read_write(conn: socket.socket, fd: int, size: int) -> float:
    """传统路径: read 到用户态再 send。"""
    t0 = time.perf_counter()
    sent = 0
    buf = bytearray(256 * 1024)
    os.lseek(fd, 0, os.SEEK_SET)
    while sent < size:
        n = os.readv(fd, [buf])  # 页缓存 → 用户态
        if n == 0:
            break
        conn.sendall(buf[:n])    # 用户态 → 内核 socket 缓冲
        sent += n
    return time.perf_counter() - t0


def send_sendfile(conn: socket.socket, fd: int, size: int) -> float:
    """零拷贝路径: os.sendfile 页缓存直达 socket。"""
    t0 = time.perf_counter()
    offset = 0
    while offset < size:
        try:
            sent = os.sendfile(conn.fileno(), fd, offset, size - offset)
        except OSError:
            # macOS 返回元组
            sent, offset_new = os.sendfile(conn.fileno(), fd, offset, size - offset)
            sent = sent if not isinstance(sent, tuple) else sent[0]
            offset = offset_new
            continue
        if sent == 0:
            break
        offset += sent
    return time.perf_counter() - t0


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile() as f:
        f.write(os.urandom(SIZE))
        f.flush()
        box: list = []
        ready = threading.Event()
        t = threading.Thread(target=serve_one, args=(box, ready), daemon=True)
        t.start()
        ready.wait()
        while not box:
            time.sleep(0.01)
        port = box[0]

        c = socket.create_connection(("127.0.0.1", port))
        conn, _ = (socket.socket(), None)  # 占位
        # 服务端 accept 在线程里, 这里直接演示两种发送方式于同一连接的两端
        # 实际上 conn 已在线程中 accept; 简化: 客户端读取字节计数
        fd = os.open(f.name, os.O_RDONLY)

        def drain(sock: socket.socket, total: int) -> None:
            got = 0
            while got < total:
                n = sock.recv(1024 * 1024)
                if not n:
                    break
                got += len(n)

        # 两种方法交替各发一次, 客户端消费
        import time as _t
        # 由于 accept 阻塞在线程内, 这里改用两轮独立连接测量
        c.close()

        def measure(method) -> float:
            conn2 = serve_one(box, ready)
            client = socket.create_connection(("127.0.0.1", conn2.getpeername()[0]))
            # conn2 是服务端 accept 到的连接; client 是客户端侧
            dt = method(conn2, fd, SIZE)
            client.close()
            conn2.close()
            return dt

        # 直接在主线程演示: 建立一对 loopback socket
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)
        cli = socket.create_connection(("127.0.0.1", srv.getsockname()[1]))
        conn, _ = srv.accept()
        threading.Thread(target=drain, args=(cli, SIZE * 2), daemon=True).start()

        t_rw = send_read_write(conn, fd, SIZE)
        t_sf = send_sendfile(conn, fd, SIZE)
        print(f"read+send (4 拷贝): {t_rw * 1000:.1f}ms")
        print(f"os.sendfile (零拷贝): {t_sf * 1000:.1f}ms")
        print(f"提升: {t_rw / max(t_sf, 1e-9):.2f}x (回环上差距保守, 真实网卡更明显)")
        conn.close()
        cli.close()
        srv.close()
        os.close(fd)
