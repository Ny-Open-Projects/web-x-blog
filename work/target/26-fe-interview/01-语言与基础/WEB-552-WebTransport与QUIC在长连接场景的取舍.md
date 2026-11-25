---
title: [WEB-552] WebTransport 与 WebSocket 在长连接场景的取舍
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-552：WebTransport 与 WebSocket 在长连接场景的取舍

**答**：
- WebTransport 基于 HTTP/3（QUIC），支持多流、不可靠数据报（datagram）、连接迁移；WebSocket 是单流可靠有序，基于 TCP
- 选 WebTransport 的场景：实时协作（光标/草稿同步要不可达快通道）、云游戏/音视频控制信令（要低延迟、允许丢包）、弱网移动端（连接迁移）
- 选 WebSocket 的场景：普通 IM 消息（可靠有序正好）、成熟生态与既有网关/鉴权中间件、需要兼容老代理环境
- 落地差异要注意：WebTransport 需 h3 可用（UDP 通），在 h3 被拦地区需 WebSocket 兜底，客户端要做双通道探测降级
- 消息语义自己定：WebTransport 的 datagram 不可靠、stream 可靠但流间独立，业务要显式设计「哪些消息走哪条通道 + 重传策略」

```javascript
const wt = new WebTransport('https://api.example.com/wt');
await wt.ready;
// 可靠有序: 用 stream（类似双工流）
const stream = await wt.createBidirectionalStream();
// 低延迟可丢: 用 datagram（控制信令/光标位置）
wt.datagrams.writable.getWriter().write(new TextEncoder().encode(JSON.stringify({ t: 'cursor', x: 12, y: 5 })));
// 双通道降级: wt.ready 超时 → 切 WebSocket
const fallback = Promise.race([wt.ready, new Promise((_, r) => setTimeout(() => r(new Error('wt timeout')), 2000))]);
fallback.catch(() => connectWebSocket());
```

**追问**：

1. datagram 不可靠，业务层怎么知道消息丢了并补发？ → 加 seq/ack：接收方回确认，发送方超时未确认就重传；纯状态型消息（光标位置）则直接用后续快照覆盖，不必重传。
2. 网络封了 UDP 时 WebTransport 建连是什么表现？ → `wt.ready` 可能长时间 pending 或直接 reject，不能只 await 它，要 `Promise.race` 加超时；并且先判断 `'WebTransport' in window` 再探测。
3. 原来的 WebSocket 心跳与重连逻辑迁过来还要吗？ → 还要，但语义变了：datagram 没有内建保活，stream 关闭也只影响本流；仍需应用层 ping、重连和 session 恢复，避免丢会话状态。
