---
title: [MFW-596] 笔试：手写 SSG 增量构建 diff 器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-596：笔试：手写 SSG 增量 diff 器

**答**：实现 `buildDiff(pages, lastManifest, depGraph, { renderHashOf })`。pages: `{ path, sourceHash, component }[]`；lastManifest: `Record<path, { sourceHash, renderHash }>`；depGraph: `Record<pagePath, string[]>`（页面依赖的组件/数据文件列表）；renderHashOf: `(component) => string`（组件文件 hash——模板变更检测）。规则：1) 页面级变更：sourceHash 变 → 重渲染；2) **级联变更**：页面引用的组件 hash 变（renderHashOf 与 manifest 记录不同）→ 重渲染该页；3) 新页（不在 manifest）→ 渲染；删除页（manifest 有 pages 无）→ removed；4) 返回 `{ toRender: string[], removed: string[], unchanged: number }`。边界：lastManifest 空（全渲染）；depGraph 缺页（按 sourceHash 判定）；组件 hash 相同（不重渲染）。

```javascript
function buildDiff(pages, lastManifest = {}, depGraph = {}, { renderHashOf } = {}) {
  const toRender = [], removed = [];
  const pageSet = new Set(pages.map(p => p.path));
  for (const p of pages) {
    const prev = lastManifest[p.path];
    // 新页
    if (!prev) { toRender.push(p.path); continue; }
    // 内容变更
    if (prev.sourceHash !== p.sourceHash) { toRender.push(p.path); continue; }
    // 级联：依赖组件 hash 变
    const deps = depGraph[p.path] ?? [];
    const depChanged = deps.some(c =>
      prev.renderHashes?.[c] !== renderHashOf(c));
    if (depChanged) { toRender.push(p.path); continue; }
    // 模板全局变更（renderHash 记录）
    if (prev.renderHash !== renderHashOf(p.component)) toRender.push(p.path);
  }
  for (const path of Object.keys(lastManifest))
    if (!pageSet.has(path)) removed.push(path);
  return { toRender: [...new Set(toRender)].sort(), removed: removed.sort(),
    unchanged: pages.length - toRender.length };
}

// 自测
const pages = [
  { path: '/a', sourceHash: 'h1', component: 'LayoutA' },
  { path: '/b', sourceHash: 'h2-changed', component: 'LayoutA' },    // 内容变
  { path: '/c', sourceHash: 'h3', component: 'LayoutB' },            // 新页
];
const lastManifest = {
  '/a': { sourceHash: 'h1', renderHash: 'L1v1',
    renderHashes: { LayoutA: 'L1v1' } },
  '/b': { sourceHash: 'h2', renderHash: 'L1v1', renderHashes: { LayoutA: 'L1v1' } },
  '/old': { sourceHash: 'h9', renderHash: 'L9' },
};
let r = buildDiff(pages, lastManifest, { '/a': ['LayoutA'] }, { renderHashOf: (c) => c === 'LayoutA' ? 'L1v1' : 'L2v1' });
// /a：内容同 + 组件 hash 同 → unchanged；/b：内容变 → render；/c：新页 → render；/old：删除
console.log(r.toRender.sort().join(','));                // /b,/c
console.log(r.removed.join(',') === '/old');
console.log(r.unchanged === 1);

// 组件级联变更
r = buildDiff(pages, lastManifest, { '/a': ['LayoutA'] },
  { renderHashOf: (c) => 'L1v2' });                      // LayoutA 变了
console.log(r.toRender.includes('/a'));                  // 级联：/a 重渲染

// 全新构建
r = buildDiff(pages, {}, {}, { renderHashOf: () => 'x' });
console.log(r.toRender.length === 3 && r.unchanged === 0);
```

**评分点**：
- 三级变更检测：内容 hash / 依赖组件 hash / 模板 hash（依赖闭包的静态分析 RBL-635 SSG 版）
- 新页/删除页的对账；unchanged 计数（增量收益可量化）
- 边界：空 manifest 全渲染、depGraph 缺失降级 sourceHash 判定
- 能说清「SSG 无运行时失效信号——依赖闭包的静态分析是增量精度的唯一手段，漏依赖 = 静默旧内容」属于加分
