---
title: [MFW-777] SSG 增量构建的组件级依赖追踪
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-777：SSG 组件级依赖追踪

**答**:
- SSG 增量的依赖精度（RBL-705 的深水）：1) **页面 → 组件 → 文件的三级依赖**（page.tsx 引用 Header.tsx——Header.tsx 变更 → 引用 Header 的页面重渲染；2) **依赖的提取方式**：静态分析（import 图——AST 解析 import 语句）vs 运行时追踪（渲染时的模块加载记录——esbuild/turbopack 的 trace RBL-581）；3) **共享组件的爆炸半径**（Header.tsx 被 200 页引用 → Header 变更 = 200 页重渲染——共享组件的变更影响面 = 引用页面数）；「组件的变更频率 × 引用面」决定重建时间。
- 依赖图的管理：依赖图持久化（上次构建的 dep graph——增量 diff 的依据 RBL-533 缓存）；「dep graph 的更新」：每次构建后更新（新页面/组件变更后重建图）。
- 追问钩子：为什么「组件级的依赖追踪」比「页面级的文件 hash」更精确？——页面级 = 只看 page 文件 hash（page.tsx 未变但 Header.tsx 变了 → 页面漏检——静默旧渲染）；组件级 = 看 import 闭包的所有文件（Header.tsx 变 → 引用它的页面全部检出）；「依赖闭包的完备性」（RBL-582）：影响渲染输出的所有文件（组件/样式/配置/数据）都要在依赖闭包中——闭包漏一环 = 静默旧渲染。

```typescript
// 依赖图构建（import 图）
function buildDepGraph(files: Record<string, { imports: string[] }>) {
  const graph = new Map<string, Set<string>>();          // file -> { who imports me }
  for (const [file, meta] of Object.entries(files))
    for (const imp of meta.imports) {
      (graph.get(imp) || graph.set(imp, new Set()).get(imp)).add(file);
    }
  return graph;
}
// 增量 diff：组件变更 → 受影响页面
function affectedPages(changedFiles: string[], depGraph: Map<string, Set<string>>) {
  const affected = new Set<string>();
  const queue = [...changedFiles];
  while (queue.length) {
    const file = queue.shift();
    const importers = depGraph.get(file) ?? new Set();
    for (const importer of importers) {
      if (affected.has(importer)) continue;
      affected.add(importer);
      queue.push(importer);                              // 传递依赖：importer 的 importer 也受影响
    }
  }
  return [...affected].filter(f => f.startsWith('pages/') || f.startsWith('app/'));
}
// Header.tsx 变更 → 传递追踪 → 200 页面重渲染
```
