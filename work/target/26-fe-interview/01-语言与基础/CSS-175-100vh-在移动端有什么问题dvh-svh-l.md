---
title: [CSS-175] 100vh 在移动端有什么问题？dvh/svh/lvh 怎么选？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-175：100vh 在移动端有什么问题？dvh/svh/lvh 怎么选？

**答**：
- 问题：iOS Safari 的 100vh 按“地址栏收起后的最大视口”计算，地址栏展开时底部被裁掉一截。
- `svh`（small）：地址栏展开时的最小视口，任何时刻都完整可见——适合 hero 区、首屏。
- `lvh`（large）：地址栏收起后的最大视口，滚动中被裁——适合背景图/视频等不怕裁切的场景。
- `dvh`（dynamic）：随地址栏实时变化，最精确但滚动中会抖动，注意配 transition 或避免贴底元素。
- 兼容写法：先写 100vh 再写新单位覆盖，老内核自动回退。

```css
/* 首屏内容：永远完整可见，选 svh */
.hero {
  height: 100vh;
  height: 100svh;   /* 地址栏展开时的最小高度 */
}
/* 全屏背景：允许被地址栏裁切，选 lvh，无跳动 */
.bg-cover {
  height: 100vh;
  height: 100lvh;
  background: url(bg.jpg) center / cover;
}
/* 沉浸式布局：跟随地址栏动态变化，选 dvh */
.immersive {
  height: 100vh;
  height: 100dvh;
  display: flex;
  flex-direction: column;
}
.immersive .foot { margin-top: auto; }  /* 贴底元素注意 dvh 抖动 */
/* 老内核：仅支持第一行 100vh，回退为旧有行为 */
```
