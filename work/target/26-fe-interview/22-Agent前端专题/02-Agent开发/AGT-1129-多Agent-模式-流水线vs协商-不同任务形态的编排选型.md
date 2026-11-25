---
title: [1129] 流水线、路由、协商三种编排形态怎么按任务选
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 选型]
type: 面试题
---

## 1129：流水线、路由、协商三种编排形态怎么按任务选

**答**：
- 三形态：流水线（固定阶段串行/并行，确定性高）、路由分发（意图 → 专职 Agent，独立互不干扰）、协商协作（多 Agent 往返讨论，适合无标准答案的综合判断）。
- 选型锚点：任务能预先画流程图 → 流水线；任务互异且无依赖 → 路由；任务需要多方观点收敛（评审、权衡）→ 协商。多数业务是「路由为主 + 关键环节流水线」。
- 混合形态的边界清晰化：形态切换点要显式（路由决定进入哪条流水线、流水线某阶段触发协商），不要让 Agent 自由切换形态——形态自由 = 成本与延迟不可预测。
- 追问钩子：怎么评估形态选错了？——协商形态的轮次预算经常打满（收敛慢）说明该任务其实有标准流程，降级为流水线；流水线的分支覆盖不住真实流量（长尾意图），说明需要路由兜底。

```ts
// 形态注册与显式切换
const shapes = {
  qa: pipeline(['retrieve', 'answer']),          // 流水线
  coding: route({ bugfix: coderFix, feature: coderPlan }), // 路由
  design_review: negotiate({ budget: { rounds: 4 } }),     // 协商
};
function dispatch(task) {
  const s = shapes[task.kind] ?? shapes.qa;      // 默认形态兜底
  return s.run(task);                            // 形态切换点显式
}
```

