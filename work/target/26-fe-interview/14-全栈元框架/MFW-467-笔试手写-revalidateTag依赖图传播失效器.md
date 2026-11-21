---
title: [MFW-467] 笔试：手写 revalidateTag 依赖图传播失效器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-467：revalidateTag 依赖图传播失效器
**需求**：实现 `createTagGraph()`：1) `tag(tag, deps[])` 注册 tag 依赖（'product' 依赖 'category'——分类变商品列表也要失效）；2) `invalidate(tag)` 返回所有应失效 tag 的拓扑序数组（先依赖后自身，保证下游失效时上游数据已可重建）；3) 处理环：检测到环时只失效环内节点并标 `cyclic: true`（不无限递归）；4) 重复 invalidate 同 tag 短期内去重（防并发 Webhook 打爆——5s 窗口）。

```javascript
export function createTagGraph() {
  const deps = new Map()      // tag -> Set(上游依赖)
  const last = new Map()
  const WINDOW = 5000

  function tag(name, ds = []) {
    if (!deps.has(name)) deps.set(name, new Set())
    ds.forEach(d => deps.get(name).add(d))
  }

  function invalidate(name, seen = new Set(), chain = []) {
    const now = Date.now()
    if (now - (last.get(name) || 0) < WINDOW) return [] // 窗口去重
    if (chain.includes(name)) return { cyclic: true, order: [...chain, name] } // 环断路
    if (seen.has(name)) return []
    seen.add(name)
    const order = []
    for (const d of deps.get(name) || []) {
      const sub = invalidate(d, seen, [...chain, name])
      order.push(...(Array.isArray(sub) ? sub : sub.order))
    }
    order.push(name)
    last.set(name, now)
    return { order, cyclic: false }
  }

  return { tag, invalidate: n => { const r = invalidate(n); return r.cyclic ? r : r.order } }
}
```

**评分点**：
- 依赖方向：失效自身先失效上游（重建时数据就绪）
- 访问链检测环（图失效不设防会栈溢出）
- 时间窗口去重（并发 webhook 抖动合并）
- cyclic 结果显式暴露（环是配置错误，要报警不是静默）
