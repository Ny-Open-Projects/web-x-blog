---
title: [RBL-416] 笔试：手写 Module Graph 构建器（递归解析 + 循环处理）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-416：手写 Module Graph 构建器
**需求**：实现 `buildGraph(entries, { readFile, resolve })`：1) 从入口递归：readFile → 提取 import（静态字符串）→ resolve → 递归子模块；2) 图节点 { id, content, imports: string[] }，去重（同模块单实例）；3) 循环引用：标记 cycle 但不无限递归（访问中集合）；4) 动态 import（变量参数）标记 dynamic-unresolved（保守策略：视为无法静态分析）；5) 缺失模块：报错带完整解析链（从哪个文件引用的）；6) 输出 { modules: Map, entry: id, cycles: [][] }。

```javascript
export function buildGraph(entries, { readFile, resolve, extractImports }) {
  const modules = new Map()
  const cycles = []
  const state = new Map()                            // 0=未访问 1=访问中 2=完成

  function visit(id, refChain) {
    if (modules.has(id)) {
      if (state.get(id) === 1) cycles.push([...refChain, id])    // 循环
      return
    }
    state.set(id, 1)
    const content = readFile(id)
    if (content === null)
      throw new Error(`cannot resolve: ${id}, imported from ${(refChain.at(-2) ?? '<entry>')}`)
    const mod = { id, content, imports: [], dynamic: false }
    modules.set(id, mod)
    for (const spec of extractImports(content)) {
      if (spec.dynamic) { mod.dynamic = true; continue }         // 保守标记
      const resolved = resolve(id, spec.path)
      if (!resolved) throw new Error(`unresolved: ${spec.path} from ${id}`)
      mod.imports.push(resolved)
      visit(resolved, [...refChain, id])
    }
    state.set(id, 2)
  }

  const entryIds = entries.map((e) => resolve(null, e))
  entryIds.forEach((id) => visit(id, []))
  return { modules, entry: entryIds[0], cycles }
}

// 提取器（简化正则）：/import\s+.*?from\s+['"]([^'"]+)['"]/g + /\bimport\(\s*['"]([^'"]+)['"]\s*\)/g（静态动态）
```
**评分点**：
- 访问三态防循环（state 1=访问中 → cycle 记录不递归）
- 去重（同模块单实例——多入口共享模块合并）
- 动态 import 保守策略（变量路径 static-unresolved，不猜）
- 错误带解析链（从哪个文件引用的——排查体验）
