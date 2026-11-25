---
title: [932] 多 Agent 系统怎么评测？单 Agent 评测方法不够用在哪
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 评测]
type: 面试题
---

## 932：多 Agent 系统怎么评测？单 Agent 评测方法不够用在哪

**答**：
- 多 Agent 特有问题：接力损耗（信息在 Agent 间传递衰减）、循环抖动（两个 Agent 互相改对方的输出）、责任模糊（不知道哪个环节引入错误）。
- 评测三层：单 Agent 能力评测（复用单智能体方法）、协作过程评测（消息轮次、传导准确率、重试率）、端到端任务评测（完成率、人工评分、成本）。
- 关键指标「信息保真度」：任务书里的 N 个约束，最终产物保留几个——专门抓接力损耗。
- 追问钩子：怎么定位是哪个 Agent 的锅？——全链路 trace 按消息 ID 串联，每个产物标注生产者，回放坏 case 逐跳对比。

```ts
async function evalMultiAgent(task) {
  const trace = await orchestrator.run(task, { trace: true });
  const fidelity = task.constraints.filter(c =>
    trace.final.includes(c)).length / task.constraints.length;  // 信息保真度
  return {
    done: trace.success, fidelity,
    rounds: trace.msgCount, cost: trace.totalTokens,
    retries: trace.retries,                     // 协作过程健康度
  };
}
```

