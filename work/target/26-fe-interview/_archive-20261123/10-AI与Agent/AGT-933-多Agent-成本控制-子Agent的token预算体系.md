---
title: [933] 多 Agent 系统 token 消耗是单 Agent 的 10 倍，预算体系怎么建
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 成本]
type: 面试题
---

## 933：多 Agent 系统 token 消耗是单 Agent 的 10 倍，预算体系怎么建

**答**：
- 预算三级下发：任务总预算 → 编排器按子任务分配 → 子 Agent 单轮上限；任何一级超限触发「总结当前进展并收尾」而不是硬截断。
- 砍成本三板斧：子 Agent 用小模型（80% 的子任务不需要旗舰模型）、上下文最小化传递、重复检索结果全局缓存。
- 成本可见性：每次调用记录（任务 ID、Agent、模型、token 数），按任务聚合出成本瀑布，找出最贵的环节针对性优化。
- 追问钩子：预算用完任务没做完怎么办？——输出「已完成 + 剩余步骤建议」，比半截产物或静默失败都有用。

```ts
class Budget {
  constructor(total) { this.total = total; this.left = total; }
  spend(tokens, by) {
    if (tokens > this.left) throw new BudgetExceeded(by);
    this.left -= tokens;
    metrics.record('token_cost', { by, tokens });
  }
}
// 编排器按计划分配
plan.steps.forEach(s => s.budget = new Budget(total * s.weight));
```

