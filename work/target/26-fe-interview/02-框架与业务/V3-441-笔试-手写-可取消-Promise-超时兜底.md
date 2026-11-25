---
title: [V3-441] 笔试：手写带取消与超时的 Promise 包装器
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-441：笔试：手写带取消与超时的 Promise 包装器
**答**：实现 `cancellable(promiseFactory)`：返回 `{ promise, cancel }`；cancel 后 promise 永远 pending（对调用方等效取消，且不触发 unhandledrejection）；可选 timeout：超时以 TimeoutError reject；cancel 后不再 reject。

```javascript
function cancellable(factory, { timeout } = {}) {
  let cancelled = false
  let timer = null
  const promise = new Promise((resolve, reject) => {
    if (timeout) timer = setTimeout(() => {
      if (!cancelled) reject(new Error('TimeoutError'))
    }, timeout)
    factory().then(
      v => { if (!cancelled) { clearTimeout(timer); resolve(v) } },
      e => { if (!cancelled) { clearTimeout(timer); reject(e) } }
    )
  })
  return {
    promise,
    cancel() { cancelled = true; clearTimeout(timer) } // pending 状态，无 reject → 无 unhandledrejection
  }
}
// 用法：
// const { promise, cancel } = cancellable(() => api.search(q), { timeout: 5000 })
// try { const data = await promise } catch { /* TimeoutError 或业务错误 */ }
```
**评分点**：
- cancel 置 pending 且不再 reject（避免 unhandledrejection，核心细节）。
- timeout reject 错误类型明确。
- clearTimeout 防泄漏。
- 结果写入前检查 cancelled。
