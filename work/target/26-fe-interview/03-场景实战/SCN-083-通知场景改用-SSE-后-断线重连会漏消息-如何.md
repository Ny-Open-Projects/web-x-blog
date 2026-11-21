---
title: [SCN-083] 通知场景改用 SSE 后，断线重连会漏消息，如何用 Last-Event-ID 实现补传？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-083：通知场景改用 SSE 后，断线重连会漏消息，如何用 Last-Event-ID 实现补传？
**答**：
- 服务端为每条消息分配自增 id，浏览器 EventSource 重连时自动携带 Last-Event-ID 请求头，服务端据此补发该 id 之后的缺口，前端不需要自己做断点记录。
- 前端职责：不要抢在浏览器前重建连接（会丢 Last-Event-ID）；业务侧按消息 id 幂等去重，防止服务端重发造成重复渲染。
- 断线期间展示"消息同步中"，重连补传完成后隐藏，避免用户以为丢消息。

```javascript
// SSE 断线续传：浏览器自动携带 Last-Event-ID，业务层按 id 幂等去重
const seen = new Set<number>();
let synced = true;

const es = new EventSource('/api/notifications');

es.onmessage = (e) => {
  const id = Number(e.lastEventId);   // 服务端分配的自增 id
  if (seen.has(id)) return;           // 服务端可能重发，业务侧幂等
  seen.add(id);
  if (!synced) { synced = true; hideSyncingTip(); }
  renderNotification(JSON.parse(e.data));
};

es.onerror = () => {
  if (es.readyState === EventSource.CLOSED) {
    // 浏览器自动重连失败的兜底：手动重建（重建后首个请求仍带 Last-Event-ID）
    synced = false;
    showSyncingTip();                 // 断线期间明确提示，避免用户以为丢消息
    setTimeout(() => new EventSource('/api/notifications'), 3000);
  }
};

// 服务端网关注意：Nginx 对该 location 配 proxy_buffering off，
// 否则缓冲攒消息导致 SSE 延迟，proxy_read_timeout 拉长防长连接被掐断
```
