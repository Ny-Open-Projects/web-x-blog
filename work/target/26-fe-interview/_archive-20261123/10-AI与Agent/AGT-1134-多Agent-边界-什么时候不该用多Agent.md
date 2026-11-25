---
title: [1134] 哪些场景用多 Agent 是过度设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 选型]
type: 面试题
---

## 1134：哪些场景用多 Agent 是过度设计

**答**：
- 过度设计信号：单 Agent 一次调用能完成（拆开只增加延迟与成本）、子任务间强耦合（拆了以后全是传话开销）、团队没有可观测与评测基建（多 Agent 的调试成本承受不住）。
- 多 Agent 的真实收益来源：上下文隔离（各干各的互不污染）、并行（独立任务提速）、专业化（各自 prompt/工具集优化到位）——不在这三点的拆分都是负收益。
- 判断公式：拆分的协调成本（消息传递、状态同步、失败处理）< 收益（质量提升 + 延迟降低）才拆；先用数据估，再动手。
- 追问钩子：「多 Agent 看起来更厉害」是不是理由？——不是，架构选择只看指标（质量/延迟/成本/可维护性）；从单 Agent 起步、有痛点再拆，是大概率正确的路径。

```ts
function shouldSplit(single, proposal) {
  const benefit = proposal.qualityGain + latencyGain(proposal.parallel);
  const cost = proposal.coordinationOverhead + opsCost; // 协调与运维成本
  return benefit > cost && proposal.isolatable;  // 收益为正且可隔离
}
// 经验：单 Agent + 好 prompt 常常赢过草率的 5-Agent 拓扑
```

