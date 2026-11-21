---
title: [RBL-401] 笔试：手写 affected 计算器（变更文件 → 影响任务集）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-401：手写 affected 计算器
**需求**：实现 `computeAffected(changedFiles, graph, globalDeps)`：1) graph：`{ pkg, deps: string[], files: string[] }[]`（包依赖图+文件归属）；2) 变更文件 → 所属包 → 沿「被依赖方向」闭包展开（依赖该包的包都受影响）；3) globalDeps 命中（如 tsconfig.base.json）→ 全部包受影响；4) 返回受影响包集合（确定性排序）；5) 循环依赖检测（图中环则抛错——affected 依赖无环图）。

```javascript
function computeAffected(changedFiles, graph, globalDeps) {
  if (hasCycle(graph)) throw new Error('dependency cycle')
  const owner = new Map()                          // 文件 → 包
  graph.forEach((p) => p.files.forEach((f) => owner.set(f, p.pkg)))
  const touched = new Set()
  if (changedFiles.some((f) => globalDeps.includes(f))) return graph.map((p) => p.pkg).sort()

  const reverse = buildReverse(graph)              // pkg → [依赖它的 pkg]
  const queue = []
  for (const f of changedFiles) {
    const pkg = owner.get(f)
    if (pkg && !touched.has(pkg)) { touched.add(pkg); queue.push(pkg) }
  }
  while (queue.length) {
    const cur = queue.pop()
    for (const next of reverse.get(cur) ?? []) {
      if (!touched.has(next)) { touched.add(next); queue.push(next) }
    }
  }
  return [...touched].sort()
}

function buildReverse(graph) {
  const m = new Map()
  graph.forEach((p) => p.deps.forEach((d) => {
    if (!m.has(d)) m.set(d, [])
    m.get(d).push(p.pkg)
  }))
  return m
}

function hasCycle(graph) {
  const state = new Map()                          // 0=未访问 1=访问中 2=完成
  const dfs = (pkg) => {
    const s = state.get(pkg) ?? 0
    if (s === 1) return true
    if (s === 2) return false
    state.set(pkg, 1)
    const p = graph.find((x) => x.pkg === pkg)
    if (p?.deps.some((d) => dfs(d))) return true
    state.set(pkg, 2)
    return false
  }
  return graph.some((p) => dfs(p.pkg))
}
```
**评分点**：
- 方向正确：沿「被依赖方向」传播（reverse graph），不是沿依赖方向
- globalDeps 短路（全局文件 → 全量影响）
- 文件归属映射（files → pkg）；未归属文件安全忽略
- 环检测前置（affected 依赖 DAG，环即结果不可信）
