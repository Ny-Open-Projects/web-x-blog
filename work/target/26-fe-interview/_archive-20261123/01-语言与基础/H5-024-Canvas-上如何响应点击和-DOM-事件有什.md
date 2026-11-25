---
title: [H5-024] Canvas 上如何响应点击？和 DOM 事件有什么不同？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-024：Canvas 上如何响应点击？和 DOM 事件有什么不同？
**答**：
- Canvas 是一整块位图，内部图形不是 DOM，事件只落在 canvas 元素上，需要自己算"点是否在图形内"。
- 简单形状用几何计算（圆用距离、矩形用范围）；复杂 path 用 `ctx.isPointInPath(x, y)`（注意坐标要乘 DPR 换算）。
- 交互多的场景优先 SVG（每个图形都是元素，事件原生）或把元素缓存为"命中表"（hit map，给每个对象唯一颜色渲染到隐藏 canvas 再取色）。
- 拖拽要监听 pointer 事件系列，兼容鼠标与触摸。

```html
<canvas id="hit" width="300" height="200" style="width:300px;height:200px;"></canvas>

<script>
  const canvas = document.getElementById('hit');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;

  const circle = { x: 150, y: 100, r: 50 };
  ctx.beginPath();
  ctx.arc(circle.x, circle.y, circle.r, 0, Math.PI * 2);
  ctx.fill();

  canvas.addEventListener('pointerdown', (e) => {
    // 屏幕坐标换算成画布逻辑坐标
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // 方式一：isPointInPath，path 与绘制时保持一致
    ctx.beginPath();
    ctx.arc(circle.x, circle.y, circle.r, 0, Math.PI * 2);
    const inside = ctx.isPointInPath(x * dpr, y * dpr);

    // 方式二：几何计算（圆专用，更省）
    const dist = Math.hypot(x - circle.x, y - circle.y);
    console.log(inside, dist <= circle.r); // 两种判定结果一致
  });
</script>
```

## 五、SVG
