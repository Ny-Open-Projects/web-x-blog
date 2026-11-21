---
title: [NODE-259] Koa/Fastify 流式响应的实现差异？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-259：Koa/Fastify 流式响应的实现差异？
**答**:
- Koa：ctx.body = stream 框架接管 pipe（内部处理错误与 destroy）——注意 Koa 默认会把流错误上抛，需自行监听（NODE-214 背压语义保留）。
- Fastify：reply.send(stream) 同样接管；onSend hook 里修改流 payload 不适用（流无法缓存改写）——流响应要绕过 payload 改写钩子。
- 共同注意：客户端断开时框架 destroy 上游流（确认框架版本行为）；SSE 场景禁用框架的压缩/序列化（直接写 raw）。
- AI 场景（NODE-45x SSE）：框架层直接拿到 res 写 chunk + flush headers——Koa ctx.res / Fastify reply.raw。

```javascript
// Koa：SSE 直写（绕过 body 机制）
app.use(async (ctx) => {
  ctx.set({ 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', Connection: 'keep-alive' });
  ctx.respond = false;                              // 关闭 Koa 响应接管
  const res = ctx.res;
  res.writeHead(200);
  for await (const token of aiStream(prompt)) {
    res.write(`data: ${JSON.stringify({ token })}\n\n`);   // 手动 SSE 帧
  }
  res.end('data: [DONE]\n\n');
});
// Fastify：
fastify.get('/chat', (req, reply) => {
  reply.header('Content-Type', 'text/event-stream');
  reply.raw.writeHead(200, { ... });
  aiStream(req.query.prompt).forEach(token => reply.raw.write(`data: ${token}\n\n`));  // raw 直写
});
```
