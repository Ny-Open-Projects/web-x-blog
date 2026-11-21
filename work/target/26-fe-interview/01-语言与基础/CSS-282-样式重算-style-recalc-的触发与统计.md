---
title: [CSS-282] 样式重算（style recalc）的触发与统计
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-282：样式重算的触发与统计

**答**：
- 触发源：类/属性变更、DOM 插入删除、伪类状态变化（hover/:has 匹配变化）、媒体查询切换——任何可能影响选择器命中的变化都会「使样式失效」
- :has 与重算：祖先级 :has 扩大失效范围（子变→祖先重查），是现代样式卡顿的新热点
- 统计方法：Performance 面板的 Recalculate Style 事件（看耗时与元素数）；Performance Monitor 的 Styles 面板实时观察
- 优化手段：减少全局性失效（:has 限定范围、避免 body 级 class 切换驱动样式）、动画用合成属性（不触 recalc/layout）、批量 DOM 变更
- 指标：单次 Recalc Style 超过几 ms 且高频出现就要治理

```javascript
// DevTools 性能面板外的粗测
performance.mark('before');
document.body.classList.toggle('theme-dark');
requestAnimationFrame(() => performance.mark('after')); // 下一帧前完成样式+布局
```
