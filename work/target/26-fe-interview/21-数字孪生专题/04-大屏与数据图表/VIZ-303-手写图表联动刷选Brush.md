---
title: [VIZ-303] 手写图表联动刷选（Brush）：框选数据过滤（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-303：手写图表联动刷选（Brush）：框选数据过滤（笔试）

**答**：
- 题目：实现散点图刷选——拖出矩形，选中区域内点高亮，其他图表联动过滤。完整实现：绘制刷选框、命中判定、广播。
- 思路：pointer 事件记录起点/终点 → 矩形；数据点坐标→像素反查判定包含；联动广播（防环）。
- 评分点：刷选矩形绘制；命中判定（反查）；联动防环。

```javascript
class BrushSelector {
  constructor(chart, siblings) {
    this.chart = chart; this.siblings = siblings;
    this.selected = new Set();
    chart.el.addEventListener('pointerdown', e => { this.start = { x: e.offsetX, y: e.offsetY }; });
    chart.el.addEventListener('pointermove', e => {
      if (!this.start) return;
      this.rect = normRect(this.start, { x: e.offsetX, y: e.offsetY });
      chart.drawBrush(this.rect);                          // 实时画框
    });
    chart.el.addEventListener('pointerup', () => this.commit());
  }
  commit() {
    const { rect } = this;
    const inRect = this.chart.points.filter(p => {          // 数据点反查像素判定
      const [x, y] = this.chart.toPixel(p);
      return x >= rect.x && x <= rect.x + rect.w && y >= rect.y && y <= rect.y + rect.h;
    });
    this.selected = new Set(inRect.map(p => p.id));
    for (const s of this.siblings) {                       // 联动（防环由总线管）
      s.highlight(this.selected);                          // 高亮同 ID 点
      s.filterSummary([...this.selected]);
    }
  }
}
```
