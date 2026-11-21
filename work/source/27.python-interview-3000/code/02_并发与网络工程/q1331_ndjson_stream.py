import json


class LineTooLong(Exception):
    pass


class NDJSONReader:
    def __init__(self, max_line: int = 64) -> None:
        self._buf = bytearray()
        self._max = max_line
        self.bad_lines = 0

    def feed(self, data: bytes) -> list:
        self._buf.extend(data)
        out = []
        while True:
            nl = self._buf.find(b"\n")
            if nl < 0:
                if len(self._buf) > self._max:
                    raise LineTooLong(f"未换行字节 {len(self._buf)} 超过上限 {self._max}")
                break                      # 半行: 继续等
            line = bytes(self._buf[:nl])
            del self._buf[:nl + 1]         # 每轮必消费
            if not line.strip():
                continue                   # 空行跳过
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                self.bad_lines += 1        # 坏行隔离: 记账继续
                out.append({"__bad__": line.decode(errors="replace")[:32]})
        return out


def main() -> None:
    good = [{"i": i, "v": i * 2} for i in range(6)]
    stream = b""
    stream += b'{"i":0,"v":0}\n{"i":1,"v":2}\n'      # 两行合法
    stream += b'{"i":2,"v":\n{"i":3,"v":6}\n'         # 一行坏 JSON + 一行合法
    stream += b'\n{"i":4,"v":8}\n'                    # 空行 + 合法
    stream += b'{"i":5,"v":10'                        # 结尾半行等待

    reader = NDJSONReader(max_line=64)
    parsed = []
    pos = 0
    while pos < len(stream):                          # 任意碎片喂入
        step = (pos * 7 + 3) % 9 + 1
        parsed.extend(reader.feed(stream[pos:pos + step]))
        pos += step

    bad = [p for p in parsed if "__bad__" in p]
    good_parsed = [p for p in parsed if "__bad__" not in p]
    print(f"解析出 {len(parsed)} 个结果, 其中坏行 {len(bad)} 个被隔离")
    print("坏行样本:", bad[0] if bad else None)
    assert len(bad) == 1 and reader.bad_lines == 1
    assert good_parsed == [good[0], good[1], good[3], good[4]], \
        "坏行前后的合法行必须无损(坏行本身不产出数据)"

    tail = reader.feed(b'}\n')                        # 半行补齐
    good_parsed.extend([p for p in tail if "__bad__" not in p])
    assert good_parsed == good[:2] + good[3:], \
        "半行补齐后最后一行也要解析出来(坏行 i=2 永久缺失属预期)"
    print("全部合法行最终完整解析, 顺序不变")

    # 无限不换行必须被上限拦截
    r2 = NDJSONReader(max_line=16)
    try:
        r2.feed(b"x" * 100)
        print("超长行漏过!")
    except LineTooLong as exc:
        print(f"超长行被拦截: {exc}")


if __name__ == "__main__":
    main()
