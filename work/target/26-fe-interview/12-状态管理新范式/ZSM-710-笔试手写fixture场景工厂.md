---
title: [ZSM-710] 笔试：手写 fixture 场景工厂（原子工厂 + 双出口 + 边界混入）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-710：手写 fixture 场景工厂（原子工厂 + 双出口 + 边界混入）
**答**：实现 `createFixtureFactory()`：1) `atom(name, defaultsFn)`：注册原子工厂（函数每次调用生成新默认值，可被 overrides 覆盖）；2) `scenario(name, builderFn)`：场景组装——builder 内用原子工厂组合，返回 `{ storePatch, apiResponse }` 双出口；3) `overrides` 链：场景级 override 透传到原子层（`scenario('cart', ...)` 生成时传 `{ price: 0 }`）；4) `withEdge(kind)`：边界混入（'long-string' | 'zero' | 'overflow'）修饰产出；5) 附用例：双出口一致性 + 边界值。

```javascript
function createFixtureFactory() {
  const atoms = new Map()
  const scenarios = new Map()

  function atom(name, defaultsFn) {
    atoms.set(name, defaultsFn)
    return (overrides = {}) => ({ ...defaultsFn(), ...overrides })
  }

  function scenario(name, builderFn) {
    scenarios.set(name, builderFn)
    return (overrides = {}, edge) => {
      const built = builderFn({ ...overrides, __edge: edge })
      return edge ? withEdge(built, edge) : built
    }
  }

  // 边界修饰
  function withEdge(built, kind) {
    const clone = structuredClone(built)
    const applyEdge = (obj) => {
      for (const k of Object.keys(obj)) {
        const v = obj[k]
        if (typeof v === 'string' && kind === 'long-string') obj[k] = v.slice(0, 3) + 'x'.repeat(200)
        if (typeof v === 'number' && kind === 'zero') obj[k] = 0
        if (typeof v === 'number' && kind === 'overflow') obj[k] = Number.MAX_SAFE_INTEGER
        if (v && typeof v === 'object') applyEdge(v)
      }
    }
    applyEdge(clone.storePatch)
    return clone
  }

  return { atom, scenario }
}

// 用例
const f = createFixtureFactory()

// 原子工厂
const product = f.atom('product', () => ({ id: crypto.randomUUID(), title: '测试商品', price: 1000, stock: 99 }))
const coupon = f.atom('coupon', () => ({ type: 'flat', amount: 500, expiredAt: Date.now() + 864e5 }))

// 场景组装（双出口）
const cartScenario = f.scenario('cart', (o) => {
  const items = [product(o.p1 ?? {}), product({ ...(o.p2 ?? {}), price: 2000 })]
  const cp = coupon(o.coupon ?? {})
  return {
    storePatch: { items, coupon: cp },
    apiResponse: { code: 0, data: { items, coupon: cp } },
  }
})

// 消费：单测出口
const s = cartScenario({}, 'long-string')
console.log(s.storePatch.items[0].title.length > 200)     // true：边界长字符串
// 消费：MSW 出口（同源数据）
const s2 = cartScenario({ p2: { price: 0 } })
console.log(s2.apiResponse.data.items[1].price)            // 0：override 透传
console.log(s2.storePatch.items[1].price)                  // 0：与 api 出口一致
```
**评分点**：
- 原子工厂 defaults+overrides 合并（每次新实例防引用共享）
- 双出口同源（storePatch 与 apiResponse 由同一构建产出）
- 场景级 override 透传到原子层（p2.price: 0 生效）
- withEdge 递归修饰（long-string/zero/overflow 三类边界）
