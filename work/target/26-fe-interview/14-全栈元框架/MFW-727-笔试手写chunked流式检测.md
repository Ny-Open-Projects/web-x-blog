---
title: [MFW-727] 笔试：手写 chunked 流式检测
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-727：笔试：手写 chunked 流式检测

**答**：实现 `detectStreaming(url, { fetchFn, firstByteBudgetMs, totalBudgetMs })`。规则：1) 发起请求，**分块读取**（reader.read()——不是一次性 text()）；2) 首块时间 = 第一个 chunk 到达的时间（TTFB 的流式版）；3) 流式判定：首块 < totalBudget 且首块与最后块时间差 > 100ms（有流式间隔——非一次性）；4) 返回 `{ streaming, firstChunkMs, totalMs, chunks, streamingType }`（type: 'chunked'|'single'）。边界：响应立即完成（chunks=1——非流式）；超时（fetch 超时——标记 error）；HEAD 请求（无 body——no-data）。

```javascript
async function detectStreaming(url, { fetchFn = fetch, totalBudgetMs = 30000 } = {}) {
  const t0 = Date.now();
  const res = await fetchFn(url);
  const reader = res.body?.getReader();
  if (!reader) return { streaming: false, noData: true, chunks: 0 };
  let firstChunkMs = 0, chunkCount = 0;
  const events = [];
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunkCount++;
      const now = Date.now() - t0;
      if (chunkCount === 1) firstChunkMs = now;
      events.push({ chunk: chunkCount, at: now, size: value.byteLength });
      if (now > totalBudgetMs) { reader.cancel(); break; }
    }
  } catch (e) {
    return { streaming: false, error: e.message, chunks: chunkCount };
  }
  const totalMs = Date.now() - t0;
  const streaming = chunkCount > 1 && (events.at(-1).at - firstChunkMs) > 100;
  return {
    streaming, firstChunkMs, totalMs, chunks: chunkCount,
    streamingType: streaming ? 'chunked' : 'single',
  };
}

// 自测
// 流式：多 chunk 有间隔
const streamingFetch = async () => ({
  body: new ReadableStream({
    start(controller) {
      controller.enqueue(new TextEncoder().encode('<html>'));
      setTimeout(() => controller.enqueue(new TextEncoder().encode('chunk2')), 200);
      setTimeout(() => controller.enqueue(new TextEncoder().encode('chunk3')), 400);
      setTimeout(() => controller.close(), 500);
    },
  }),
});
let r = await detectStreaming('http://x', { fetchFn: streamingFetch });
console.log(r.streaming === true && r.chunks === 3);
console.log(r.streamingType === 'chunked');

// 非流式：单 chunk
const singleFetch = async () => ({
  body: new ReadableStream({
    start(controller) {
      controller.enqueue(new TextEncoder().encode('<html>all</html>'));
      controller.close();
    },
  }),
});
r = await detectStreaming('http://x', { fetchFn: singleFetch });
console.log(r.streaming === false && r.streamingType === 'single');

// 空响应
const emptyFetch = async () => ({
  body: new ReadableStream({ start(c) { c.close(); } }),
});
r = await detectStreaming('http://x', { fetchFn: emptyFetch });
console.log(r.chunks === 0 && r.streaming === false);
```

**评分点**：
- 分块读取（reader.read 循环——非一次性 text()）；流式判定（首块与最后块时间差 > 100ms）
- firstChunkMs 的 TTFB 流式版；chunk 计数；超时保护
- 边界（单 chunk 非流式/空响应/error）；CDN 缓冲的检测用途
- 能说清「chunked 流式检测验证全链路（server→代理→CDN→client）——CDN 缓冲是流式的静默杀手」属于加分
