---
title: [NODE-591] Node 服务的客服工单（分类/路由/SLA）服务端如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-591：客服工单服务端
**答**:
- 工单模型：分类体系（问题类型树——路由与统计维度）、优先级（P0~P3——SLA 差异）、状态机（待分配→处理中→待用户→已解决/关闭—— reopen 支持）。
- 路由引擎：自动分配（按分类+负载——技能组路由：会话语言/问题域匹配客服技能）、升级规则（SLA 超时升级 ARC-452 服务端）、会话转工单（IM 会话未解决 → 生成工单带上下文 ARC-526）。
- SLA 管理：分级响应/解决时效（P0 1h/P1 4h——超时升级与告警）、SLA 达成率报表（瓶颈分析）、暂停语义（待用户回复时 SLA 暂停——计时规则）。
- 知识辅助：客服辅助（相似工单检索/知识库推荐——AI 辅助回复建议人审）、话术模板。
- 闭环：用户满意度（解决后评价）、问题归因分类（Top 问题类型 → 产品改进——客服数据反哺业务）。
```javascript
// 工单路由
async function route(ticket) {
  const skill = classify(ticket);                                // 分类模型/规则
  const agent = await dispatcher.pick({ skill, load: balance(),
    lang: ticket.lang, tier: ticket.priority });
  if (!agent) return queue.push(ticket, { sla: SLA[ticket.priority] });
  await assign(ticket, agent);
}
// SLA：overdue() → escalate(assigneeManager) + alert
```
