---
title: [ZSM-195] 笔试：手写 cancelable fetch 封装（AbortController + 超时 + 竞态版本号）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-195：手写 cancelable fetch 封装（AbortController + 超时 + 竞态版本号）
**需求**：实现 `createCancelableFetch()`：1) `run(url, opts)` 返回结果 Promise；2) 内置超时（默认 10s）超时抛 TimeoutError 并中止连接；3) `runAll()` 或 `cancelAll()` 取消当前所有在途请求；4) 多次 run 并发时各自独立（一个超时不影响其他）；5) 外部传入 signal 时要和内部超时 signal 链接（任一触发即中止）。

```javascript
export function createCancelableFetch({ timeout = 10000 } = {}) {
  const inflight = new Set()

  function run(url, { signal: outer, ...opts } = {}) {
    const ctrl = new AbortController()
    inflight.add(ctrl)

    // 信号链接：外部 signal 中止 → 内部同步中止
    const onOuter = () => ctrl.abort(outer?.reason)
    outer?.addEventListener('abort', onOuter, { once: true })

    const timer = setTimeout(() => {
      const err = new Error('timeout'); err.name = 'TimeoutError'
      ctrl.abort(err)                          // 超时中止，reason 传播
    }, timeout)

    return fetch(url, { ...opts, signal: ctrl.signal })
      .then(res => {
        if (!res.ok) throw Object.assign(new Error(res.statusText), { status: res.status })
        return res.json()
      })
      .catch(err => {
        if (err.name === 'AbortError' && outer?.reason) throw outer.reason  // 还原外部原因
        throw err
      })
      .finally(() => {
        clearTimeout(timer)
        inflight.delete(ctrl)
        outer?.removeEventListener('abort', onOuter)
      })
  }

  function cancelAll() {
    inflight.forEach(c => c.abort(new Error('cancelled')))
    inflight.clear()
  }

  return { run, cancelAll }
}

// 用法：路由切换清空所有在途请求
// const cf = createCancelableFetch({ timeout: 5000 })
// useEffect(() => () => cf.cancelAll(), [])

// 评分点：
// 1. 超时用 AbortController(reason) 而非只 setTimeout reject（真正掐断连接）
// 2. 内外 signal 链接，外部取消能传播到 fetch
// 3. inflight 集合管理 + finally 清理防泄漏
// 4. 错误还原：外部中止抛外部 reason，不吞成 AbortError
// 5. TimeoutError 与 AbortError 语义可区分
```
