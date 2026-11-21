

class Resp3Parser:
    """在 Q668 基础上支持 RESP3 push 类型 >, 并按类型分流。"""

    def __init__(self) -> None:
        self.buf = b""
        self.replies: list = []
        self.pushes: list = []

    def feed(self, data: bytes) -> None:
        self.buf += data
        while True:
            value, consumed, kind = self._parse(self.buf)
            if value is _INC:
                break
            self.buf = self.buf[consumed:]
            (self.pushes if kind == "push" else self.replies).append(value)

    def _parse(self, buf: bytes) -> tuple:
        if not buf:
            return _INC, 0, "reply"
        tag, body = buf[0:1], buf[1:]
        kind = "push" if tag == b">" else "reply"
        if tag in b"+-:>" or tag in b"*":
            if tag in b"+-:":
                idx = body.find(b"\r\n")
                if idx < 0:
                    return _INC, 0, kind
                text = body[:idx].decode()
                val = text if tag in b"+>" else (int(text) if tag == b":" else text)
                return val, idx + 3, kind
            # 数组或 push: 元素个数为 N
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INC, 0, kind
            count = int(body[:idx])
            pos = idx + 2 + 1
            items = []
            for _ in range(count):
                item, used, _k = self._parse(buf[pos:])
                if item is _INC:
                    return _INC, 0, kind
                items.append(item)
                pos += used
            return items, pos, kind
        if tag == b"$":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INC, 0, kind
            length = int(body[:idx])
            if length == -1:
                return None, idx + 3, kind
            start = idx + 2                    # 载荷在 body 内的起点
            end = start + length + 2           # 载荷 + 尾部 CRLF (body 内)
            if len(body) < end:
                return _INC, 0, kind           # 载荷未到齐
            return body[start: start + length], end + 1, kind  # +1: 含首字节标记
        raise ValueError(f"未知标记 {tag!r}")


_INC = object()


if __name__ == "__main__":
    p = Resp3Parser()
    # 模拟服务端输出: 普通回复 + push 交错到达 (订阅场景的真实流)
    stream = (
        b":1\r\n"                                   # SUBSCRIBE 的回复
        b">3\r\n$7\r\nmessage\r\n$6\r\nch-at3\r\n$5\r\nhello\r\n"  # push 消息
        b"+OK\r\n"                                  # 另一条命令的回复
        b">2\r\n$10\r\ninvalidate\r\n$4\r\nkey1\r\n"  # 客户端缓存失效推送
    )
    # 分两片喂: 验证 push 恰好被切成两半时也能解析
    p.feed(stream[:40])
    p.feed(stream[40:])
    print("命令回复队列:", p.replies)
    print("push 消息队列:", p.pushes)
    assert p.replies == [1, "OK"]
    assert p.pushes[0][0] == b"message" and p.pushes[1][0] == b"invalidate"
    print("回复与推送已正确分流 — RESP3 的核心改进")
