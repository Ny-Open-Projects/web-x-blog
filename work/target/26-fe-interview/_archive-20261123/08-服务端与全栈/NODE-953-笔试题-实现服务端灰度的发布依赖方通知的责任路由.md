---
title: [NODE-953] 笔试题——实现发布通知责任路由（消费方→对接人）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-953：手写责任路由

**需求与边界**：
- 需求：通知责任路由（SCN-OPS-241/953）——① 消费方 → 对接人解析（角色路由——SCN-OPS-241）；② 代理规则（缺勤——SCN-OPS-241）；③ 通知的优先级（SLA 分级——SCN-OPS-891）；④ 路由的审计（SCN-OPS-220）。
- 边界：① 角色解析的活性（SCN-ENG-314 活跃成员）；② 通知的 ack（SCN-OPS-864）；③ 路由的自批防御（SCN-OPS-253）。

**答**：
```javascript
function notifyRoute(consumer, event) {
  const role = consumer.ownerRole;                     // 角色路由（SCN-OPS-241）
  const active = activeMembers(role, { exclude: event.initiator });   // 活跃 + 自批防御（SCN-OPS-253）
  const priority = event.sla === 'P0' ? 'urgent' : 'normal';   // SLA 优先级（SCN-OPS-891）
  return active.map(u => ({ to: u, priority,
    ackRequired: priority === 'urgent' }));            // ack（SCN-OPS-864）
}
```

**评分点**:
- 角色路由 + 活跃成员（SCN-OPS-241/ENG-314）。
- SLA 优先级（SCN-OPS-891）。
- 自批防御 + ack（SCN-OPS-253/864）。
- 审计（SCN-OPS-220）。
