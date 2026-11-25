---
title: [V3-426] 笔试：手写 WebSocket 心跳重连与消息去重（Vue composable）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-426：笔试：手写 WebSocket 心跳重连与消息去重（Vue composable）
**答**：实现 `useWs(url)`：自动心跳（30s ping，超时未收到 pong 判定断开重连）；指数退避重连（上限 30s）；消息按 msgId 去重（服务端重发场景）；组件卸载时真正关闭并停心跳。

```javascript
function useWs(url) {
  const messages = ref([])
  let ws = null, heartbeat = null, retry = 0, closed = false
  const seen = new Set()
  function connect() {
    if (closed) return
    ws = new WebSocket(url)
    ws.onopen = () => { retry = 0; startHeartbeat() }
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data)
      if (msg.type === 'pong') { resetHeartbeatTimeout(); return }
      if (seen.has(msg.id)) return // 去重
      seen.add(msg.id)
      messages.value.push(msg)
    }
    ws.onclose = () => {
      stopHeartbeat()
      if (closed) return
      const wait = Math.min(1000 * 2 ** retry++, 30000)
      setTimeout(connect, wait)
    }
  }
  function startHeartbeat() {
    heartbeat = setInterval(() => ws.send(JSON.stringify({ type: 'ping' })), 30000)
  }
  function resetHeartbeatTimeout() { /* 收到 pong 重置判定 */ }
  function stopHeartbeat() { clearInterval(heartbeat) }
  function close() { closed = true; ws?.close(); stopHeartbeat() }
  onMounted(connect); onBeforeUnmount(close)
  return { messages, close }
}
```
**评分点**：
- 心跳 ping/pong 超时判定（至少口述超时断开机制）。
- 指数退避 + 上限，onopen 重置计数。
- msgId 去重（Set）。
- 组件卸载 close 且不再重连（closed 标志，高频扣分点）。
