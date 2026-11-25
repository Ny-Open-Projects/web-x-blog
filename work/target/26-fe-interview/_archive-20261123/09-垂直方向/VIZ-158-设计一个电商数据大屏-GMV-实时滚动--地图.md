---
title: [VIZ-158] 设计一个电商数据大屏（GMV 实时滚动 + 地图 + 漏斗）。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-158：设计一个电商数据大屏（GMV 实时滚动 + 地图 + 漏斗）。
**答**：① **GMV 数字滚动**——目标值到达后 rAF 缓动插值（easeOutCubic）从当前值滚到目标值，千分位/亿元单位，避免每秒 setState 抖动；② **地图飞线**——订单城市对飞线（VIZ-112），同时最多 N 条限流；③ **漏斗**——浏览→加购→下单→支付；④ **实时链路**——WebSocket + 心跳 + 断线重连 + 消息幂等（按版本号去重），后端窗口聚合，前端不做全量计算；⑤ 适配 1920 设计稿 scale；⑥ 组件级曝光埋点便于运营复盘。

```javascript
// GMV 数字滚动器：缓动插值 + 大数格式化
class NumberTicker {
  constructor(el, { duration = 800 } = {}) { this.el = el; this.duration = duration; }
  to(target) {
    const from = this.current ?? 0, start = performance.now();
    cancelAnimationFrame(this.raf);
    const step = now => {
      const t = Math.min(1, (now - start) / this.duration);
      const eased = 1 - Math.pow(1 - t, 3);            // easeOutCubic
      this.current = from + (target - from) * eased;
      this.el.textContent = new Intl.NumberFormat('zh-CN',
        { notation: 'compact', maximumFractionDigits: 2 }).format(this.current);
      if (t < 1) this.raf = requestAnimationFrame(step);
    };
    this.raf = requestAnimationFrame(step);
  }
}
const ticker = new NumberTicker(document.querySelector('#gmv'));
ws.onmessage = e => { const { gmv } = JSON.parse(e.data); ticker.to(gmv); }; // 每秒一跳
```
