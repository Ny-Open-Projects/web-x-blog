"""TCP 粘包与半包: 长度前缀分帧器(纯标准库)。"""
import struct


def frame(msg):
    """编码: 4 字节大端长度前缀 + 载荷。"""
    payload = msg.encode("utf-8") if isinstance(msg, str) else msg
    return struct.pack(">I", len(payload)) + payload


class FrameAssembler:
    """流式装配器: 喂任意切割的字节, 吐完整消息, 剩余留在缓冲。"""

    def __init__(self):
        self.buf = b""

    def feed(self, data):
        self.buf += data
        messages = []
        while len(self.buf) >= 4:
            (length,) = struct.unpack(">I", self.buf[:4])
            if len(self.buf) < 4 + length:
                break                             # 半包: 前缀已见但载荷未到齐
            messages.append(self.buf[4:4 + length].decode("utf-8"))
            self.buf = self.buf[4 + length:]
        return messages


assembler = FrameAssembler()
stream = frame("hello") + frame(" tcp 粘包") + frame("world")
print("原始字节流 {} 字节".format(len(stream)))

# 场景一: 粘包, 三个帧一次性到达
msgs = assembler.feed(stream)
print("一次性喂入 -> {}".format(msgs))
assert msgs == ["hello", " tcp 粘包", "world"]

# 场景二: 半包, 逐字节喂入仍能精确还原
assembler2 = FrameAssembler()
collected = []
for i in range(len(stream)):
    collected += assembler2.feed(stream[i:i + 1])
print("逐字节喂入 -> {}".format(collected))
assert collected == msgs
assert assembler2.buf == b"", "完整消费后缓冲应为空"

# 场景三: 载荷里天然含有看起来像帧边界的内容也不会误切
tricky = frame("len=\x00\x00\x00\x04")
assembler3 = FrameAssembler()
assert assembler3.feed(tricky[:3]) == []
assert assembler3.feed(tricky[3:]) == ["len=\x00\x00\x00\x04"]
print("要点: TCP 是字节流没有消息边界, 粘包与半包不是 bug 而是常态; "
      "长度前缀或分隔符自己划边界, 装配器把 任意切割 归一化为 完整消息")
