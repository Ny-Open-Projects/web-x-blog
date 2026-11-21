---
title: [Q5550] UDP 数据报大小 MTU 分片容量账
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5550 · UDP 数据报大小、MTU 分片与丢包容量账

> 难度:★★★★ | 标签:UDP, MTU, 分片, 容量规划, 丢包

**问**：一个 UDP 遥测服务在内网正常、跨机房后"大部分包收不到"。MTU 分片为什么对 UDP 特别致命？单包多大才安全？为什么 QUIC 把初始包压到 1200 字节？如何实测一条链路的可用报文大小并做容量规划？

**答**：UDP 没有重传与协商：超过路径 MTU 的数据报由 IP 层分片，而任一分片丢失 = **整个数据报丢弃**（无法只重传缺的片），且 IPv4 分片丢包率随片数乘性放大——1500 字节 MTU 下 8KB 报文要 6 个分片，若分片独立丢 1%，整包丢率 ≈ 1-(1-1%)^6 ≈ 6%。跨机房故障常见根因还有：中间设备（VPN/GRE/隧道封装再吃 20-40 字节头、某些链路 MTU 只有 1400 甚至 1280）导致"内网 8KB 能过、跨机房不行"；以及 IPv6 路由器**不分片**（超过 MTU 直接 ICMPv6 Packet Too Big，若被防火墙吞了就是黑洞）。安全尺寸共识：**端到端 ~1200 字节**（IPv6 最小 MTU 1280 减头部余量，QUIC 的选值），内网可测出实际 PMTUD 后放宽。容量账三笔：1) **单包上限** = 路径最小 MTU - IP 头 - UDP 头（8B）- 业务封装；2) **丢包容忍**：应用层设计必须假设 UDP 会丢——要么消息幂等可重发，要么在应用层做批确认（类 QUIC）；3) **放大防护**：UDP 反射放大攻击面（小请求大响应）在公网服务必须限制响应尺寸。实测法：从两端用递增尺寸的 padding 数据报对打 + 应用层回执，二分找出链路可用上限；Python 里 `sendto` 超过本地 MTU 会 EMSGSIZE（macOS 本地回环宽松、真实网卡严格）。

```python
# file: code/02_并发与网络工程/q5550_udp_mtu.py
import socket
import struct
import sys

print("python:", sys.version_info[:3])

# 1) 协议头固定开销: MTU -> 有效载荷的账
MTU = 1500
ipv4_hdr, ipv6_hdr, udp_hdr = 20, 40, 8
print(f"IPv4 MTU {MTU}: UDP 载荷上限 {MTU - ipv4_hdr - udp_hdr} B")
print(f"IPv6 MTU {MTU}: UDP 载荷上限 {MTU - ipv6_hdr - udp_hdr} B (隧道 GRE+24B 后更小)")
print("跨机房安全共识: ~1200 B (QUIC 初始包同款, IPv6 最小 MTU 1280 的余量)")

# 2) 实测: 本机 UDP 对打, 递增报文尺寸探测可用上限
def probe_max_datagram(host="127.0.0.1", upper=65000):
    rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx.bind((host, 0))
    rx.settimeout(0.5)
    tx.settimeout(0.5)
    port = rx.getsockname()[1]
    lo, ok_max = 1, 0
    for size in range(1000, upper, 1000):
        pkt = b"p" * size
        try:
            tx.sendto(pkt, (host, port))
            data, _ = rx.recvfrom(upper + 1)     # recvfrom 不设上限会静默截断
            if len(data) != size:
                print(f"注意: {size} B 实收 {len(data)} -> 截断风险")
                break
            ok_max = size
        except (socket.timeout, OSError):
            break
    rx.close(); tx.close()
    return ok_max

print("本机回环实测最大完整数据报:", probe_max_datagram(), "B (真实网卡/跨机房会小得多)")

# 3) 分片丢包放大: 数学账
p_frag = 0.01                                  # 单分片丢失率 1%
for n_frag in (1, 4, 6):
    p_drop = 1 - (1 - p_frag) ** n_frag
    print(f"{n_frag} 个分片: 整包丢失率 {p_drop:.1%} (乘性放大)")

# 4) 应用层对策: 分块 + 每块带序号, 丢失可独立重发
def chunk(payload, mtu_payload=1200):
    for i in range(0, len(payload), mtu_payload):
        seq = i // mtu_payload
        yield struct.pack("!H", seq) + payload[i:i + mtu_payload]

payload = b"D" * 5000
blocks = list(chunk(payload))
print("5000B ->", len(blocks), "块, 每块 1200B 内, 丢一块只重发一块")
```

**追问**：1) 为什么 recvfrom 缓冲区小了会"静默截断"而 sendto 超限会报错？——发送端在本地 MTU 处直接 EMSGSIZE（可立即失败）；接收端按调用给的 bufsize 截断多余字节并丢弃，应用无感知——所以 UDP 接收永远要把 recvfrom 的 buffer 开到"最大可能报文+1"再检查实收长度。2) PMTUD 机制对 UDP 有效吗？——IPv4 依赖 DF 位与 ICMP Frag Needed 回传，IPv6 靠 Packet Too Big；中间设备禁 ICMP 是常见黑洞根因，所以"不依赖 PMTUD、应用层控制在 1200B"是稳妥策略。3) 什么时候该直接换 TCP/QUIC 而不是修补 UDP？——消息有顺序/完整性要求、或需要在公网穿越（NAT 打洞复杂度除外）：QUIC 在 UDP 上补齐了可靠、拥塞控制与加密，自研 UDP 协议几乎总是重复发明 QUIC。

## 背诵要点
- UDP 超过路径 MTU 由 IP 分片，任一分片丢失整包丢弃，丢包率随片数乘性放大。
- 端到端安全尺寸 ~1200B（QUIC 共识，IPv6 最小 MTU 1280 的余量）；内网实测 PMTUD 后放宽。
- 接收端 recvfrom 缓冲开到最大可能+1 防静默截断；发送端 EMSGSIZE 是立即的失败信号。

## 复盘追问
- 跨机房 UDP 丢包 30% 的服务如何在一小时内定位是 MTU 黑洞还是拥塞丢包？（提示：递增尺寸对打二分上限 + 对照 ICMP 可达性 + 丢包是否集中于大包）
- 设计 UDP 遥测协议时，你的"分块+确认"应选择 ACK 全部还是 NACK 缺失？两者在什么丢包率下反转？（提示：高丢包下 NACK 反馈风暴，全员 ACK 开销线性，按丢包率与块数做混合）
