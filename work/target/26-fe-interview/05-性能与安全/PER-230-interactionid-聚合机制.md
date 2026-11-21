---
title: [PER-230] Event Timing 里一次交互（interactionId）怎么聚合多个事件？键盘/指针事件为什么算同一交互？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-230：Event Timing 里一次交互（interactionId）怎么聚合多个事件？键盘/指针事件为什么算同一交互？

**答**：
- 交互定义：一次"交互"= 用户的一个意图动作，可能派发多个事件——点击产生 pointerdown/pointerup/click，触摸还有 touchstart/touchend。Event Timing 给同一次交互的这些事件相同 `interactionId`。
- 聚合规则：INP 取该次交互中所有事件里"耗时最长者"的完整 duration（input delay + processing + presentation），不是求和——三个事件各 80ms 算 80ms 而不是 240ms。
- 只统计三类：鼠标点击、触屏点按、键盘按键（keydown/keyup 计一次）。scroll/hover/pointermove 不算交互（无明确完成边界），所以滚动流畅度要靠单独指标（FPS/长帧）看。
- 实现含义：采集端要按 interactionId 建立会话，跨事件取 max；同一交互的第二批事件到达时更新而不是新建会话；未结束的交互要等 presentation 完成才能定值。

```javascript
const sessions = new Map();   // interactionId -> { start, maxDur, events }

function onEventEntry(e) {
  if (e.interactionId == null) return;                 // scroll 等非交互事件无 id
  const s = sessions.get(e.interactionId) || { start: e.startTime, maxDur: 0, events: [] };
  // pointerdown 与 click 同 id：取 max 而非 sum
  s.maxDur = Math.max(s.maxDur, e.duration);
  s.events.push({ name: e.name, dur: Math.round(e.duration),
                  inputDelay: e.processingStart - e.startTime,
                  processing: e.processingEnd - e.processingStart });
  sessions.set(e.interactionId, s);
  // INP 候选 = s.maxDur；inputDelay/processing/三段拆解可直接归因
}
new PerformanceObserver((l) => l.getEntries().forEach(onEventEntry))
  .observe({ type: 'event', durationThreshold: 16, buffered: true });
```
