---
title: [CSS-351] Houdini：CSS 可编程化的引擎扩展点
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-351：Houdini：CSS 可编程化的引擎扩展点

**答**：
- 四大扩展点：CSS Paint API（registerPaint 自定义 background/border-image 绘制）、Properties & Values（@property 注册类型化变量，可动画）、Layout API（自定义布局算法，支持度差）、Parser/Typed OM（结构化操作 CSS）
- Paint API 实战：复杂背景（棋盘格/斜纹/进度环）从「多层渐变拼」变「一段 JS 绘制」——绘制在 paint 阶段（paint worklet 线程），不进主线程；输入参数通过 inputArguments 与 CSS 变量传入，变量变化触发重绘
- @property 的价值：变量从「字符串」变「有类型值」——number/color/length 可参与 transition/animation、calc 运算；这是纯 CSS 实现进度条动画的基础（CSS-334 已提）
- 支持度现实：Paint/@property 广泛可用，Layout API 仅 Chromium——生产只在 paint 与 property 上用，其余留概念
- 降级与注册时机：worklet 注册是异步的，CSS.paintWorklet.addModule 后元素才有效——首屏关键视觉别依赖 Paint API（有闪烁窗口）

```javascript
// paint-worklet.js
registerPaint('ring', class {
  static get inputArguments() { return ['<percentage>']; }
  paint(ctx, geom, props, args) {
    const p = parseFloat(args[0]) / 100;
    ctx.strokeStyle = '#ddd'; ctx.lineWidth = 8;
    ctx.beginPath(); ctx.arc(geom.width/2, geom.height/2, geom.width/2 - 8, 0, Math.PI*2); ctx.stroke();
    ctx.strokeStyle = '#1677ff';
    ctx.beginPath();
    ctx.arc(geom.width/2, geom.height/2, geom.width/2 - 8, -Math.PI/2, -Math.PI/2 + Math.PI*2*p);
    ctx.stroke();
  }
});
CSS.paintWorklet.addModule('/paint-worklet.js');
```

```css
.ring { background: paint(ring, var(--p)); transition: --p .3s; }
```
