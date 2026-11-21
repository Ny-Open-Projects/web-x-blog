---
title: [WEB-488] 笔试：手写心跳保活的 WebSocket 客户端
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebSocket]
type: 笔试题
---

## WEB-488：笔试：手写心跳保活的 WebSocket 客户端

**题目**：实现可靠 WS 客户端：30s 心跳、pong 超时判定半开连接并主动断开、断线指数退避重连（含上限）、重连期间消息入队、恢复后补发。

**答**：
```javascript
function createWs(url) {
  let ws, heartbeat, pongTimer, retry = 0;
  const queue = [];
  let closed = false;

  function connect() {
    ws = new WebSocket(url);
    ws.onopen = () => {
      retry = 0;
      heartbeat = setInterval(() => {
        ws.send(JSON.stringify({ type: 'PING' }));
        pongTimer = setTimeout(() => ws.close(), 5000); // 5s 没回 pong 视为半开
      }, 30000);
      queue.splice(0).forEach(m => ws.send(m)); // 补发积压消息
    };
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      if (msg.type === 'PONG') { clearTimeout(pongTimer); return; }
      onMessage?.(msg);
    };
    ws.onclose = () => {
      clearInterval(heartbeat); clearTimeout(pongTimer);
      if (!closed) {
        const delay = Math.min(30000, 1000 * 2 ** retry++) + Math.random() * 1000;
        setTimeout(connect, delay);
      }
    };
  }
  let onMessage;
  connect();
  return {
    send(msg) { ws.readyState === 1 ? ws.send(JSON.stringify(msg)) : queue.push(JSON.stringify(msg)); },
    onMessage(fn) { onMessage = fn; },
    close() { closed = true; ws.close(); },
  };
}
```

**评分点**：
- 心跳 + pong 超时双检测，识别「TCP 未断但对端死掉」的半开连接
- 指数退避带随机抖动和上限，防重连风暴
- 断线期间消息入队、恢复后补发（顺序不保证，能提补拉离线更佳）
- close() 必须终止重连循环（closed 标志）
