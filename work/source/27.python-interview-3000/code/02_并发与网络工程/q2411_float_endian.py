# -*- coding: utf-8 -*-
"""浮点数的跨端互操作: IEEE754 位样 + 字节序, 两个坑叠一起。

- float 的字节序跟整数一样分大小端, struct 默认按本机序打包;
- 同一位样按错的序读, 得到的不是精度损失, 是完全不相干的浮点数;
- 跨端协议里浮点一律 struct 的 '>d'/'>f' 打包, 并用位样而非数值比对。
"""
import binascii
import struct

PI = 3.141592653589793


def main():
    be = struct.pack(">d", PI)                   # 网络序 8 字节
    le = struct.pack("<d", PI)                   # 本机小端 8 字节
    print("PI 的网络序位样:", binascii.hexlify(be).decode())
    print("PI 的小端位样  :", binascii.hexlify(le).decode())
    assert le == be[::-1], "浮点同样适用字节翻转规律"

    # 事故现场: 小端机器按本机序去读网络序的 8 字节
    wrong = struct.unpack("<d", be)[0]
    print("字节序读错得到的数: %.6g" % wrong)
    assert wrong != PI and (abs(wrong) > 1e100 or abs(wrong) < 1e-100), \
        "读错字节序得到的是完全不相干的数, 不是精度损失"

    # 正确姿势: 两端都用大端 d
    ok = struct.unpack(">d", be)[0]
    print("统一网络序读回: %.17g, 与原值 bits 相等: %s" %
          (ok, struct.pack(">d", ok) == be))
    assert struct.pack(">d", ok) == be, "跨端浮点必须按位样比对, 不按 =="

    # 精度提示: float32 会丢精度, 协议里要显式选择 f 或 d
    f32 = struct.unpack(">f", struct.pack(">f", PI))[0]
    print("过一遍 float32: %.9g (精度已损)" % f32)
    assert f32 != PI, "float32 往返必有精度损失, 要在协议文档里写明"

    # 同步发送双精度与单精度, 接收端按字段序解
    payload = struct.pack(">df", PI, 2.5)
    v1, v2 = struct.unpack(">df", payload)
    assert abs(v1 - PI) < 1e-15 and v2 == 2.5
    print("混合字段打包 12 字节, 解包一致")


if __name__ == "__main__":
    main()
