---
title: [WCN-988] 可访问性 + 性能 + SSR 三方权衡：加 a11y 审计和 ARIA 会不会拖慢首屏
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-988：可访问性 + 性能 + SSR 三方权衡：加 a11y 审计和 ARIA 会不会拖慢首屏

**答**：
- 结论先行：合理的 a11y 几乎不拖慢首屏——ARIA 是 HTML 属性、语义标签是原生能力，成本主要在「运行时审计脚本」和「过度动态 ARIA」，把它们移出关键路径即可。
- 成本拆解：SSR 输出 ARIA 是零运行时成本（服务端算好）；a11y 自动审计应放 CI 或异步采样，不要在首屏主线程跑 axe。
- 真会拖慢的情况：大量 aria-live 频繁播报、动态计算 aria 值导致频繁重排、审计库同步阻塞——这些要节流/异步化。
- 正向收益：语义标签利于 SEO 与 LCP（结构化内容），焦点管理与键盘可达提升可用性，a11y 与性能并非零和。
- 追问钩子：面试官问「怎么向老板证明 a11y 不亏」——答：用数据——审计放 CI 不影响 LCP 指标，同时合规避免法律风险、覆盖更广用户，ROI 正面。

```javascript
// a11y 审计异步化，不阻塞首屏
function deferA11yAudit() {
  if ('requestIdleCallback' in window) {
    requestIdleCallback(() => import('axe-core').then(axe => axe.run(document)));
  } else {
    setTimeout(() => import('axe-core').then(axe => axe.run(document)), 2000);
  }
}
window.addEventListener('load', deferA11yAudit); // 首屏完成后才审计
// ARIA 在 SSR 阶段已输出，运行时零成本
```
