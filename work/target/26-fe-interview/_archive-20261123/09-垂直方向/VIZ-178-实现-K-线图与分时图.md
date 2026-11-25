---
title: [VIZ-178] 实现 K 线图与分时图。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-178：实现 K 线图与分时图。
**答**：分时图——当日 1 分钟线 + 均价线 + 昨收基准线，面积渐变填充；K 线——蜡烛（开高低收），红涨绿跌可配置，副图成交量。实现要点：Canvas 自绘（数据量大、交互密，不套 ECharts），十字光标 snap 最近 K 线，tooltip 显示 OHLC；缩放模型是"可见根数"（30~500 根）——滚轮改可见数 + 拖拽平移（带惯性），指标（MA/MACD）只按窗口 + 周期余量重算，不全量重算。

```javascript
// K 线窗口模型：可见根数 + 惯性平移
const view = { offset: 0, visible: 120 };       // offset: 距最新 K 线的偏移
canvas.addEventListener('wheel', e => {
  view.visible = Math.round(clamp(view.visible * (e.deltaY > 0 ? 1.1 : 0.9), 30, 500));
  draw(); e.preventDefault();
}, { passive: false });
let dragging = null;
canvas.addEventListener('pointerdown', e => dragging = e.clientX);
canvas.addEventListener('pointermove', e => {
  if (dragging == null) return;
  view.offset = clamp(view.offset + Math.round((e.clientX - dragging) / candleW()),
                      0, candles.length - view.visible);
  dragging = e.clientX; draw();
});
function draw() {
  const { lo, hi } = visibleRange();
  drawCandles(ctx, candles, { lo, hi });        // 见 VIZ-163
  drawVolume(ctx, candles, { lo, hi });
  drawMA(ctx, candles, { lo, hi }, [5, 10, 20]);// 指标只算窗口 + 周期余量
}
```
