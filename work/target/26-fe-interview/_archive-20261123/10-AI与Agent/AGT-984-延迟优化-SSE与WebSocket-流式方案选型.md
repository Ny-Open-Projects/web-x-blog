---
title: [984] Agent 输出流式回传前端，SSE 和 WebSocket 怎么选
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, 流式]
type: 面试题
---

## 984：Agent 输出流式回传前端，SSE 和 WebSocket 怎么选

**答**：
- 默认 SSE：单向流（服务端→客户端）够用、HTTP 兼容性好（过网关/CDN/负载均衡无障碍）、断线自动重连是协议自带；聊天回答、进度推送都是典型场景。
- 选 WebSocket 的场景：双向交互（用户中途打断/批注需要高频上行）、二进制流、单连接多路复用；代价是网关配置、心跳保活、重连状态恢复都要自己做。
- 混合方案常见：SSE 推输出流，控制类操作（打断、重试）走普通 POST——避免为一个打断功能维护整套 WS。
- 追问钩子：SSE 在 HTTP/1.1 下浏览器 6 连接限制怎么办？——HTTP/2 多路复用解决；多标签页场景用 HTTP/2 或收敛到单连接复用。

```ts
// SSE 服务端
res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' });
for await (const chunk of llmStream) {
  res.write(`event: delta\ndata: ${JSON.stringify(chunk)}\n\n`);
}
res.write('event: done\ndata: {}\n\n');
// 客户端：断线重连协议自带
const es = new EventSource('/chat/123');
es.addEventListener('delta', e => append(JSON.parse(e.data)));
```

