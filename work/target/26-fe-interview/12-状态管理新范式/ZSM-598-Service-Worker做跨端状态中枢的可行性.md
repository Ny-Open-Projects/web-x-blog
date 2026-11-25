---
title: [ZSM-598] Service Worker 做跨端状态中枢可行吗：能力与限制
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-598：Service Worker 做跨端状态中枢可行吗：能力与限制

**答**：
- SW 的独特价值：**生命周期独立于页面**——页面全关了 SW 还能处理推送（Push API）、后台同步（Background Sync）、代理所有网络请求。作为「跨 tab 中枢」比 SharedWorker 更长寿。
- 可行的中枢能力：1) 请求代理层——所有 API 请求经 SW，SW 维护「版本号/ETag」做跨 tab 的响应共享缓存（同请求只发一次）；2) Background Sync——离线队列的重放交给 SW（页面关了也能补发）；3) Push——服务端推送直接进 SW，转发给活跃 tab。
- 硬限制：1) **SW 不持有内存状态**——SW 可能随时被杀（空闲终止），内存 Map 清空；持久状态只能进 IndexedDB/Caches，读取是异步的；2) SW 与页面通信要走 MessageChannel，双向都异步，没有同步读取；3) 更新机制复杂（新旧 SW 版本共存期）。
- 结论：SW 适合做「持久层的执行者」（离线队列重放、缓存协调、推送路由），不适合做「实时状态中枢」（热数据中枢用 SharedWorker/主 tab leader）。
- 追问钩子：SW 与页面共享 IndexedDB 是它传递状态的桥梁——「SW 写队列结果 → 广播 MessageChannel → 页面更新 store」是标准接法。

```javascript
// SW：离线队列重放中枢（页面关闭也能执行）
// sw.js
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-ops') {
    event.waitUntil(replayQueue())   // Background Sync：联网后自动触发
  }
})

async function replayQueue() {
  const db = await openDB()
  const ops = await getAll(db, 'ops')
  for (const op of ops) {
    try {
      const res = await fetch('/api/replay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(op),          // opId 幂等
      })
      if (res.ok) await remove(db, 'ops', op.opId)
    } catch { throw e }   // 抛出让 Sync 失败，浏览器稍后重试
  }
  // 结果通知活跃页面（页面可能已经关了，广播尽力而为）
  const clients = await self.clients.matchAll()
  clients.forEach((c) => c.postMessage({ type: 'ops-replayed' }))
}

// 页面：接收 SW 通知更新 store
navigator.serviceWorker.addEventListener('message', (e) => {
  if (e.data.type === 'ops-replayed') {
    queryClient.invalidateQueries()        // 对账刷新
    useOfflineQueue.getState().refresh()   // 队列 UI 更新
  }
})

// 请求代理：SW 共享响应缓存（同请求跨 tab 只发一次）
self.addEventListener('fetch', (e) => {
  if (e.request.url.includes('/api/config')) {
    e.respondWith(caches.open('shared-api').then(async (c) => {
      const hit = await c.match(e.request)
      return hit ?? fetch(e.request).then((r) => { c.put(e.request, r.clone()); return r })
    }))
  }
})
```
