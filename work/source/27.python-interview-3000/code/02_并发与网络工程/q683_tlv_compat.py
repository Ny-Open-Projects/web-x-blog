import struct

TLV = struct.Struct("!BH")  # type(1) + length(2)
FLAG_REQUIRED = 0x80        # type 高位: 必须理解, 否则报错

TYPE_NAME, TYPE_SCORE, TYPE_REGION, TYPE_TRACE = 0x01, 0x02, 0x03, 0x84


def encode_tlv(ftype: int, value: bytes) -> bytes:
    required = ftype & FLAG_REQUIRED
    base = ftype & 0x7F
    return TLV.pack(required | base, len(value)) + value


def encode_v1() -> bytes:
    return encode_tlv(TYPE_NAME, b"ada") + encode_tlv(TYPE_SCORE, b"99")


def encode_v2() -> bytes:
    return (encode_v1()
            + encode_tlv(TYPE_REGION, b"cn-east")          # 老版本可安全跳过
            + encode_tlv(TYPE_TRACE, b"trace-id-xyz"))     # 带必须位: 老版本须报错


def parse(buf: bytes, known: dict, version: int) -> dict:
    fields = {}
    pos = 0
    while pos < len(buf):
        ftype, length = TLV.unpack_from(buf, pos)
        pos += TLV.size
        value = buf[pos:pos + length]
        pos += length
        required = ftype & FLAG_REQUIRED
        base = ftype & 0x7F
        if base in known:
            fields[known[base]] = value.decode()
        elif required:
            raise ValueError(
                f"v{version} 遇到不认识的必须字段 type={base}: 拒绝处理 (fail fast)")
        else:
            print(f"    [v{version}] 跳过未知可选字段 type={base} len={length} (前向兼容)")
    return fields


if __name__ == "__main__":
    v1_fields = {0x01: "name", 0x02: "score"}
    v2_fields = {0x01: "name", 0x02: "score", 0x03: "region", 0x04: "trace"}

    v1 = encode_v1()
    v2 = encode_v2()
    print(f"v1 报文 {len(v1)}B, v2 报文 {len(v2)}B (新增 region 与 trace 字段)")

    print("v1 解析器读 v1:", parse(v1, v1_fields, 1))
    print("v2 解析器读 v2:", parse(v2, v2_fields, 2))
    print("v2 解析器读 v1:", parse(v1, v2_fields, 2))
    print("v1 解析器读 v2 (trace 是新增必须字段, 旧解析器必然 fail fast):")
    try:
        print("  →", parse(v2, v1_fields, 1))
    except ValueError as e:
        print("  →", e)
