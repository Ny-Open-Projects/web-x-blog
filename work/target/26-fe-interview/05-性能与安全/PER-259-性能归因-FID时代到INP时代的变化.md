---
title: [PER-259] 性能归因手段从"看瀑布图"进化到"自动归因"，LoAF/Event Timing 各解决什么问题？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-259：性能归因手段从"看瀑布图"进化到"自动归因"，LoAF/Event Timing 各解决什么问题？

**答**：
- 瀑布图时代：开发者工具里人肉看资源瀑布与火焰图，只能"个案定位"，无法规模化——RUM 里成千上万个慢样本没法逐个看。
- Event Timing：把每次交互拆成 input delay / processing / presentation 三段并给 interactionId，让"慢交互"可批量聚合——按交互类型出"哪类操作最慢"排行。
- LoAF：把慢帧归因到脚本（invoker、URL、行号）与渲染段占比，让"哪个函数/哪个 SDK 拖慢页面"可自动聚合——三方脚本追责的利器。
- 两者配合是 INP 归因的完整闭环：Event Timing 告诉你"什么操作慢"，LoAF 告诉你"哪段代码背锅"。再配上 LCP 的 element/url 字段与 CLS 的 sources，四大指标全部可自动归因。
- 落地形态：RUM SDK 把归因结果随指标一起上报，看板直接产出"慢页面 × 慢脚本 × 慢交互"的交叉清单，工单自动带归因。

```javascript
// 交互慢 + 慢帧归因联动：报告单条 = 交互三段 + 帧内脚本榜
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.interactionId == null || e.duration < 200) continue;
    report({
      type: 'slow-interaction',
      interaction: e.name, target: e.target?.tagName,
      inputDelay: +(e.processingStart - e.startTime).toFixed(1),
      processing: +(e.processingEnd - e.processingStart).toFixed(1),
      presentation: +(e.duration - (e.processingEnd - e.startTime)).toFixed(1),
      scripts: recentLoAFScripts(),          // LoAF 缓存里最近慢帧的 invoker top3
    });
  }
}).observe({ type: 'event', durationThreshold: 200, buffered: true });
```
