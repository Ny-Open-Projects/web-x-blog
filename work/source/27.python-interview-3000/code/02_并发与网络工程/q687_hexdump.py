import struct


def hexdump(data: bytes, width: int = 16) -> str:
    lines = []
    for off in range(0, len(data), width):
        row = data[off:off + width]
        hex_part = " ".join(f"{b:02x}" for b in row)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in row)
        lines.append(f"{off:06x}  {hex_part:<{width * 3 - 1}}  |{ascii_part}|")
    return "\n".join(lines)


HEADER = struct.Struct("!2sBHI")
MAGIC = b"PY"


def annotate(data: bytes) -> str:
    lines = []
    try:
        magic, ver, mtype, length = HEADER.unpack_from(data)
        lines.append(f"  偏移 0-6  头部: magic={magic!r} ver={ver} type={mtype:#x} length={length}")
        ok_magic = magic == MAGIC
        body_end = HEADER.size + length
        actual = len(data) - HEADER.size
        lines.append(f"  长度字段={length}, 实际载荷={actual} → "
                     f"{'一致' if actual == length else '不一致 (典型 bug: 长度含头/含CRC)'}")
        lines.append(f"  magic 校验: {'通过' if ok_magic else '失败'}")
        lines.append(f"  预期帧总长 = 头{HEADER.size} + 体{length} = {body_end}, "
                     f"实际 {len(data)} 字节")
    except struct.error:
        lines.append("  数据不足以解析头部")
    return "\n".join(lines)


if __name__ == "__main__":
    # 构造一帧带 JSON 体的协议数据
    body = b'{"action":"reload","target":"config"}'
    frame = HEADER.pack(MAGIC, 1, 0x02, len(body)) + body
    print(hexdump(frame))
    print(annotate(frame))
    print()

    # 一个"长度算错"的坏帧: 长度多算了 4
    bad = HEADER.pack(MAGIC, 1, 0x02, len(body) + 4) + body
    print(hexdump(bad))
    print(annotate(bad))
