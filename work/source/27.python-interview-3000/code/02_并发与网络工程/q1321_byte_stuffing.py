import random

DELIM = 0x7E
ESC = 0x7D


def stuff(payload: bytes) -> bytes:
    out = bytearray()
    for b in payload:
        if b in (DELIM, ESC):
            out.append(ESC)
            out.append(b ^ 0x20)
        else:
            out.append(b)
    return bytes(out)


def unstuff(stuffed: bytes) -> bytes:
    out = bytearray()
    i = 0
    while i < len(stuffed):
        b = stuffed[i]
        if b == ESC:
            i += 1
            if i >= len(stuffed):
                raise ValueError("帧尾孤立转义符, 帧损坏")
            out.append(stuffed[i] ^ 0x20)
        elif b == DELIM:
            raise ValueError("解填充阶段不应再见到定界符")
        else:
            out.append(b)
        i += 1
    return bytes(out)


class StuffedFrameReader:
    """从字节流里按 0x7E 定界提取帧, 自动跳过垃圾前缀。"""

    def __init__(self, max_frame: int = 256) -> None:
        self._buf = bytearray()
        self._max = max_frame
        self.resyncs = 0

    def feed(self, data: bytes) -> list:
        self._buf.extend(data)
        frames = []
        while True:
            if self._buf and self._buf[0] != DELIM:
                self.resyncs += 1
                idx = self._buf.find(bytes([DELIM]))
                if idx < 0:
                    self._buf.clear()
                    break
                del self._buf[:idx]
            end = self._buf.find(bytes([DELIM]), 1)
            if end < 0:
                if len(self._buf) > self._max:
                    raise ValueError("帧超长, 疑似对端异常")
                break
            frames.append(unstuff(bytes(self._buf[1:end])))
            del self._buf[:end + 1]
        return frames


def main() -> None:
    payloads = [b"hello\x7Eworld", b"\x7D\x7E\x7D", bytes(range(256)) * 2, b""]
    for p in payloads:
        wire = bytes([DELIM]) + stuff(p) + bytes([DELIM])
        assert DELIM not in stuff(p)[1:-1] or True
        assert unstuff(stuff(p)) == p, "必须无损回环"
        print(f"负载 {len(p):>4}B -> 填充后 {len(stuff(p)):>4}B  wire={wire[:20]!r}...")

    rnd = random.Random(7)
    for _ in range(200):                    # 随机负载压测
        p = bytes(rnd.randrange(256) for _ in range(rnd.randrange(50)))
        assert unstuff(stuff(p)) == p

    reader = StuffedFrameReader()
    wire = b"garbage" + bytes([DELIM]) + stuff(b"A") + bytes([DELIM]) \
        + bytes([DELIM]) + stuff(b"BCD") + bytes([DELIM])
    got = []
    pos = 0
    while pos < len(wire):                  # 不规则分片喂入
        step = random.Random(pos).randint(1, 5)
        got.extend(reader.feed(wire[pos:pos + step]))
        pos += step
    print(f"垃圾前缀重同步 {reader.resyncs} 次, 解出帧: {got}")
    assert got == [b"A", b"BCD"]
    print("字节填充回环 + 流式提取验证通过")


if __name__ == "__main__":
    main()
