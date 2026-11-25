---
title: [CSS-144] writing-mode 下 flex 的主轴方向怎么变？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-144：writing-mode 下 flex 的主轴方向怎么变？

**答**：
- flex 的 row/column 是**逻辑方向**：`writing-mode: vertical-rl` 下主轴变成纵向、交叉轴变成横向，gap/对齐全部跟着逻辑轴走。
- vertical-rl 与 vertical-lr 只是行块堆叠方向相反（右起 vs 左起），不影响 flex 轴定义。
- 子元素可单独切回 `writing-mode: horizontal-tb` 做“竖排版式里嵌横排”（如竖排海报里的英文数字）。
- 兼容注意：老 Safari 对 vertical writing-mode 的 flex 支持有缺陷，竖排布局优先用 grid 验证。

```css
.poster { writing-mode: vertical-rl; }  /* 整体竖排，从右往左 */

/* 竖排容器里的 flex：主轴纵向排列，gap 沿纵向 */
.v-layout {
  display: flex;
  writing-mode: vertical-rl;
  gap: 24px;
  height: 300px;
}
.v-layout .col { flex: 1; } /* 每列沿交叉轴（横向）等分 */

/* 竖排版式里嵌回横排：数字/英文更易读 */
.v-layout .num {
  writing-mode: horizontal-tb;
  unicode-bidi: plaintext;
}
```
