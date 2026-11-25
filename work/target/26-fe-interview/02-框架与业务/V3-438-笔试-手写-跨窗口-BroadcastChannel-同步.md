---
title: [V3-438] 笔试：手写跨窗口状态同步（BroadcastChannel + 兜底 storage 事件）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-438：笔试：手写跨窗口状态同步（BroadcastChannel + 兜底 storage 事件）
**答**：实现 `useCrossTabSync(store)`：BroadcastChannel 广播 store 变更（带来源 tabId，忽略自己发的消息）；不支持 BroadcastChannel 时用 storage 事件兜底；消息带版本号防乱序；卸载关闭 channel。

```javascript
export function useCrossTabSync(store) {
  const tabId = crypto.randomUUID()
  let seq = 0
  let bc = null
  if ('BroadcastChannel' in window) {
    bc = new BroadcastChannel('store-sync')
    bc.onmessage = (e) => {
      const { from, s, patch } = e.data
      if (from === tabId) return          // 忽略自己
      if (s <= lastSeq) return            // 乱序丢弃
      lastSeq = s
      store.$patch(patch)
    }
  } else {
    window.addEventListener('storage', (e) => {
      if (e.key !== 'sync') return
      const { from, s, patch } = JSON.parse(e.newValue || '{}')
      if (from === tabId || s <= lastSeq) return
      lastSeq = s
      store.$patch(patch)
    })
  }
  let lastSeq = 0
  const send = (patch) => {
    const msg = { from: tabId, s: ++seq, patch }
    if (bc) bc.postMessage(msg)
    else localStorage.setItem('sync', JSON.stringify(msg))
  }
  store.$subscribe((mutation, state) => send(mutation.payload), { detached: true })
  onBeforeUnmount(() => bc?.close())
  return { send }
}
```
**评分点**：
- tabId 过滤自身消息（storage 事件本身不过滤发送方，必须显式）。
- 版本号防乱序。
- BroadcastChannel 降级 storage 方案。
- 卸载 close 防泄漏。
