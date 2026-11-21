---
title: [VIZ-070] 设计一个实时行情图：K 线 / 分时高频更新。（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-070：设计一个实时行情图：K 线 / 分时高频更新。（压轴）
**答**：核心是**K 线聚合器**：逐笔成交按时间片（1 分钟）聚合成 OHLCV——同片更新当前 K 线的 close/high/low/volume，跨片则收盘旧的、开启新的。渲染只动"最后一根"：未完成 K 线高频跳变，用局部 setOption 替换最后一位；完成的 K 线 appendData 入历史。分时图 = 当日 1 分钟线 + 均价线。再叠加：涨跌颜色、dataZoom 默认聚焦最新、断线时用 REST 补齐缺口数据。

```javascript
// 行情高频更新：当前 K 线逐笔聚合（秒 -> 分），完成才入历史，避免整表重排
class KlineAggregator {
  constructor(intervalMs) { this.interval = intervalMs; this.current = null; }
  tick(trade) { // trade: { price, time, volume }
    const bucket = Math.floor(trade.time / this.interval) * this.interval;
    if (!this.current || this.current.time !== bucket) {
      if (this.current) this.onClose?.(this.current);   // 上一根完成，入历史
      this.current = { time: bucket, open: trade.price, close: trade.price,
        high: trade.price, low: trade.price, volume: trade.volume };
    } else {
      const c = this.current;
      c.close = trade.price;
      c.high = Math.max(c.high, trade.price);
      c.low = Math.min(c.low, trade.price);
      c.volume += trade.volume;
    }
    return this.current; // 未完成 K 线实时更新最后一根
  }
}
// 渲染：未完成 K 线只 setOption 替换最后一位；完成走 appendData；dataZoom 默认聚焦最新
```
