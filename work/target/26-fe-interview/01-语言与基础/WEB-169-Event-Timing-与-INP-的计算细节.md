---
title: [WEB-169] Event Timing 与 INP 的计算细节是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-169：Event Timing 与 INP 的计算细节是什么？
**答**：
- Event Timing 记录每次用户交互事件：startTime、processingStart（事件处理器开始）、processingEnd、duration。
- 单次交互的延迟 = 该交互内所有事件 duration 的最大值（duration 覆盖到下一次绘制完成，含渲染）。
- INP = 统计周期内所有交互延迟的"最差档"（接近 P98），衡量的是页面里表现最差的那次交互，不是平均值。
- 归因：把命中的那次交互的 target、事件类型与当帧 LoAF 数据一起上报才能定位代码。
- 阈值：小于 200ms 良好，200-500ms 需改进，大于 500ms 差。

```javascript
const interactions = new Map();
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    // 同一次交互可能派发多个事件，interactionId 相同，保留最大 duration
    const prev = interactions.get(e.interactionId);
    if (!prev || e.duration > prev.duration) interactions.set(e.interactionId, e);
  }
}).observe({ type: 'event', durationThreshold: 16, buffered: true });
// 采样结束时取最差交互作为 INP
function reportINP() {
  const worst = [...interactions.values()].sort((a, b) => b.duration - a.duration)[0];
  if (worst) report('inp', {
    value: worst.duration,             // 阈值 200/500ms
    target: worst.target?.tagName,     // 命中的元素
    latency: worst.processingStart - worst.startTime, // 事件处理前的延迟
  });
}
```
