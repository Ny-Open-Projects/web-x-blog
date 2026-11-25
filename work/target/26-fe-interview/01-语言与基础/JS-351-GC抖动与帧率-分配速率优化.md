---
title: [JS-351] GC 抖动与帧率：分配速率优化
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## JS-351：GC 抖动与帧率：分配速率优化

**答**：
- GC 抖动机制：渲染循环里高频分配临时对象 → 新生代快速填满 → 频繁 minor GC（每次几 ms）→ 帧率抖动「卡卡的感觉」——优化核心是降低分配速率（allocations/sec）
- 高分配热点清单：循环里创建对象/数组/闭包、字符串模板拼接、数组方法链（map/filter/slice 各产生新数组）、解构与展开（...args）
- 优化手段：对象池（复用实例）、循环外提（不变量移出循环）、就地修改（arr[i] = 而不是 map）、复用临时 buffer（TypedArray 复用）、避免闭包创建（循环内定义函数）
- 量化工具：DevTools Memory 的 allocation instrumentation（按函数看分配热点）；Performance 面板看 GC 频率与帧分布
- 平衡原则：优化分配在「每帧执行的热路径」（游戏循环/动画），冷路径（初始化/事件处理）不必过度优化牺牲可读性

```javascript
// 反模式: 每帧分配
function tick() {
  const pts = points.map(p => ({ x: p.x * 2, y: p.y * 2 }));   // 每帧新对象数组
  draw(pts);
  requestAnimationFrame(tick);
}
// 正解: 复用缓冲
const buf = points.map(p => ({ x: 0, y: 0 }));   // 一次性分配
function tick() {
  for (let i = 0; i < points.length; i++) {      // 就地更新
    buf[i].x = points[i].x * 2; buf[i].y = points[i].y * 2;
  }
  draw(buf);
  requestAnimationFrame(tick);
}
```
