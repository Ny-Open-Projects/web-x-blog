---
title: [AGT-047] 流中途网络异常断开，如何用 offset 续传恢复？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-047：流中途网络异常断开，如何用 offset 续传恢复？
**答**：
- 与 AGT-042 的「用户主动中断」不同，这是异常恢复：客户端记录已收到的事件序号，重连时通过 SSE 原生的 `Last-Event-ID` 头或显式 offset 参数回传。
- 服务端必须缓存正在生成的响应（内存/Redis，TTL 数分钟）：重连先按 offset 幂等回放缓存，再把新产生的事件边写缓存边推。
- 服务端给每个事件编单调递增 id，回放与续推不重不漏，靠 id 对齐。
- 客户端流异常结束后指数退避重连，从 lastId 继续，而不是从头重新生成。

```typescript
// server：按 offset 回放缓存并续推
const streamCache = new Map<string, { events: string[]; done: boolean }>();

app.get('/api/chat/stream', async (req, res) => {
  const { sessionId } = req.query as { sessionId: string };
  const offset = Number(req.headers['last-event-id'] ?? 0);
  const cache = streamCache.get(sessionId);
  if (!cache) return res.status(404).end();

  res.setHeader('Content-Type', 'text/event-stream');
  // 1) 先幂等回放 offset 之后的全部缓存事件
  for (let i = offset; i < cache.events.length; i++) {
    res.write(`id: ${i}\ndata: ${cache.events[i]}\n\n`);
  }
  if (cache.done) return res.end();

  // 2) 新产生的事件：先写缓存再推送，id 单调递增
  const live = createResumableUpstream(sessionId); // 内部生成 delta 时同步 push 进 cache.events
  live.on('event', (data: string) => {
    const idx = cache.events.push(data) - 1;
    res.write(`id: ${idx}\ndata: ${data}\n\n`);
  });
  live.on('done', () => { cache.done = true; res.write('data: [DONE]\n\n'); res.end(); });
  req.on('close', () => live.detach(res)); // 连接再断也不怕：缓存仍在，客户端带 Last-Event-ID 重连
});

// client：fetch 流手动记录 lastId 并重试（EventSource 则原生携带该头）
async function consume(sessionId: string, offset = 0): Promise<void> {
  const res = await fetch(`/api/chat/stream?sessionId=${sessionId}`, { headers: { 'Last-Event-ID': String(offset) } });
  let lastId = offset;
  for await (const ev of parseSSE(res.body!)) {
    if (ev.id) lastId = Number(ev.id);
    if (ev.data === '[DONE]') return;
    renderDelta(ev.data);
  }
  await sleep(1000);            // 退避后从断点续传
  return consume(sessionId, lastId);
}
```

---

## 十三、Prompt 工程进阶
