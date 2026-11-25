---
title: [WCN-925] Partial Hydration 与 Islands 的本质区别：组件级 vs 叶子级水合怎么选
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-925：Partial Hydration 与 Islands 的本质区别：组件级 vs 叶子级水合怎么选

**答**：
- 结论先行：Islands 是「页面里若干棵独立小树分别水合」，Partial Hydration 是「一棵组件树里按组件粒度跳过部分子树的水合」——前者多入口、后者单树内裁剪。
- Islands 适合内容为主、交互点零散的页面（详情/博客/Astro）；Partial Hydration 适合整体是应用、只想跳过纯展示子树（Qwik/Marko 的细粒度恢复）。
- 成本差异：Islands 每个岛有独立运行时与 chunk，边界清晰但岛间状态难共享；Partial Hydration 共享同一运行时，裁剪更细但实现复杂。
- 选型经验：营销/电商落地页用 Islands（SEO + 首屏优先）；复杂后台用 Partial Hydration 或整体应用，别硬套 Islands。
- 追问钩子：面试官问「两者能混用吗」——答：可以——用 Islands 划大边界，边界内部用 Partial Hydration 做叶子级裁剪，但要警惕运行时叠加。

```javascript
// 两种模型示意
// Islands：多棵独立树
const islands = [
  { root: '#nav', hydrate: hydrateNav },    // 独立入口
  { root: '#buy-box', hydrate: hydrateBuy },
];
islands.forEach(i => i.hydrate(document.querySelector(i.root)));

// Partial Hydration：单树内按标记裁剪
function hydrateTree(node) {
  if (node.dataset.static === 'true') return; // 跳过纯展示子树
  node._hydrated = true;
  (node.children || []).forEach(hydrateTree);
}
hydrateTree(document.getElementById('app'));
```
