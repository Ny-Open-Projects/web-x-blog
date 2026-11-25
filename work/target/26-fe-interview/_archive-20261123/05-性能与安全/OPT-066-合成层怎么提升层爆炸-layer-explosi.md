---
title: [OPT-066] 合成层怎么提升？层爆炸（layer explosion）怎么治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-066：合成层怎么提升？层爆炸（layer explosion）怎么治理？

**答**：
- 元素拥有 3D transform/fixed/opacity 过渡/`will-change` 等条件时被提升为合成层，动画只在 compositor 线程跑，不受主线程阻塞。
- 层爆炸：滥用 `will-change: transform` 或大量固定元素，GPU 内存被层吃光（每层是按面积算的位图），表现为掉帧、闪烁甚至崩溃（移动端大图 + 多层尤其明显）。
- 排查：Layers 面板看层数量与每层内存（`Memory estimate`）；`will-change` 要在动画前加、动画后移除，常驻等于永久占用。
- 治理原则：只提升"真正做动画"的元素；大图先缩小再进层；用 `transform: translateZ(0)` 临时验证后及时撤掉。

```css
/* 一一对应：合成层提升与层爆炸治理 */
/* 正确：仅动画期间提升，配合 JS 在动画结束移除 */
.toast-enter {
  will-change: transform, opacity;  /* 提前告知，避免动画首帧才建层的卡顿 */
  animation: slide-in 0.3s;
}
@keyframes slide-in {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}

/* 反例 1：全局滥用 —— 页面上 500 个卡片每个都建层，GPU 位图爆掉 */
/* .card { will-change: transform; }  <- 删掉 */

/* 反例 2：超大图片整体建层 —— 4000x3000 图的一层就吃约 46MB 内存 */
/* .big-photo { transform: translateZ(0); }  <- 改为缩小解码尺寸（见 OPT-078） */

/* 正确治理 2：滚动容器内的固定表头只提升表头本身，不提升整个容器 */
.table th {
  position: sticky;
  top: 0;
  z-index: 1;
  background: #fff;
}

/* 正确治理 3：backface-visibility 与 transform 提升的检查口 */
.promote-during-anim {
  transform: translateZ(0); /* 仅当确有闪烁/不出层问题时临时用 */
  backface-visibility: hidden;
}
```
