---
title: [WEB-078] 什么是带宽时延积 BDP？如何指导内核网络参数调优？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-078：什么是带宽时延积 BDP？如何指导内核网络参数调优？
**答**：
- BDP = 带宽 × RTT，表示"网络管道里同时能装多少数据"；TCP 吞吐要跑满带宽，收发缓冲区必须不小于 BDP。
- 典型误判：内网测试正常、跨国链路吞吐上不去——100Mbps 带宽 + 200ms RTT 的 BDP 约 2.5MB，默认 rmem 远不够。
- 调参对象是接收/发送缓冲区上限 rmem_max/wmem_max 与 tcp_rmem/tcp_wmem 三元组的最大值。
- BBR 官方建议额外开启 tcp_notsent_lowpath 之类细项可不管，先把缓冲区配够再谈其他。

```bash
# 计算 BDP：100Mbps 带宽、200ms RTT
awk 'BEGIN { printf "BDP = %.1f MB\n", 100 * 1000 * 1000 / 8 * 0.2 / 1024 / 1024 }'

# 按结果调大内核缓冲区上限
cat >> /etc/sysctl.conf << 'CONF'
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216
CONF
sysctl -p
# 验证：ss -tin 观察实际连接的 cwnd 与缓冲区
ss -tin dst example.com
```
