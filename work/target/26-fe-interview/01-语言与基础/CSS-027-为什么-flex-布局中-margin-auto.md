---
title: [CSS-027] 为什么 flex 布局中 margin: auto 可以实现居中？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-027：为什么 flex 布局中 margin: auto 可以实现居中？

**答**：
- flex 容器内 `margin: auto` 会吸收该方向上的**全部剩余空间**，优先级高于 justify-content/align-items 的分配。
- 由此可得多种局部对齐技巧：`margin-left: auto` 把项目推到最右。
- 相比 absolute + transform 居中，它不脱离文档流、无需已知尺寸。
- 多个 auto margin 时剩余空间被均分，可实现非对称排版。

```css
.modal-row {
  display: flex;
  height: 300px;
}
.modal-row .box {
  margin: auto;      /* 水平 + 垂直同时居中 */
  width: 200px;
}

/* 技巧：最后一项推到最右 */
.toolbar { display: flex; gap: 8px; }
.toolbar .spacer-free { margin-left: auto; }
```

## 五、Grid 布局
