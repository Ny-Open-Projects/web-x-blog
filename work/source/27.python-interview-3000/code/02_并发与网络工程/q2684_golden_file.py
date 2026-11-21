# -*- coding: utf-8 -*-
"""协议测试的黄金文件: 冻结字节做回归基准。

- 黄金文件是手工核定过的字节序列, 编码器的任何漂移都逃不过比对;
- 流程: 解析黄金字节 -> 字段正确; 重新编码 -> 与黄金字节逐位一致;
- 再难的边界(空载荷、0x00、0xff)都固化进黄金里, 一次核定永久受益。
"""
import struct

HEADER = ">BHI"                              # magic 1B + seq 2B + len 4B


def encode(seq, payload):
    return struct.pack(HEADER, 0xA5, seq, len(payload)) + payload


def parse(buf):
    magic, seq, ln = struct.unpack_from(HEADER, buf, 0)
    assert magic == 0xA5, "magic 错误"
    payload = buf[7:7 + ln]
    assert len(payload) == ln, "载荷不完整"
    return seq, payload, buf[7 + ln:]


# 黄金文件: 手工核算过的字节, 十六进制冻结在此, 不由被测代码生成
GOLDEN = [
    ("普通帧 seq=1 PING", "a500010000000450494e47", (1, b"PING")),
    ("载荷含 0x00 与 0xff", "a5002a0000000200ff", (42, b"\x00\xff")),
    ("空载荷与最大 seq", "a5ffff00000000", (65535, b"")),
]


def run_golden_suite():
    passed = 0
    for name, hexstr, expect in GOLDEN:
        raw = bytes.fromhex(hexstr)
        seq, payload, rest = parse(raw)
        ok1 = (seq, payload) == expect and rest == b""
        ok2 = encode(seq, payload) == raw     # 重编码逐位回归
        status = "PASS" if (ok1 and ok2) else "FAIL"
        print("%s %s: 解析=%s 重编码一致=%s" % (status, name, ok1, ok2))
        passed += ok1 and ok2

    # 黄金流: 两帧粘连, 解析器必须按帧切开
    stream = bytes.fromhex(GOLDEN[0][1]) + bytes.fromhex(GOLDEN[2][1])
    seq1, p1, rest = parse(stream)
    seq2, p2, rest2 = parse(rest)
    ok = (p1 == b"PING" and p2 == b"" and rest2 == b"")
    print("%s 黄金流粘连解析: %s %s, 剩余 %d 字节" % ("PASS" if ok else "FAIL", p1, p2, len(rest2)))
    return passed + ok


if __name__ == "__main__":
    n = run_golden_suite()
    print("黄金文件回归: %d/%d 通过" % (n, len(GOLDEN) + 1))
    print("要点: 黄金文件的价值在'冻结'——用版本控制锁住字节, 而不是现场生成")
