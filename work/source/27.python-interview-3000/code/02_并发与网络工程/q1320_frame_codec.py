import random
from dataclasses import dataclass

HEADER_LEN = 4   # 2 字节类型 + 2 字节负载长度(大端)
MAX_FRAME = 0xFF00   # 2 字节长度上限之内再留一条业务红线, 越线即恶意帧


@dataclass(frozen=True)
class Frame:
    msg_type: int
    payload: bytes


class EncodeError(ValueError):
    pass


DecodeError = EncodeError   # 解码失败与编码失败同族, 便于上层统一 except


class DecoderBroken(Exception):
    pass


def encode(frame: Frame) -> bytes:
    if len(frame.payload) >= MAX_FRAME:
        raise EncodeError(f"负载 {len(frame.payload)} 超过上限 {MAX_FRAME}")
    return frame.msg_type.to_bytes(2, "big") + len(frame.payload).to_bytes(2, "big") + frame.payload


class FrameDecoder:
    """有状态的流式解码器: feed 任意碎片, 吐出完整帧。"""

    def __init__(self, max_frame: int = MAX_FRAME) -> None:
        self._buf = bytearray()
        self._max = max_frame
        self._broken = False

    def feed(self, data: bytes) -> list:
        if self._broken:
            raise DecoderBroken("解码器已因非法帧报废, 应重连")
        self._buf.extend(data)
        frames = []
        while True:
            if len(self._buf) < HEADER_LEN:
                break
            msg_type = int.from_bytes(self._buf[0:2], "big")
            length = int.from_bytes(self._buf[2:4], "big")
            if length > self._max:
                self._broken = True     # 恶意长度: 立刻拒绝而不是试图跳过
                raise DecodeError(f"声明的负载长度 {length} 超过上限")
            if len(self._buf) < HEADER_LEN + length:
                break                    # 半包: 继续攒
            payload = bytes(self._buf[HEADER_LEN:HEADER_LEN + length])
            del self._buf[:HEADER_LEN + length]
            frames.append(Frame(msg_type, payload))
        return frames


def main() -> None:
    frames_in = [
        Frame(0x0001, b"hello"),
        Frame(0x0002, bytes(range(64))),
        Frame(0x0003, b"x" * 300),
    ]
    raw = b"".join(encode(f) for f in frames_in)
    print(f"编码得到 {len(raw)} 字节流")

    dec = FrameDecoder()
    rnd = random.Random(42)
    frames_out = []
    pos = 0
    cuts = 0
    while pos < len(raw):
        step = rnd.randint(1, 7)          # 极端碎片化: 1-7 字节一喂
        chunk = raw[pos:pos + step]
        pos += len(chunk)
        frames_out.extend(dec.feed(chunk))
        cuts += 1
    print(f"分 {cuts} 次碎片喂入, 解出 {len(frames_out)} 帧")
    assert frames_out == frames_in, "解码结果必须与原始帧完全一致"

    # 恶意长度必须被拒收: 长度字段写满 0xFFFF, 越过业务红线
    evil = (1).to_bytes(2, "big") + (0xFFFF).to_bytes(2, "big")
    try:
        dec.feed(evil[:2])
        dec.feed(evil[2:])
        print("恶意长度未被拦截!")
    except (DecodeError, DecoderBroken) as exc:
        print(f"恶意长度被拦截: {exc}")
        try:
            dec.feed(b"more")
        except DecoderBroken:
            print("报废状态确认: 后续 feed 直接抛错, 调用方应重连")


if __name__ == "__main__":
    main()
