---
title: [934] 多 Agent 自动化流程里，哪些环节必须留人工审批门
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 人机协同]
type: 面试题
---

## 934：多 Agent 自动化流程里，哪些环节必须留人工审批门

**答**：
- 审批门放「不可逆 + 高影响」动作：对外发送（邮件/公告）、资金/权限变更、删除操作、发布上线；其余环节自动执行。
- 干预点设计：审批请求携带「Agent 的计划 + 依据 + 影响面」三件套，人审的不是话术而是计划；支持「批准/修改后批准/拒绝并给理由」。
- 超时策略：审批超时默认拒绝（fail-closed），不要默认通过；紧急通道需二次鉴权。
- 追问钩子：审批门太多拖慢流程怎么办？——按风险分级别自动化（低风险免审、中风险抽审、高风险全审），抽审比例随该类操作的历史通过率动态调整。

```ts
async function gatedAction(plan) {
  if (plan.risk === 'low') return execute(plan);           // 免审
  const ticket = await approval.create({
    plan: plan.summary, evidence: plan.evidence, impact: plan.impact,
    ttl: plan.risk === 'high' ? '24h' : '4h',
  });
  const decision = await approval.wait(ticket, { timeoutMs: ttl(plan) });
  if (decision.action === 'reject') return recordReject(plan, decision.reason);
  return execute(plan.modified ?? plan);                   // 修改后批准
}
```

