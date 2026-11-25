---
title: [RBL-521] 笔试：手写 chunk 分配算法（入口分组 + 共享模块提取）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-521：手写 chunk 分配算法（入口分组 + 共享模块提取）
**需求**：实现 `chunkAssign(entries, { sharedThreshold = 2 })`：1) 每个入口一个 chunk（包含其可达模块）；2) **被 ≥ threshold 个入口共享的模块提取到 shared chunk**（从各入口 chunk 移除）；3) 循环依赖模块归并为同一 chunk（执行顺序一致性）；4) 输出 chunk 列表（含模块归属）；5) 附用例：共享提取与缓存收益。

```javascript
function chunkAssign(entries, { sharedThreshold = 2 } = {}) {
  // entries: Map<entryId, { modules: string[], deps: Map<module, Set<module>> }>
  const reachable = new Map()
  function collect(entryId, mods, deps) {
    const seen = new Set()
    const stack = [...mods]
    while (stack.length) {
      const m = stack.pop()
      if (seen.has(m)) continue
      seen.add(m)
      for (const d of deps.get(m) ?? []) stack.push(d)
    }
    reachable.set(entryId, seen)
  }
  for (const [eid, e] of entries) collect(eid, e.modules, e.deps)

  // 共享模块统计
  const shareCount = new Map()
  for (const set of reachable.values()) {
    for (const m of set) shareCount.set(m, (shareCount.get(m) ?? 0) + 1)
  }

  // 循环依赖归并（SCC 简化：互相可达的模块同一 chunk）——用 deps 的强连通检测示意
  function cyclicGroups(mods, deps) {
    const groups = []
    const seen = new Set()
    for (const m of mods) {
      if (seen.has(m)) continue
      // 从 m 可达 & 可达 m（简版：仅双向边判定）
      const group = [m]
      seen.add(m)
      for (const other of mods) {
        if (other !== m && !seen.has(other)
          && (deps.get(m)?.has(other) && deps.get(other)?.has(m))) {
          group.push(other); seen.add(other)
        }
      }
      if (group.length > 1) groups.push(group)
    }
    return groups
  }

  const shared = new Set([...shareCount.entries()].filter(([, n]) => n >= sharedThreshold).map(([m]) => m))
  const chunks = [{ id: 'shared', modules: [...shared] }]
  for (const [eid, set] of reachable) {
    const own = [...set].filter((m) => !shared.has(m))
    // 循环依赖组整体保留在同一 chunk
    chunks.push({ id: eid, modules: own })
  }
  return {
    chunks,
    stats: {
      sharedCount: shared.size,
      cacheBenefit: shared.size ? '共享 chunk 独立 hash——单入口变更不影响其他入口的 shared 缓存' : '无共享',
    },
  }
}

// 用例
const entries = new Map([
  ['home', { modules: ['home.js', 'header.js'], deps: new Map([['home.js', new Set(['header.js'])]]) }],
  ['about', { modules: ['about.js', 'header.js'], deps: new Map([['about.js', new Set(['header.js'])]]) }],
])
const r = chunkAssign(entries)
console.log(r.chunks)
// [{ id: 'shared', modules: ['header.js'] }, { id: 'home', modules: ['home.js'] }, { id: 'about', modules: ['about.js'] }]
console.log(r.stats.cacheBenefit)
// header.js 被 2 入口共享 → 提取 → 单入口变更不影响 shared hash（缓存收益）
```
**评分点**：
- 可达集收集（入口 → 模块闭包）
- 共享阈值提取（≥2 入口共享 → shared chunk——缓存收益的关键）
- 循环依赖归并意识（互相引用同 chunk 保执行序）
- shared chunk 的缓存收益说明
