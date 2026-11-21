---
title: [AIC-087] 编码 Agent 的成本怎么核算与控制？「按任务计费」的账本长什么样？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-087：编码 Agent 的成本怎么核算与控制？「按任务计费」的账本长什么样？
**答**：
- 成本构成：token 消耗（输入常占大头——上下文贵）、轮次数量（agent 循环每轮都是一次完整调用）、失败重试（失败任务的成本经常是成功任务的 3~5 倍）、并行度放大效应。
- 账本设计：以任务为单位记账——task id、模型、轮次、输入/输出 token、费用、结果（成功/失败）；按任务类型聚合，找出「费效比」最差的类别。
- 控制手段：输入 token 预算（上下文裁剪，AIC-028）、轮次上限（AIC-083）、缓存复用（相同上下文前缀的 KV cache）、便宜模型先试（简单任务路由到小模型，AIC-160）。
- 预算护栏：任务开始前估算预估成本，超过阈值（如单任务 $1）需要人工放行；月度预算超 80% 告警。
- 追问钩子：成本优化的最大杠杆通常不是换便宜模型，而是「别让 agent 做错误的事」——失败任务砍一半，成本直接腰斩。

```javascript
// 任务账本 + 预算护栏
const ledger = [];
function billTask(taskId, model, usage, price) {
  const cost = (usage.input * price.input + usage.output * price.output) / 1e6;
  ledger.push({ taskId, model, ...usage, cost, at: Date.now() });
  const month = monthSum(ledger);
  if (month > BUDGET * 0.8) alert('月预算使用超 80%');
  return cost;
}
function preCheck(estimate) { return estimate < PER_TASK_LIMIT ? 'AUTO' : 'NEED_HUMAN_APPROVAL'; }
```
