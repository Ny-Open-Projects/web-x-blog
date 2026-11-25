---
title: [1127] 单 Agent 太复杂了，怎么拆成多 Agent
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 重构]
type: 面试题
---

## 1127：单 Agent 太复杂了，怎么拆成多 Agent

**答**：
- 拆分信号：prompt 超长（系统指令 3k+）、行为互斥（一个 Agent 干互相冲突的事）、工具集混用导致选择错误率上升——满足其一就值得拆。
- 拆分路径渐进式：先「内部分支」再「外部 Agent」——把单 Agent 里的任务类型分支先整理成显式路由（意图 → 分支 prompt），分支稳定后再把每个分支独立成子 Agent（独立上下文与工具集），风险分两步释放。
- 拆分后回归：拆分前后跑同一评估集对比，端到端指标不降级才算拆成；中间态（路由 + 分支）作为回滚锚点。
- 追问钩子：拆完反而更差怎么办？——常见原因是拆分后上下文传递丢信息（子 Agent 缺全局视野），解法是任务书强化（见上下文工程卡）而不是合并回去。

```ts
// 第一步：内部分支（单 Agent 显式路由）
const branch = pickBranch(intent);    // qa | coding | review
// 第二步：分支稳定后独立成子 Agent
const agent = branch === 'coding' ? coderAgent : qaAgent;
// 拆分验收：同一评估集，拆前 vs 拆后
const cmp = await evalBoth(splitEvalSet, before, after);
if (cmp.after.acc < cmp.before.acc) return rollbackToBranchMode();
```

