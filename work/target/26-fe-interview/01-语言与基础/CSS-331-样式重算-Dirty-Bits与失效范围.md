---
title: [CSS-331] 样式重算（Style Recalc）：Dirty Bits 与失效范围
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-331：样式重算（Style Recalc）：Dirty Bits 与失效范围

**答**：
- 样式失效机制：改 class/DOM 后引擎打 dirty 标记，下一帧 style recalc 阶段只重算「失效子树」，已无效化的共享规则跳过——失效范围决定重算成本
- 失效传播根因：选择器带祖先/兄弟方向（`.a .b`、`.a ~ .b`、:has()）时，改动会影响其他元素的匹配 → 失效范围从「自身」扩大到「子树/兄弟链」；只有 `.a`（单元素规则）失效最便宜
- StyleSharing：相同 class/属性/tag 的兄弟元素共享 ComputedStyle，一个被标脏才重算——动态给某个兄弟加 class 会使共享失效，整组重算（列表 hover 场景的性能坑）
- 强制同步布局：JS 里读 offsetTop//getComputedStyle 在「样式已脏未重算」时会触发同步 recalc + layout（layout thrashing 根源）
- 度量：DevTools Performance 的 Recalculate Style 事件，看「Elements Affected」数量；上千元素受影响就要查失效范围问题

```javascript
// 失效范围实验: 只影响子树 vs 兄弟链
parent.classList.add('open');           // 后代选择器匹配 → 子树失效
el.classList.add('active');             // 若存在 .a ~ .b → 兄弟方向失效扩大
// layout thrashing 反例(每轮读写强制同步):
items.forEach(i => i.el.style.height = i.el.offsetHeight + 1 + 'px');
// 正解: 批量读 → 批量写
```
