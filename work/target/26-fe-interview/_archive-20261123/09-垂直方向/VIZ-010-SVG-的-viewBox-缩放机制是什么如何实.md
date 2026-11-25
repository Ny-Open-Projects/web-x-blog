---
title: [VIZ-010] SVG 的 viewBox 缩放机制是什么？如何实现滚轮以鼠标为锚点缩放？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-010：SVG 的 viewBox 缩放机制是什么？如何实现滚轮以鼠标为锚点缩放？
**答**：viewBox 定义了 SVG 内部逻辑坐标系到视口的映射，`preserveAspectRatio` 控制宽高比不一致时的对齐方式。缩放 = 修改 viewBox 的 x/y/w/h。关键点是**锚点计算**：把鼠标位置换算成 viewBox 坐标，缩放后保证"指针下的点缩放前后位置不变"，即 `newX = mx - (mx - oldX) * k`。平移则直接平移 viewBox 原点。

```html
<svg id="s" viewBox="0 0 600 400" width="600" height="400" style="border:1px solid #ccc">
  <circle cx="300" cy="200" r="80" fill="steelblue"></circle>
</svg>
<script>
  const svg = document.getElementById('s');
  let vb = { x: 0, y: 0, w: 600, h: 400 };
  svg.addEventListener('wheel', e => {
    e.preventDefault();
    const k = e.deltaY < 0 ? 0.9 : 1.1;
    // 鼠标位置换算到 viewBox 逻辑坐标，作为缩放锚点，保证指针下的点不动
    const mx = vb.x + (e.offsetX / svg.clientWidth) * vb.w;
    const my = vb.y + (e.offsetY / svg.clientHeight) * vb.h;
    vb = {
      x: mx - (mx - vb.x) * k,
      y: my - (my - vb.y) * k,
      w: vb.w * k,
      h: vb.h * k,
    };
    svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
  }, { passive: false });
</script>
```
