---
title: [CSS-158] View Transitions API 怎么做页面切换转场？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-158：View Transitions API 怎么做页面切换转场？

**答**：
- 文档级转场：JS 用 `document.startViewTransition(callback)` 包住 DOM 更新，浏览器对旧新状态各拍一张快照，通过 `::view-transition-old(root)` / `new(root)` 交叉过渡。
- 元素级共享转场：新旧页面同一元素标同名 `view-transition-name`，浏览器自动做位置/尺寸/形状插值（列表缩略图 → 详情大图）。
- CSS 只负责定义转场样式，时机由 JS 控制；两者天然分层。
- MPA 也支持（`@view-transition { navigation: auto }`）；name 必须页面内唯一，否则转场跳过。

```css
/* 1. 文档级：自定义默认交叉转场 */
::view-transition-old(root) { animation: vt-out .25s both; }
::view-transition-new(root) { animation: vt-in  .25s both; }
@keyframes vt-out { to { opacity: 0; } }
@keyframes vt-in  { from { opacity: 0; } }

/* 2. 元素级共享转场：列表图与详情图同名，自动插值 */
.card-img   { view-transition-name: hero-img; contain: paint; }
.detail-img { view-transition-name: hero-img; contain: paint; }

/* 3. MPA 跨页面转场（同源） */
@view-transition { navigation: auto; }
/* JS 触发 SPA 转场：
   document.startViewTransition(() => renderDetail(id)); */
```
