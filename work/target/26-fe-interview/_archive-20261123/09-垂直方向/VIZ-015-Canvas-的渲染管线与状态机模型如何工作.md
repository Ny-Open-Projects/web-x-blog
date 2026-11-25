---
title: [VIZ-015] Canvas 的渲染管线与"状态机"模型如何工作？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-015：Canvas 的渲染管线与"状态机"模型如何工作？
**答**：Canvas 是立即模式（immediate mode）：每帧重画全部内容，浏览器不保留图形对象，只有一张位图。其上下文是**状态机**——fillStyle、strokeStyle、lineWidth、font、globalAlpha、变换矩阵都是全局状态，`save()` 压栈、`restore()` 出栈。绘制调用顺序即绘制结果（后画的盖前画的）。工程意义：状态切换本身有开销（同类图元应合并填充），忘记 restore 会让状态"泄漏"影响后续绘制，封装 withState 是常见实践。

```javascript
const ctx = document.querySelector('canvas').getContext('2d');
// Canvas 是立即模式 + 状态机：fillStyle/lineWidth/font/transform 都是全局状态
function withState(c, patch, draw) {
  c.save();                 // 当前状态压栈
  Object.assign(c, patch);  // 局部修改
  draw(c);
  c.restore();              // 弹栈还原，避免状态泄漏到后续绘制
}
withState(ctx, { fillStyle: 'red', lineWidth: 3 }, c => c.fillRect(10, 10, 50, 50));
withState(ctx, { fillStyle: 'blue' }, c => c.fillRect(80, 10, 50, 50));
// 优化点：同类图元合并设置状态——先统一 fillStyle 画完所有红点，再切蓝色，减少状态切换
```
