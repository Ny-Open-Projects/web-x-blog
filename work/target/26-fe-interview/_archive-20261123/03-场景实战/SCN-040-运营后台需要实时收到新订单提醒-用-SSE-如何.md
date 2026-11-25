---
title: [SCN-040] 运营后台需要实时收到新订单提醒，用 SSE 如何落地？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-040：运营后台需要实时收到新订单提醒，用 SSE 如何落地？
**答**：
- SSE 单向推送（服务端 → 前端）足够，基于 HTTP 自带断线重连，比 WebSocket 轻；EventSource 只能 GET 且不能自定义 Header，鉴权用 Cookie 或 query 里的一次性 ticket。
- 心跳与续传：服务端每 30 秒发一条注释帧防代理超时断开；配合 Last-Event-ID 让浏览器重连后不丢消息。
- 注意连接数：HTTP/1.1 同域只有 6 个连接，生产环境通知中心收敛为一个 SSE 连接，域名升级 HTTP/2。

```javascript
function connectNotify(onMessage) {
  const es = new EventSource(`/api/notify?ticket=${getTicket()}`);
  es.addEventListener('order', (e) => {          // 具名事件：订单提醒
    onMessage(JSON.parse(e.data));
  });
  es.onopen = () => console.log('通知通道已建立');
  es.onerror = () => {
    // 浏览器会自动重连；ticket 过期时先换票再重建
    if (es.readyState === EventSource.CLOSED) setTimeout(connectNotify, 3000);
  };
  return es;
}
// 服务端每 30 秒发送 ": ping" 注释帧作为心跳，防止 nginx 等代理超时断开
// nginx 需关闭缓冲：proxy_buffering off 或响应头 X-Accel-Buffering: no
```
