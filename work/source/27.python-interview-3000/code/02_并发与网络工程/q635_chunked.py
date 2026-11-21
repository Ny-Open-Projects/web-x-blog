import socket
import threading
import time


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            conn.close()
            return
        data += chunk
    # 服务端边生成边发送: 模拟动态内容
    conn.sendall(
        b"HTTP/1.1 200 OK\r\n"
        b"Transfer-Encoding: chunked\r\n"
        b"Content-Type: text/plain\r\n\r\n"
    )
    for piece in (b"hello, ", b"chunked ", b"world!"):
        conn.sendall(f"{len(piece):x}\r\n".encode() + piece + b"\r\n")
        time.sleep(0.05)
    conn.sendall(b"0\r\nX-Trailer: done\r\n\r\n")  # 0 块 + trailer
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


class ChunkedParser:
    """流式 chunked 解析状态机: feed 任意切片, 输出完整内容与 trailer。"""

    def __init__(self) -> None:
        self.buf = b""
        self.state = "size"  # size / data / crlf / trailer / done
        self.remaining = 0
        self.body = b""
        self.trailers = {}

    def feed(self, data: bytes) -> None:
        self.buf += data
        while True:
            if self.state == "size":
                idx = self.buf.find(b"\r\n")
                if idx < 0:
                    return
                line, self.buf = self.buf[:idx], self.buf[idx + 2:]
                size = int(line.split(b";")[0], 16)  # 忽略扩展
                if size == 0:
                    self.state = "trailer"
                else:
                    self.remaining = size
                    self.state = "data"
            elif self.state == "data":
                if len(self.buf) < self.remaining:
                    return
                self.body += self.buf[:self.remaining]
                self.buf = self.buf[self.remaining:]
                self.state = "crlf"
            elif self.state == "crlf":
                if len(self.buf) < 2:
                    return
                self.buf = self.buf[2:]  # 块尾 CRLF
                self.state = "size"
            elif self.state == "trailer":
                idx = self.buf.find(b"\r\n")
                if idx < 0:
                    return
                line, self.buf = self.buf[:idx], self.buf[idx + 2:]
                if not line:
                    self.state = "done"
                    return
                k, _, v = line.partition(b": ")
                self.trailers[k.decode()] = v.decode()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n\r\n")
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += c.recv(4096)
    head, rest = buf.split(b"\r\n\r\n", 1)
    parser = ChunkedParser()
    parser.feed(rest)
    while parser.state != "done":
        data = c.recv(4096)
        if not data:
            break
        parser.feed(data)
    c.close()
    print("解析出的内容:", parser.body.decode())
    print("trailer:", parser.trailers)
    assert parser.body == b"hello, chunked world!"
    stop.set()
