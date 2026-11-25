---
title: [AGT-293] 工具调用与审批的 UI——怎么呈现 Agent 的执行过程？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-293：Agent 的工具调用与人工审批，前端 UI 怎么呈现？

**答**:
- 过程透明化：工具调用以"步骤时间线"呈现（每步：工具名+简短参数摘要+状态+耗时），可展开看详情（完整参数/返回）——透明建立信任，也方便用户发现 Agent 跑偏及时打断。
- 审批交互：确认卡流内呈现（AGT-286 的决策卡：动作/diff/风险），阻塞式（流暂停等决策）或异步式（Agent 继续其他分支）；决策后卡片状态更新（已批准/已修改/已拒绝），决策原因回流。
- 失败呈现：工具失败展示"失败原因+Agent 的应对（重试中/已降级）"而不是裸 error——用户关心"还要不要等"而不是堆栈；重试次数与预计时间透明。
- 密度控制：多工具高频调用时折叠（默认显示当前步骤+摘要"已完成 12 步"，展开看全部）——过程可见性要与信息噪音平衡。

```jsx
function ToolTimeline({ steps }) {
  return steps.map(s => (
    <Step key={s.id} status={s.status} dur={s.duration}
      summary={brief(s.tool, s.args)}>
      <details>{JSON.stringify(s.args)}</details>
      {s.status === 'failed' && (
        <RetryInfo attempts={s.attempts} next={s.nextAction} />)}
      {s.type === 'approval' && <ApprovalCard {...s.card}
        onDecide={d => respond(s.id, d)} />}
    </Step>));
}
// 折叠：超过 5 步默认收起，显示当前+计数。
```
