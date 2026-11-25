---
title: [CSS-288] currentColor 与继承的取色链路
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 基础]
type: 面试题
---

## CSS-288：currentColor 与继承的取色链路

**答**：
- currentColor = 元素自身的 color 计算值——border/background/svg fill 等处引用，实现「一处改色，联动多处」
- 继承规则：color 是可继承属性；currentColor 引用的是「本元素计算后的 color」，不是父元素的原始值（子元素覆盖 color 后 currentColor 跟着变）
- 典型场景：按钮边框/图标随文字色统一（hover 只改 color 一处）；分割线颜色继承文字灰度
- 陷阱：currentColor 不能用于「继承父色但自己要不同色」的场景——需要时显式写值或用变量
- 与 CSS 变量的分工：currentColor 是「动态引用」语义，变量是「命名值」语义；图标主题化优先 currentColor

```css
.btn {
  color: #4285f4;
  border: 1px solid currentColor;   /* 边框跟随文字色 */
  svg { fill: currentColor; }       /* 图标同步 */
}
.btn:hover { color: #1a73e8; }      /* 边框/图标自动联动 */
```
