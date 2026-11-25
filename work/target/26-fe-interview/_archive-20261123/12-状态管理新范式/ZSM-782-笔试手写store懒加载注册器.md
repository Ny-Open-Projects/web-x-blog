---
title: [ZSM-782] 笔试：手写 store 懒加载注册器（动态 import + 单例保证 + 双实例检测）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-782：手写 store 懒加载注册器（动态 import + 单例保证 + 双实例检测）
**需求**：实现 `createLazyStores()`：1) `register(name, loader)`：登记异步 store 工厂（loader 返回 store 实例）；2) `get(name)`：返回 Promise——首次调用触发 loader 并缓存实例（并发调用共享同一 Promise，单例保证）；3) `instanceId`：每个实例带唯一 id + `__storeTag`；`detectDuplicates()`：检查全局命名空间里同名 store 的实例 id 是否唯一（双实例检测）；4) `preload(names)`：批量预加载；5) 附用例：并发 get 单例、双实例检出。

```javascript
function createLazyStores({ globalRef = globalThis } = {}) {
  const loaders = new Map()      // name -> loader
  const instances = new Map()    // name -> Promise<store>
  const meta = new Map()         // name -> instanceId

  function register(name, loader) {
    loaders.set(name, loader)
    return () => loaders.delete(name)
  }

  function get(name) {
    if (!loaders.has(name)) return Promise.reject(new Error(`unknown store ${name}`))
    // 并发调用共享同一 Promise：单例保证
    if (!instances.has(name)) {
      instances.set(name, (async () => {
        const store = await loaders.get(name)()
        const id = crypto.randomUUID()
        store.__storeTag = { name, id }
        meta.set(name, id)
        // 全局命名空间登记：双实例检测的基础
        globalRef.__storeRegistry ??= new Map()
        globalRef.__storeRegistry.set(name, id)
        return store
      })())
    }
    return instances.get(name)
  }

  async function detectDuplicates() {
    const dupes = []
    // 扫描全局命名空间中同名的不同实例
    const registry = globalRef.__storeRegistry ?? new Map()
    const seen = new Map()
    for (const [name, id] of registry) {
      if (seen.has(name) && seen.get(name) !== id) {
        dupes.push(name)                            // 同名不同实例：双实例
      }
      seen.set(name, id)
    }
    // 本地 meta 对比：本管理器创建的实例与 registry 一致性
    for (const [name, id] of meta) {
      if (registry.has(name) && registry.get(name) !== id) dupes.push(`${name}(external)`)
    }
    return { duplicates: [...new Set(dupes)], healthy: dupes.length === 0 }
  }

  function preload(names) {
    return Promise.allSettled(names.map((n) => get(n)))
  }

  return { register, get, detectDuplicates, preload, meta: () => Object.fromEntries(meta) }
}

// 用例：并发单例
const lazy = createLazyStores()
let creations = 0
lazy.register('cart', async () => {
  creations++
  return { state: { items: [] }, getState: () => this?.state, setState() {} }
})

const [a, b, c] = await Promise.all([lazy.get('cart'), lazy.get('cart'), lazy.get('cart')])
console.log(creations)                       // 1：并发只创建一次
console.log(a === b && b === c)              // true：同一实例

// 双实例检测（模拟另一入口创建了同名 store）
globalThis.__storeRegistry.set('cart', 'other-id')
const report = await lazy.detectDuplicates()
console.log(report.duplicates)               // ['cart(external)']：检出双实例
console.log(report.healthy)                  // false
```
**评分点**：
- 并发单例（Promise 缓存共享，creations = 1）
- 实例 tag（__storeTag 唯一 id 供检测）
- 双实例检测（全局 registry 对比 + external 标记）
- preload 批量预加载（allSettled 不互相拖累）
