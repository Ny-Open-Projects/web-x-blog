---
title: [NODE-661] AI 推理网关（流式代理/排队/降级）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-661：AI 推理网关怎么做？
**答**：
- 网关职责：模型路由（按任务/成本/可用性选模型——SCN-ENG-225 平台边界）、流式透传（SSE——上游 chunk 转发到客户端，背压处理，SCN-NODE-636）、排队与限流（推理资源贵——队列 + 租户配额，SCN-NODE-641）、降级（主模型超时降级备用模型/缓存结果）。
- 流式细节：SSE 转发不缓存（chunk 透传——客户端打字机效果）；断线续传（生成中断——上下文截断重试或放弃）；token 计量（用量计费——流中计数）。
- 成本治理：缓存（相同 prompt 语义缓存——命中率即省钱）、配额（租户级 token 预算——超配额排队）、异步任务化（长生成转异步任务轮询——不占连接）。
- 安全：prompt 注入检测（输入清洗——SCN-FIN-556 安全信号同源）、输出审核（敏感内容过滤钩子）。
- 追问钩子：为什么 AI 网关的「排队」必须区分「交互式」与「异步」——交互式对话排队 30s 用户体验已死（等待不可接受——超限快速失败 + 建议稍后）；异步生成（文章/报告）排队完全可接受（任务化 + 轮询/SSE 通知）——两类请求混在一个队列里，异步任务会把交互请求饿死——队列分级是 AI 网关的容量核心。

```javascript
app.post('/ai/chat', async (req, res) => {
  const slot = await interactiveQueue.tryAcquire();    // 交互队列（快速失败）
  if (!slot) return res.status(429).json({ retryAfter: 5 });
  const upstream = await modelClient.stream(req.body, { signal: req.signal });
  pipeline(upstream, sseTo(res));                      // 流式透传（背压）
  meterTokens(upstream, req.user);                     // 计量
});
```
