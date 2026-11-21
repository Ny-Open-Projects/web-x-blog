import socket
import threading


class ReplyReader:
    """行缓冲必须跨应答存活: 一次 recv 可能带回下一应答的前几行。"""

    def __init__(self, sock: socket.socket) -> None:
        self._sock = sock
        self._buf = b""

    def read_reply(self) -> list:
        lines = []
        while True:
            while b"\r\n" not in self._buf:    # 严格 CRLF, 不吃裸 \n
                chunk = self._sock.recv(256)
                if not chunk:
                    raise ConnectionError("对端在应答中途断开")
                self._buf += chunk
            line, self._buf = self._buf.split(b"\r\n", 1)
            text = line.decode("ascii", errors="replace")
            if len(text) < 3 or not text[:3].isdigit():
                raise ProtocolError(f"应答行格式非法: {text!r}")
            lines.append(text)
            if len(text) == 3 or text[3] == " ":
                return lines                    # 第 4 字符是空格或行止于三位码: 结束
            if text[3] != "-":
                raise ProtocolError(f"第 4 字符既非 '-' 也非空格: {text!r}")


class ProtocolError(ValueError):
    pass


def main() -> None:
    replies = [
        b"220 mail.local ESMTP\r\n",
        b"250-PIPELINING\r\n250-SIZE 10485760\r\n250 HELP\r\n",
    ]
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.listen(1)

    def fake_server():
        conn, _ = srv.accept()
        try:
            for r in replies:
                conn.sendall(r)
        finally:
            conn.close()
            srv.close()

    threading.Thread(target=fake_server, daemon=True).start()
    cli = socket.create_connection(("127.0.0.1", port), timeout=2)
    reader = ReplyReader(cli)

    first = reader.read_reply()
    print("单行应答:", first)
    assert first == ["220 mail.local ESMTP"]

    caps = reader.read_reply()
    print("多行应答:", caps)
    assert caps == ["250-PIPELINING", "250-SIZE 10485760", "250 HELP"]
    assert caps[0][:3] == caps[-1][:3], "首末状态码一致"
    print("续行规则验证通过: 第 4 字符 '-' 继续, 空格结束, 状态码首末一致")
    cli.close()


if __name__ == "__main__":
    main()
