import struct
import zlib

HEADER = struct.Struct("!2sBBHI")  # magic ver type flags length (演示简化, 校验放体尾)
MAGIC = b"PY"
MAX_BODY = 65536


def encode(msg_type: int, body: bytes, flags: int = 0, ver: int = 1) -> bytes:
    crc = zlib.crc32(body)
    return HEADER.pack(MAGIC, ver, msg_type, flags, len(body)) + body + struct.pack("!I", crc)


class FrameDecoder:
    def __init__(self) -> None:
        self.buf = bytearray()
        self.frames: list = []
        self.errors: list = []

    def feed(self, data: bytes) -> list:
        self.buf += data
        out = []
        while True:
            if len(self.buf) < HEADER.size:
                break
            magic, ver, mtype, flags, length = HEADER.unpack_from(self.buf, 0)
            if magic != MAGIC:
                self.errors.append(f"bad magic at offset, drop {len(self.buf)} bytes")
                self.buf.clear()  # 防灌垃圾: 头非法立即清空
                break
            if length > MAX_BODY:
                self.errors.append(f"length {length} 超限, 断连级错误")
                self.buf.clear()
                break
            total = HEADER.size + length + 4
            if len(self.buf) < total:
                break  # 半包: 等更多数据
            body = bytes(self.buf[HEADER.size: HEADER.size + length])
            (crc,) = struct.unpack_from("!I", self.buf, HEADER.size + length)
            if zlib.crc32(body) != crc:
                self.errors.append("CRC mismatch, drop frame")
                del self.buf[:total]  # 只丢这一帧, 继续解析后续
                continue
            out.append({"ver": ver, "type": mtype, "flags": flags, "body": body})
            del self.buf[:total]
        return out


if __name__ == "__main__":
    d = FrameDecoder()
    f1 = encode(0x01, b"hello")
    f2 = encode(0x02, b"x" * 100, flags=0x01)
    f3 = encode(0x03, b"tail")

    # 极端切片: 头被劈开、帧体逐字节到达、多帧合并
    stream = f1 + f2 + f3
    chunks = [stream[:3], stream[3:20], stream[20:21], stream[21:110],
              stream[110:111], stream[111:]]

    got: list = []
    for i, chunk in enumerate(chunks):
        frames = d.feed(chunk)
        got.extend(frames)
        print(f"feed 片段{i} ({len(chunk)}B) → 解析出 {len(frames)} 帧, 缓冲 {len(d.buf)}B")

    print(f"\n共解析 {len(got)} 帧:", [f["body"][:10] for f in got])
    assert [f["body"] for f in got] == [b"hello", b"x" * 100, b"tail"]

    # CRC 损坏帧: 只丢该帧不伤后续
    d2 = FrameDecoder()
    corrupted = f1[:-1] + bytes([f1[-1] ^ 0xFF]) + f3
    frames = d2.feed(corrupted)
    print("CRC 损坏后恢复:", [f["body"] for f in frames], "错误:", d2.errors)
    assert [f["body"] for f in frames] == [b"tail"]
