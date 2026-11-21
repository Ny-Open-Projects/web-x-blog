---
title: [NODE-170] 设计一个 AI 应用后端（流式/会话/工具调用网关）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-170：设计一个 AI 应用后端（流式/会话/工具调用网关）？
**答**：
- 网关三职责：**统一协议**（多模型适配层）、**流式透传**（SSE，NODE-120）、**会话与计费管理**（记忆、token 计量、限流预算）。
- 流式链路：客户端 SSE ← BFF ← 上游 LLM SSE；逐块转发同时统计 usage，结束后落计费流水。
- 会话记忆：超窗滑动截断 + 早期对话摘要压缩；工具调用（function calling）：模型返回 tool_calls → 服务端执行 → 结果回填再请求，循环直到终止。
- 治理：按用户限流与日预算、敏感词前置过滤（NODE-096）、prompt 注入检测、超时与重试。

```javascript
app.post('/api/chat', rateLimitPerUser({ rpm: 10 }), async (ctx) => {
  const { messages, tools } = ctx.request.body;
  ctx.set('content-type', 'text/event-stream; charset=utf-8');   // SSE 流式

  const upstream = await fetch(`${LLM_BASE}/chat/completions`, {
    method: 'POST',
    headers: { authorization: `Bearer ${env.LLM_KEY}` },
    body: JSON.stringify({
      model: 'glm-4',
      messages: withMemory(ctx.state.uid, messages),  // 会话记忆注入
      tools,
      stream: true,
    }),
  });

  let usage = { prompt: 0, completion: 0 };
  const reader = upstream.body.getReader();
  const decoder = new TextDecoder();
  while (true) {                                      // 逐块透传 + 计量
    const { done, value } = await reader.read();
    if (done) break;
    const text = decoder.decode(value);
    usage = accumulateUsage(usage, text);
    ctx.res.write(text);
  }
  ctx.res.end();
  await billing.record(ctx.state.uid, usage, 'glm-4'); // token 计费落流水
});
// 工具调用循环：model 返回 tool_calls → 服务端执行 → 结果回填 messages → 再次请求
```
