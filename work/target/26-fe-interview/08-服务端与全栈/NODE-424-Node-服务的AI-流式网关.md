---
title: [NODE-424] Node 服务作为 AI 流式网关（LLM 代理层）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-424：AI 流式网关设计
**答**:
- 网关职责：统一接入（多模型厂商适配）、流式转发（上游 SSE → 下游 SSE/NDJSON，解析增量转发）、鉴权与配额（按用户/token 用量计量 NODE-401）、内容安全（输入输出过滤钩子）、成本与路由（便宜模型优先，复杂任务路由高级模型）。
- 流式转发细节：上游 chunk 解析（SSE 解析器：data: 行处理、[DONE] 标记）、逐 token 转发（不缓存整响应——首 token 延迟是体验核心）、断流恢复（上游中断 → 给下游明确的错误事件，前端可重试，ARC-423 不完整数据语义）。
- 用量计量：token 数从上游 usage 字段或本地估算（tokenizer）→ 计量事件 → 配额超限中断（流中断的用户提示）。
- 超时与重试：首 token 超时（连接建立但慢出——快速失败换路由）与流中断重试不同策略；重试带幂等（同一请求 ID）。
- 降级：模型不可用 → 备用模型路由 → 最终降级提示；限流排队（并发上限保护上游配额）。
```javascript
app.post('/ai/chat', async (req, res) => {
  res.writeHead(200, sseHeaders());
  const upstream = await llm.stream({ model: route(req.body), ...req.body,
    signal: reqAbortSignal(req) });
  let usage = 0;
  for await (const chunk of upstream) {
    if (req.closed) break;                                       // 取消传播
    usage += chunk.usage ?? estimate(chunk.delta);
    res.write(sseData(chunk.delta));                             // 逐块转发
  }
  res.write(sseData('[DONE]')); res.end();
  await meterUsage(req.user, usage);                             // 计量
});
```
