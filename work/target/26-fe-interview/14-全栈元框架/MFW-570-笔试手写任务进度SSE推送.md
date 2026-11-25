---
title: [MFW-570] 笔试：手写任务进度 SSE 推送（pub/sub → 流）
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-570：笔试：手写任务进度 SSE 推送

**答**：实现 `taskProgressSSE(taskId, { subscribe, signal })`。subscribe: `(taskId, cb) => unsubscribe`（模拟 Redis pub/sub——worker 完成时 publish）。返回 Response（SSE 流）。规则：1) 初始事件：`event: start, data: {"taskId"}`；2) 订阅进度：`event: progress, data: {pct}`；3) 完成：`event: done, data: {result}` 后 close 流；4) client 断开（signal abort）→ unsubscribe（防泄漏 RBL-874 清理契约）；5) 超时保护：60s 无事件 → `event: ping`（保活）；6) 用 ReadableStream + TextEncoder。边界：taskId 不存在 → 立即 done + 404 语义（SSE 内 error 事件）。

```javascript
function taskProgressSSE(taskId, { subscribe, signal, timeoutMs = 60000 } = {}) {
  const encoder = new TextEncoder();
  return new Response(new ReadableStream({
    async start(controller) {
      let closed = false;
      const send = (event, data) => {
        if (closed) return;
        controller.enqueue(encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`));
      };
      send('start', { taskId });
      const keepalive = setInterval(() => send('ping', {}), timeoutMs);
      const onAbort = () => cleanup();
      signal?.addEventListener('abort', onAbort);
      function cleanup() {
        if (closed) return;
        closed = true;
        clearInterval(keepalive);
        unsub?.();
        controller.close();
      }
      const unsub = subscribe(taskId, (msg) => {
        if (msg.type === 'progress') send('progress', { pct: msg.pct });
        if (msg.type === 'done') {
          send('done', { result: msg.result });
          cleanup();
        }
        if (msg.type === 'error') {
          send('error', { message: msg.message });
          cleanup();
        }
      });
      signal?.addEventListener('abort', onAbort, { once: true });
    },
  }), { headers: { 'content-type': 'text/event-stream',
    'cache-control': 'no-cache, no-transform', connection: 'keep-alive' } });
}

// 自测（注入 subscribe 与手工 publish）
function fakePubSub() {
  const subs = new Map();
  return {
    subscribe: (id, cb) => { (subs.get(id) || subs.set(id, []).get(id)).push(cb);
      return () => { subs.set(id, subs.get(id).filter(f => f !== cb)); }; },
    publish: (id, msg) => subs.get(id)?.forEach(f => f(msg)),
  };
}
const ps = fakePubSub();
const ctrl = new AbortController();
const res = taskProgressSSE('t1', { subscribe: ps.subscribe, signal: ctrl.signal });
const reader = res.body.getReader();
const chunks = [];
(async () => {
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(new TextDecoder().decode(value));
  }
})();
await sleep(0);
ps.publish('t1', { type: 'progress', pct: 50 });
ps.publish('t1', { type: 'done', result: 'ok' });
await sleep(10);
const text = chunks.join('');
console.log(text.includes('event: start') && text.includes('"pct":50'));
console.log(text.includes('event: done') && text.includes('"ok"'));
// client 断开清理
ctrl.abort();
console.log(ps.subs.get('t1').length === 0);             // unsubscribe 防泄漏
```

**评分点**：
- SSE 协议格式（event/data 双字段 + 空行分隔）；done 后 close 流（完成即断——不占连接）
- 断开清理契约（abort → unsubscribe——pub/sub 泄漏防线 RBL-874）；keepalive ping
- ReadableStream + TextEncoder 实现；边界（不存在任务走 error 事件）
- 能说清「任务进度推送的清理契约与 Action 轮询/SSE 的选型：轮询简单可靠、SSE 实时但连接管理成本高」属于加分
