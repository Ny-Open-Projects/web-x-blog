---
title: [ZSM-225] subscribeWithSelector 的 selector 订阅是怎么实现的（源码级）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-225：subscribeWithSelector 的 selector 订阅是怎么实现的（源码级）

**答**：
- 给 api.subscribe 加重载：`subscribe(selector, listener, equalityFn?)`，内部把整树 state 订阅转成「selector 结果比较」订阅
- 实现：整树 listener 里对每次新 state 跑 selector，与上次结果用 equalityFn（默认 Object.is）比较，不同才通知——通知粒度从「state 变了」细化到「关心的片段变了」
- 返回 unsubscribe 同样隔离；selector 结果是引用类型时默认比较会失效，要么返回原始值要么传 shallow 相等函数
- 源码启示：selector 在「每次任意 setState」时都会执行，selector 本身要便宜，昂贵派生放 useMemo/select 层

```javascript
function subscribeWithSelectorImpl(config) {
  return (set, get, api) => {
    const origSubscribe = api.subscribe
    api.subscribe = (selector, listener, eq = Object.is) => {
      let prev = selector(get())
      return origSubscribe((state) => {
        const next = selector(state)
        if (!eq(prev, next)) { const p = prev; prev = next; listener(next, p) }
      })
    }
    return config(set, get, api)
  }
}
```
