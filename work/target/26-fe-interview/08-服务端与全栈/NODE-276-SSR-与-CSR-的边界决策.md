---
title: [NODE-276] SSR 与 CSR 的边界决策？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-276：SSR 与 CSR 的边界决策？
**答**:
- 决策三输入：SEO 需求（必须 SSR/SSG）、首屏性能要求（TTI 敏感页面 SSR）、服务成本（SSR 需要常驻服务+容量）。
- 混合策略：营销页/文档 SSG，列表/详情 SSR/ISR，重交互应用（编辑器/工作台）CSR + 骨架——同站多策略（ARC-060 渲染矩阵）。
- 成本核算：SSR 实例数 ≈ QPS × 渲染耗时 P95 / 实例并发——大促前容量评估（ARC-260）。
- 收敛原则：能用静态解决的绝不上 SSR；SSR 页面尽量流式（慢块不影响 TTFB）。

```javascript
// 渲染策略决策表
const strategy = (page) => {
  if (page.needsSeo && page.contentFresh === 'static') return 'SSG';
  if (page.needsSeo && page.contentFresh === 'periodic') return 'ISR';
  if (page.needsSeo && page.personalized) return 'SSR-stream';
  return 'CSR';                                    // 内部工具/编辑器
};
// 成本：SSR 实例数 = QPS × 0.2s(P95) / 2(并发) → 1000 QPS ≈ 100 实例（SSG = 0）
```
