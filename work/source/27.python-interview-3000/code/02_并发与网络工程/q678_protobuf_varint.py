

def encode_varint(n: int) -> bytes:
    """无符号 varint: 每 7 位一组, 高位为续传标志。"""
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b | 0x80)  # 最高位置 1: 还有后续字节
        else:
            out.append(b)
            return bytes(out)


def decode_varint(buf: bytes, pos: int = 0) -> tuple:
    result = 0
    shift = 0
    while True:
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        if not b & 0x80:
            return result, pos
        shift += 7


WIRE_VARINT, WIRE_LEN = 0, 2


def encode_field_varint(field: int, value: int) -> bytes:
    tag = (field << 3) | WIRE_VARINT
    return encode_varint(tag) + encode_varint(value)


def encode_field_string(field: int, s: str) -> bytes:
    tag = (field << 3) | WIRE_LEN
    payload = s.encode()
    return encode_varint(tag) + encode_varint(len(payload)) + payload


def decode_message(buf: bytes) -> dict:
    msg = {}
    pos = 0
    while pos < len(buf):
        tag, pos = decode_varint(buf, pos)
        field, wire = tag >> 3, tag & 0x7
        if wire == WIRE_VARINT:
            msg[field], pos = decode_varint(buf, pos)
        elif wire == WIRE_LEN:
            length, pos = decode_varint(buf, pos)
            msg[field] = buf[pos:pos + length].decode()
            pos += length
        else:
            raise ValueError(f"演示不支持 wire_type {wire}")
    return msg


if __name__ == "__main__":
    # 经典验证: message { int32 id = 1; } id=150 → 08 96 01
    assert encode_varint(150) == b"\x96\x01"
    assert decode_varint(b"\x96\x01") == (150, 2)
    print("varint 150:", encode_varint(150).hex(" "), "(协议文档同款)")

    # 完整消息: {id=150, name='ada'}
    msg = encode_field_varint(1, 150) + encode_field_string(2, "ada")
    print("完整消息:", msg.hex(" "), f"共 {len(msg)} 字节")
    print("解码:", decode_message(msg))
    assert decode_message(msg) == {1: 150, 2: "ada"}

    # 对比 JSON 同内容
    import json
    j = json.dumps({"id": 150, "name": "ada"}).encode()
    print(f"JSON {len(j)} 字节 vs protobuf {len(msg)} 字节 → 体积比 {len(j) / len(msg):.1f}x")

    # 大数与边界
    print("varint 2^31:", encode_varint(2 ** 31).hex(" "), "(5 字节, 每 7 位进一位)")
    assert decode_varint(encode_varint(2 ** 31)) == (2 ** 31, 5)
