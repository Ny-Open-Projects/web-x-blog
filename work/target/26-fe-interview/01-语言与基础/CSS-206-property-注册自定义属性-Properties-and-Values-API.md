---
title: [CSS-206] @property 注册自定义属性（Properties and Values API）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-206：@property 注册自定义属性

**答**：
- 普通自定义属性（--var）是「无类型的字符串」，不能过渡/动画；@property 给它注册类型（syntax）后浏览器可插值计算
- 三个必填：syntax（类型如 `<angle>` `<color>` `<length>`）、initial-value、inherits
- 立刻解锁的能力：渐变角度动画、颜色过渡、数字滚动——以前必须 JS 的动画
- JS 侧 API：`CSS.registerProperty()` 等价；读取用 getComputedStyle
- 兼容好（全主流已支持），是 Houdini 里最实用的一块，性价比最高

```css
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
.spinner {
  background: conic-gradient(from var(--angle), #4285f4, transparent);
  animation: spin 2s linear infinite;
}
@keyframes spin { to { --angle: 360deg; } } /* 渐变角度动画，纯 CSS */
```
