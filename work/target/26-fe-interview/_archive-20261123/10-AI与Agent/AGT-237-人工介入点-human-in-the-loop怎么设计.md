---
title: [AGT-237] Human-in-the-loop——多 Agent 流程的人工审批点怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-237：Agent 工作流里的人工介入点（审批/纠偏）怎么设计？

**答**:
- 介入点三要素：触发条件（什么必须人来——高危操作/不可逆动作/低置信决策/合规要求）、呈现形式（给人的不是原始日志而是"决策卡"：选项+依据+风险摘要）、超时策略（审批超时的默认动作：暂停/按预设走/升级——必须预定义，不能挂着）。
- 挂起与恢复实现：工作流在审批节点持久化状态并挂起（不是轮询等待占资源），审批完成后带"人工决策+备注"恢复，决策本身写入 trace 供审计。
- 分级设计：全自动（低风险）/ 事后抽检（批量操作抽 X% 人审）/ 事前审批（高危）——分级依据操作风险与可逆性，全自动比例随信任积累逐步提高（灰度放权）。
- 体验细节：审批卡要可一键采纳/修改后采纳/拒绝并说明；拒绝原因回流到 prompt/规则（负反馈闭环），让同样错误不再触发审批。

```javascript
async function approvalNode(step, state) {
  if (!needsHuman(step)) return exec(step);      // 分级路由
  const card = buildDecisionCard(step);          // 选项+依据+风险
  const decision = await pendingApproval(card, {
    timeout: 24 * 3600e3,
    onTimeout: step.onTimeout || 'pause',        // 预定义超时策略
  });
  await trace.log({ type: 'human_decision', ...decision });
  if (decision.rejected) feedbackToPrompt(decision.reason); // 负反馈闭环
  return exec(step, decision);
}
```
