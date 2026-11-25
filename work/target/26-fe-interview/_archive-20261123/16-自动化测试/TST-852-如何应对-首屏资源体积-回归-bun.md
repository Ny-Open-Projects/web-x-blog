---
title: [TST-852] 如何应对「首屏资源体积」回归（bundle 体积门禁的深水问题）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-852：如何应对「首屏资源体积」回归（bundle 体积门禁的深水问题）？
**答**：
- 结论：体积门禁要「按入口/路由拆维度 + gzip/brotli 口径 + 增量归因」——只看总 bundle 会漏掉「总量没变但首屏变大」的退化。
- 拆维度：按路由 chunk 分别设预算，首屏关键 chunk 重点盯；区分初始加载与懒加载资源。
- 口径统一：用压缩后体积（gzip/brotli）对比，明确是否含 source map，避免口径不一致产生假波动。
- 增量归因：体积上涨时定位是哪个依赖/模块引入的（bundle analyzer / size-limit diff），让 PR 作者看到影响。
- 追问钩子：某 PR 只加了一个「小」第三方库，体积却涨了 200KB，你如何定位原因？

```javascript
// 体积门禁：按 chunk 设预算 + 增量对比
const budgets = { 'main': 180, 'vendor': 150, 'route-product': 80 }; // KB (gzip)
function checkBundleSize(sizes) {
  return Object.entries(budgets).map(([chunk, budget]) => ({
    chunk, budget, actual: sizes[chunk] ?? 0,
    pass: (sizes[chunk] ?? 0) <= budget,
    delta: (sizes[chunk] ?? 0) - budget,
  }));
}
console.log(checkBundleSize({ main: 175, vendor: 160, 'route-product': 60 }));
// vendor +10KB 超标，main 接近上限需警惕
```
