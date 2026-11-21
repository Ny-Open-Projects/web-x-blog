---
title: [NODE-445] Node 服务的 AB 实验服务端配合（分流/指标/护栏）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-445：AB 实验服务端配合
**答**:
- 服务端在 AB 中的职责：分流（正交分层，NODE-444/ARC-277）、实验参数下发（实验配置随响应）、行为一致性（分桶内请求全走同一变体——同一用户请求中途变桶会污染数据）、护栏指标采集（错误率/延迟按桶打标 NODE-372）。
- 分流实现：实验服务（分桶 SDK 服务端版）→ 结果缓存（用户-实验-桶，会话内稳定）；流量分配支持占比调整（放量 1%→5%→50% 平滑，已有桶不迁移——hash 基数排序法）。
- 指标采集：实验维度自动注入所有日志/指标/trace（NODE-421 上下文扩展），数仓按桶切片（ARC-390 数据链路）。
- 护栏自动化：桶内错误率/LCP 超阈值自动停止实验（ARC-475 止损闭环服务端版）、实验时长与样本量校验（ARC-289 统计功效）。
- 治理：实验注册（假设/指标/时长/负责人）、实验上限（同时在线实验数——互相干扰评估）、实验结论归档。
```javascript
// 服务端分流 + 注入
const bucket = await experiments.assign(userId, 'checkout-v2', { layers: ['pay'] });
ctx.state.experiment = { id: 'checkout-v2', bucket };
als.getStore().exp = ctx.state.experiment;                       // 进日志上下文
if (bucket === 'treatment') return newCheckout(ctx);             // 变体路由
return oldCheckout(ctx);
// 护栏：metrics.byBucket('checkout-v2').watch({ errRate: 3x, p99: 1.5x }, () => stopExperiment())
```
