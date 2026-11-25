---
title: [NODE-716] 长连接选型（WS/SSE/长轮询）怎么定？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-716：长连接怎么选？
**答**：
- WebSocket：双向（客户端也能发）、二进制支持、协议升级——IM/协作（双向场景标配）。
- SSE：单向服务端推送（纯 HTTP——代理友好、自动重连内建、文本流）——AI 流式输出/通知推送（单向场景够用且更简单）。
- 长轮询：兼容兜底（SSE/WS 不可用降级——SCN-NODE-558 降级链）；成本最高（每请求新建）。
- 选型准则：双向需求（用户也发消息）→ WS；纯推送 → SSE（简单可靠）；兼容性差的环境 → 长轮询兜底——按「数据方向」选，WS 不是默认答案。
- 追问钩子：为什么「AI 流式输出」社区普遍选 SSE 而不是 WebSocket——SSE 纯 HTTP（经过代理/负载均衡无升级握手问题——CDN/网关兼容性好）、自动重连内建（Last-Event-ID 续传）、单向语义与场景匹配（只需服务端→客户端）；WS 的双向能力在此是冗余复杂度——按场景最小化协议能力。

```javascript
// SSE（AI 流式）
res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' });
for await (const chunk of llmStream) res.write(`data: ${JSON.stringify(chunk)}\n\n`);
// WS（双向 IM）
io.on('connection', socket => { socket.on('msg', handle); socket.emit('msg', out); });
```
