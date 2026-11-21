import struct

REQ_HEADER = struct.Struct("!BBHBBHIIQ")  # 24 字节请求头
RESP_HEADER = struct.Struct("!BBHBBHIIQ")  # 响应头同构

MAGIC_REQ = 0x80
MAGIC_RES = 0x81
OP_GET = 0x00
OP_SET = 0x01


def build_set_request(key: bytes, value: bytes, flags: int = 0, exptime: int = 0,
                      opaque: int = 1) -> bytes:
    """SET: extras = flags(4) + exptime(4)。"""
    extras = struct.pack("!II", flags, exptime)
    total = len(extras) + len(key) + len(value)
    header = REQ_HEADER.pack(
        MAGIC_REQ, OP_SET, len(key), len(extras), 0, 0, total, opaque, 0
    )
    return header + extras + key + value


def build_get_request(key: bytes, opaque: int = 2) -> bytes:
    header = REQ_HEADER.pack(MAGIC_REQ, OP_GET, len(key), 0, 0, 0, len(key), opaque, 0)
    return header + key


def parse_response(raw: bytes) -> dict:
    magic, opcode, key_len, extras_len, dtype, status, total, opaque, cas = \
        RESP_HEADER.unpack_from(raw, 0)
    body = raw[24:24 + total]
    extras = body[:extras_len]
    key = body[extras_len:extras_len + key_len]
    value = body[extras_len + key_len:]
    return {"opcode": opcode, "status": status, "key": key,
            "value": value, "opaque": opaque, "cas": cas}


if __name__ == "__main__":
    set_req = build_set_request(b"user:1", b"ada")
    print(f"SET 请求 {len(set_req)} 字节 = 24 头 + 8 extras + 6 key + 3 value")
    print("  头部 hex:", set_req[:24].hex(" "))

    get_req = build_get_request(b"user:1")
    print(f"GET 请求 {len(get_req)} 字节, 头部:", get_req[:24].hex(" "))

    # 模拟服务端响应: GET 命中
    value = b"ada"
    resp_body = value  # 无 extras
    resp = RESP_HEADER.pack(
        MAGIC_RES, OP_GET, 0, 0, 0, 0, len(resp_body), 2, 12345
    ) + resp_body
    parsed = parse_response(resp)
    print("响应解析:", parsed)
    assert parsed["value"] == b"ada" and parsed["opaque"] == 2
    print("opaque 字段回传: 客户端用它把响应配对到请求 (管线的基石)")

    # 对比文本协议报文
    print("\n同一 SET 的文本协议: 'set user:1 0 0 3\\r\\nada\\r\\n' =",
          len(b"set user:1 0 0 3\r\nada\r\n"), "字节")
