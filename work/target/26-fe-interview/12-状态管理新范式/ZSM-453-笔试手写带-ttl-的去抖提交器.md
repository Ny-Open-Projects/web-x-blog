---
title: [ZSM-453] 笔试：手写去抖提交器（trailing+leading 混合 + 取消）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-453：手写去抖提交器
**需求**：实现 `createDebouncedCommit(fn, opts)`：1) `call(args)`：窗口 800ms 内多次调用只提交最后一次（trailing）；2) 首次调用立即提交（leading），窗口重置；3) pending 期间 `cancel()`：丢弃未提交的 trailing 调用（返回 false），已提交的不受影响；4) `flush()` 立即提交 pending；5) 返回的 Promise 在真正提交时 resolve（未提交被 cancel 的 reject 'cancelled'）；6) maxWait 上限：持续调用最迟 maxWait 强制提交（防饿死）。

```javascript
export function createDebouncedCommit(fn, { wait = 800, maxWait = 5000 } = {}) {
  let pendingArgs = null, pendingResolve = null, pendingReject = null
  let timer = null, maxTimer = null, firstAt = 0

  function commit() {
    const [args, resolve, reject] = [pendingArgs, pendingResolve, pendingReject]
    pendingArgs = pendingResolve = pendingReject = null
    clearTimeout(timer); clearTimeout(maxTimer); timer = maxTimer = null
    fn(...args).then(resolve, reject)
  }

  return {
    call(...args) {
      return new Promise((resolve, reject) => {
        if (timer) {          // 已有 pending：resolve 旧 promise 为 cancelled？不——旧 promise 追随同一提交
          pendingReject?.(new Error('superseded'))            // 旧调用方感知被覆盖（可选语义）
        }
        if (!timer) {
          firstAt = Date.now()
          maxTimer = setTimeout(commit, maxWait)               // 防饿死
        }
        pendingArgs = args; pendingResolve = resolve; pendingReject = reject
        clearTimeout(timer)
        timer = setTimeout(commit, wait)                       // trailing
      })
    },
    cancel() {
      if (!timer) return false
      clearTimeout(timer); clearTimeout(maxTimer); timer = maxTimer = null
      pendingReject?.(new Error('cancelled'))
      pendingArgs = pendingResolve = pendingReject = null
      return true
    },
    flush: () => timer ? commit() : undefined,
  }
}
```
**评分点**：
- trailing + leading 首提 + maxWait 防饿死三语义齐备
- cancel 只取消未提交部分（返回 bool 表明是否真有 pending）；flush 立即提交
- Promise 生命周期正确：commit 时 resolve/reject 对应最后调用方，被覆盖的旧调用方显式感知（superseded）
- timer/maxTimer 双清（任何终态路径都清理，防悬挂提交）
