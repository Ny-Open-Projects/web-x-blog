---
title: [CSS-275] accent-color 与原生表单控件着色
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 表单]
type: 面试题
---

## CSS-275：accent-color 与原生表单控件着色

**答**：
- accent-color：一行给 checkbox/radio/range/progress 的「强调色」上品牌色——不用再自绘控件
- 价值：自绘 checkbox 的无障碍成本高（焦点/键盘/读屏），accent-color 保留原生控件的可访问性
- 配合 color-scheme：暗色模式下 accent-color 与控件底色联动正确
- 深度定制仍需自绘（appearance: none + 伪元素）——区分「换色」与「换形态」两个层级
- 兼容：全主流，可生产

```css
:root { --brand: #4285f4; }
input[type='checkbox'], input[type='radio'], input[type='range'], progress {
  accent-color: var(--brand);
}
/* 需要完全自定义形态时才走 appearance: none */
```
