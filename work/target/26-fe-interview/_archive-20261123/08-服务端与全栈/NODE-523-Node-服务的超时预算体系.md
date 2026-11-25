---
title: [NODE-523] Node 服务的超时预算体系（全链路 deadline 管理）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-523：超时预算体系
**答**:
- 预算链：用户体感预算（页面 5s）→ 网关（500ms）→ BFF 聚合（400ms）→ 下游（各 200ms）——逐层分配，每层只许用自己份额（超支会拖垮整链）。
- deadline 传播：入口生成总预算 → 每跳透传剩余（header x-deadline）→ 每层按剩余收紧自己的超时（剩余 100ms 时下游调用只给 90ms——不够就快速失败走降级 NODE-377/471）。
- 超时配置纪律：超时 < 下游 P99（P99 500ms 的下游配 400ms 超时 = 1% 请求必超时——预算按下游实测 P99 留余量）、重试超时（per-attempt ≤ deadline 剩余的 1/2——留一次重试空间）、取消传播（超时 → AbortSignal 级联取消下游计算 NODE-422）。
- 预算治理：各层预算声明化（配置中心——改预算热更 + 影响面提示）、预算审计（实际耗时 vs 预算分布——哪层在超支，NODE-501 瀑布数据）、预算违约率（超预算完成的比例——预算体系的健康指标）。
- 特殊场景：流式/长轮询的预算语义不同（连接保持 vs 计算预算——分开设）。
```javascript
// deadline 传播
function propagate(req) {
  const budget = Number(req.get('x-deadline-ms') ?? 5000);
  const next = { total: budget - elapsed(), forThis: Math.min(200, (budget - elapsed()) * 0.4) };
  return fetch(url, { headers: { 'x-deadline-ms': next.total },
    signal: AbortSignal.timeout(next.forThis) });               // 剩余预算内收紧
}
```
