---
title: [MFW-720] 渐进式水合的实现层次
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-720：渐进式水合的实现层次

**答**:
- 渐进式水合的四层实现：1) **框架内建**（React 的 Suspense 边界水合——RSC 流式边界按数据到达水合 RBL-710）；2) ** Islands**（Astro client:visible/idle——水合时机声明化 RBL-538）；3) **选择性水合**（React 18.3 的交互优先——RBL-710 调度器）；4) **自定义调度**（手写水合队列——priority/condition/delay 的自定义策略（RBL-720 层次的自定义版）。
- 各层的适用场景：框架内建 = 通用（RSC 架构默认）；Islands = 内容站（大部分静态+少量交互）；选择性 = 应用型（大量交互组件——按需）；自定义 = 特殊需求（广告延迟/分析后置——精细控制）。
- 水合的度量：TTI（可交互时间）的分解——「HTML 可见 → JS 下载 → 水合完成」的三段（每段的优化策略不同：HTML = SSR、JS = code split、水合 = 优先级调度）。
- 追问钩子：为什么「渐进式水合」的层次选择由「交互密度」决定？——交互密度低（内容站）：Islands（少数交互组件 lazy）；交互密度高（应用）：选择性水合（全页交互组件——调度优先级）；「水合策略 × 交互密度」的匹配：无最优策略只有最优匹配（RBL-620 渲染模式决策树的水合维度）。

```tsx
// 四层渐进水合
// 1) RSC 内建：Suspense 边界自动
// 2) Islands（Astro）
// <Counter client:visible />           ← 视口内才水合
// <Search client:idle />               ← 空闲时
// 3) React 18.3 选择性水合
// React.lazy + Suspense 的交互优先（RBL-710）
// 4) 自定义调度器
const hydrateQueue = [
  { component: 'ChatWidget', condition: () => window.innerWidth > 768, priority: 3 },
  { component: 'Analytics', condition: () => document.readyState === 'complete', priority: 10 },
];
function scheduleHydration(queue) {
  const sorted = queue.sort((a, b) => a.priority - b.priority);
  for (const item of sorted) {
    const check = setInterval(() => {
      if (item.condition()) {
        clearInterval(check);
        import(`./components/${item.component}`).then(mod => mod.mount());
      }
    }, 100);
  }
}
// TTI 分解
// TTI = HTML received + JS downloaded + hydration completed
//     = TTFB + (bundle size / bandwidth) + (hydration work / CPU)
// 每段的优化：SSR + code split + priority scheduling
```
