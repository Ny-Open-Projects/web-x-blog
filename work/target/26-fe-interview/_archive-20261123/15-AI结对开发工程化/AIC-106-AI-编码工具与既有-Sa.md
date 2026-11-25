---
title: [AIC-106] AI 编码工具如何与既有 SaaS（Code Review 平台、任务系统、监控）打通？数据流怎么设计？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-106：AI 编码工具如何与既有 SaaS（Code Review 平台、任务系统、监控）打通？数据流怎么设计？
**答**：
- 打通靠「网关 + 事件」：AI 工具侧产出（review 意见、生成报告、任务状态）统一进事件总线，订阅方各取所需——评论写入 Code Review 平台、状态回写任务系统、指标进监控看板。
- 数据流设计原则：① 单一事实源——AI 的意见以「门禁平台」为存储地，聊天工具里的只是转发 ② 双向关联——AI 意见要带 PR/任务/trace id 反链，任何一条数据能跳到全部上下文 ③ 幂等回写——重试不能造成重复评论（按 event id 去重）。
- 与监控打通的价值闭环：线上缺陷带「AI 生成标记」（AIC-074 的口径），缺陷率按生成方式分组统计——这是评估 AI 真实质量的最硬数据。
- 集成成本控制：优先用平台 webhook/Actions 原生能力，不要自建中间层；自建网关只在多工具混合时才值得。
- 追问钩子：打通的终点是「AI 成为流程里的一个角色」——有身份（trace）、有账户（计费）、有记录（审计），而不是游离的旁路工具。

```javascript
// 事件总线回写（幂等）
async function onAiEvent(e) {
  if (await seen(e.id)) return;                 // 幂等
  await markSeen(e.id);
  switch (e.type) {
    case 'review_finding': await postComment(e.pr, renderFinding(e)); break;
    case 'task_done': await updateTicket(e.ticket, { status: 'ai-done', report: e.report }); break;
    case 'incident_flag': await metrics.inc('ai_related_incident', { team: e.team });
  }
}
```
