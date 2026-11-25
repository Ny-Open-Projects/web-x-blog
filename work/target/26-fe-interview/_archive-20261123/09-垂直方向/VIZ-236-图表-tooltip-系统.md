---
title: [VIZ-236] 图表 tooltip 系统：定位策略与数据聚合提示
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-236：图表 tooltip 系统：定位策略与数据聚合提示

**答**：
- tooltip 定位：跟随光标 / 锚定数据点 / 智能翻转（视口边缘）——复用 HW-300 策略。
- 数据聚合提示：十字准线模式（hover x 轴位置聚合多条 series 值）——tooltip 内容按 x 查询各 series。
- 性能：tooltip DOM 独立（不在主 canvas 重绘）；高频移动节流。

```javascript
class TooltipSystem {
  showCrosshair(xPx, series) {                           // 十字准线聚合模式
    const xValue = this.scaleX.invert(xPx);
    const rows = series.map(s => {
      const point = nearestByX(s.data, xValue);           // 各系列最近点
      return { name: s.name, value: formatValue(point.v), color: s.color };
    });
    this.dom.innerHTML = renderRows(rows);
    this.position(flipAware(xPx, this.dom.offsetWidth));   // 边缘翻转（HW-300）
  }
}
const flipAware = (x, w) => x + w + 16 > innerWidth ? x - w - 16 : x + 16;   // 翻转
// 性能：mousemove 节流 rAF；tooltip 内容 diff 更新（不重建 DOM）
```
