---
title: [CSS-284] Containment 与 content-visibility 的差别
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-284：Containment 与 content-visibility 的差别

**答**：
- contain 是「手动声明隔离边界」：告诉浏览器内部变化不外溢，缩小重算范围——始终生效
- content-visibility: auto 是「隔离 + 调度」：containment 之上再加视口裁剪——屏幕外子树完全不渲染，接近时才渲染
- 关系：cv: auto ≈ contain: strict + 浏览器自动开关渲染；contain 是 cv 的地基
- 选用决策：组件恒可见但常更新 → contain（缩小失效范围）；长列表/长页面 → content-visibility（跳过屏幕外）
- 两者都依赖 contain-intrinsic-size/显式尺寸防滚动条跳动

```css
/* 组件常更新：限界 */
.widget { contain: layout paint; }
/* 长列表：跳过屏幕外 */
.item { content-visibility: auto; contain-intrinsic-size: auto 120px; }
```
