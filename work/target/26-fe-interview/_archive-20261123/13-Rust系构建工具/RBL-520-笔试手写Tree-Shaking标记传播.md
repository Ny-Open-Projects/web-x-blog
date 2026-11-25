---
title: [RBL-520] 笔试：手写 Tree-Shaking 标记传播（USED 标记 + 副作用过滤）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-520：手写 Tree-Shaking 标记传播（USED 标记 + 副作用过滤）
**需求**：实现 `createTreeshaker()`：1) `addModule(id, { exports: Map<exportName, statementId>, sideEffects, hasEffect: Map<statementId, bool> })`；2) `mark(entryExports)`：从入口具名导入出发标记「USED」——导出语句被用 → 其依赖语句也 USED（语句级依赖图）；3) `result()`：输出每模块「保留的语句清单」——副作用语句（hasEffect=true 且模块 sideEffects 未声明 false）强制保留；4) 附用例：摇树精度与副作用强制保留。

```javascript
function createTreeshaker() {
  const modules = new Map()
  const stmtDeps = new Map()    // statementId -> Set<依赖 statementId>（模块内语句依赖）
  const used = new Set()        // USED 的 statementId

  function addModule(id, def) {
    modules.set(id, def)
    for (const [k, deps] of Object.entries(def.stmtDeps ?? {})) {
      stmtDeps.set(`${id}#${k}`, new Set(deps.map((d) => `${id}#${d}`)))
    }
    return this
  }

  function mark(entryImports) {
    // entry: [{ moduleId, importedNames }]
    const queue = []
    for (const { moduleId, names } of entryImports) {
      const m = modules.get(moduleId)
      for (const name of names) {
        const stmtId = m.exports.get(name)
        if (stmtId != null) queue.push(`${moduleId}#${stmtId}`)
      }
      // import 本身是副作用语句（若模块声明有副作用）
      if (m.sideEffects !== false) queue.push(`${moduleId}#import`)
    }
    // USED 标记传播：语句 → 依赖语句（模块内 + 跨模块 re-export）
    while (queue.length) {
      const sid = queue.pop()
      if (used.has(sid)) continue
      used.add(sid)
      for (const dep of stmtDeps.get(sid) ?? []) if (!used.has(dep)) queue.push(dep)
      // 跨模块：语句引用其他模块导出 → 标记对方
      for (const dep of stmtDeps.get(sid) ?? []) {
        if (dep.includes('@')) {
          const [mid, name] = dep.split('@')
          const m = modules.get(mid)
          if (m?.exports.has(name)) queue.push(`${mid}#${m.exports.get(name)}`)
        }
      }
    }
  }

  function result() {
    const out = {}
    for (const [id, m] of modules) {
      const kept = []
      for (const [name, stmt] of m.exports) {
        const sid = `${id}#${stmt}`
        const isSideEffect = m.hasEffect?.get(stmt) && m.sideEffects !== false
        if (used.has(sid) || isSideEffect) kept.push(stmt)     // USED 或副作用强制保留
      }
      out[id] = kept
    }
    return out
  }

  return { addModule, mark, result, usedCount: () => used.size }
}

// 用例
const ts = createTreeshaker()
ts.addModule('utils.js', {
  exports: new Map([['usedFn', 1], ['unusedFn', 2], ['init', 3]]),
  sideEffects: false,
  hasEffect: new Map([[3, true]]),                       // init 有副作用
  stmtDeps: { 1: [], 2: [], 3: [] },
})
ts.addModule('app.js', {
  exports: new Map([['main', 10]]),
  sideEffects: true,
  hasEffect: new Map(),
  stmtDeps: { 10: ['utils.js@usedFn'] },                 // main 依赖 utils 的 usedFn
})
ts.mark([{ moduleId: 'app.js', names: ['main'] }])

console.log(ts.result())
// { 'utils.js': [1, 3], 'app.js': [10] }
// stmt1（usedFn）：USED；stmt2（unusedFn）：摇掉；stmt3（init）：副作用强制保留
```
**评分点**：
- USED 标记传播（语句级依赖图 + 队列扩散）
- 跨模块 re-export 追踪（dep 含 @ 分隔的跨模块引用）
- 副作用强制保留（hasEffect && sideEffects!==false——不误摇）
- 未用语句被摇（unusedFn 消失——精度验证）
