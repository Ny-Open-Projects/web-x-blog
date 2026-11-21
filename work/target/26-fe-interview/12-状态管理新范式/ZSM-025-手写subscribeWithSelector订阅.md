---
title: [ZSM-025] 笔试：手写 subscribeWithSelector 中间件（selector 级订阅）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-025：手写 subscribeWithSelector 中间件（selector 级订阅）

**题目要求**：
- 实现 `subscribeWithSelector(config)`：增强 `api.subscribe`，支持 `subscribe(selector, listener, opts)`。
- 每次 store 变化执行 selector，与上次结果比较（Object.is），变化才调用 listener，回调入参 `(selected, prevSelected, state, prevState)`。
- 返回取消订阅函数；`fireImmediately: true` 时订阅后立刻触发一次。

**边界说明**：保持原始 subscribe（单参 listener）行为兼容。

```javascript
export function subscribeWithSelector(config) {
  return (set, get, api) => {
    const origSubscribe = api.subscribe

    api.subscribe = (selector, listener, opts = {}) => {
      // 兼容原始用法：subscribe(listener)
      if (typeof selector !== 'function') return origSubscribe(selector)

      let prev = selector(get())
      const wrapped = (state, prevState) => {
        const next = selector(state)
        if (!Object.is(next, prev)) {
          const p = prev
          prev = next
          listener(next, p, state, prevState)
        }
      }
      const unsub = origSubscribe(wrapped)
      if (opts.fireImmediately) listener(prev, prev, get(), get())
      return unsub
    }
    return config(set, get, api)
  }
}
```

**评分点**：
- 闭包保存 prev selection，每次变更才通知，避免 listener 频繁空跑。
- fireImmediately 只触发 listener，不等待下一次真实变更。
- 原始 subscribe 语义兼容（单参时走原逻辑）。
- selector 异常（如字段不存在）不应中断整体订阅链——可选 try/catch 加分。
