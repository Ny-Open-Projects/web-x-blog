---
title: [PER-781] 手写一个 WebView 池容量伸缩控制器：按路由访问频率动态调整池大小并输出伸缩日志
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-781：手写一个 WebView 池容量伸缩控制器：按路由访问频率动态调整池大小并输出伸缩日志

**答**：
- 需求：统计各路由访问频率，高频路由占比升高时扩热池、持续低频时缩池；伸缩带滞回防抖动；每次伸缩输出日志（时间/原因/前后容量）。
- 边界：伸缩周期内最多调整一次（冷却时间）；低端机强制上限；页面正在使用中的实例不计入可缩容量。
- 评分点：滞回/冷却防抖；伸缩依据是频率统计而非瞬时值。

```javascript
class PoolScaler {
  constructor(pool, { windowMs = 60000, coolMs = 120000, hysteresis = 0.3 } = {}) {
    this.pool = pool; this.freq = new Map(); this.lastScale = 0;
    this.windowMs = windowMs; this.coolMs = coolMs; this.hys = hysteresis;
    this.logs = [];
  }
  hit(route) {                                // 记录路由访问
    const now = Date.now();
    const list = (this.freq.get(route) || []).filter(t => now - t < this.windowMs);
    list.push(now); this.freq.set(route, list);
  }
  scale() {                                   // 冷却期内不动
    const now = Date.now();
    if (now - this.lastScale < this.coolMs) return;
    const hotRate = [...this.freq.values()].reduce((s, l) => s + l.length, 0) / (this.windowMs / 1000);
    const cur = this.pool.limit.hot;
    let next = cur;
    if (hotRate > 2 + this.hys && cur < 4) next = cur + 1;        // 高频：扩
    if (hotRate < 0.5 - this.hys && cur > 1) next = cur - 1;      // 持续低频：缩
    if (next !== cur) {
      this.pool.limit.hot = next; this.lastScale = now;
      if (next > cur) this.pool.warm();
      this.logs.push({ t: now, reason: `hotRate=${hotRate.toFixed(2)}/s`, from: cur, to: next });
    }
  }
}
```
