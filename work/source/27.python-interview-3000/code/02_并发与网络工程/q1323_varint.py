

def encode_varint(n: int) -> bytes:
    if n < 0:
        raise ValueError("无符号 varint 不收负数, 有符号请用 zigzag")
    out = bytearray()
    while True:
        group = n & 0x7F
        n >>= 7
        if n:
            out.append(group | 0x80)   # 继续位置 1
        else:
            out.append(group)          # 结束组
            return bytes(out)


def decode_varint(data: bytes, offset: int = 0) -> tuple:
    result = 0
    shift = 0
    while True:
        if offset >= len(data):
            raise ValueError("varint 在流中被截断")
        b = data[offset]
        offset += 1
        result |= (b & 0x7F) << shift
        if not (b & 0x80):
            return result, offset
        shift += 7
        if shift >= 64:
            raise ValueError("varint 超过 10 字节, 恶意或损坏")


def zigzag(n: int) -> int:
    return (n << 1) ^ (n >> 63) if n < 0 else n << 1


def main() -> None:
    cases = [0, 1, 127, 128, 300, 16383, 16384, 2**31, 2**63 - 1]
    for n in cases:
        raw = encode_varint(n)
        back, consumed = decode_varint(raw)
        assert back == n and consumed == len(raw)
        print(f"{n:>20} -> {len(raw)} 字节  {raw.hex()}")
        if len(raw) < 8:
            print(f"{'':20}   定长 8 字节编码省了 {8 - len(raw)} 字节")

    # 连续多个 varint 的流式解码
    stream = encode_varint(300) + encode_varint(7) + encode_varint(2**40)
    values = []
    offset = 0
    while offset < len(stream):
        v, offset = decode_varint(stream, offset)
        values.append(v)
    assert values == [300, 7, 2**40]
    print(f"流式解码 3 个连续 varint: {values}")

    # 截断与恶意超长必须报错
    for bad in (encode_varint(300)[:-1], b"\x80" * 11):
        try:
            decode_varint(bad)
            print("坏数据漏过!")
        except ValueError as exc:
            print(f"坏数据被拒: {exc}")

    print(f"zigzag(-1)={zigzag(-1)} zigzag(1)={zigzag(1)}: 有符号数先映射再 varint")


if __name__ == "__main__":
    main()
