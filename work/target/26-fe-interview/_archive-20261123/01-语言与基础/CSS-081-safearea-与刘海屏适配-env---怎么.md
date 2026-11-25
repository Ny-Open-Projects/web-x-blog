---
title: [CSS-081] safe-area 与刘海屏适配，env() 怎么用全？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-081：safe-area 与刘海屏适配，env() 怎么用全？

**答**：
- 刘海/圆角/Home 条会遮挡内容，`env(safe-area-inset-*)` 给出四边安全区距离。
- 前提：viewport meta 加 `viewport-fit=cover`，页面铺满后才有安全区可言。
- 四个值：`top / bottom / left / right`，常用于 fixed 顶栏、底部 TabBar、全屏弹窗。
- 用 `max()` 包裹实现"有安全区就加上，没有就用默认值"的兜底；老设备 env 不支持时回退值生效。
- 配合 `@supports (padding: max(0px))` 可进一步收束旧浏览器行为。

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
/* 顶部导航：避开刘海 */
.app-header {
  position: fixed; inset-inline: 0; top: 0;
  padding-top: max(12px, env(safe-area-inset-top));
}

/* 底部 TabBar：避开 Home 条 */
.tabbar {
  padding-bottom: max(8px, env(safe-area-inset-bottom));
}

/* 横屏时左右也要避让 */
.fullscreen-dialog {
  padding-inline: max(16px, env(safe-area-inset-left), env(safe-area-inset-right));
}
```

## 十五、动画工程
