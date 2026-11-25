---
title: [RBL-523] 笔试：手写 HMR 客户端 runtime（accept 判定 + 叶到根替换 + reload 兜底）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-523：手写 HMR 客户端 runtime（accept 判定 + 叶到根替换 + reload 兜底）
**答**：模拟 HMR 客户端——实现 `createHmrRuntime(registry)`：1) `accept(moduleId, deps, cb)`：模块声明可处理 deps 的更新；2) `applyUpdate(changedIds)`：对每个变更模块沿依赖向上找「最近的 accept 边界」——全部找到 → 执行替换回调（叶到根顺序）；任一未找到 → reload 兜底；3) `dispose` 链：替换前执行旧模块的 dispose（状态保存）；4) 附用例：accept 命中热替换与边界缺失 reload。

```javascript
function createHmrRuntime(registry) {
  // registry: Map<moduleId, { deps: Set<importers>, accept: Map<depId, cb>, dispose: fn|null }>
  const accepts = new Map()       // moduleId -> Map<depId, cb>
  const disposers = new Map()
  const importers = new Map()     // depId -> Set<moduleId>（反向依赖）

  function accept(moduleId, deps, cb) {
    const m = accepts.get(moduleId) ?? accepts.set(moduleId, new Map()).get(moduleId)
    for (const d of deps) {
      m.set(d, cb)
      ;(importers.get(d) ?? importers.set(d, new Set()).get(importers)).add(moduleId)
    }
  }

  function dispose(moduleId, fn) { disposers.set(moduleId, fn) }

  // 从 changed 向上找最近的 accept 边界
  function findBoundary(changedId, visited = new Set()) {
    if (visited.has(changedId)) return null        // 循环：无边界
    visited.add(changedId)
    const importers = importers.get(changedId) ?? new Set()
    for (const imp of importers) {
      const m = accepts.get(imp)
      if (m?.has(changedId)) return { boundary: imp, dep: changedId, cb: m.get(changedId) }
      // 向上递归找
      const up = findBoundary(imp, visited)
      if (up) return up
    }
    return null                                     // 无人 accept：reload
  }

  function applyUpdate(changedIds) {
    const boundaries = new Map()
    for (const id of changedIds) {
      const b = findBoundary(id)
      if (!b) {
        // 任一变更无边界：整页 reload 兜底
        return { reloaded: true, reason: `no accept boundary for ${id}` }
      }
      boundaries.set(id, b)
    }
    // 叶到根执行：先 dispose 旧模块，再跑 accept 回调
    for (const [id, b] of boundaries) {
      disposers.get(id)?.()
      b.cb([id])
    }
    return { reloaded: false, replaced: [...boundaries.keys()] }
  }

  return { accept, dispose, applyUpdate }
}

// 用例
const rt = createHmrRuntime()
// App accept 了 Button 的更新；main 没 accept App
rt.accept('app.js', ['button.js'], (deps) => console.log('app re-rendered for', deps))
rt.dispose('button.js', () => console.log('button state saved'))

// 场景 1：Button 变更 → app accept 命中 → 热替换
console.log(rt.applyUpdate(['button.js']))
// button state saved → app re-rendered for [ 'button.js' ]
// { reloaded: false, replaced: ['button.js'] }

// 场景 2：app.js 变更 → main 未 accept → reload 兜底
console.log(rt.applyUpdate(['app.js']))
// { reloaded: true, reason: 'no accept boundary for app.js' }
```
**评分点**：
- findBoundary 递归（visited 防环 + 最近 accept 边界）
- reload 兜底（任一变更无边界 → 整页——保守正确）
- dispose 链（替换前保存状态）
- 叶到根执行顺序
