---
title: [AIC-544] AI 上下文注入：相关文件自动发现
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-544：相关文件自动发现

**答**:
- AI 补全时需要知道"当前文件依赖什么"——相关文件的发现策略：1) **import 追踪**（当前文件 import 了什么 → 带上这些文件的签名（RBL-502 符号级裁剪）；2) **同目录文件**（同目录下的文件——可能是相关组件/utils）；3) **git 历史**（最近修改的文件——可能是相关联的（一起修改的文件 tend to be related）；4) **语义检索**（embedding 搜索——与当前光标附近的代码语义相似的文件片段 RBL-502 semantic 级。
- 发现的优先级：import 闭包 > 同目录 > git co-change > 语义检索——「import 最精确（显式依赖）、语义最模糊（可能相关）」。
- 追问钩子：为什么「git co-change」（一起修改的文件）是有效信号？——两个文件经常同时修改 = 业务上相关（Payment.tsx 和 Payment.test.tsx 一起改；API route 和它的 hook 一起改）；git log 的 co-change 频率 = 文件的关联度——「co-change 矩阵」：fileA 修改时 fileB 也修改的概率——比 import 追踪多覆盖了"隐式关联"（测试文件与实现文件、API 与前端调用）。

```typescript
// 相关文件发现
function findRelatedFiles(currentFile: string, ctx: {
  imports: string[];              // 当前文件的 import 闭包
  sameDir: string[];              // 同目录文件
  gitCoChange: Map<string, string[]>;  // git co-change 矩阵
  embeddings: { file: string; score: number }[];
}): { file: string; source: string; priority: number }[] {
  const results = new Map<string, { source: string; priority: number }>();
  // import 闭包：priority 1
  for (const imp of ctx.imports) {
    results.set(imp, { source: 'import', priority: 1 });
  }
  // 同目录：priority 2
  for (const f of ctx.sameDir) {
    if (!results.has(f)) results.set(f, { source: 'same-dir', priority: 2 });
  }
  // git co-change：priority 3
  const coChanged = ctx.gitCoChange.get(currentFile) ?? [];
  for (const f of coChanged) {
    if (!results.has(f)) results.set(f, { source: 'co-change', priority: 3 });
  }
  // 语义检索：priority 4
  for (const e of ctx.embeddings.slice(0, 5)) {
    if (!results.has(e.file) && e.score > 0.7)
      results.set(e.file, { source: 'semantic', priority: 4 });
  }
  return [...results.entries()]
    .map(([file, v]) => ({ file, ...v }))
    .sort((a, b) => a.priority - b.priority);
}
```
