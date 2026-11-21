---
title: [CSS-069] 九宫格有哪些实现方式？gap 相比老 margin 方案好在哪？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-069：九宫格有哪些实现方式？gap 相比老 margin 方案好在哪？

**答**：
- Grid：`grid-template-columns: repeat(3, 1fr)` + `gap`，最简洁。
- Flex：`flex-wrap: wrap` + 子项宽度 1/3 减 margin，需要 `nth-child(3n)` 去右边距。
- 老 margin 方案的痛点：末行元素去边距要写反直觉的负 margin 容器或复杂 nth 规则。
- `gap` 不作用于边缘，行列间距天然均匀，还支持不等宽 `repeat(3, 1fr 2fr)`。
- 移动端常见 2 列改 3 列，只需重写一个声明。

```css
/* 推荐：Grid + gap */
.grid9 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

/* 对比：Flex + margin 老方案，需要去边距 hack */
.flex9 { display: flex; flex-wrap: wrap; margin: -6px; }
.flex9 > .cell {
  flex: 0 0 calc(33.333% - 12px);
  margin: 6px;
  aspect-ratio: 1;
}
/* 老方案里 3n 去右边距、末行去下边距的规则在 gap 方案中完全消失 */
```
