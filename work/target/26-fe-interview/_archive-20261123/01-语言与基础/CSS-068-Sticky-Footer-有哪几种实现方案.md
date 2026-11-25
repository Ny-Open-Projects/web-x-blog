---
title: [CSS-068] Sticky Footer 有哪几种实现方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-068：Sticky Footer 有哪几种实现方案？

**答**：
- 目标：内容不足一屏时 footer 贴底，内容超屏时 footer 正常跟随。
- Flex 方案：容器 `min-height: 100dvh`，主内容 `flex: 1` 撑开剩余空间。
- Grid 方案：`grid-template-rows: auto 1fr auto`，语义更直观。
- 用 `dvh` 替代 `vh` 规避 iOS 键盘弹出时视口变化导致的跳动。
- 老式 `calc(100vh - footer高度)` 硬编码方案已不推荐。

```css
/* 方案一：Flex */
.layout-flex {
  display: flex; flex-direction: column;
  min-height: 100dvh;
}
.layout-flex > main { flex: 1; }

/* 方案二：Grid */
.layout-grid {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100dvh;
}

/* footer 无需任何特殊样式，自然贴底或跟随 */
footer { padding: 16px; background: var(--bg-sunken); }
```
