---
title: [VIZ-461] 大规模折线图（十万点）的 Canvas 渲染优化
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-461：大规模折线图（十万点）的 Canvas 渲染优化

**答**：
- 手段：LTTB 降采样（1235 思路）、路径分块缓存（视口外不画）、Canvas 分层（网格层缓存 + 数据层重绘）。
- 交互：缩放平移触发重采样（节流 rAF），hover 用空间索引（网格/R 树）查点。
- 兜底：点数超 50 万强制服务端聚合（前端只画聚合结果）。

```javascript
// 大折线渲染
function drawBigLine(ctx, data, view, { maxPx = 4000 } = {}) {
  const visible = data.filter(d => d.x >= view.x0 && d.x <= view.x1);
  const step = Math.max(1, Math.floor(visible.length / maxPx));
  ctx.beginPath();
  for (let i = 0; i < visible.length; i += step) {
    const p = visible[i];
    const px = (p.x - view.x0) * view.scaleX;
    const py = (p.y - view.y0) * view.scaleY;
    i === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py);
  }
  ctx.stroke();
}
```
