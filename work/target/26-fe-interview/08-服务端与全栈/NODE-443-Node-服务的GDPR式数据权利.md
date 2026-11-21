---
title: [NODE-443] Node 服务的数据权利（导出/更正/删除/可携带）如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-443：数据权利落地（导出/更正/删除）
**答**:
- 用户数据权利四件：知情（收集清单公示 ARC-458）、访问与导出（个人信息导出通道，时效要求内完成——异步任务 ARC-441）、更正（自助修改 + 全链路同步）、删除（注销与"被遗忘权"）。
- 删除的架构难点：数据散落多存储（DB/ES/缓存/备份/日志/数仓）——删除编排器（各存储的删除任务 + 确认回执），备份中的数据按保留策略自然过期（说明义务），日志中 PII 短保留（NODE-396）。
- 删除级联：业务关联数据级联（订单保留但 PII 匿名化——法律要求留交易记录场景用"匿名化"替代"删除"，规则显式化）。
- 账号注销流程：冷静期（可撤回）→ 权益处理（余额/订阅确认）→ 数据删除编排 → 完成通知；注销状态跨系统同步（防残留登录 ARC-415 踢出）。
- 验证：删除完成度抽检（注销后全局搜索该用户标识应为零）、删除 SLA 监控。
```javascript
// 删除编排（各存储任务 + 回执）
const deletePlan = [
  { store: 'pg', run: () => anonymizeUserTables(uid) },          // 匿名化替代删除
  { store: 'es', run: () => es.deleteByQuery({ query: { term: { uid } } }) },
  { store: 'cache', run: () => redis.delPattern(`u:${uid}:*`) },
  { store: 'dw', run: () => scheduleDwPurge(uid, { sla: '30d' }) } // 数仓延迟清除
];
await orchestrate(deletePlan, { onDone: () => markPurged(uid) });// 完成度可追踪
```
