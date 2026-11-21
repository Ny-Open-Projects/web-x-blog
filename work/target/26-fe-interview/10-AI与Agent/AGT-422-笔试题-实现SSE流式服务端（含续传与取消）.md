---
title: [AGT-422] 笔试题——实现 Agent 流式输出服务端（SSE+续传+取消）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-422：手写 SSE 流服务：事件信封、seq 保序、断线续传、取消接口

**需求与边界**：
- 输入：生成器（async iterator 产出事件）；输出：SSE 响应。
- 边界要求：① 事件统一信封 {type, seq, payload}；② 事件持久化（Last-Event-ID 续传不丢）；③ 客户端断开服务端仍写完整（可重连取增量）；④ 取消接口终止生成并落终态。

**答**：
```javascript
// Node/Express 风格
async function streamAgent(req, res, { taskId, generator, store }) {
  const last = +(req.get('last-event-id') ?? -1);
  let seq = last;
  res.writeHead(200, { 'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache', Connection: 'keep-alive' });
  // 1. 续传：先补齐落库事件
  if (last >= 0) {
    for (const ev of await store.after(taskId, last)) {
      res.write(fmt(ev)); seq = ev.seq;
    }
  }
  const cancel = { flag: false };
  store.setCancel(taskId, cancel);
  try {
    for await (const ev of generator(cancel)) {      // 生成器感知取消
      if (cancel.flag) break;
      seq++;
      const envelope = { type: ev.type, seq, payload: ev.payload };
      await store.append(taskId, envelope);          // 先落库
      res.write(fmt(envelope));                      // 再发送
    }
    const done = { type: cancel.flag ? 'cancelled' : 'done',
      seq: seq + 1, payload: { taskId } };
    await store.append(taskId, done);
    res.write(fmt(done));
  } finally {
    res.end(); store.setCancel(taskId, null);
  }
}
const fmt = (ev) => `id: ${ev.seq}\nevent: ${ev.type}\ndata: ${JSON.stringify(ev)}\n\n`;
// 取消：POST /cancel → store.setCancel(taskId, {flag:true})
// 生成器内部检查 cancel.flag 终止上游 LLM 调用。
```

**评分点**:
- 信封与 seq 全局递增；落库先行再发送（断线重连不丢帧）。
- Last-Event-ID 续传先补齐历史事件再继续流。
- 取消机制贯通：cancel 标志→生成器终止→终态事件（cancelled）落库。
- 断开后生成继续（服务端持久），finally 清理连接资源。
