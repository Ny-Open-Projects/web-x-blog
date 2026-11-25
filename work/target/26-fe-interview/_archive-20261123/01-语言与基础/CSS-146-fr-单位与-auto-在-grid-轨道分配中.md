---
title: [CSS-146] fr 单位与 auto 在 grid 轨道分配中是怎么算的？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-146：fr 单位与 auto 在 grid 轨道分配中是怎么算的？

**答**：
- 分配顺序：固定尺寸轨道（px）→ 内容驱动轨道（auto/min-content 等）→ 剩余空间才轮到 fr 按比例瓜分。
- auto 轨道先按内容（max-content）拿自己的份额，fr 只分剩下的；auto 也有 `minmax(auto, 1fr)` 语义参与竞争。
- `1fr` 实际是 `minmax(auto, 1fr)`：内容的最小尺寸会撑破轨道导致溢出；`minmax(0, 1fr)` 才是“严格等分可收缩”。
- 面试答法：先讲三段式分配，再补 minmax(0,1fr) 的溢出坑，基本是标准满分结构。

```css
.grid {
  display: grid;
  grid-template-columns: 100px auto 1fr 2fr;
  width: 900px;
}
/* 分配过程：
   1. 100px 固定轨道先占 100px
   2. auto 轨道按内容取宽（设内容 180px）
   3. 剩余 900 - 100 - 180 = 620px，由 1fr + 2fr = 3 份瓜分
      → 1fr ≈ 206.67px，2fr ≈ 413.33px */

/* 坑：1fr 含 minmax(auto, ...)，超长内容会撑破列 */
.overflow-demo { display: grid; grid-template-columns: 1fr 1fr; }
/* 修正：严格等分且可收缩 */
.fixed { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
```
