---
title: [NODE-452] Node 服务的内部工单系统（审批/流转/SLA）服务端如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-452：内部工单系统服务端
**答**:
- 核心：流程引擎（状态机 + 审批人解析 + 条件分支 ARC-453 服务端版）+ 表单 schema 校验 + SLA 计时（节点超时升级/提醒）。
- 审批人解析：按角色/按主管链/按值班表——解析服务独立（组织架构同步源），解析失败兜底（默认管理员 + 告警，防工单卡死无人审批）。
- 幂等与并发：工单操作幂等（操作 ID 去重 NODE-381）、并发审批冲突（两人同时审批——先到先得，后到收到状态冲突）；状态变更单点串行（同工单按 orderId 分区 MQ，NODE-412）。
- SLA 治理：每节点 SLA 配置、超时自动升级（提醒 → 升级上级 → 挂起告警）、SLA 达成率报表（流程瓶颈分析——哪一步总是超时）。
- 与业务联动：工单结果回调业务（审批通过 → 触发业务动作，本地消息表保证可靠触发 NODE-380）。
```javascript
// SLA 超时升级
schedule.checkOverdue(async (node) => {
  if (node.overdue > sla(node.type)) {
    if (node.reminds < 2) await notify(node.assignee, 'SLA 临期');
    else { await escalate(node, node.assigneeManager);           // 升级主管
           alertOps(`工单 ${node.id} SLA 超时已升级`); }
  }
});
// 审批人解析：resolver.byRole(role) → resolver.byManagerChain(uid) → fallback admin + alert
```
