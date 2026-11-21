---
title: [NODE-297] 采样策略与观测成本？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-297：采样策略与观测成本？
**答**:
- 头部采样：入口按比例（1%/10%）决定整条链是否采——省大部分成本，但可能错过"恰好没采到的问题请求"。
- 尾部采样：全采 + collector 按（耗时/错误/慢）筛选保留——可见性最好，采集成本高（中转带宽/内存）。
- 动态采样：按服务重要性/流量时段调整（大促 1% → 平时 10%）；错误请求 100% 保留（尾部规则）。
- 成本账：span 数 ≈ QPS × 平均 span 数 × 采样率 × span 大小——月成本估算进架构评审。

```javascript
// 尾部采样规则（collector 侧配置示意）
const tailPolicy = [
  { type: 'status_code', status_code: 'ERROR', percentage: 100 },     // 错误全留
  { type: 'latency', latency_threshold_ms: 2000, percentage: 100 },   // 慢请求全留
  { type: 'trace_state', key: 'vip', values: ['1'], percentage: 100 },// 重点用户全留
  { type: 'always_sample', percentage: 5 },                            // 其余 5%
];
// 动态采样（入口）
function sampleRatio() {
  if (bigSaleWindow()) return 0.01;                     // 大促 1%
  if (isHighValueRoute(ctx.path)) return 0.5;           // 核心链路 50%
  return 0.1;
}
```
