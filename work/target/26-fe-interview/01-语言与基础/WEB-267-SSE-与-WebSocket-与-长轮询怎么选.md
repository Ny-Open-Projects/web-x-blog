---
title: [WEB-267] SSE 与 WebSocket 与长轮询怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, WebSocket]
type: 面试题
---

## WEB-267：SSE 与 WebSocket 与长轮询怎么选？

**答**：
- SSE：HTTP 单向服务器推送（text/event-stream），自带断线重连与 Last-Event-ID 续传，浏览器原生 EventSource。适合通知、进度、AI 流式输出（GPT 打字机就是 SSE）。
- WebSocket：全双工二进制/文本，适合 IM、协同编辑、游戏等双向高频场景。
- 长轮询：兼容性兜底，服务端 hold 请求直到有数据再响应；资源开销大，现代场景仅在代理/老环境限制 WS 时用。
- 选型一句话：只下行选 SSE（简单可靠 HTTP 生态），要上行交互选 WS；都能走标准 HTTP 基础设施（SSE 不需要协议升级，经过负载均衡/网关更省心）。

```javascript
// SSE 接收（AI 流式回复典型用法）
const es = new EventSource('/api/chat/stream?msg=hi');
es.onmessage = (e) => { render.append(JSON.parse(e.data).delta); };
es.addEventListener('done', () => es.close());
// 注意 EventSource 不支持自定义 header，token 用 cookie 或 query
```
