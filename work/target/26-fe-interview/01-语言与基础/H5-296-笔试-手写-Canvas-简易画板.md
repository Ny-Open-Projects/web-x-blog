---
title: [H5-296] 笔试：手写 Canvas 简易画板
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-296：笔试：手写 Canvas 简易画板

**题目**：实现画板组件：mousedown/mousemove/mouseup（PointerEvent 优先）绘制线条；支持笔宽与颜色；高分屏不模糊；提供 clear 与撤销（保存快照栈，上限 20 步）。

**答**：
```javascript
function createBoard(canvas) {
  const ctx = canvas.getContext('2d');
  const dpr = devicePixelRatio;
  function setup() {
    canvas.width = canvas.clientWidth * dpr;
    canvas.height = canvas.clientHeight * dpr;
    ctx.scale(dpr, dpr);
    ctx.lineCap = ctx.lineJoin = 'round';
  }
  setup();
  let drawing = false;
  const snaps = [];

  function pos(e) {
    const r = canvas.getBoundingClientRect();
    return { x: e.clientX - r.left, y: e.clientY - r.top }; // CSS 坐标（ctx 已缩放）
  }
  canvas.addEventListener('pointerdown', (e) => {
    if (snaps.length >= 20) snaps.shift();
    snaps.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
    drawing = true;
    const p = pos(e);
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
    canvas.setPointerCapture(e.pointerId);
  });
  canvas.addEventListener('pointermove', (e) => {
    if (!drawing) return;
    const p = pos(e);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
  });
  canvas.addEventListener('pointerup', () => (drawing = false));
  return {
    setStyle({ color = '#333', width = 3 } = {}) { ctx.strokeStyle = color; ctx.lineWidth = width; },
    undo() { const s = snaps.pop(); s && ctx.putImageData(s, 0, 0); },
    clear() { snaps.push(ctx.getImageData(0, 0, canvas.width, canvas.height)); ctx.clearRect(0, 0, canvas.width, canvas.height); },
  };
}
```

**评分点**：
- getBoundingClientRect 换算坐标（不能用 offsetX 硬写）
- DPR 缩放防高分屏模糊
- 撤销用 ImageData 快照（push/pop），数量上限防内存爆
- pointer capture 保证移出画布仍能绘制
