---
title: [ZSM-716] 笔试：手写 Mermaid 状态图生成器（slice 扫描 + action 边 + 环检测）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-716：手写 Mermaid 状态图生成器（slice 扫描 + action 边 + 环检测）
**答**：实现 `generateStateGraph(slices)`（输入为结构化 slice 描述而非 AST，聚焦图算法）：1) slices 形如 `{ name, state: [字段], reducers: ['add','remove'], extra: ['other/action1'] }`；2) 输出 Mermaid `graph TD`：slice 子图 + 字段节点 + action 边（自环标 internal、跨 slice 标 external）；3) **环检测**：跨 slice 的 action 依赖成环（A 的 extra 监听 B 产生的 action 且反向）时警告并标红边；4) `stats()`：slice 数、边数、外部依赖度（每 slice 的 extra 入边数）；5) 附用例：两 slice 互相监听检出环。

```javascript
function generateStateGraph(slices) {
  const byName = new Map(slices.map((s) => [s.name, s]))
  const lines = ['graph TD']
  const edges = []
  const cycEdges = new Set()

  // 子图与字段节点
  for (const s of slices) {
    lines.push(`  subgraph ${s.name}`)
    s.state.forEach((f) => lines.push(`    ${s.name}__${f}["${f}"]`))
    lines.push('  end')
  }

  // 边：reducers 自环（internal）+ extra 跨域（external）
  for (const s of slices) {
    s.reducers.forEach((r) => edges.push({ from: `${s.name}/${r}`, to: s.name, kind: 'internal' }))
    s.extra.forEach((a) => {
      const owner = a.split('/')[0]
      const kind = byName.has(owner) ? 'external' : 'global'
      edges.push({ from: a, to: s.name, kind })
    })
  }

  // 环检测：external 边构成的跨 slice 依赖图
  const depAdj = new Map()
  edges.filter((e) => e.kind === 'external').forEach(({ from, to }) => {
    const owner = from.split('/')[0]
    ;(depAdj.get(owner) ?? depAdj.set(owner, []).get(owner)).push(to)
  })
  const color = new Map()
  function dfs(n, stack) {
    color.set(n, 1)
    stack.push(n)
    for (const m of depAdj.get(n) ?? []) {
      if (color.get(m) === 1) stack.slice(stack.indexOf(m)).concat(m).forEach((x) => cycEdges.add(x))
      else if (!color.get(m)) dfs(m, stack)
    }
    stack.pop()
    color.set(n, 2)
  }
  slices.forEach((s) => { if (!color.get(s.name)) dfs(s.name, []) })

  // 渲染
  for (const e of edges) {
    const label = e.kind === 'internal' ? '|internal|' : e.kind === 'global' ? '|global|' : ''
    const style = cycEdges.has(e.to) ? ' :::alert' : ''
    lines.push(`  ${e.from.replace(/\W/g, '_')} -->${label} ${e.to}${style}`)
  }
  if (cycEdges.size) lines.push('  classDef alert fill:#f66;')

  const stats = () => ({
    slices: slices.length,
    edges: edges.length,
    externalDeps: Object.fromEntries(slices.map((s) => [
      s.name,
      edges.filter((e) => e.to === s.name && e.kind === 'external').length,
    ])),
    cycles: [...cycEdges],
  })

  return { mermaid: lines.join('\n'), stats }
}

// 用例
const g = generateStateGraph([
  { name: 'cart', state: ['items'], reducers: ['addItem'], extra: ['checkout/cleared'] },
  { name: 'checkout', state: ['total'], reducers: ['submit'], extra: ['cart/changed'] },
  { name: 'auth', state: ['user'], reducers: ['login'], extra: [] },
])
console.log(g.mermaid.split('\n').length > 5)
console.log(g.stats())
// { slices: 3, edges: 5, externalDeps: { cart: 1, checkout: 1, auth: 0 }, cycles: ['cart','checkout'] }
// cart ↔ checkout 互相监听：检出环并标红
```
**评分点**：
- 三类边语义（internal/external/global）
- 跨 slice 依赖环检测（extra 边构成的图 DFS 三色标记）
- externalDeps 依赖度统计（架构健康度量）
- Mermaid 输出可直接进 PR 文档（同源不过期）
