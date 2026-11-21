import os
import socket
import struct
import time


def checksum(data: bytes) -> int:
    """RFC 1071 校验和: 按 16 位字求和取反码。"""
    if len(data) % 2:
        data += b"\x00"
    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i + 1]
    while total >> 16:          # 高位进位折回低位
        total = (total & 0xFFFF) + (total >> 16)
    return (~total) & 0xFFFF


def build_echo(ident: int, seq: int, payload: bytes = b"py-ping") -> bytes:
    """ICMP Echo Request: type=8 code=0 + 校验和 + id + seq + 数据。"""
    header = struct.pack("!BBHHH", 8, 0, 0, ident, seq)
    packet = header + payload
    cksum = checksum(packet)
    return struct.pack("!BBHHH", 8, 0, cksum, ident, seq) + payload


if __name__ == "__main__":
    # 校验和自检: 补上校验和后整包再算应为 0
    # 注意奇数长度包要先补零再按 16 位字累加, 否则最后一对字节 IndexError
    pkt = build_echo(ident=0x1234, seq=1)
    csum_field = struct.unpack("!H", pkt[2:4])[0]
    zeroed = pkt[:2] + b"\x00\x00" + pkt[4:]
    if len(zeroed) % 2:
        zeroed += b"\x00"
    total = 0
    for i in range(0, len(zeroed), 2):
        total += (zeroed[i] << 8) + zeroed[i + 1]
    total += csum_field
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    verified = (~total & 0xFFFF) == 0
    print(f"ICMP 包 {len(pkt)} 字节, 校验和 0x{csum_field:04x}, 整包验证 {'通过' if verified else '失败'}")
    assert verified, "ICMP 校验和自检失败"

    # 尝试真实 raw socket: 普通用户大概率 PermissionError
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        print("raw socket 创建成功 (root/cap_net_raw): 可发真实 ICMP Echo")
        s.settimeout(1)
        s.sendto(pkt, ("127.0.0.1", 0))
        t0 = time.monotonic()
        data, addr = s.recvfrom(2048)
        icmp = data[20:]  # 跳过 IP 头
        itype, code = icmp[0], icmp[1]
        print(f"收到 ICMP type={itype} code={code} RTT={(time.monotonic() - t0) * 1000:.1f}ms")
        s.close()
    except PermissionError:
        print("raw socket 被拒: 普通用户无 cap_net_raw, 用 TCP 探活替代 (见 Q699)")
    except OSError as e:
        print(f"raw socket 不可用 ({e!r}): 本环境不支持, 演示跳过")
