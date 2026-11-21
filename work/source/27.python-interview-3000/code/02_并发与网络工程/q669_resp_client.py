import socket
import threading
from q668_resp_parser import RespParser, RespError, _INCOMPLETE  # 复用解析器


def encode_bulk(data: bytes) -> bytes:
    if data is None:
        return b"$-1\r\n"
    return b"$" + str(len(data)).encode() + b"\r\n" + data + b"\r\n"


def encode_command(*args: str) -> bytes:
    out = b"*" + str(len(args)).encode() + b"\r\n"
    for a in args:
        out += encode_bulk(a.encode())
    return out


store: dict = {}


def dispatch(cmd: list) -> bytes:
    """语义层: 命令 → RESP 回复。"""
    name = cmd[0].decode().upper()
    if name == "PING":
        return b"+PONG\r\n"
    if name == "SET" and len(cmd) >= 3:
        store[cmd[1]] = cmd[2]
        return b"+OK\r\n"
    if name == "GET" and len(cmd) >= 2:
        return encode_bulk(store.get(cmd[1]))
    if name == "DEL" and len(cmd) >= 2:
        return b":1\r\n" if store.pop(cmd[1], None) is not None else b":0\r\n"
    return f"-ERR unknown command {name}\r\n".encode()


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=serve_conn, args=(conn,), daemon=True).start()
    srv.close()


def serve_conn(conn: socket.socket) -> None:
    parser = RespParser()
    conn.settimeout(2)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            for cmd in parser.feed(data):  # 一次可能解析出多条命令 (管道)
                if isinstance(cmd, list):
                    conn.sendall(dispatch(cmd))
    except (OSError, ValueError):
        pass
    finally:
        conn.close()


class RespClient:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.create_connection((host, port), timeout=2)
        self.sock.settimeout(2)
        self.parser = RespParser()
        self.pending: list = []  # 未消费的回复队列

    def command(self, *args: str):
        self.sock.sendall(encode_command(*args))
        return self._read_reply()

    def _read_reply(self):
        while not self.pending:
            data = self.sock.recv(4096)
            if not data:
                raise ConnectionError("closed")
            self.pending.extend(self.parser.feed(data))
        reply = self.pending.pop(0)
        if isinstance(reply, RespError):
            raise reply
        return reply


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)

    c = RespClient("127.0.0.1", box[0])
    print("PING:", c.command("PING"))
    print("SET:", c.command("SET", "name", "redis-mini"))
    print("GET:", c.command("GET", "name"))
    print("GET missing:", c.command("GET", "nope"))
    print("DEL:", c.command("DEL", "name"))
    print("DEL again:", c.command("DEL", "name"))
    try:
        c.command("BOGUS")
    except RespError as e:
        print("错误传播:", e)
    c.sock.close()
    stop.set()
