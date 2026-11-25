---
title: [1085] 成本类实验（砍上下文/换小模型）怎么设计才可信
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, 实验]
type: 面试题
---

## 1085：成本类实验（砍上下文/换小模型）怎么设计才可信

**答**：
- 成本实验三原则：对照同时期跑（排除流量结构变化的干扰）、质量护栏同测（成本降了质量崩了等于白干）、按意图分层看（某些意图成本敏感某些不敏感，一刀切结论会误导）。
- 常见误读：平均成本下降不等于成本问题解决——长尾任务（P95 成本）才是烧钱大头，实验要报分位数不报均值。
- 实验周期：至少覆盖一个完整流量周期（周），且避开大促等异常期。
- 追问钩子：成本实验和 A/B 质量实验能合并吗？——可以且应该：一次实验同时采质量与成本数据，分层交叉分析（哪个意图「质降费降」「质稳费降」），一次流量成本出双结论。

```ts
function costExpReport(exp, control) {
  return {
    avg: pctChange(control.avgCost, exp.avgCost),      // 均值（易误导）
    p95: pctChange(control.p95Cost, exp.p95Cost),      // 分位数（真问题）
    quality: qualityGuard(exp),                        // 质量护栏
    byIntent: intents.map(i => ({ intent: i,
      cost: pctChange(control.byIntent[i].cost, exp.byIntent[i].cost),
      acc: accDelta(i) })),                            // 分层交叉
  };
}
```

