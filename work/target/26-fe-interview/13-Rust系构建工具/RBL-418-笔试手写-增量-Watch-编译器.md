---
title: [RBL-418] 笔试：手写增量 watch 编译器（脏传播 + 部分重编译）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-418：手写增量 watch 编译器
**答**：实现 `createWatcher(graph, { compileModule, onChange })`：1) 初始全量编译（缓存每模块编译产物与输入 hash）；2) watch 文件变更事件：变更模块重编译；3) 脏传播：沿反向依赖边把「引用变更模块」的模块也重编译（引用内容变化）；4) 产物级聚合：受影响 chunk 重渲染，未影响 chunk 跳过（输出 rebuild 列表）；5) 批处理：100ms 窗口内多事件合并一次重编译；6) 内容相等短路：重编译产物与缓存相同 → 不传播（hash 短路）。

```javascript
export function createWatcher(graph, { compileModule, windowMs = 100 } = {}) {
  const cache = new Map()      // id → { inputHash, output, outputHash }
  const reverse = new Map()    // id → [引用者]
  for (const m of graph.modules.values())
    m.imports.forEach((dep) => {
      if (!reverse.has(dep)) reverse.set(dep, [])
      reverse.get(dep).push(m.id)
    })

  let pending = new Set(), timer = null

  function onFileChange(id) {
    pending.add(id)
    clearTimeout(timer)
    timer = setTimeout(() => rebuild(), windowMs)     // 批合并
  }

  function rebuild() {
    const dirty = new Set(), queue = [...pending]
    pending = new Set()
    while (queue.length) {
      const id = queue.pop()
      if (dirty.has(id)) continue
      dirty.add(id)
      const out = compileModule(graph.modules.get(id))
      const prev = cache.get(id)
      if (prev && prev.outputHash === out.hash) { dirty.delete(id); continue }  // 内容相等短路
      cache.set(id, { inputHash: out.inputHash, output: out, outputHash: out.hash })
      queue.push(...(reverse.get(id) ?? []))          // 脏传播
    }
    // chunk 级聚合：受影响模块的归属 chunk 重渲染（示意）
    const affectedChunks = [...dirty].map((id) => graph.chunkOf(id)).filter(Boolean)
    return { recompiled: [...dirty], chunks: [...new Set(affectedChunks)] }
  }

  return { onFileChange, rebuild, getCache: (id) => cache.get(id) }
}
```
**评分点**：
- 反向依赖传播（引用者重编译——依赖边方向别搞反）
- 内容相等短路（编译结果 hash 相同不再传播——防止全链重编译的关键优化）
- 批处理合并（100ms 窗口，保存行为）
- 输出 rebuild 清单（增量可观测）
