---
title: [BAS-154] min()、max()、clamp() 有什么实际应用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-154：min()、max()、clamp() 有什么实际应用？
**答**：
- min(a, b) 取较小值：`width: min(300px, 100%)` 表示"最多 300px，窄屏时贴满"。
- max(a, b) 取较大值：保证间距或尺寸的下限。
- clamp(min, 理想值, max)：三者合一，最典型是流式排版——字号随视口缩放但被夹在两端之间。

```css
h1 { font-size: clamp(24px, 5vw, 48px); }  /* 视口缩放但夹在 24~48px */
.sidebar { width: min(300px, 100%); }      /* 最多 300px，小屏贴满 */
.gutter { margin: max(16px, 4vh); }        /* 间距保底 16px */
```
