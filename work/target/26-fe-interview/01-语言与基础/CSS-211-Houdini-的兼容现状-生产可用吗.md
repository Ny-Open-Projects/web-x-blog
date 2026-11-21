---
title: [CSS-211] Houdini 的兼容现状，生产可用吗
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-211：Houdini 的兼容现状，生产可用吗

**答**：
- 分模块看：@property（全主流，可生产）> Typed OM（Chromium 全、Safari 部分）> Paint Worklet（Chromium+Safari 16.4）> Layout/Parser Worklet（Chromium 实验或无）
- 生产策略：@property 类效果放心用（降级时只是不动画，不破功能）；Paint Worklet 要给静态 fallback background（多背景叠加）
- 降级模式：`CSS.paintWorklet ? paint(x) : 'fallback'` 或 @supports 检测 `background: paint(x)` 支持性
- 决策框架：装饰性效果用（锦上添花），功能性布局别用（Layout 未成熟）
- 面试话术：Houdini 不是「一个东西」，逐模块评估兼容性才是正确回答

```css
.fancy {
  /* 多背景叠加做降级：支持 paint 时覆盖纯色 */
  background: linear-gradient(#eee, #eee); /* fallback */
}
@supports (background: paint(confetti)) {
  .fancy { background: paint(confetti); }
}
```
