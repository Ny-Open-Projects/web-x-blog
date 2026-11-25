---
title: [WEB-560] 直播场景的 QUIC 迁移收益怎么评估
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-560：直播场景的 QUIC 迁移收益怎么评估

**答**：
- 直播三类流量分开评估：拉流（HLS/LL-HLS 大文件）、弹幕（长连接小消息）、上行连麦（RTC 自有协议为主）
- 弹幕上 QUIC/HTTP3 长连接收益明确：弱网不重握手 + 连接迁移，配合 datagram 发「允许丢弃」的高频状态（在线人数、点赞数）
- 拉流若走 TCP 系（HLS over h2），迁移到 h3 的收益来自丢包恢复不阻塞流，弱网地区起播率/卡顿率是核心指标
- 连麦 RTC 一般已用 UDP 自有栈（WebRTC），QUIC 收益有限，别为了「全面 h3」强行迁，改造得不偿失
- 评估指标：起播时间 P75、卡顿人次比、弹幕端到端延迟 P95、弱网样本（RTT>150ms 或 loss>2%）单独出报表

```javascript
// 弹幕通道升级: 高频可丢消息走 WebTransport datagram
const wt = new WebTransport('https://live.example.com/dm');
await wt.ready;
const writer = wt.datagrams.writable.getWriter();
setInterval(() => {
  writer.write(enc.encode(JSON.stringify({ t: 'online', n: cnt }))); // 允许丢
}, 500);
// 可靠消息(礼物/进场)仍走 QUIC stream 或 WebSocket
```
