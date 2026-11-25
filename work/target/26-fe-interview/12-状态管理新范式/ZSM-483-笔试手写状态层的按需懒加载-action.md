---
title: [ZSM-483] 笔试：手写状态层按需懒加载 action
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-483：手写状态层按需懒加载 action
**答**：实现 `lazyActions(store, loaders)`：1) loaders：`{ exportExcel: () => import('./excelAction') }`——大动作代码分包；2) 调用 `store.exportExcel(...)`：动态 import → 拿到真实 action → 执行；3) 并发调用去重：同 action 在途 import 共享同一 Promise；4) 加载中再次调用排队等待后执行（语义：每次调用都执行，共享 import 不共享执行）；5) 加载失败：抛错并允许下次重试（失败不缓存）；6) TS 类型：懒加载 action 签名与同步一致（声明式映射）。

```javascript
export function lazyActions(store, loaders) {
  const modules = new Map()   // name → Promise<module>
  const cache = new Map()     // name → { mod, error? }

  for (const name of Object.keys(loaders)) {
    store[name] = async (...args) => {
      let entry = cache.get(name)
      if (entry?.mod) return entry.mod[name](store, ...args)
      if (entry?.error) throw entry.error                      // 失败不缓存语义：这里应重试
      if (!modules.has(name)) {
        const p = loaders[name]()
          .then((mod) => { cache.set(name, { mod: mod.default ?? mod }); return mod })
          .catch((e) => { cache.delete(name); throw e })       // 失败清缓存允许重试
        modules.set(name, p)
      }
      const mod = await modules.get(name)
      return (mod.default ?? mod)[name](store, ...args)
    }
  }
  return store
}

// loaders 定义（chunk 分包）
const loaders = {
  exportExcel: () => import('./actions/excel'),   // excel.js export default { exportExcel(store, rows) {...} }
  printReport: () => import('./actions/print'),
}
```
**评分点**：
- 代码分包语义正确（大动作按需加载，主包不膨胀）
- 「共享 import 不共享执行」——每次调用都执行 action，只有模块加载去重（常见混淆点）
- 失败清缓存允许重试；在途 Promise 共享（并发加载防抖）
- store[name] 动态挂载，调用面与同步 action 一致
