---
title: [CSS-150] grid 的 justify/align/place 六件套各自管什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-150：grid 的 justify/align/place 六件套各自管什么？

**答**：
- 双轴两层：`justify-*` 管 inline（水平）轴，`align-*` 管 block（垂直）轴；`place-*` 是两者简写（先 align 后 justify）。
- 容器级 `justify-content/align-content`：分配“轨道整体”在容器内的多余空间。
- 项目级 `justify-self/align-self`：分配“项目”在所处网格区域内的空间；简写 `place-self`。
- 记忆法：content 分给轨道、items 分给项目；与 flex 的差别是 grid 独有 `justify-items/justify-self`（flex 只有 align-self，没有 inline 轴的单项对齐）。

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 100px);  /* 轨道总宽 300px */
  grid-template-rows: 80px;
  height: 400px;
  justify-content: center;  /* 整组轨道在容器内水平居中 */
  align-content: center;    /* 轨道垂直居中 */
  place-content: center;    /* 上面两行的简写 */
  gap: 8px;
}
.cell {
  justify-self: center;  /* 项目在所在区域内水平居中 */
  align-self: end;       /* 项目贴区域底部 */
  /* place-self: end center; 先 align 后 justify 的简写 */
}
/* 全部项目统一设置等价于容器上写 align-items / justify-items */
.grid-uniform { align-items: center; justify-items: center; }
```
