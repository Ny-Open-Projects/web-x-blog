---
title: [1047] 多 Agent 任务的成本账单怎么出（给业务方看）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 成本]
type: 面试题
---

## 1047：多 Agent 任务的成本账单怎么出（给业务方看）

**答**：
- 账单维度：任务 ID → 子 Agent → 模型调用/工具调用，聚合成「业务方可懂」的单位（每次问答成本、每份报告成本），业务方看不懂 token，要翻译成钱和单位。
- 分摊规则：基础设施成本（编排器、监控）按任务量均摊，直接成本（模型 token、外部 API）按实际用量计入——两栏分开，防「为什么我多用一次贵 10 倍」的扯皮。
- 异常标注：账单里超预算任务单独标出并附归因链接，业务方能自查「贵在哪」而不是来问平台。
- 追问钩子：账单粒度多细合适？——任务级到业务方、Agent 级到平台团队、调用级只进 trace；粒度越细维护成本越高，按受众分层。

```ts
function bill(task) {
  const direct = sum(task.calls.filter(c => c.billable), c => costOf(c));
  const infra = infraRate * taskUnits(task);        // 基础设施均摊
  return { unit: task.unitCost, direct, infra, over: direct + infra > task.budget,
    breakdown: groupBy(task.calls, c => c.agent) };  // 明细供自查
}
```
