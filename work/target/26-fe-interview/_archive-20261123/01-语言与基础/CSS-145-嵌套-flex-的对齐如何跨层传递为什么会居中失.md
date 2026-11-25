---
title: [CSS-145] 嵌套 flex 的对齐如何跨层传递？为什么会“居中失效”？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-145：嵌套 flex 的对齐如何跨层传递？为什么会“居中失效”？

**答**：
- 默认 `align-items: stretch` 让子容器被拉满交叉轴，子容器内部的对齐才有完整空间可用——这是对齐“传递”的隐含前提。
- 陷阱：外层设了 `align-items: center`，子容器高度塌缩为内容高，子容器内的 `height: 100%`、内部 stretch 全部失效。
- 修正思路：需要“外层整体居中 + 内部撑满”时，给子容器 `align-self: stretch`，把居中下沉到子容器内部去做。
- 排查口诀：先看每层的高度来源（stretch 还是内容），再看对齐作用在哪个轴。

```css
.outer { display: flex; height: 300px; background: #f5f5f5; }

/* 正常：默认 stretch，.inner 撑满高度，内部居中有完整空间 */
.inner {
  flex: 1;
  display: flex;
  align-items: center;      /* 内容在自身内部垂直居中 */
  justify-content: center;
}

/* 陷阱：外层 center 让 .inner 塌缩为内容高，
   内部看起来"也居中了"是巧合，一旦内容复杂立刻错位 */
.outer-trap { align-items: center; }

/* 修正：既要外层约束高度，又要内部完整空间 */
.outer-fix { align-items: center; }
.outer-fix .inner { align-self: stretch; } /* 该子项单独撑满 */
```

## 二十四、Grid 深水区
