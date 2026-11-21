---
title: [CSS-032] Grid 中的对齐属性 place-items、place-content、place-self 区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-032：Grid 中的对齐属性 place-items、place-content、place-self 区别？

**答**：
- `place-items`：容器属性，设置所有项目在其格子内的对齐（align-items + justify-items 简写）。
- `place-content`：容器属性，当容器比所有轨道总和大时，控制整个“轨道组”的对齐。
- `place-self`：项目属性，单个项目在所属格子内的对齐。
- 记忆：items 管“项目在格子里”，content 管“格子整体在容器里”，self 管“单个项目”。

```css
.board {
  display: grid;
  grid-template-columns: repeat(3, 120px);
  width: 600px;
  height: 400px;
  place-content: center;      /* 整组轨道在容器内居中 */
  place-items: center;        /* 每个项目在自己格子内居中 */
}
.board .special { place-self: start end; } /* 垂直 start，水平 end */
```
