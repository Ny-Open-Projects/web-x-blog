---
title: [CSS-238] View Transitions：同文档路由动画 SPA 怎么接
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-238：View Transitions：同文档路由动画，SPA 怎么接

**答**：
- 核心 API：`document.startViewTransition(() => 更新DOM)`——浏览器自动截图旧状态、渲染新状态、交叉渐变
- SPA 接入点：路由切换回调里包住 DOM 更新；React/Vue 可在路由 hook 或封装的 navigate 函数中调用
- 元素级动画：给要「跨状态移动」的元素加 `view-transition-name: hero`，新旧同名元素自动做位置/尺寸过渡（列表→详情的共享元素动画）
- 自定义动画：::view-transition-old/new 伪元素上写 CSS 动画替代默认渐变
- 兼容：Chrome 111+；需特性检测降级为直接切换（try/catch 包裹）

```javascript
function navigateWithTransition(render) {
  if (!document.startViewTransition) { render(); return; }
  document.startViewTransition(render);
}
/* 列表项 → 详情封面共享元素 */
.card img { view-transition-name: cover-1; }
.detail img { view-transition-name: cover-1; }
```
