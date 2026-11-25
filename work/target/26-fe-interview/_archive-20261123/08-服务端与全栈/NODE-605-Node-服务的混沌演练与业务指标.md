---
title: [NODE-605] Node 服务的混沌演练与业务指标联动（演练看到用户视角）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-605：混沌演练与业务指标
**答**:
- 视角升级：技术指标（错误率/延迟）≠ 用户体感——演练验收加业务指标（下单成功率/支付成功率/页面可完成率——用户视角的韧性验证）。
- 业务指标注入验证：演练期间的真实用户行为监控（灰度域用户的漏斗对比——故障对转化的实际影响量化）、合成用户（拨测机器人走核心链路——演练期间的业务探针 NODE-480）。
- 业务韧性验收标准：每核心链路的业务级验收（"支付故障演练 → 支付成功率 ≥ 99%（降级渠道接管）+ 用户可重试"——业务方参与定义）、演练与业务方协同（业务侧观察大屏——技术演练业务可感知）。
- 量化用户影响：演练影响核算（受影响用户数/影响时长/业务损失估算——演练报告业务语言化 ARC-583 翻译）。
- 演练→改进→复演：业务指标不达标的缺陷优先级最高（用户体感优先——排序规则）。
```yaml
# 业务级验收（支付演练）
scenario: pay-channel-down
observe:
  tech: [errorRate, breakerState, recovery]
  biz: [paySuccessRate, funnelDrop, complaintDelta]              # 业务探针
accept:
  biz: { paySuccessRate: '>=99% (backup channel)', funnelDrop: '<0.5%' }
report: { userImpact: 'affected 1.2k, est loss 0 — 降级接管生效' }
```
