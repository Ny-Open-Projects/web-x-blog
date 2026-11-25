---
title: [ZSM-523] Zustand 怎么实现一次事务里的批量变更只通知一次
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-523：Zustand 怎么实现一次事务里的批量变更只通知一次

**答**：
- 原生行为：每次 `setState` 都会立刻执行 listeners 通知——连续 N 次 set 触发 N 轮通知（React 18 会在事件处理里自动批处理渲染，但「组件外的订阅回调」仍会跑 N 次）。
- 批量需求场景：一个业务操作要改多个不相干切片（购物车加商品 + 优惠券重算 + 角标刷新），希望所有订阅者只感知一次「事务提交」。
- 方案一（推荐）：一次 `setState` 合并写——Zustand 的 set 是幂等函数式的，本来就该把多字段变更写成一次 set；配合 `replace: false` 浅合并。
- 方案二：封装 `transact(fn)`：内部挡住通知（静默收集 changed），fn 跑完统一 flush 一次；实现上要用「通知代理」包住 setState。
- 方案三：subscribeWithSelector 让「无关变更」自然被 selector 过滤——粒度足够细时批量反而没那么必要。
- 追问钩子：React 18 的自动批处理只覆盖渲染，`useEffect` 里的多次 set 在异步回调（setTimeout/await 之后）也已批处理（18 起全场景批处理），但原生订阅仍是逐次通知。

```javascript
// 方案二：transact 实现
function withTransact(create) {
  return (origSet, get, api) => {
    const origNotify = api.listeners ?? (() => {})   // 内部通知入口
    let batching = false
    const pending = []

    api.transact = (fn) => {
      batching = true
      try { fn() } finally {
        batching = false
        const batch = pending.splice(0)  // 取走积累的变更
        if (batch.length) api.setState(batch.at(-1), true) // 只 flush 最后状态
      }
    }
    return create(origSet, get, api)
  }
}

// 简化落地：直接合并写（方案一）
const useCheckout = create((set) => ({
  cart: [], coupon: null, badge: 0,
  addItem(item, discount) {
    // 一次 set 完成三个切片的事务性变更
    set((s) => ({
      cart: [...s.cart, item],
      coupon: discount ?? s.coupon,
      badge: s.cart.length + 1,
    }))
  },
}))
```
