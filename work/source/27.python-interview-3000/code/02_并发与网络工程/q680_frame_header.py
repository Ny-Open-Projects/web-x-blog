import struct
import zlib

MAGIC = b"PY"
VERSION = 1
HEADER = struct.Struct("!2sBBBBII")  # magic ver type flags rsv length crc
MAX_BODY = 1024 * 1024

T_HELLO, T_DATA, T_PING = 0x01, 0x02, 0x03
FLAG_COMPRESSED = 0x01


def build_frame(msg_type: int, body: bytes, flags: int = 0, version: int = VERSION) -> bytes:
    crc = zlib.crc32(MAGIC + bytes([version, msg_type, flags, 0]))  # 头参与校验
    crc = zlib.crc32(body, crc)
    header = HEADER.pack(MAGIC, version, msg_type, flags, 0, len(body), crc)
    return header + body


def parse_frame(data: bytes) -> dict:
    if len(data) < HEADER.size:
        raise ValueError("头不完整")
    magic, ver, mtype, flags, _rsv, length, crc = HEADER.unpack_from(data)
    if magic != MAGIC:
        raise ValueError(f"魔数不匹配: {magic!r}")
    if ver != VERSION:
        raise ValueError(f"版本不匹配: {ver}")
    if length > MAX_BODY:
        raise ValueError(f"长度超限: {length}")
    body = data[HEADER.size: HEADER.size + length]
    expect = zlib.crc32(MAGIC + bytes([ver, mtype, flags, 0]))
    expect = zlib.crc32(body, expect)
    if crc != expect:
        raise ValueError(f"CRC 校验失败: 期望 {expect:#x} 实际 {crc:#x}")
    if len(body) < length:
        raise ValueError("载荷不完整")  # 流式场景由上层缓冲后重试
    return {"version": ver, "type": mtype, "flags": flags,
            "length": length, "body": body}


if __name__ == "__main__":
    frame = build_frame(T_DATA, b"payload-1234", flags=FLAG_COMPRESSED)
    print(f"帧总长 {len(frame)} 字节 = 头 {HEADER.size} + 体 {len(frame) - HEADER.size}")
    print("头部 hex:", frame[:HEADER.size].hex(" "))

    parsed = parse_frame(frame)
    print("解析:", parsed)
    assert parsed["body"] == b"payload-1234"

    # 防御性校验逐一演示
    bad_magic = b"XX" + frame[2:]
    try:
        parse_frame(bad_magic)
    except ValueError as e:
        print("魔数错误拦截:", e)
    bad_ver = frame[:2] + bytes([9]) + frame[3:]
    try:
        parse_frame(bad_ver)
    except ValueError as e:
        print("版本错误拦截:", e)
    bad_crc = frame[:-1] + bytes([frame[-1] ^ 0xFF])
    try:
        parse_frame(bad_crc)
    except ValueError as e:
        print("CRC 错误拦截:", e)
