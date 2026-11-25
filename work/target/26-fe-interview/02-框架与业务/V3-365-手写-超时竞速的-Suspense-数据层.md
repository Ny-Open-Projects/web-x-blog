---
title: [V3-365] 手写：带超时竞速与兜底的 Suspense 数据层
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-365：手写：带超时竞速与兜底的 Suspense 数据层
**答**：实现 `loadResource(loader, { timeout = 3000, fallback = null })`：loader 超时改用 fallback 数据（不 reject），失败也回退 fallback 并上报错误；多次调用同 key 需去重（进行中的 promise 复用）。

```javascript
const inflight = new Map()
function loadResource(key, loader, { timeout = 3000, fallback = null, onError } = {}) {
  if (inflight.has(key)) return inflight.get(key)
  const p = (async () => {
    let timer
    const timeoutP = new Promise(r => { timer = setTimeout(() => r(fallback), timeout) })
    try {
      const data = await Promise.race([loader(), timeoutP])
      return data
    } catch (e) {
      onError?.(e)
      return fallback
    } finally {
      clearTimeout(timer)
      inflight.delete(key)
    }
  })()
  inflight.set(key, p)
  return p
}
// 用法：Suspense 内 await loadResource(`goods:${id}`, () => fetchGoods(id), { fallback: cachedGoods })
```
**评分点**：
- 超时不 reject 而是切 fallback（Suspense 场景比报错更可用）。
- inflight Map 去重，finally 里清理防止泄漏。
- 失败路径上报 + 兜底，异常不会让整页崩溃。
- timer 在成功路径也要清理（clearTimeout 在 finally）。
