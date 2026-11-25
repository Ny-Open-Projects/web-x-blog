---
title: [NODE-603] Node 服务的容量自动伸缩（指标驱动 HPA + 依赖联动）如何深化？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-603：容量自动伸缩深化
**答**:
- 伸缩信号深化：业务指标伸缩（订单 QPS/队列深度——比 CPU 更早反映负载 NODE-375）、预测性伸缩（周期性流量模式预测——提前扩容： Cron + 历史模型）、多指标组合（CPU + QPS + 事件循环延迟——任一超标即扩）。
- 依赖联动扩容：上游扩容 → 下游流量增（下游也要能接住——联动 HPA 或下游容量余量保障 NODE-405）、扩容审批自动化（非核心服务自动、核心服务半自动——成本与风险平衡 NODE-434）。
- 缩容安全：缩容窗口（流量低谷缩容——连接 drain NODE-351）、缩容防抖（stabilizationWindow——防反复横跳）、最小副本（可用性底线——可用性 SLA 对齐）。
- 弹性演练常态化（NODE-533）、伸缩事件审计（每次扩缩容记录：触发指标/决策/结果——决策可追溯）。
- 成本护栏：扩容成本上限（超预算扩容需人工确认——NODE-434 成本护栏）、闲时回收（非高峰自动缩到 min——资源利用效率）。
```yaml
# 多指标 + 预测伸缩
metrics: [cpu(65%), qps(300/replica), el-delay(50ms)]
predictive:
  cron: '0 8 * * *'        # 每日早高峰前
  from: historical-model   # 按历史流量模型提前扩
  to: peakReplicas
cost-guard: { maxReplicas: 50, overBudget: 'require-approve' }
```
