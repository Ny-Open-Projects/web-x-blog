---
title: [ARC-351] 可观测性深水区：Trace 采样策略如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-351：可观测性深水区：Trace 采样策略如何设计？
**答**：
- 全量采集成本爆炸（一个页面一次会话几十个 span，QPS 大时上报量与存储都是天量），必须采样；核心矛盾是"保真"与"成本"。
- 头部采样（Head Sampling）：入口处决定是否采样，链路上所有 span 跟随 root 决策（traceparent 里的 flags），保证链路完整。
- 尾部采样（Tail Sampling）：全量暂存后按结果丢——只留慢请求、出错请求、特殊用户，覆盖率对排障最有价值。
- 前端场景混合策略：错误 100% 保留、P95 慢会话保留、抽样 1%~5% 常规流量、灰度/实验流量按需提额。
- 采样率配置中心下发 + 版本对账，避免"各端采样口径不一致导致数据不可比"。
```javascript
// 前端 Trace 采样决策器
function shouldSample(traceCtx, config) {
  if (traceCtx.hasError) return true;                     // 错误全保
  if (traceCtx.duration > config.slowThreshold) return true; // 慢会话全保
  if (traceCtx.userData.isInternal) return true;          // 内部用户调试
  return Math.random() < config.sampleRate;               // 常规按率
}
// config 从配置中心拉取：{ sampleRate: 0.02, slowThreshold: 8000 }
// 采样决策在 root span 创建时做出，写入 tracestate 传递给后续 span
```
