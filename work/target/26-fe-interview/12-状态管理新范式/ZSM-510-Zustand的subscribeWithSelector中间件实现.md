---
title: [ZSM-510] subscribeWithSelector 中间件的实现原理与 fireImmediately
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-510：subscribeWithSelector 中间件的实现原理与 fireImmediately

**答**：
- 原生 `store.subscribe(fn)` 是「状态一变就通知整个 listener」，粒度到 store 级。subscribeWithSelector 把 subscribe 改造成 `subscribe(selector, listener, options)`：每次状态变化先跑 selector，与上次结果 `Object.is` 比对，不同才调 listener。
- 实现上中间件包了 `subscribe`：内部用 `Map<listener, { selector, listener, lastValue, hasValue }>` 存订阅元数据，在原 subscribe 的回调里逐个跑 selector 再分发。
- 第三个参数 `options.fireImmediately` 为 true 时，订阅注册当下就用当前状态值触发一次 listener——用于「初始渲染同步 + 后续变更」模式，避免手动读一次初始值。
- selector 返回新引用（数组/对象字面量）会每次都触发，需配合 useShallow 类似的浅比较或 selector 里做记忆化。
- 追问钩子：组件外的订阅不会自动随组件卸载清理，必须在 useEffect 返回里调用返回的 unsubscribe，否则内存泄漏。

```javascript
// 简化实现
function subscribeWithSelectorImpl(fn) {
  return (set, get, api) => {
    const origSubscribe = api.subscribe
    const meta = new Map() // listener -> { selector, lastValue, hasValue }

    api.subscribe = (selector, optListener, options) => {
      if (optListener == null) return origSubscribe(selector) // 兼容原签名

      let lastValue, hasValue = false
      const listener = () => {
        const next = selector(get())
        if (hasValue && Object.is(lastValue, next)) return // 值没变不通知
        hasValue = true
        lastValue = next
        optListener(next, get())
      }
      const un = origSubscribe(listener)
      if (options?.fireImmediately) listener() // 注册即触发一次
      return un
    }

    return fn(set, get, api)
  }
}

// 用法：商品库存变化才刷新角标
const unsub = useCartStore.subscribe(
  (s) => s.items.reduce((a, i) => a + i.qty, 0),
  (count) => updateBadge(count),
  { fireImmediately: true }   // 首次立即用当前值刷一次角标
)
```
