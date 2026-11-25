---
title: [WEB-547] HTTP/3 迁移：服务器 UDP 缓冲区与内核调优
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-547：HTTP/3 迁移：服务器 UDP 缓冲区与内核调优

**答**：
- 最常见的翻车点：UDP 接收缓冲区太小，QUIC 实现启动时直接警告（ngtcp2/quiche 都会打印），高并发下大量丢包被内核丢弃而不是被协议层感知
- 核心参数：`net.core.rmem_max`/`wmem_max` 建议提到 16MB 以上；QUIC 是单 UDP socket 承载多流，突发吞吐远大于普通 UDP 服务
- `reuseport` 多进程分发：每个 worker 独立 socket，内核按四元组哈希分发——但 QUIC 连接迁移会换四元组，需实现共享 Connection ID 路由（较新内核的 SO_REUSEPORT + bpf 助手）
- GSO/UDP 分段卸载：开启 UDP GSO 能大幅降低 syscall 开销，这是 QUIC 服务器性能与 h2 拉平的关键
- 验证方法：`ss -ulmpn` 看缓冲区占用与丢弃计数（`netstat -su` 的 receive buffer errors），压测到高水位再观察

```bash
sysctl -w net.core.rmem_max=16777216
sysctl -w net.core.wmem_max=16777216
# 压测后检查丢包
netstat -su | grep -i "receive buffer errors"
# 期望: 0；若持续增长 → 缓冲区仍不足或 CPU 打满
```
