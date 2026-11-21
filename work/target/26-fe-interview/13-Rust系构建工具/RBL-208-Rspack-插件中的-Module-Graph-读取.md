---
title: [RBL-208] 插件里怎么读 Module Graph 做依赖分析
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-208：插件里怎么读 Module Graph 做依赖分析

**答**:
- 入口：`compilation.hooks.finishModules.tap` 后模块图就绪；通过 `compilation.modules` 或 `chunk.getModules()` 遍历
- 常用分析：模块被多少 chunk 引用（共享度）、入口到模块的可达性（死代码候选）、外部依赖统计（node_modules 命中列表）
- 成本意识：全图遍历是大工程，输出必须缓存（finishModules 一次算好存 compilation），不要在 processAssets 里重复遍历
- 与 stats API 的取舍：简单统计用 `stats.toJson({ modules: true, chunkModules: true })`；深度图分析才遍历 graph

```javascript
compiler.hooks.thisCompilation.tap('DepStats', (compilation) => {
  compilation.hooks.finishModules.tap('DepStats', (modules) => {
    const usage = new Map()   // resource → chunk 数
    for (const chunk of compilation.chunks) {
      for (const m of chunk.getModules?.() ?? []) {
        const key = m.resource ?? m.name
        usage.set(key, (usage.get(key) ?? 0) + 1)
      }
    }
    compilation.__depUsage = usage          // 缓存给后续钩子用
  })
})
```
