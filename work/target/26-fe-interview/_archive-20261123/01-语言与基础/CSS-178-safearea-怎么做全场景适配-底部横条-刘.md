---
title: [CSS-178] safe-area 怎么做全场景适配（底部横条、刘海、横屏）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-178：safe-area 怎么做全场景适配（底部横条、刘海、横屏）？

**答**：
- 前提：meta viewport 加 `viewport-fit=cover`，页面才允许延伸进刘海与底部横条区域，env() 才有非零值。
- 四个方向：`safe-area-inset-top/bottom/left/right`，用 `calc(常量 + env(...))` 叠加到 padding 上。
- 降级：`max(12px, env(safe-area-inset-bottom))` 同时满足“无刘海机型保底 12px”与“有刘海取更大值”，老内核 env 解析失败时整条声明失效，需要再写一行兜底。
- 场景映射：底部 TabBar 用 bottom、顶部 banner 用 top、横屏全屏视频用 left/right。

```css
/* 前提：<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"> */

/* 底部 TabBar：避开 Home Indicator */
.tabbar {
  position: fixed;
  left: 0; right: 0; bottom: 0;
  padding-bottom: 12px;
  padding-bottom: max(12px, env(safe-area-inset-bottom));
}

/* 顶部 banner：避开刘海/状态栏 */
.banner {
  padding-top: 8px;
  padding-top: max(8px, env(safe-area-inset-top));
}

/* 横屏全屏：左右两侧避让 */
.landscape-stage {
  padding-left: max(16px, env(safe-area-inset-left));
  padding-right: max(16px, env(safe-area-inset-right));
}

/* 老内核兜底：max() 整条失效时回退到上一行常量声明 */
```

## 二十九、CSS 与 JS 协作
