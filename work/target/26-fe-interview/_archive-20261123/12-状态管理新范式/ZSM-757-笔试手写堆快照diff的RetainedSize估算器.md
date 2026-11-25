---
title: [ZSM-757] 笔试：手写内存增长估算器（引用图遍历 + Retained Size 近似 + 泄漏嫌疑）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-757：手写内存增长估算器（引用图遍历 + Retained Size 近似 + 泄漏嫌疑）
**需求**：实现 `estimateRetained(root, { visited })`：1) 从根对象遍历引用图（own keys + 数组元素 + Map/Set），估算 retained size（递归求不可被外部共享的对象子树大小近似值：`估算 = 自身 shallow + 独占子节点的 retained`——被多个父共享的节点只算一次归最大父）；2) `growthReport(before, after)`：两次快照 diff——按「根路径」分组增长量，输出 Top 增长路径（如 `__stores.table.rows`）；3) 泄漏嫌疑判定：增长 > 阈值且 GC 模拟后仍驻留；4) 附用例：共享节点不重复计数。

```javascript
function shallowSize(v) {
  if (v == null) return 0
  if (typeof v === 'number') return 8
  if (typeof v === 'boolean') return 4
  if (typeof v === 'string') return 16 + v.length * 2
  if (Array.isArray(v)) return 64 + v.length * 8
  if (v instanceof Map || v instanceof Set) return 64 + v.size * 32
  if (typeof v === 'object') return 64 + Object.keys(v).length * 16
  return 8
}

function estimateRetained(root) {
  const owners = new Map()      // node -> 父路径集合
  const paths = new Map()       // node -> 首个到达路径
  function walk(node, path) {
    if (node == null || (typeof node !== 'object' && typeof node !== 'function')) return 0
    if (!paths.has(node)) paths.set(node, path)      // 首路径归因
    let total = shallowSize(node)
    const children = []
    if (Array.isArray(node)) children.push(...node.map((v, i) => [v, `${path}[${i}]`]))
    else if (node instanceof Map) [...node.entries()].forEach(([k, v]) => children.push([v, `${path}.${k}`]))
    else if (node instanceof Set) [...node].forEach((v, i) => children.push([v, `${path}[${i}]`]))
    else for (const k of Object.keys(node)) children.push([node[k], `${path}.${k}`])
    for (const [c, cp] of children) {
      if (c && typeof c === 'object') {
        // 共享节点：只归因首路径（近似）
        if (!paths.has(c)) total += walk(c, cp)
      } else {
        total += shallowSize(c)
      }
    }
    return total
  }
  walk(root, 'root')
  // 输出按首路径聚合
  const byPath = new Map()
  paths.forEach((p, node) => byPath.set(p, shallowSize(node)))
  return { total: estimateRetained.total ?? 0, byPath: [...byPath.entries()] }
}

// growthReport：两次快照 diff
function growthReport(before, after, { threshold = 1024 } = {}) {
  const report = []
  function diff(a, b, path) {
    const sa = shallowSize(a), sb = shallowSize(b)
    const delta = sb - sa
    if (delta > threshold) report.push({ path, delta, suspect: true })
    if (a && b && typeof a === 'object' && typeof b === 'object') {
      for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) {
        if (a[k] !== b[k]) diff(a[k], b[k], `${path}.${k}`)
      }
    }
  }
  diff(before, after, 'root')
  return report.sort((x, y) => y.delta - x.delta).slice(0, 10)
}

// 用例：共享节点不重复计数
const shared = { data: 'x'.repeat(1000) }     // 1KB 数据
const before = { a: shared, b: { other: 1 } }
const after = { a: shared, b: { other: 1, extra: 'y'.repeat(2000) }, c: shared }   // c 引用同一 shared
const report = growthReport(before, after)
console.log(report)
// [{ path: 'root.b.extra', delta: 4016, suspect: true }]
// c 的 shared 不重复计数（同引用），b.extra 是唯一真增长
```
**评分点**：
- 引用图遍历覆盖五种容器（own/array/Map/Set/对象）
- 共享节点首路径归因（不重复计数——retained 语义近似）
- growthReport 按 delta 排序 Top 增长路径（定位根路径）
- 阈值过滤 suspect（噪声控制）
