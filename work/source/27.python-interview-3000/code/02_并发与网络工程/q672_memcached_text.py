import socket
import threading


def memcached_server(stop: threading.Event, port_box: list) -> None:
    store: dict = {}
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)

    def handle(conn: socket.socket) -> None:
        conn.settimeout(2)
        buf = b""
        try:
            while True:
                data = conn.recv(65536)
                if not data:
                    break
                buf += data
                while b"\r\n" in buf:
                    line, buf = buf.split(b"\r\n", 1)
                    parts = line.decode().split()
                    if parts[0] == "set":
                        _cmd, key, flags, exptime, nbytes = parts
                        nbytes = int(nbytes)
                        while len(buf) < nbytes + 2:  # 数据 + \r\n 可能未到齐
                            chunk = conn.recv(65536)
                            if not chunk:
                                return
                            buf += chunk
                        value, buf = buf[:nbytes], buf[nbytes + 2:]
                        store[key] = (int(flags), value)
                        conn.sendall(b"STORED\r\n")
                    elif parts[0] == "get":
                        out = b""
                        for key in parts[1:]:
                            if key in store:
                                flags, value = store[key]
                                out += (f"VALUE {key} {flags} {len(value)}\r\n").encode() + value + b"\r\n"
                        out += b"END\r\n"
                        conn.sendall(out)
                    else:
                        conn.sendall(b"ERROR\r\n")
        except OSError:
            pass
        finally:
            conn.close()

    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(conn,), daemon=True).start()
    srv.close()


class MemcachedClient:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.create_connection((host, port), timeout=2)
        self.sock.settimeout(2)
        self.buf = b""  # 接收缓冲: 一次 recv 可能吞进多行, 必须按帧切分

    def _fill(self) -> None:
        chunk = self.sock.recv(4096)
        if not chunk:
            raise ConnectionError("server closed connection")
        self.buf += chunk

    def _readline(self) -> bytes:
        """读到一行 (含 CRLF); 多读的字节留在缓冲区给后续读取。"""
        while b"\r\n" not in self.buf:
            self._fill()
        line, self.buf = self.buf.split(b"\r\n", 1)
        return line + b"\r\n"

    def _read_exact(self, n: int) -> bytes:
        while len(self.buf) < n:
            self._fill()
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def set(self, key: str, value: bytes, flags: int = 0, exptime: int = 0) -> bool:
        head = f"set {key} {flags} {exptime} {len(value)}\r\n".encode()
        self.sock.sendall(head + value + b"\r\n")
        return self._readline() == b"STORED\r\n"

    def get(self, *keys: str) -> dict:
        self.sock.sendall(("get " + " ".join(keys) + "\r\n").encode())
        result = {}
        while True:
            line = self._readline()
            if line == b"END\r\n":
                break
            _tag, key, _flags, nbytes = line.decode().split()
            nbytes = int(nbytes)
            data = self._read_exact(nbytes + 2)  # 裸数据 + 尾部 CRLF
            result[key] = data[:nbytes]
        return result


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=memcached_server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)

    c = MemcachedClient("127.0.0.1", box[0])
    print("set:", c.set("user:1", b'{"name":"ada"}'))
    print("set:", c.set("user:2", b"\x00\x01\x02binary"))
    got = c.get("user:1", "user:2", "missing")
    for k, v in got.items():
        print(f"get {k}: {v!r}")
    assert got["user:2"] == b"\x00\x01\x02binary"
    print("一次 get 多 key + 二进制安全验证通过")
    c.sock.close()
    stop.set()
