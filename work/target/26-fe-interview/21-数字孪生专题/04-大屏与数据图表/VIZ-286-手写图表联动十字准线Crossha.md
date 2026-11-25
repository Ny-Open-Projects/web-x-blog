---
title: [VIZ-286] 手写图表联动十字准线（Crosshair）：多图同步
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-286：手写图表联动十字准线（Crosshair）：多图同步

**答**：
- 题目：多图十字准线——光标在任一图上移动，所有图同 x 位置画准线并显示各自值。事件总线同步（防环）。
- 思路：主图 mousemove → 广播 xPx → 其他图画竖线（各自比例尺反查）；节流 rAF。
- 评分点：广播与防环；各图独立反查；rAF 节流。

```javascript
class CrosshairSync {
  constructor(charts) {
    this.charts = charts; this.source = null;
    charts.forEach(c => c.onMouseMove = e => this.broadcast(c, e.offsetX));
    charts.forEach(c => c.onMouseLeave = () => this.clear());
  }
  broadcast(source, xPx) {
    if (this.source) return;                               // 防重入
    this.source = source;
    requestAnimationFrame(() => {                           // rAF 节流
      const xVal = source.scaleX.invert(xPx);              // 数据域坐标
      for (const c of this.charts) {
        const px = c.scaleX.scale(xVal);                   // 各图独立映射
        c.drawCrosshair(px);                               // 各自画准线
      }
      this.source = null;
    });
  }
  clear() { this.charts.forEach(c => c.clearCrosshair()); }
}
```
