---
title: [NODE-468] Node 服务的日志采样与热点路径（不打全量也找得到）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-468：日志采样与热点路径
**答**:
- 成本矛盾：热点接口（10w QPS）全量日志=存储灾难，但不打日志出问题没现场。解法：动态采样 + 尾部保真。
- 采样策略：常态采样（成功请求 1%~5%）、异常保真（错误/慢请求/重试请求 100%）、特征保真（特定用户/灰度标签/实验桶全量——排障与实验需要）、动态提额（当前接口错误率上升 → 采样率自动提到 100%——出问题自动"开灯"）。
- 尾部保真的实现：先决定采样再打日志（入口采样决策传上下文 ALS NODE-421——所有日志统一决策，避免部分打部分不打）；环形缓冲（最近 N 条未采样日志驻内存，错误发生时把缓冲补报——错误前后的现场都拿到）。
- 聚合替代：超高频确定性事件（每请求都成功的埋点）改为指标计数，不打日志（NODE-426 同思想）。
- 观测：采样率/保真率/日志量成本看板，采样策略变更留痕。
```javascript
// 入口采样决策 + 环形补报
app.use((ctx, next) => {
  const s = sampler.decide(ctx);                                 // {sample: bool, keep: bool}
  als.run({ sample: s.sample, ring: s.keep ? new RingBuffer(100) : null, ...ctxInfo }, next);
});
logger.on('error', (e) => als.getStore()?.ring && reportRing(als.getStore().ring.dump())); // 补报现场
```
