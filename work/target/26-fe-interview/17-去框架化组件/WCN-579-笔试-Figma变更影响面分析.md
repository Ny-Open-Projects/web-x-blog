---
title: [WCN-579] 笔试：实现「Figma token 变更 → 影响面分析」工具（依赖图反查 + 受影响的 CSS 变量清单）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-579：笔试：实现「Figma token 变更 → 影响面分析」工具（依赖图反查 + 受影响的 CSS 变量清单）。

**答**：
- 结论：构建「设计变量 → 语义 token → CSS 变量 → 组件」的四级依赖图，变更某变量时沿图正向传播得到全部影响。
- 用 BFS 遍历下游节点，收集 CSS 变量与组件清单，去重。
- 输出变更报告：变量、受影响 token、CSS 变量、组件，供精准回归。
- 追问：循环引用（token 互相引用）如何防死循环？（答：visited 集合，BFS 天然防环）

```javascript
function buildReverse(graph) {
  const rev = new Map();
  for (const [from, tos] of graph) for (const to of tos) {
    if (!rev.has(to)) rev.set(to, new Set()); rev.get(to).add(from);
  }
  return rev;
}
function impact(changedVar, graph) {
  const rev = buildReverse(graph), seen = new Set([changedVar]), queue = [changedVar];
  const cssVars = new Set(), comps = new Set();
  while (queue.length) {
    const cur = queue.shift();
    for (const next of rev.get(cur) || []) {
      if (seen.has(next)) continue; seen.add(next); queue.push(next);
      if (next.startsWith('--')) cssVars.add(next);
      if (next.startsWith('ds-')) comps.add(next);
    }
  }
  return { cssVars: [...cssVars], components: [...comps] };
}
```

**评分点**：
- 四级依赖图构建
- BFS 正向传播 + visited 防环
- CSS 变量与组件清单去重
- 变更报告可回归
