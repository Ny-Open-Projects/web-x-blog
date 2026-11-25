---
title: [MFW-797] 路由级 bundle 依赖图
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-797：路由级 bundle 依赖图

**答**:
- 路由 bundle 的依赖关系：1) **共享 chunk 的引用图**（路由 A 引用 shared.js、路由 B 也引用 shared.js——共享 chunk 被多路由依赖；2) **路由级别的 bundle 独立性**（路由 A 的 bundle 变更 → 只影响 A（独立 chunk）；共享 chunk 变更 → 影响所有引用路由——变更影响面的差异 RBL-778 传递依赖）；3) **依赖图的用途**：体积预算的路由归因（超预算路由的依赖分析 RBL-561——哪个依赖导致了超标）、chunk 共享的优化决策（RBL-719 引用计数）。
- 依赖图的构建：build manifest（.next/build-manifest.json——pages → files 映射）；「manifest → 依赖图」的反转（route → files vs file → routes——路由级 bundle 分析）。
- 追问钩子：为什么「路由级依赖图」能帮助发现「共享 chunk 膨胀」？——共享 chunk（common.js）被 50 路由引用 → 任何一个路由引入新依赖 → 共享 chunk 膨胀 → 50 路由的 First Load JS 全部增加；「膨胀的源头」：路由级依赖图显示「哪个路由最先引入了这个依赖」→ PR 归因（谁引入了 lodash → shared chunk +30KB）；「膨胀的传播面」：共享 chunk 的变更影响所有路由（RBL-778 的 bundle 维度）——路由级依赖图让共享膨胀的归因精确到 PR。

```typescript
// 路由级 bundle 依赖图
function buildBundleGraph(buildManifest: Record<string, string[]>) {
  // buildManifest: { '/page-a': ['common.js', 'page-a.js'], '/page-b': ['common.js', 'page-b.js'] }
  const fileToRoutes = new Map<string, Set<string>>();
  for (const [route, files] of Object.entries(buildManifest))
    for (const f of files)
      (fileToRoutes.get(f) || fileToRoutes.set(f, new Set()).get(f)).add(route);
  return fileToRoutes;
}
// 共享 chunk 的膨胀归因
function findBloatSource(fileToRoutes, file, sizeGrowth, gitLog) {
  const routes = fileToRoutes.get(file) ?? new Set();
  const commits = gitLog.filter(c => c.files.includes(file));
  return { file, affectedRoutes: [...routes], sizeGrowth,
    commits: commits.map(c => ({ sha: c.sha, author: c.author, message: c.message })) };
}
// 输出：common.js +30KB → 影响 50 路由 → commit abc123 (dev@x) "add lodash"
```
