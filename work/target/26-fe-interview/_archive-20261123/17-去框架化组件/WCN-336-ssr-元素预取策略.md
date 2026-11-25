---
title: [WCN-336] 元素 chunk 的预取策略（链接悬停/视口/路由预测）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-336：元素 chunk 的预取策略（链接悬停/视口/路由预测）？
**答**：
- 悬停预取：hover 200ms 后 prefetch 目标页元素 chunk（最高置信）。
- 视口预取：懒注册元素进入视口前 200px 预取。
- 路由预测：高频跳转路径预热（统计驱动 topN）。
- 成本：预取带宽 vs 命中率——预算上限（每页面预取 ≤ 5 chunk），低价值不预取。

```javascript
link.addEventListener('mouseenter', () => {
  setTimeout(() => prefetch('/chunks/goods-card.js'), 200);
}, { once: true });
r
```
