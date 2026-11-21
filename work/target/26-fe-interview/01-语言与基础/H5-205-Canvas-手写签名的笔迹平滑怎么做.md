---
title: [H5-205] Canvas 手写签名的笔迹平滑怎么做
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-205：Canvas 手写签名的笔迹平滑怎么做

**答**：
- 直接连线抖且生硬；业界标准是「中点二次贝塞尔」：把相邻采样点的中点作为曲线端点，原点作为控制点
- 线宽随速度变化：采样点间距大（手速快）→ 线细，间距小 → 线粗，模拟真实笔锋
- 输入降噪：pointermove 事件本身有抖动，可加最小移动距离阈值（如 2px 以下忽略）与 EMA 平滑
- 高分屏适配与 pressure 支持（PointerEvent.pressure 可直接用压感）
- 收尾：笔画存储为点序列而非位图，方便撤销/重放/再导出

```javascript
let last = null;
function onMove(e) {
  const p = getPos(e);
  if (last) {
    const mid = { x: (last.x + p.x) / 2, y: (last.y + p.y) / 2 };
    ctx.beginPath();
    ctx.moveTo(prevMid.x, prevMid.y);
    ctx.quadraticCurveTo(last.x, last.y, mid.x, mid.y); // 中点法平滑
    ctx.lineWidth = 2 + 8 / Math.hypot(p.x - last.x, p.y - last.y); // 快细慢粗
    ctx.stroke();
    prevMid = mid;
  } else { prevMid = p; }
  last = p;
}
```
