---
title: [PER-978] 同文档视图过渡（View Transitions）的性能代价与降级
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-978：同文档视图过渡（View Transitions）的性能代价与降级

**答**：
- 原理：startViewTransition 快照新旧状态为两个伪元素树，动画由合成器驱动；快照成本与页面复杂度相关。
- 代价：大页面快照占内存、旧状态冻结期间交互不可用；动画属性应仅限 transform/opacity。
- 降级策略：不支持时直接切换 DOM（渐进增强）；低端机跳过过渡（提前探测 + 用户偏好 prefers-reduced-motion）。
- 深水：过渡期间的渲染阻塞会让 INP 变差，切换动画应短（<300ms）且不覆盖高频交互区域。

```javascript
function safeTransition(update) {
  const lowEnd = navigator.deviceMemory && navigator.deviceMemory <= 2;
  if (!document.startViewTransition || lowEnd ||
      matchMedia('(prefers-reduced-motion: reduce)').matches) {
    update(); return;                     // 直接切换
  }
  document.startViewTransition(update);   // 平滑过渡
}
// 使用：safeTransition(() => router.render(next));
```
