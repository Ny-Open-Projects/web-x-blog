---
title: [MFW-457] 笔试：手写 RSC 树 diff 增量重渲染决策器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-457：RSC 树 diff 增量重渲染决策器
**答**：实现 `planRerender(prevTree, nextTree)`：1) 树节点 { id, type: 'server'|'client', props, children }；2) diff 后输出需重新在服务端执行的 server 段集合：client 节点 props 变了只重发 props，不重跑其 server 子树；server 节点 props 变了（或 key 变）连同整段 server 子树标 `rerun`；3) key 相同的 server 叶子 props 深相等 → 标 `skip`（缓存命中语义）；4) 输出 [{ id, action: 'rerun'|'reprop'|'skip' }]，顺序保持先序。

```javascript
function same(a, b) { return JSON.stringify(a ?? null) === JSON.stringify(b ?? null) }

export function planRerender(prev, next, out = []) {
  if (!prev || !next || prev.id !== next.id || prev.key !== next.key) {
    collectAll(next, out, 'rerun'); return out
  }
  const propsChanged = !same(prev.props, next.props)
  if (prev.type === 'server') {
    if (propsChanged) { collectAll(next, out, 'rerun'); return out }
    out.push({ id: next.id, action: 'skip' })
  } else {
    // client 节点：props 变了只 reprop，子树是否重跑由 server 子节点自判
    out.push({ id: next.id, action: propsChanged ? 'reprop' : 'skip' })
  }
  const pk = new Map(prev.children.map(c => [c.key ?? c.id, c]))
  for (const nc of next.children) {
    const pc = pk.get(nc.key ?? nc.id)
    planRerender(pc, nc, out) // 没有对应旧节点 → 内部 collectAll 兜底 rerun
  }
  return out
}

function collectAll(node, out, action) {
  if (!node) return
  out.push({ id: node.id, action })
  node.children.forEach(c => collectAll(c, out, action))
}
```

**评分点**：
- client/server 分叉：client 变化止于 reprop（不向上污染 server 段）
- key/id 不匹配整段 rerun（结构变化不走逐字段比较）
- server props 深相等 → skip（等价 Data Cache 命中）
- 先序输出保证 payload 可按序下发
