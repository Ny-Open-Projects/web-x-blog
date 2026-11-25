---
title: [WEB-081] MTU 与分片的网络层常识有哪些？前端会遇到什么场景？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-081：MTU 与分片的网络层常识有哪些？前端会遇到什么场景？
**答**：
- MTU 是链路层单帧上限（以太网 1500），IP 层超过就分片；TCP 用 MSS（MTU 减去 IP+TCP 头约 40 字节 = 1460）避免 IP 分片。
- 隧道场景（VPN、PPPoE 1492、云上 VXLAN）实际 MTU 更小，PMTUD 若被 ICMP 拦截会出现"小包通、大包卡"的经典故障。
- HTTPS 握手证书往往超过一个 MSS，MTU 不匹配时表现为"TCP 通了但 TLS 卡死"。
- QUIC 走 UDP，UDP 不像 TCP 有自动分段，QUIC 强制规定最小 1200 字节的初始包以规避分片问题。

```bash
# 探测路径实际 MTU：-M do 表示禁止分片，超限时直接报错
ping -M do -s 1472 example.com   # 1472 + 28 字节头 = 1500，若通则路径 MTU 为 1500
ping -M do -s 1452 example.com   # 逐步下调二分查找能通过的最大值

# 查看与设置网卡 MTU
ip link show eth0 | grep mtu
ip link set dev eth0 mtu 1420   # VPN 环境常见的调小操作

# 用 curl 复现大 MTU 卡死：-s 看是否停在握手阶段
curl -v --max-time 5 https://example.com
```

## 十五、浏览器架构与进程
