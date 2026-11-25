---
title: [NODE-760] 笔试题——实现 AI 网关流式透传与计量（SSE + token + 配额）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-760：手写 AI 网关

**需求与边界**：
- 需求：AI 网关（SCN-NODE-661）——① 交互/异步队列分级（SCN-NODE-661 核心设计）；② SSE 流式透传（背压——SCN-NODE-636）；③ token 计量（流中计数——计费）；④ 断线处理（客户端断开 abort 上游——资源释放）。
- 边界：① prompt 缓存（语义 hash——省钱）；② 模型路由（任务/成本/可用性——降级备用模型）；③ 输出审核钩子（敏感过滤——流中截断）。

**答**：
```javascript
app.post('/ai/chat', async (req, res) => {
  if (!interactiveQueue.tryAcquire(req.user))
    return res.status(429).json({ retryAfter: 5 });    // 交互队列快速失败（SCN-NODE-661）
  const cacheKey = semanticHash(req.body.prompt);
  const cached = await cache.get(cacheKey);            // prompt 缓存（省钱）
  if (cached) return sseRespond(res, cached);
  const upstream = await modelRoute(req.body, {        // 模型路由（主→备用降级）
    signal: AbortSignal.any([clientGone(req), AbortSignal.timeout(60_000)]) });
  let tokens = 0;
  const metered = upstream.pipe(new Transform({        // 流中计量（SCN-NODE-661）
    transform(chunk, enc, cb) {
      tokens += countTokens(chunk);
      if (containsBlocked(chunk)) return cb(null, '[filtered]');   // 输出审核截断
      cb(null, chunk);
    } }));
  await pipeline(metered, sseTo(res));                 // SSE 透传（背压——SCN-NODE-636）
  await metering.charge(req.user, tokens);             // 计费
  cache.set(cacheKey, sseSnapshot);                    // 缓存
});
```

**评分点**:
- 交互/异步队列分级（SCN-NODE-661 容量核心）。
- 流中计量 + 审核截断（transform 管道）。
- SSE 透传背压 + 客户端断开 abort（SCN-NODE-636/744）。
- prompt 语义缓存 + 模型路由降级（成本与可用性）。

## 变体与延伸（补充）

**变体与延伸**：

1. 客户端断开后上游模型还在生成，token 还在烧怎么止损 → 监听 req 的 close 事件立刻 abort 上游 fetch，并按实际已产出 token 入账，否则断线越多亏得越多。
2. SSE 透传时下游比上游慢，背压怎么处理 → 检查 res.write 返回值，false 时暂停读取上游 reader，等 drain 再继续，不然内存里堆的是整段模型输出。
3. 流到一半模型报错，已经吐给前端的内容怎么收尾 → 发一个 error 事件帧而不是直接断流，前端可展示部分结果并标记不完整，计费按已产出 token 折算。
