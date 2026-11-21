---
title: [CSS-205] Paint Worklet 是什么，自绘背景怎么做
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-205：Paint Worklet 是什么，自绘背景怎么做

**答**：
- Paint Worklet：注册一个 JS「画笔函数」，CSS 里 `background: paint(name)` 直接调用，参数通过 CSS 自定义属性传入
- 流程：`CSS.paintWorklet.addModule('paint.js')` 注册 → worklet 内 `registerPaint` → CSS 引用
- 优势：绘制逻辑响应式（自定义属性变化自动重绘）、矢量清晰、运行在渲染进程（不阻塞主线程）
- 典型场景：斜切背景、彩带粒子、复杂边框、动态网格线——以前要 canvas/伪元素 hack 的效果
- 兼容：Chromium 系与 Safari 16.4+ 支持，Firefox 未支持；必须降级处理

```javascript
// paint.js
registerPaint('confetti', class {
  static get inputProperties() { return ['--confetti-color']; }
  paint(ctx, size, props) {
    ctx.fillStyle = props.get('--confetti-color').toString() || 'gold';
    for (let i = 0; i < 30; i++) {
      ctx.fillRect(Math.random() * size.width, Math.random() * size.height, 3, 8);
    }
  }
});
// main.js
CSS.paintWorklet.addModule('/paint.js');
```
```css
.banner { background: paint(confetti); --confetti-color: gold; }
```
