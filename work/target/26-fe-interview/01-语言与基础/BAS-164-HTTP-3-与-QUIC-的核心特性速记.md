---
title: [BAS-164] HTTP/3 与 QUIC 的核心特性速记？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-164：HTTP/3 与 QUIC 的核心特性速记？
**答**：
- 传输层换 UDP + QUIC：TLS 1.3 内建进握手，首次连接 1-RTT，重连可 0-RTT。
- 连接迁移：靠 Connection ID 识别连接，Wi-Fi 切 4G 不掉线（TCP 换 IP 必断）。
- 每条流独立确认与重传，彻底消除 TCP 队头阻塞；头部压缩用 QPACK 替代 HPACK。

```http
# HTTP/3 = HTTP over QUIC over UDP
# 1. 内建 TLS 1.3：握手与加密合并，1-RTT 建连，会话恢复 0-RTT
# 2. Connection ID：网络切换 IP 变了连接还在
# 3. 流级别独立丢包恢复：一条流丢包不再拖累其他流
# 4. QPACK 头部压缩、所有传输数据强制加密
```
