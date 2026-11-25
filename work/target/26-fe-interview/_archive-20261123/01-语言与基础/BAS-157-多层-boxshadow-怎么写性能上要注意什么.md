---
title: [BAS-157] 多层 box-shadow 怎么写？性能上要注意什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-157：多层 box-shadow 怎么写？性能上要注意什么？
**答**：
- 多层阴影逗号分隔、按"近小远大"叠加，可模拟真实的柔光投影。
- box-shadow 变化不触发重排，但大模糊半径会扩大绘制区域，动画阴影会拖慢 paint。
- 优化：需要"阴影动起来"的效果优先用伪元素 + opacity 过渡，或 transform 让整个层走合成。

```css
.card {
  /* 多层阴影逗号分隔，从近到远叠加出立体感 */
  box-shadow:
    0 1px 2px rgba(0, 0, 0, .08),
    0 4px 8px rgba(0, 0, 0, .12),
    0 16px 32px rgba(0, 0, 0, .16);
}
/* hover 要动阴影时：切 opacity 而不是动 blur，避免重绘开销 */
```
