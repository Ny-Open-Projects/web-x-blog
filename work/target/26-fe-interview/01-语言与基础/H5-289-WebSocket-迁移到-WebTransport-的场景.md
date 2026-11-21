---
title: [H5-289] WebSocket 迁移到 WebTransport 的场景
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-289：WebSocket 迁移到 WebTransport 的场景

**答**：
- WebTransport：基于 QUIC 的下一代传输 API——多路复用（不队头阻塞）、可靠流 + 不可靠数据报并存、0-RTT 建连
- 相比 WS 的优势场景：云游戏/实时协作（不可靠数据报送最新状态，丢包不用重传）、多路媒体传输、移动网络连接迁移
- 三种通信模式：unidirectional/bidirectional streams（可靠有序）+ datagrams（不可靠无序）——按消息性质选通道
- 迁移成本：需要服务端 HTTP/3 栈支持、中间设备 UDP 放通、TLS 证书；浏览器支持已较广（Chromium 全量、Safari 就绪）
- 兼容策略：feature detect 降级到 WS；消息协议层设计成传输无关，只换传输适配层

```javascript
if ('WebTransport' in window) {
  const wt = new WebTransport('https://transport.example.com/wt');
  await wt.ready;
  const writer = wt.datagrams.writable.getWriter();
  writer.write(new TextEncoder().encode(JSON.stringify({ x: 1 }))); // 不可靠数据报
} else {
  const ws = new WebSocket('wss://transport.example.com/ws');
}
```
