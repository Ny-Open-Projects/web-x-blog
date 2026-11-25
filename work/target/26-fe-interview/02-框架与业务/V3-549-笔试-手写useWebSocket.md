---
title: [V3-549] 笔试：手写 useWebSocket（重连 + 心跳 + 竞态收口）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## V3-549：笔试：手写 useWebSocket

**答**：实现 `useWebSocket(url, { autoReconnect, heartbeat, onMessage })`：① 状态：CONNECTING/OPEN/CLOSING/CLOSED 响应式；② 断线自动重连（指数退避 + 上限次数，组件卸载停止）；③ 心跳（interval ping，超时未收到 pong 判死重连）；④ 消息回调 + send（OPEN 前发送入队，连上后 flush）；⑤ 组件卸载主动 close（不触发重连）。写出实现。

```javascript
export function useWebSocket(url, {
  autoReconnect = true, maxRetries = 5,
  heartbeat = 30_000, onMessage,
} = {}) {
  const status = ref('CLOSED');
  let ws = null, retries = 0, hbTimer = null, pongTimer = null;
  const queue = [];
  let disposed = false;

  function connect() {
    if (disposed) return;
    status.value = 'CONNECTING';
    ws = new WebSocket(url);
    ws.onopen = () => {
      status.value = 'OPEN';
      retries = 0;                                 // 成功重置退避
      while (queue.length) ws.send(queue.shift()); // flush 挂起消息
      startHeartbeat();
    };
    ws.onmessage = (e) => {
      clearTimeout(pongTimer);                     // 收到任何消息视为活跃
      onMessage?.(e.data);
    };
    ws.onclose = () => {
      status.value = 'CLOSED';
      stopHeartbeat();
      if (!disposed && autoReconnect && retries < maxRetries) {
        const delay = Math.min(1000 * 2 ** retries++, 30_000);
        setTimeout(connect, delay);                // 指数退避
      }
    };
    ws.onerror = () => ws.close();
  }
  function startHeartbeat() {
    hbTimer = setInterval(() => {
      if (ws.readyState !== 1) return;
      ws.send(JSON.stringify({ type: 'ping' }));
      pongTimer = setTimeout(() => ws.close(), 5000);  // 5s 无响应判死 → onclose → 重连
    }, heartbeat);
  }
  function send(data) {
    if (ws?.readyState === 1) ws.send(data);
    else queue.push(data);                          // 未连接先入队
  }
  connect();
  onScopeDispose(() => {
    disposed = true;                                // 卸载: 不再重连
    stopHeartbeat();
    ws?.close();
  });
  return { status, send, close: () => { autoReconnect = false; ws?.close(); } };
}
```

**评分点**：
- 五态状态机 + 指数退避（上限与成功重置）
- 心跳 + pong 超时判死（半开连接检测）
- 未连接消息入队 flush
- disposed 标志区分「主动卸载」与「意外断开」
