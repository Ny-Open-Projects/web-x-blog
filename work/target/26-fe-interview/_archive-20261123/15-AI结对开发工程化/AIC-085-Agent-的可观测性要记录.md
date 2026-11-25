---
title: [AIC-085] 生产中跑的编码 Agent，可观测性要记录什么？出问题后靠什么回放现场？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-085：生产中跑的编码 Agent，可观测性要记录什么？出问题后靠什么回放现场？
**答**：
- 记录三层：决策层（任务输入、计划、每步意图）、执行层（每次工具调用的命令/文件/参数 + 返回摘要）、模型层（prompt/response、token 数、耗时、模型版本）。
- 回放现场的关键是「全链路 trace id」：一次任务一个 trace，所有日志带 trace 关联，出事后可以完整重演「它为什么决定改这个文件」。
- 隐私约束：日志里 prompt 可能含代码，存储要有级别控制与保留期；敏感 repo 的 trace 只存哈希摘要。
- 指标看板：任务成功率、平均轮次、工具调用分布、失败类型分布——观测不仅是排障，更是 agent 调优的数据源。
- 追问钩子：与 AIC-083 的失败报告衔接——超限失败时 trace 就是人工接管时的第一手材料。

```javascript
// agent 执行的结构化日志
function logStep(traceId, step) {
  logger.info({
    traceId, step: step.n,
    intent: step.intent,                       // 决策层
    tool: step.tool, args: redact(step.args),  // 执行层（脱敏）
    tokens: step.usage, model: step.model,     // 模型层
    result: summarize(step.result, 200),
  });
}
// 回放：按 traceId 聚合全部日志重建时间线
```
