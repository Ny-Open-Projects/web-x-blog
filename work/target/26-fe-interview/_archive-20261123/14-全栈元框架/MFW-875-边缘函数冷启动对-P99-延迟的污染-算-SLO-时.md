---
title: [MFW-875] 边缘函数冷启动对 P99 延迟的污染，算 SLO 时该怎么处理
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-875：边缘函数冷启动对 P99 延迟的污染，算 SLO 时该怎么处理

**答**：
- 结论：冷启动是偶发的长尾延迟，会显著抬高 P99；算 SLO 要么把冷启动单列为独立指标，要么明确纳入并单独设定预算，不能混在一起掩盖真实性能。
- 落地：给请求打 coldStart 标记，延迟指标分「含冷启动」与「稳态」两套；SLO 分别对账，冷启动用预热/快照优化。
- 追问钩子：能不能直接剔除冷启动样本？——可以但必须透明标注口径，否则会虚报 SLO。

```javascript
function recordLatency(span) {
  const bucket = span.coldStart ? 'withCold' : 'steady';
  metrics.histogram('render.latency', span.duration, { bucket, route: span.route });
}
function sloViolation(route) {
  // 稳态 P99 衡量代码性能；含冷启动 P99 衡量真实用户体验
  const steadyP99 = metrics.p99('render.latency', { bucket: 'steady', route });
  const coldP99 = metrics.p99('render.latency', { bucket: 'withCold', route });
  return { steadyOk: steadyP99 < 200, coldOk: coldP99 < 800, steadyP99, coldP99 };
}
// 口径必须明确：剔除冷启动要标注，避免虚报
```
