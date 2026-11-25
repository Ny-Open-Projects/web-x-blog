---
title: [RBL-410] 笔试：手写产物 diff 报告生成器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-410：手写产物 diff 报告生成器
**答**：实现 `diffManifests(prev, next)`：1) 按 hash 对比文件：新增/删除/修改（hash 变）/不变；2) 修改文件输出体积变化（绝对+百分比）；3) 按「源文件归因」：利用 renames 与 chunk 映射把变化归到 chunk 与来源包（可选深度）；4) 输出结构化 + markdown 双格式（markdown 用于 PR 评论）；5) 排序：按体积变化绝对值降序（最影响看板的排前）；6) 汇总统计 { added, removed, changed, unchanged, sizeDelta }。

```javascript
export function diffManifests(prev, next) {
  const prevByHash = new Map(Object.entries(prev.files).map(([p, f]) => [f.hash, p]))
  const nextByHash = new Map(Object.entries(next.files).map(([p, f]) => [f.hash, p]))
  const items = []
  const all = new Set([...Object.keys(prev.files), ...Object.keys(next.files)])
  for (const p of all) {
    const a = prev.files[p], b = next.files[p]
    if (a && b && a.hash === b.hash) { items.push({ path: p, status: 'unchanged', size: b.size }); continue }
    if (a && b) items.push({ path: p, status: 'changed',
      delta: b.size - a.size, pct: +(((b.size - a.size) / a.size) * 100).toFixed(1) })
    else if (!a) items.push({ path: p, status: 'added', size: b.size })
    else items.push({ path: p, status: 'removed', size: a.size })   // 或标记 rename：hash 在 next 中存在
    if (a && !b && nextByHash.has(a.hash))
      items[items.length - 1].renamedTo = nextByHash.get(a.hash)     // rename 识别
  }
  const sorted = items.filter((i) => i.status !== 'unchanged')
    .sort((x, y) => Math.abs(y.delta ?? y.size ?? 0) - Math.abs(x.delta ?? x.size ?? 0))
  const sizeDelta = Object.values(next.files).reduce((s, f) => s + f.size, 0)
    - Object.values(prev.files).reduce((s, f) => s + f.size, 0)
  const summary = {
    added: items.filter((i) => i.status === 'added').length,
    removed: items.filter((i) => i.status === 'removed').length,
    changed: items.filter((i) => i.status === 'changed').length,
    sizeDelta,
  }
  const md = [
    `**产物 diff**（${summary.sizeDelta >= 0 ? '+' : ''}${(sizeDelta / 1024).toFixed(1)}KB）`,
    ...sorted.slice(0, 20).map((i) => `- [${i.status}] ${i.path}${i.delta ? ` (${i.delta > 0 ? '+' : ''}${i.delta}B ${i.pct}%)` : ''}${i.renamedTo ? ` → ${i.renamedTo}` : ''}`),
  ].join('\n')
  return { summary, items: sorted, md }
}
```
**评分点**：
- hash 对比的状态分类完整（added/removed/changed/unchanged + rename 识别——rename 常被误报为删+增）
- 体积变化绝对+百分比；排序按影响面（绝对值降序）
- 双格式输出（结构化供机器/markdown 供 PR）
- sizeDelta 全量口径正确（含新增减删除）
