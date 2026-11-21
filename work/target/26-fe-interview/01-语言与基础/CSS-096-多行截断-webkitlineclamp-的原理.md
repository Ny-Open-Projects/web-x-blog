---
title: [CSS-096] 多行截断 -webkit-line-clamp 的原理与替代方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-096：多行截断 -webkit-line-clamp 的原理与替代方案？

**答**：
- 标准写法三件套：`display: -webkit-box` + `-webkit-box-orient: vertical` + `-webkit-line-clamp: N`，配合 `overflow: hidden`。
- 原理：webkit 私有的旧版弹性盒模型按行盒裁剪并追加省略号，现已写入规范成为正式标准。
- 替代一：`max-height = 行高 × N` + overflow hidden（无省略号）；替代二：::after 渐隐；替代三：JS 按字符测量。
- 单行截断仍是 `white-space: nowrap + text-overflow: ellipsis + overflow: hidden` 三件套。
- clamp 区域若参与动画，注意旧内核渲染层重建的开销。

```css
/* 多行截断（现代浏览器直接可用，已是标准） */
.clamp-2 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}

/* 替代：max-height 方案，无省略号但无私有前缀 */
.clamp-max {
  overflow: hidden;
  max-height: calc(1.6em * 3); /* 行高 1.6 × 3 行 */
}

/* 单行截断 */
.ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```
