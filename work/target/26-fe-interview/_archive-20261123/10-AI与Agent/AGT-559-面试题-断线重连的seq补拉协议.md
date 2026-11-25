---
title: [AGT-559] SSE 断线重连后，如何用 seq + Last-Event-ID 补齐缺失片段？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-559：SSE 断线重连后，如何用 seq + Last-Event-ID 补齐缺失片段

**答**：
- 服务端每条事件带单调递增 seq，缓存最近 N 秒的事件窗口（或写入可回放的持久层）；客户端断线时记录 lastSeq，重连带上它。
- 服务端三种情况：lastSeq 仍在窗口→补发缺失；窗口已过→发 snapshot 事件（当前全量）替代增量；回合已结束→直接发 done + 最终内容。
- 客户端补发期间 UI 显示"同步中"，补齐后继续流式渲染；snapshot 与本地 delta 合并要做内容对齐（以服务端为准）。

```javascript
// 客户端
const es = new EventSource(`/stream/${turnId}?lastSeq=${lastSeq}`);
es.addEventListener('miss', (e) => JSON.parse(e.data).deltas.forEach(applyDelta));
es.addEventListener('snapshot', (e) => {        // 窗口过期：全量对齐
  const snap = JSON.parse(e.data);
  replaceContent(snap.content); lastSeq = snap.seq;
});
es.addEventListener('done', () => es.close());
// 服务端：窗口判断
function replay(lastSeq) {
  if (log.latestSeq - lastSeq <= WINDOW) return sendMiss(log.range(lastSeq));
  if (!turn.finished) return sendSnapshot(turn.contentNow());
  sendDone(turn.final);
}
```

