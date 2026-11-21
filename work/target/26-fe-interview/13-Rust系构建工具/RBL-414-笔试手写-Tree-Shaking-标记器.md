---
title: [RBL-414] 笔试：手写 Tree-Shaking 标记器（从入口标记可达导出）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-414：手写 Tree-Shaking 标记器
**需求**：实现 `markUsedExports(entryExports, modules)`：1) modules：`{ id, exports: string[], imports: [{ from, names: string[] }], sideEffects: boolean }[]`；2) 从入口被引用的导出出发，沿 import 链标记「使用的导出」（跨模块传播）；3) sideEffects: true 的模块整体保留（所有导出标记 used）；4) 输出每个模块的 usedExports 与 unusedExports（shaking 候选）；5) 循环引用安全（标记过程不死循环）；6) re-export 链（barrel）穿透（a re-export b 的 x）。

```javascript
export function markUsedExports(entryRefs, modules) {
  const byId = new Map(modules.map((m) => [m.id, m]))
  const used = new Map(modules.map((m) => [m.id, new Set()]))
  const queue = []                                   // [moduleId, exportName]
  const seen = new Set()

  for (const ref of entryRefs) queue.push([ref.from, ref.name])

  while (queue.length) {
    const [mid, name] = queue.pop()
    const key = `${mid}#${name}`
    if (seen.has(key)) continue                      // 循环安全
    seen.add(key)
    const mod = byId.get(mid)
    if (!mod) continue
    if (mod.sideEffects) {
      mod.exports.forEach((e) => used.get(mid).add(e))          // 整体保留
    } else {
      used.get(mid).add(name)
    }
    // 该模块内声明用到的依赖：简化——每导出关联其 import（真实实现需语句级绑定分析）
    for (const imp of mod.imports) {
      for (const n of imp.names) {
        const depKey = `${imp.from}#${n}`
        if (!seen.has(depKey)) queue.push([imp.from, n])        // 穿透 re-export 链
      }
    }
  }

  return modules.map((m) => ({
    id: m.id,
    usedExports: [...used.get(m.id)],
    unusedExports: m.exports.filter((e) => !used.get(m.id).has(e)),
  }))
}

// barrel 穿透：index re-export a 的 x → 使用 index.x 标记 a.x used
```
**评分点**：
- 从使用侧标记（entry 引用出发反向传播），不是从定义侧猜
- sideEffects: true 整体保留语义正确
- 循环安全（seen 集合）；barrel re-export 穿透
- 简化点诚实标注：真实 shaking 需语句级绑定与副作用注解（#__PURE__）——说明模型局限是加分项
