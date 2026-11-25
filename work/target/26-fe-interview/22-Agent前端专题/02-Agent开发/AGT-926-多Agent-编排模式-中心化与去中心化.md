---
title: [926] 多 Agent 系统的中心化编排和去中心化协作怎么选
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 架构模式]
type: 面试题
---

## 926：多 Agent 系统的中心化编排和去中心化协作怎么选

**答**：
- 中心化（Orchestrator-Worker）：一个主 Agent 分解任务、分派给专职子 Agent（检索/编码/审查），结果汇总。可控、易调试、token 成本可预测，是 90% 业务场景的正确起点。
- 去中心化（Agent 间对话协商）：适合「没有全局视角的分工」，如多方评审、辩论式校验；缺点是消息轮次不可控、成本易爆炸、难收敛。
- 选型判断题：任务能否预先画出 DAG？能就中心化+固定管线；不能但子任务边界清晰才考虑协商式。
- 追问钩子：为什么生产很少用纯去中心化？——无终止条件的对话很容易「礼貌循环」，必须配轮次预算和裁判 Agent。

```ts
// 中心化编排骨架
async function orchestrator(task: string) {
  const plan = await planner.run(task);            // 拆解为子任务 DAG
  const results = {};
  for (const step of plan.steps) {
    const worker = workers[step.type];             // coder / searcher / reviewer
    results[step.id] = await worker.run(step, results); // 注入上游结果
    if (!results[step.id].ok) return retryOrEscalate(step); // 失败升级而不是死磕
  }
  return synthesizer.run(results);
}
```

