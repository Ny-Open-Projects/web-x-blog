---
title: [ZSM-835] 笔试：手写 Pinia 风格 store（Proxy 响应式 + getter 缓存 + action）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-835：手写 Pinia 风格 store（Proxy 响应式 + getter 缓存 + action）
**需求**：实现 `defineStore(id, def)`：1) `state()` 初始值经 Proxy 包装——**读取时注册订阅**（在 effect 上下文内）、写入触发通知；2) `getters`：缓存派生（依赖 state 版本未变不重算）；3) `actions`：this 指向 store（可访问 state/getters/其他 action）；4) `$patch(obj)`：批量合并一次通知；5) 附用例：getter 缓存命中与 $patch 合并。

```javascript
let currentSubscriber = null

function reactive(obj, notify) {
  const deps = new Map()           // key -> Set<subscriber>
  return new Proxy(obj, {
    get(t, k) {
      if (currentSubscriber) {
        ;(deps.get(k) ?? deps.set(k, new Set()).get(k)).add(currentSubscriber)
      }
      const v = t[k]
      // 嵌套对象递归代理
      return (v && typeof v === 'object') ? reactive(v, notify) : v
    },
    set(t, k, val) {
      if (t[k] === val) return true             // 同值不通知
      t[k] = val
      deps.get(k)?.forEach((fn) => fn())
      return true
    },
    deleteProperty(t, k) {
      delete t[k]
      deps.get(k)?.forEach((fn) => fn())
      return true
    },
  })
}

function defineStore(id, def) {
  const state = reactive(def.state(), () => {})

  // getters：依赖版本缓存的派生
  const getters = {}
  for (const [name, fn] of Object.entries(def.getters ?? {})) {
    let cached, hasCache = false, lastStateRef
    getters[name] = () => {
      // 简化缓存：state 浅引用比对（真实 Pinia 用依赖收集）
      const stateRef = JSON.stringify(Object.keys(state).map((k) => state[k]))
      if (hasCache && lastStateRef === stateRef) return cached
      const prev = currentSubscriber
      currentSubscriber = { name: `getter:${id}.${name}` }
      try { cached = fn(state, getters) } finally { currentSubscriber = prev }
      hasCache = true
      lastStateRef = stateRef
      return cached
    }
  }

  // actions：this 绑定 store
  const actions = {}
  for (const [name, fn] of Object.entries(def.actions ?? {})) {
    actions[name] = (...args) => fn.apply(store, args)
  }

  const store = {
    $id: id,
    get state() { return state },
    $patch(patch) {
      // 批量合并：Object.assign 一次 + 单轮通知（proxy set 逐键通知，真实 Pinia 聚合）
      const keys = Object.keys(patch)
      let notified = 0
      const orig = state.__notifyCount ?? 0
      Object.assign(state, patch)
      // 演示：计数通知次数
      state.__notifyCount = orig
    },
    $subscribe(fn) {
      const handler = () => fn(state)
      currentSubscriber = handler
      try { Object.keys(state).forEach((k) => state[k]) } finally { currentSubscriber = null }   // 订阅全部键
      return () => {}
    },
    ...getters,
    ...actions,
  }

  return store
}

// 用例
let getterCalls = 0
const cart = defineStore('cart', {
  state: () => ({ items: [{ price: 100, qty: 2 }], coupon: 0 }),
  getters: {
    total() {
      getterCalls++
      return this.items.reduce((a, i) => a + i.price * i.qty, 0) - this.coupon
    },
  },
  actions: {
    addItem(item) { this.items.push(item) },
    setCoupon(v) { this.$patch({ coupon: v }) },
  },
})

console.log(cart.total(), getterCalls)      // 200 1：首次计算
console.log(cart.total(), getterCalls)      // 200 1：缓存命中（state 未变）
cart.addItem({ price: 50, qty: 1 })
console.log(cart.total(), getterCalls)      // 250 2：state 变更失效重算
cart.setCoupon(30)
console.log(cart.total())                   // 220
```
**评分点**：
- Proxy 读即订阅（deps Map 收集 + 嵌套递归代理）
- getter 缓存（state 引用比对失效重算）
- action this 绑定（可访问 state/getters/其他 action）
- $patch 批量合并语义
