---
title: [CSS-147] grid 自动放置算法 sparse 和 dense 有什么区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-147：grid 自动放置算法 sparse 和 dense 有什么区别？

**答**：
- 默认 sparse：游标只向前走，遇到放不下的大块就跳过留洞，绝不开倒车——结果 DOM 顺序与位置一致但可能有空洞。
- `dense`：每放一个 item 都从头扫描网格，能塞进之前的空洞就回填——网格更紧凑，但元素位置不再跟随 DOM 顺序。
- dense 的代价：视觉顺序与 DOM/读屏顺序脱节，且布局计算量增大；只适合“卡片大小不一、无强顺序语义”的图库类页面。
- 面试加分：能描述“跨行卡片 + sparse 留洞”的具体复现场景。

```css
/* 复现：第 2 个 item 高度跨 2 行，sparse 下第 3、4 个绕过它，
   第 5 个无法回填第 2 个留下的空洞 */
.grid-sparse {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 80px;
  grid-auto-flow: row;            /* 默认 sparse */
}
.grid-sparse .tall { grid-row: span 2; }

/* dense：后续小卡片回填空洞，网格更满 */
.grid-dense {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 80px;
  grid-auto-flow: row dense;
}
.grid-dense .tall { grid-row: span 2; }
/* 注意：dense 打乱视觉顺序，带顺序语义的列表禁用 */
```
