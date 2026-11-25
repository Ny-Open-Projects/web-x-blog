---
title: [CSS-231] color-mix() 是什么：调色板怎么做
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 设计系统]
type: 面试题
---

## CSS-231：color-mix() 是什么：调色板怎么做

**答**：
- color-mix(in 色彩空间, 颜色A 百分比, 颜色B)：在指定色彩空间（srgb/oklch/…）混合两个颜色
- 典型用途：主色派生悬停色（混黑/混白）、透明度调整（与 transparent 混合替代 rgba）、状态色推导
- 用 oklch 混合明度更均匀（srgb 混出的中间色常发灰）；比例省略默认 50/50
- 与 CSS 变量组合：`color-mix(in oklch, var(--primary) 90%, black)` 一行生成色阶
- 兼容：全主流已支持，可放心生产

```css
:root { --primary: oklch(60% 0.15 250); }
.btn:hover  { background: color-mix(in oklch, var(--primary) 90%, black); }  /* 深 10% */
.btn:active { background: color-mix(in oklch, var(--primary) 80%, black); }
.btn-outline{ color: var(--primary);
  background: color-mix(in srgb, var(--primary) 10%, transparent); } /* 浅底 */
```
