

class RespParser:
    """流式 RESP2 解析器: feed 任意切片, 输出完整值列表。"""

    def __init__(self) -> None:
        self.buf = b""

    def feed(self, data: bytes) -> list:
        self.buf += data
        out = []
        while True:
            value, consumed = self._parse(self.buf)
            if value is _INCOMPLETE:
                break
            out.append(value)
            self.buf = self.buf[consumed:]
        return out

    def _parse(self, buf: bytes) -> tuple:
        if not buf:
            return _INCOMPLETE, 0
        tag, body = buf[0:1], buf[1:]
        if tag in b"+-:":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            text = body[:idx].decode()
            n = idx + 2 + 1
            if tag == b"+":
                return text, n
            if tag == b"-":
                return RespError(text), n
            return int(text), n
        if tag == b"$":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            length = int(body[:idx])
            if length == -1:
                return None, idx + 2 + 1
            start = idx + 2                    # 载荷在 body 内的起点
            end = start + length + 2           # 载荷 + 尾部 CRLF (body 内)
            if len(body) < end:
                return _INCOMPLETE, 0          # 载荷未到齐
            return body[start: start + length], end + 1  # +1: 消耗含首字节标记
        if tag == b"*":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            count = int(body[:idx])
            if count == -1:
                return None, idx + 2 + 1
            pos = idx + 2 + 1
            items = []
            for _ in range(count):
                item, used = self._parse(buf[pos:])
                if item is _INCOMPLETE:
                    return _INCOMPLETE, 0
                items.append(item)
                pos += used
            return items, pos
        raise ValueError(f"未知 RESP 标记: {tag!r}")


class RespError(Exception):
    pass


_INCOMPLETE = object()


if __name__ == "__main__":
    p = RespParser()
    # 半包: 一个 bulk string 分三次喂入
    r1 = p.feed(b"$11\r\nhello ")
    print("第一片:", r1, "(应为空: 未到齐)")
    r2 = p.feed(b"world")
    print("第二片:", r2)
    r3 = p.feed(b"\r\n")
    print("第三片:", r3, "→", r3[0])

    # 粘包: 三种类型一次喂入
    mixed = b"+OK\r\n:42\r\n*2\r\n$3\r\nfoo\r\n$-1\r\n"
    vals = p.feed(mixed)
    print("粘包解析:", vals)
    assert vals[0] == "OK" and vals[1] == 42 and vals[2] == [b"foo", None]
    print("半包与粘包均正确处理")
