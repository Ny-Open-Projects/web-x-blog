---
title: [NODE-120] SSE 服务端如何实现（与 WebSocket 如何取舍）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-120：SSE 服务端如何实现（与 WebSocket 如何取舍）？
**答**：
- 三个响应头定生死：`content-type: text/event-stream`、`cache-control: no-cache`、`connection: keep-alive`；nginx 场景加 `x-accel-buffering: no` 关缓冲，否则事件被攒住不实时。
- 报文格式：`id:`/`event:`/`data:` 字段 + **空行分隔**；浏览器 EventSource 断线自动重连并回传 `Last-Event-ID`，服务端据此续传。
- 心跳用注释行 `: ping` 防代理掐空闲连接；`req.on('close')` 必须清理订阅与定时器，防连接泄漏。
- 取舍：单向推送/纯 HTTP/易过网关 → SSE；双向实时 → WebSocket（NODE-073/079）。

```javascript
app.get('/api/events', (req, res) => {
  res.writeHead(200, {
    'content-type': 'text/event-stream; charset=utf-8',
    'cache-control': 'no-cache, no-transform',
    connection: 'keep-alive',
    'x-accel-buffering': 'no', // 关 nginx 缓冲
  });
  res.flushHeaders();

  const lastId = Number(req.headers['last-event-id'] ?? 0); // 断线续传游标
  sendEventsSince(res, lastId);

  const onOrder = (e) => {
    res.write(`id: ${e.id}\nevent: order\ndata: ${JSON.stringify(e)}\n\n`);
  };
  bus.on('order-update', onOrder);
  const hb = setInterval(() => res.write(': hb\n\n'), 15_000); // 注释行心跳

  req.on('close', () => {          // 客户端断开必清理
    bus.off('order-update', onOrder);
    clearInterval(hb);
  });
});
```

---

## 十四、数据库与存储深入
