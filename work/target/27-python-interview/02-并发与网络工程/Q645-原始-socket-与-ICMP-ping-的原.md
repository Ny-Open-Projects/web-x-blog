---
title: [Q645] 原始 socket 与 ICMP:ping 的原理
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q645 · 原始 socket 与 ICMP:ping 的原理

> 难度:★★★★ | 标签:raw socket, ICMP, ping

**问**:ping 是怎么实现的?为什么普通用户不能直接发 ICMP?

**答**:ping 用 ICMP Echo Request(type 8)/Reply(type 0),报文含校验和、标识符、序号,RTT 由发送/接收时间差算出。构造 ICMP 需要 raw socket(SOCK_RAW + IPPROTO_ICMP),能读写 IP 头之上的原始包,权限太大(可伪造源地址),所以 Linux 默认只有 root 或 cap_net_raw 能建;普通用户走的 ping 是 setuid/capabilities 包装的。Python 演示:尝试建 raw socket,无权限则降级演示 ICMP 报文构造与校验和算法(校验和计算是可离线验证的核心知识)。校验和实现的注意点:按 16 位字累加前奇数长度报文必须先补零,否则最后一对字节直接越界;高位进位要折回低位。TCP 探活(Q699)是无权限环境的替代方案。

```python
# file: code/02_并发与网络工程/q645_raw_icmp.py
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
```

**追问**:1) traceroute 的原理是什么?——发送 TTL=1,2,3... 的探测包,每个路由器转发前 TTL 减 1,减到 0 回 ICMP Time Exceeded,依次暴露沿途每一跳地址;UDP 版靠高端口不可达回 ICMP Port Unreachable 判断到达终点。2) ICMP 校验和算法的完整步骤?——按 16 位字累加、奇数长度先补零、高位进位折回低位、最后取反存入校验和字段;这是面试手写题的标准答案,且离线可验证(demo 无权限时降级演示的就是它)。3) 无权限环境怎么探活?——TCP connect 探测服务端口(Q699)、UDP 发包+端口不可达推断、应用层 health check;raw socket 需要 root 或 cap_net_raw(setcap 的原理),容器里还要看 capabilities 是否被裁剪。4) 生产陷阱?——RTT 用 time.time 计算,NTP 跳变出负数(用 monotonic);并发 ping 的标识符/序号冲突,应答错配;大批量 ping 触发 ICMP 速率限制,静默丢包被误判宕机。

---
