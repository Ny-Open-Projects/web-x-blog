import socket
import struct
import sys

VALUE = 0x12345678

if __name__ == "__main__":
    print("本机原生字节序:", sys.byteorder)

    be = struct.pack("!I", VALUE)   # 网络序 = 大端
    le = struct.pack("<I", VALUE)   # 小端
    native = struct.pack("=I", VALUE)
    print(f"大端   !I: {be.hex(' ')}")
    print(f"小端   <I: {le.hex(' ')}")
    print(f"原生   =I: {native.hex(' ')} (={'大端' if sys.byteorder == 'big' else '小端'})")
    assert struct.unpack("!I", be)[0] == VALUE
    assert struct.unpack("<I", le)[0] == VALUE

    # socket 字节序转换函数: 与 struct ! 等价
    n = socket.htonl(VALUE)
    print(f"htonl 结果 0x{n:08x} (内存按本机序解释即为大端字节排列)")
    assert socket.ntohl(n) == VALUE
    h = socket.htons(8080)
    print(f"htons(8080) = {h:#06x} → 线上字节 {h.to_bytes(2, 'big').hex(' ')}")

    # IP 地址的"点分十进制"本身就是大端读法
    packed = socket.inet_aton("192.168.1.1")
    print(f"inet_aton('192.168.1.1') = {packed.hex(' ')} (第一字节 0xc0 即 192 在最前 = 大端)")
    num = struct.unpack("!I", packed)[0]
    print(f"按网络序读成 uint32 = {num:#010x}")

    # 反例: 小端机器上用 '=' 传协议的灾难
    print("\n危险演示: 两台机器用 '=' 互传 0x12345678")
    print("  大端机解读小端机数据:", struct.unpack("!I", le)[0], "(错值!)")
    print("结论: 协议字段一律 '!' 或显式 '<', 永远不用 '='")
