---
title: [WCN-333] SSR 阶段元素渲染错误的隔离与降级？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-333：SSR 阶段元素渲染错误的隔离与降级？
**答**：
- 单个元素渲染错误不应拖垮整页——元素渲染包 try-catch，输出降级片段 + 错误标记。
- 降级片段：skeleton/静态替代（带 data-error 属性，客户端可重试）。
- 错误上报：SSR 错误结构化（tag/props 摘要/错误码）——按元素聚合监控。
- 重试：客户端水合时发现 data-error → 重新渲染（可能已恢复）。

```javascript
function safeRenderDSD(props) {
  try { return renderDSD(props); }
  catch (e) {
    reportSSRError({ tag: 'ds-chart', code: classify(e) });
    return `<ds-chart data-error="ssr-render"><div class="skeleton"></div></ds-chart>`;
  }
}
r
```
