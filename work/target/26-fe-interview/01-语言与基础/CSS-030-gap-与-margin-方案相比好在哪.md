---
title: [CSS-030] gap 与 margin 方案相比好在哪？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-030：gap 与 margin 方案相比好在哪？

**答**：
- `row-gap/column-gap`（或简写 gap）在轨道与项目之间产生固定间距，首尾不产生多余空白。
- 用 margin 实现同样效果需要 `nth-child` 去边距或负 margin 技巧，代码更脆弱。
- flex 与 grid 都支持 gap，多行换行场景下不用处理行尾对齐问题。
- gap 参与容器尺寸计算，配合 fr 与 auto-fill 时结果精确。

```css
/* margin 方案的繁琐 */
.list-margin { display: flex; flex-wrap: wrap; margin: -8px; }
.list-margin .item { margin: 8px; width: calc(25% - 16px); }

/* gap 方案 */
.list-gap {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;            /* 行列间距都为 16 */
}
.list-gap .item { /* 无需任何 margin 计算 */ }
```
