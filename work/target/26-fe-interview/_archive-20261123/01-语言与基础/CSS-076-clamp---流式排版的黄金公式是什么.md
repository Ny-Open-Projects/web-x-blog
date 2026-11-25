---
title: [CSS-076] clamp() 流式排版的黄金公式是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-076：clamp() 流式排版的黄金公式是什么？

**答**：
- `clamp(min, preferred, max)`：首选值随视口线性缩放，被 min/max 夹住。
- 黄金公式：`clamp(rem最小值, rem基础值 + 每px视口斜率 * 1vw, rem最大值)`，斜率 = (max-min) / (最大视口-最小视口)。
- 用 rem 做夹持端可继承用户浏览器字号设置，保住无障碍。
- 标题适合流式缩放；正文建议固定字号，避免可读性波动。
- 在线工具生成系数后 固化进 token，不手算。

```css
/* clamp(2rem, 1rem + 3vw, 3.5rem)：320px 时约 2rem，1280px 时到 3.5rem 封顶 */
:root {
  --fs-display: clamp(2rem, 1rem + 3vw, 3.5rem);
  --fs-h1:      clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem);
  --fs-h2:      clamp(1.25rem, 1rem + 0.8vw, 1.6rem);
}

/* 正文保持固定，只有标题流式 */
h1 { font-size: var(--fs-h1); }
h2 { font-size: var(--fs-h2); }
p  { font-size: 1rem; line-height: 1.75; }
```
