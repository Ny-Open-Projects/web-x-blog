---
title: [RBL-556] 笔试：手写 assets 双向同步视图（读快照 + 写回传）
date: 2025-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-556：手写 assets 双向同步视图（读快照 + 写回传）
**需求**：555 落地——实现 `createAssetsView(rustAssets, syncBack)`：1) `view`：Proxy 视图——读取 `view['a.js']` 返回 `{ source() }` 形态（webpack 插件习惯）；2) 插件写（`view['b.js'] = { source() {...} }` 或 delete）→ 记录变更 → `flush()` 批量同步回 Rust 侧（syncBack 回调）；3) 变更追踪（added/deleted/replaced 三类）；4) 附用例：读写追踪与批量同步。

```javascript
function createAssetsView(rustAssets, syncBack) {
  const changes = { added: new Map(), deleted: new Set(), replaced: new Map() }

  const view = new Proxy({}, {
    get(_, name) {
      if (typeof name !== 'string') return undefined
      if (changes.replaced.has(name)) return { source: () => changes.replaced.get(name) }
      if (changes.added.has(name)) return { source: () => changes.added.get(name) }
      if (rustAssets.has(name) && !changes.deleted.has(name)) {
        const content = rustAssets.get(name)
        return { source: () => content }              // webpack 插件习惯形态
      }
      return undefined
    },
    set(_, name, value) {
      if (typeof value?.source !== 'function') throw new Error('assets 赋值需 { source() } 形态')
      if (rustAssets.has(name) || changes.replaced.has(name)) changes.replaced.set(name, value.source())
      else changes.added.set(name, value.source())
      return true
    },
    deleteProperty(_, name) {
      if (rustAssets.has(name) || changes.replaced.has(name)) changes.deleted.add(name)
      return true
    },
    ownKeys() {
      const keys = new Set([...rustAssets.keys(), ...changes.added.keys()])
      changes.deleted.forEach((k) => keys.delete(k))
      return [...keys]
    },
  })

  function flush() {
    const summary = {
      added: [...changes.added.entries()],
      replaced: [...changes.replaced.entries()],
      deleted: [...changes.deleted],
    }
    syncBack(summary)                                  // 批量同步回 Rust（一次跨桥）
    // 清空变更（同步后）
    changes.added.clear(); changes.replaced.clear(); changes.deleted.clear()
    return summary
  }

  return { view, flush }
}

// 用例
const rustAssets = new Map([['a.js', 'orig-a']])
const synced = []
const { view, flush } = createAssetsView(rustAssets, (summary) => synced.push(summary))

// 插件读
console.log(view['a.js'].source())                     // 'orig-a'
// 插件写：替换 + 新增 + 删除
view['a.js'] = { source: () => 'modified-a' }
view['new.js'] = { source: () => 'brand-new' }
delete view['old.js']                                  // rustAssets 无 old.js——忽略（防御）
const s = flush()
console.log(s.replaced.map(([k]) => k), s.added.map(([k]) => k))
// ['a.js'] ['new.js']：变更追踪
console.log(synced.length)                             // 1：批量一次同步
```
**评分点**：
- Proxy 视图（webpack 插件习惯的 { source() } 形态）
- 三类变更追踪（added/replaced/deleted）
- flush 批量同步（一次跨桥回传）
- delete 的防御（不存在的资产忽略）
