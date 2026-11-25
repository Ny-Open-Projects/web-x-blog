---
title: [ZSM-482] 笔试：手写状态层 SW 缓存同步
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-482：手写状态层 SW 缓存同步
**答**：实现主页面与 Service Worker 的状态缓存同步：1) 页面 `pushToSW(key, data)`：把关键状态写入 SW 持有的 Cache（离线可用）；2) SW 侧监听 message 写 Cache API；3) 页面冷启动 `pullFromSW(key)`：SW 缓存优先于网络（离线优先读路径）；4) 版本戳：每次写入带 `{ v, data }`，读取时版本较旧的数据标记 stale；5) 双通道：BroadcastChannel 兜底 SW 不可用时直接 localStorage。

```javascript
// 页面侧
export async function pushToSW(key, data) {
  if (navigator.serviceWorker.controller) {
    navigator.serviceWorker.controller.postMessage({ type: 'state:put', key, data })
  } else {
    localStorage.setItem(`sw:${key}`, JSON.stringify({ v: Date.now(), data }))   // 兜底
  }
}

export async function pullFromSW(key) {
  if (navigator.serviceWorker.controller) {
    const res = await caches.open('state-v1')
      .then((c) => c.match(`/state/${key}`))
    if (res) { const { v, data } = await res.json(); return { data, stale: Date.now() - v > 60_000 } }
    return null
  }
  const raw = localStorage.getItem(`sw:${key}`)
  if (!raw) return null
  const { v, data } = JSON.parse(raw)
  return { data, stale: Date.now() - v > 60_000 }
}

// SW 侧（sw.js）
self.addEventListener('message', (e) => {
  if (e.data?.type === 'state:put') {
    e.waitUntil(caches.open('state-v1').then((c) =>
      c.put(`/state/${e.data.key}`, new Response(JSON.stringify({ v: Date.now(), data: e.data.data })))))
  }
})
```
**评分点**：
- SW Cache API 写读协议（Request/Response 语义）
- 版本戳 stale 判定（SW 数据仅作离线兜底，不作新鲜事实）
- controller 不存在（首次加载 SW 未接管）的 localStorage 兜底
- 离线优先读路径的定位（SW 缓存是「冷启动恢复层」不是真相源）
