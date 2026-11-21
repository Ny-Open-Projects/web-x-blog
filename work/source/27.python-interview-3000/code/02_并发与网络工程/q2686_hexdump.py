# -*- coding: utf-8 -*-
"""帧级排障日志: 十六进制 dump 与现场还原。

- 排障第一现场是字节: hexdump 让人眼直接核对线上到底发了什么;
- dump 的三段式: 偏移 + 十六进制 + ASCII 侧写, 不可打印字节显形为点;
- 拿着 dump 可以手工解帧, 验证协议实现的边界对不对。
"""
import struct


def hexdump(data, width=16):
    lines = []
    for off in range(0, len(data), width):
        chunk = data[off:off + width]
        hx = " ".join("%02x" % b for b in chunk)
        pad = " " * (width * 3 - len(hx))
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append("%08x  %s%s |%s|" % (off, hx, pad, asc))
    return "\n".join(lines)


def make_stream():
    """模拟抓包: 两帧 TLV 粘在一起, 第二帧载荷里有不可打印字节。"""
    f1 = struct.pack(">BH", 1, 4) + b"PING"
    f2 = struct.pack(">BH", 2, 7) + b"hi\x00\xff!"
    return f1 + f2


def dissect(stream):
    """从原始字节里手工解帧, 还原协议结构。"""
    off = 0
    while off < len(stream):
        typ, ln = struct.unpack_from(">BH", stream, off)
        payload = stream[off + 3: off + 3 + ln]
        print("  帧 @%#x type=%d len=%d payload=%r"
              % (off, typ, ln, payload))
        off += 3 + ln
    return off


if __name__ == "__main__":
    stream = make_stream()
    print("== 抓包原始字节 hexdump ==")
    print(hexdump(stream))
    print("== 手工解帧还原 ==")
    total = dissect(stream)
    print("共解析 %d 字节, 无剩余" % total)
    print("要点: 有 dump 在, '应该发了什么'与'实际发了什么'才对得上")
