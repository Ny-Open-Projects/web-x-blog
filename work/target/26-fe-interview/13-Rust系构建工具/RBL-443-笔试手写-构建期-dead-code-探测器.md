---
title: [RBL-443] 笔试：手写构建期 dead code 探测器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-443：手写构建期 dead code 探测器
**需求**：实现 `findDeadModules(graph, entry)`：1) graph（RBL-416）；2) 可达性分析：从入口沿 import 边遍历——不可达模块即 dead 候选；3) 动态引用豁免：被动态 import（含字符串模板构造路径目录）引用的模块保守保留（标记 dynamic-ref 不删）；4) re-export 穿透：仅被 barrel re-export 且 barrel 未被使用的模块仍是 dead（barrel 本身可达不算豁免）；5) 输出 dead 列表（含体积——删除收益量化）与置信度（static-analysis vs needs-review）。

```javascript
export function findDeadModules(graph, entry) {
  const reachable = new Set()
  const dynamicRefs = new Set()
  const stack = [entry]

  function walk(id) {
    if (reachable.has(id)) return
    reachable.add(id)
    const mod = graph.modules.get(id)
    if (!mod) return
    for (const dep of mod.imports) walk(dep)                 // 静态可达
    if (mod.dynamic) mod.dynamicTargets?.forEach((t) => dynamicRefs.add(t))   // 动态引用目录
  }
  walk(entry)

  const dead = []
  for (const [id, mod] of graph.modules) {
    if (reachable.has(id)) continue
    if (dynamicRefs.has(id)) {                               // 动态引用豁免
      dead.push({ id, size: mod.size ?? 0, confidence: 'needs-review', reason: 'dynamic ref' })
      continue
    }
    // re-export 穿透：仅被 barrel 引且 barrel 自己也不可达（已由可达性覆盖）→ dead
    dead.push({ id, size: mod.size ?? 0, confidence: 'static-analysis' })
  }
  const wasted = dead.reduce((s, d) => s + d.size, 0)
  return { dead, wastedBytes: wasted, summary: `${dead.length} modules, ${(wasted / 1024).toFixed(1)}KB` }
}
```
**评分点**：
- 可达性分析方向正确（从入口正向遍历，不达即 dead）
- 动态引用保守豁免（needs-review 分类——不假装确定）
- barrel 语义正确（barrel 可达不代表被 re-export 的模块被用——但完整判定需导出级分析，简化版要标注局限）
- 收益量化（dead 模块体积合计）
