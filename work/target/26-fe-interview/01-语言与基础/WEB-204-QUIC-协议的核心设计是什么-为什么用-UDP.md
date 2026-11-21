---
title: [WEB-204] QUIC 协议的核心设计是什么？为什么基于 UDP？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-204：QUIC 协议的核心设计是什么？为什么基于 UDP？

**答**：
- 为什么用 UDP：TCP 由内核实现，改不动（中间设备僵化，中间盒会劫持/优化 TCP 特性）；UDP 几乎无状态，QUIC 在用户态重新实现可靠传输、拥塞控制、加密，迭代快。
- 核心设计：stream 独立可靠（单 stream 丢包不影响其他 stream）、内建 TLS 1.3（握手与传输合体，防明文中间盒干预）、连接 ID 标识连接（网络切换不断连）、每包独立加密序号防重放。
- QUIC 的拥塞控制在用户态实现，可按场景选择 BBR / Cubic 并快速迭代。
- 前端感知：首次建连快、弱网丢包下吞吐明显提升；UDP 被封锁时浏览器自动回落 HTTP/2（Alt-Svc 协商）。

```javascript
// QUIC vs TCP 建连 RTT 对比（示意）
// TCP+TLS1.2: 1(RTT SYN) + 1(SYN/ACK) + 1(TLS) + 1(TLS) ≈ 3~4 RTT
// TCP+TLS1.3: 2 RTT（TCP 1 + TLS 1）
// QUIC+TLS1.3 首连: 1 RTT（传输参数与握手合并）
// QUIC 重连(0-RTT): 0 RTT，直接带数据发早期包
console.log('弱网高丢包下，HTTP/2 全部 stream 卡在重传，HTTP/3 只有丢包的 stream 受影响');
```
