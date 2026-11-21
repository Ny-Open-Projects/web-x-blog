# -*- coding: utf-8 -*-
"""大端小端的互操作实测: 各说各话就是乱码, 网络字节序是普通话。

- 同一个 int 在小端机器上是 78 56 34 12, 大端机器上是 12 34 56 78;
- 两端都用 struct 的 '>' 网络序打包, 才能互相解码;
- "本机能跑"测不出字节序 bug, 要用两端视角交叉验证。
"""
import binascii
import struct

VALUE = 0x12345678


def le_host_pack(v):
    """小端主机(多数 x86/ARM)用它自己的本机序打包。"""
    return struct.pack("<I", v)


def be_host_pack(v):
    """大端主机(一些网络设备/老架构)用它自己的本机序打包。"""
    return struct.pack(">I", v)


def main():
    le_wire = le_host_pack(VALUE)
    be_wire = be_host_pack(VALUE)
    print("小端机的线序:", binascii.hexlify(le_wire).decode())
    print("大端机的线序:", binascii.hexlify(be_wire).decode())
    assert le_wire != be_wire, "两端本机序的线序必然不同"

    # 互操作事故: 双方各用本机序解码对方的字节
    le_sees = struct.unpack("<I", be_wire)[0]
    be_sees = struct.unpack(">I", le_wire)[0]
    print("小端机误读大端线序: 0x%08X" % le_sees)
    print("大端机误读小端线序: 0x%08X" % be_sees)
    assert le_sees == 0x78563412, "字节序颠倒有确定的可预测错误值"
    assert be_sees == 0x78563412

    # 正确姿势: 双方都使用网络字节序(大端)
    net_wire = struct.pack(">I", VALUE)          # 或 struct.pack('!I', ...)
    ok_le = struct.unpack(">I", net_wire)[0]
    ok_be = struct.unpack(">I", net_wire)[0]
    print("统一网络序后两端都读到: 0x%08X" % ok_le)
    assert ok_le == ok_be == VALUE

    # socket 标准库自带的 htons/htonl 走同一条路
    port_net = socket_htons(8080)
    assert struct.unpack(">H", struct.pack(">H", 8080))[0] == 8080
    print("htons 打包端口: 0x%04X" % port_net)


def socket_htons(port):
    import socket
    return socket.htons(port)


if __name__ == "__main__":
    main()
