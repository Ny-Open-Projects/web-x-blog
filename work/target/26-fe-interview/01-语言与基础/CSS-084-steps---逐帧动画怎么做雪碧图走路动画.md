---
title: [CSS-084] steps() 逐帧动画怎么做雪碧图走路动画？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-084：steps() 逐帧动画怎么做雪碧图走路动画？

**答**：
- `steps(n)` 把一段动画切成 n 个跳变帧，帧与帧之间无过渡，是逐帧动画的本质。
- 经典应用：雪碧图 + `background-position` 平移 + steps，实现人物走路/加载角色动画。
- 计算要点：8 帧雪碧图共 8 个展示位置（0 到 -700px，帧宽 100px），用 `steps(7)` 走完 7 次跳变正好停住。
- `steps(n, jump-start/jump-end)` 决定跳变发生在区间头还是尾；`jump-none` 两端都不跳。
- `animation-iteration-count: infinite` 循环，`infinite alternate` 可做往返帧。

```css
/* 雪碧图：横向 8 帧，每帧 100px，总宽 800px */
.walker {
  width: 100px; height: 120px;
  background: url("/sprites/walk.png") 0 0 / 800px 120px no-repeat;
  animation: walk 0.8s steps(7) infinite;  /* 7 次跳变覆盖 8 个位置 */
}
@keyframes walk {
  from { background-position: 0 0; }
  to   { background-position: -700px 0; }  /* -100px * 7 = 第 8 帧位置 */
}

/* 停止时定在最后一帧：加 fill-mode 并去掉 infinite，或用 paused 类 */
.walker.paused { animation-play-state: paused; }
```
