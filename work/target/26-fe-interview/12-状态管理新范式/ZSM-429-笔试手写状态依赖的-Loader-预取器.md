---
title: [ZSM-429] 笔试：手写路由级预取器（意图分层 + 去重 + 取消）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-429：手写路由级预取器（意图分层 + 去重 + 取消）
**答**：实现 `createPrefetcher(queryClient, optionsFn)`：1) `hover(id)`：hover 意图 → 预取（500ms 防抖，鼠标快速扫过不触发）；2) `viewport(id)`：进入视口意图 → 立即预取（低优先级标记）；3) `confirm(id)`：实际导航 → 等待预取完成（复用同一 Promise，不重复请求）；4) 同 id 并发预取去重（共享 inflight）；5) hover 后 3s 未 confirm 自动 abort（释放资源）；6) 预取失败静默。

```javascript
export function createPrefetcher(queryClient, optionsFn) {
  const inflight = new Map()   // id → { promise, ac, timer }

  function start(id, { priority, ttlMs = 3000 } = {}) {
    if (inflight.has(id)) return inflight.get(id).promise
    const ac = new AbortController()
    const opts = optionsFn(id)
    const promise = queryClient.fetchQuery({ ...opts, signal: ac.signal }).catch(() => {})   // 静默
    const entry = { promise, ac, timer: null }
    if (ttlMs) entry.timer = setTimeout(() => { if (inflight.get(id) === entry) { ac.abort(); inflight.delete(id) } }, ttlMs)
    inflight.set(id, entry)
    promise.finally(() => { clearTimeout(entry.timer); if (inflight.get(id) === entry) inflight.delete(id) })
    return promise
  }

  let hoverTimer = null
  return {
    hover(id) { clearTimeout(hoverTimer); hoverTimer = setTimeout(() => start(id, { priority: 'low' }), 500) },
    viewport: (id) => start(id, { priority: 'low', ttlMs: 10000 }),
    confirm(id) {
      const cur = inflight.get(id)
      return cur ? cur.promise : queryClient.fetchQuery(optionsFn(id))   // 复用或直发
    },
  }
}
```
**评分点**：
- 意图分层（hover 防抖 500ms / viewport 立即 / confirm 必达），同一 inflight 共享（去重）
- hover TTL 自动 abort（扫过页面的资源回收）；confirm 复用预取 Promise
- fetchQuery 语义（缓存命中不重发）+ 预取失败静默不阻塞导航
- finally 清理 inflight（完成或失败都释放，不泄漏）
