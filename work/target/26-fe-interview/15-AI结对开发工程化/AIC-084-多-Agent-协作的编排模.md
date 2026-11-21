---
title: [AIC-084] 多 Agent 协作（如一个写码一个审查）有哪些编排模式？什么场景值得用、什么场景是过度设计？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-084：多 Agent 协作（如一个写码一个审查）有哪些编排模式？什么场景值得用、什么场景是过度设计？
**答**：
- 常见编排：主从式（一个 orchestrator 拆任务分派、汇总结果）、流水线式（生成 agent → 审查 agent → 修复 agent 串行）、对抗式（写/审两个角色互相挑错，类似 AIC-048 交叉审查）。
- 值得用的场景：任务可并行拆分（多文件批量迁移）、需要独立视角（生成者自查存在自我偏好）、上下文隔离（审查者不该被生成过程污染）。
- 过度设计信号：agent 数量超过 3 个还没有清晰的输入输出契约；orchestrator 本身复杂到需要调试；简单单文件任务也套多 agent——通信成本超过收益。
- 工程要点：agent 间的交接物必须是结构化产物（diff + 说明 + 验证结果），不能是对话记录；每个 agent 有独立上下文与独立权限。
- 追问钩子：先问「单 agent + 好 checklist 能不能解决」再上多 agent——多数团队的问题不是 agent 不够多，是任务定义不够清。

```javascript
// 流水线式编排（生成→审查→修复）
async function pipeline(task) {
  const gen = await agent('coder', task);
  let review = await agent('reviewer', { code: gen, checklist: REVIEW_LIST });
  let rounds = 0;
  while (review.blockers.length && rounds++ < 3) {
    const fixed = await agent('fixer', { code: gen, findings: review });
    review = await agent('reviewer', { code: fixed, checklist: REVIEW_LIST });
  }
  return { code: gen, review, passed: !review.blockers.length };
}
```
