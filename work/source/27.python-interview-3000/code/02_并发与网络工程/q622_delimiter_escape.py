import socket
import threading
import time

DELIM = b"\n"


def encode(msg: str) -> bytes:
    """转义为线上载荷(不含分隔符): 先转义反斜杠再转义换行, 顺序不能反。"""
    return msg.encode().replace(b"\\", b"\\\\").replace(b"\n", b"\\n")


def frame(msg: str) -> bytes:
    """完整一帧 = 转义载荷 + 分隔符; decode 只处理载荷本身。"""
    return encode(msg) + DELIM


def decode(raw: bytes) -> str:
    out = raw.replace(b"\\\\", b"\x00")  # 占位避免二次替换
    out = out.replace(b"\\n", b"\n").replace(b"\x00", b"\\")
    return out.decode()


class DelimParser:
    """基于缓冲区的分隔符解析: 天然处理半包与多包。"""

    def __init__(self) -> None:
        self.buf = b""

    def feed(self, data: bytes) -> list:
        self.buf += data
        msgs = []
        while True:
            idx = self.buf.find(DELIM)
            if idx < 0:
                break
            raw, self.buf = self.buf[:idx], self.buf[idx + 1:]
            msgs.append(decode(raw))
        return msgs


def server(stop: threading.Event, port_box: list) -> None:
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
        parser = DelimParser()
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                for msg in parser.feed(data):
                    print(f"[server] 完整消息: {msg!r}")
                    conn.sendall(frame("ack:" + msg))
        except OSError:
            pass
        finally:
            conn.close()
    srv.close()


def client(port: int) -> None:
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    # 消息内容含真实 \n 与 \, 编码后安全传输
    c.sendall(frame("line1\nline2") + frame("back\\slash"))
    c.settimeout(2)
    parser = DelimParser()
    got = []
    while len(got) < 2:
        got += parser.feed(c.recv(1024))
    for m in got:
        print("[client] 应答:", repr(m))
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)
    client(box[0])
    stop.set()
    assert decode(encode("a\nb\\c")) == "a\nb\\c"
    print("转义往返一致")
