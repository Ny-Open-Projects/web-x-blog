---
title: [1043] 100 并发 Agent 任务需要多少资源，怎么估算
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 容量]
type: 面试题
---

## 1043：100 并发 Agent 任务需要多少资源，怎么估算

**答**：
- 估算公式：并发任务数 × 每任务平均并发请求数（模型调用 + 工具调用）× 安全系数；模型侧受供应商 TPM/QPS 配额约束，工具侧受内部服务容量约束——瓶颈通常在工具侧。
- 关键参数实测：单任务平均轮次、每轮 token 数、工具调用次数与 P95 耗时；这些来自 trace 统计而不是拍脑袋。
- 队列容量 = 高峰到达率 × 平均任务时长（Little's Law），超过就扩并发或排队告知；峰谷差大的业务配弹性并发（夜间批处理让出容量）。
- 追问钩子：容量估算最常见的错？——按「平均」估算：Agent 任务方差极大（长尾任务 10 倍时长），必须按 P95 规划，否则高峰必崩。

```ts
function capacity({ peakRps, avgRounds, avgToolMs, toolSlots }) {
  const toolDemand = peakRps * avgRounds * 2;            // 每任务轮次 × (模型+工具)
  const need = Math.ceil(toolDemand * avgToolMs / 1000); // 需要的并发槽（P95 口径）
  return { toolSlots: need, modelTpm: peakRps * avgRounds * 4000,  // 每轮约4k token
    queueDepth: peakRps * 30 };                           // 队列容量（30s平均时长）
}
```
