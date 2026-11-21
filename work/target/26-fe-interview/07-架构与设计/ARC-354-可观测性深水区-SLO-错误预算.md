---
title: [ARC-354] 可观测性深水区：SLO 与错误预算在前端如何定义与运转？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-354：可观测性深水区：SLO 与错误预算在前端如何定义与运转？
**答**：
- SLI 选用户可感知的：页面可用性（白屏率取反）、LCP 达标率、核心 API 成功率、JS 错误率；不选工程内部指标（构建时长）当 SLI。
- SLO 设定：基于历史基线 + 业务期望，如"月度白屏率 < 0.5%、LCP<2.5s 占比 > 75%"；留出预算空间而不是拍理想值。
- 错误预算 = 1 - SLO：预算烧完自动触发机制——冻结非必要发布、只允许稳定性修复，这是 SLO 的真正价值（给决策提供客观依据而非吵架）。
- 前端落地：SLO 计算走 RUM 真实用户数据而非拨测，按端/版本/地域多维切片，避免"平均数掩盖局部灾难"。
- 运转节奏：周会看预算燃烧速率（burn rate），快速燃烧（1h 烧掉 2% 预算）直接告警。
```javascript
// 错误预算计算（日维度）
const slo = { whiteScreenRate: 0.995 };        // 白屏率 SLO 99.5%
const burn = (1 - slo.whiteScreenRate) * totalPv; // 预算额度：0.5% 的 PV
const used = whiteScreenPv;
const budgetLeft = 1 - used / burn;
if (budgetLeft < 0.2) notify('错误预算仅剩 20%：冻结特性发布');
// burn rate：近 1h 消耗速率 / 均衡速率 > 14.4 触发快速告警（Google SRE 标准）
```
