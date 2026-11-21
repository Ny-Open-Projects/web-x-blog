---
title: [PER-204] INP 的统计口径是什么？p98 与交互采样怎么理解？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-204：INP 的统计口径是什么？p98 与交互采样怎么理解？

**答**：
- 单页面生命周期内：每 50 个独立交互事件组（一次 interactionId 相同的按键/点击算一组）采样一次，取其中"最差交互"作为该页的 INP 值上报（近似最大值，避免极端离群）。
- 聚合口径：CrUX / 看板层面对全站所有页面的单页 INP 取 **第 98 分位（p98）** 评估，即"98% 的用户访问体验不差于该值"。阈值：好 ≤ 200ms，需改进 200~500ms，差 > 500ms。
- 为什么不是平均值：延迟分布是长尾的，平均会被大量快交互稀释，掩盖少数卡死体验；p98 直接对齐"最难受的那批用户"，这也是性能 SLO 常用 p75/p98 的原因。
- 实践含义：本地手测点几下不卡 ≠ 达标。必须用真实用户监控（RUM）按 p98 口径看数，且注意剔除 bfcache 恢复、后台标签页等无效样本（navigation type / visibility 过滤）。

```javascript
// RUM 上报端近似实现"每 50 次交互取最差"的采样策略
const interactions = new Map(); // interactionId -> {start, worst}
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.interactionId == null) continue;
    const cur = interactions.get(e.interactionId) || { start: e.startTime, worst: 0 };
    // 同一次交互可能派发多个事件（pointerdown+pointerup），取耗时最长者
    cur.worst = Math.max(cur.worst, e.duration);
    interactions.set(e.interactionId, cur);
  }
}).observe({ type: 'event', buffered: true, durationThreshold: 16 });

function reportOnUnload() {
  const worstOfPage = Math.max(...interactions.values().map(v => v.worst));
  // 页面级 INP 上报；服务端再对所有页面取 p98 出指标
  navigator.sendBeacon('/rum/inp', JSON.stringify({ url: location.pathname, inp: worstOfPage }));
}
```
