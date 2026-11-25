---
title: [NODE-347] Node 服务的 SSE 与长轮询实现要点有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-347：Node 服务的 SSE 与长轮询实现
**答**:
- SSE 优势：纯 HTTP、自动重连（浏览器 EventSource 内建）、代理友好；限制：单向（服务端→客户端）、HTTP/1.1 下占连接数（HTTP/2 复用解决）、只能文本。适合通知流/进度推送；双向交互用 WS。
- Node 实现要点：Content-Type: text/event-stream、禁缓存（Cache-Control: no-cache）与 nginx 缓冲关闭（X-Accel-Buffering: no）、心跳注释行（: ping 30s 防 LB 掐连接）、事件 id 支持 Last-Event-ID 续传。
- 生命周期：res.write 后不能 end；客户端断开监听 req close 清理订阅与定时器（防泄漏）；每连接内存最小化（订阅引用而非拷贝数据）。
- 长轮询（降级方案）：请求挂起直到有数据或超时（30s）返回，客户端立即重发；实现上注意连接池占用与超时对齐；数据去重靠游标。
- 与 WS 的降级链：优先 WS → 失败探测 → SSE → 短轮询，客户端 SDK 收口（ARC-416）。
```javascript
app.get('/events', (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache', Connection: 'keep-alive', 'X-Accel-Buffering': 'no' });
  let lastId = Number(req.headers['last-event-id'] ?? 0);
  const hb = setInterval(() => res.write(': ping\n\n'), 30000);   // 心跳
  const sub = bus.subscribe(e => {
    if (e.id <= lastId) return;                                   // 续传去重
    res.write(`id: ${e.id}\nevent: ${e.type}\ndata: ${JSON.stringify(e)}\n\n`);
  });
  req.on('close', () => { clearInterval(hb); sub.unsub(); });     // 清理防泄漏
});
```
