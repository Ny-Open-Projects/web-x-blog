---
title: [SOFT-739] 手写 crisisAssign：故障时按资历/域自动分配角色（指挥/执行/沟通/记录）、预案缺失提醒？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-739：手写 crisisAssign：故障时按资历/域自动分配角色（指挥/执行/沟通/记录）、预案缺失提醒

**需求与边界**：
- 实现 crisisAssign(incident, people)。
- 边界要求：① 四角色：指挥（现场最资深+域匹配）/执行（按域分组分配）/沟通（对外口径 1 人）/记录（时间线 1 人）——一人可兼多角色但指挥与执行互斥；② 域匹配：incident.domain 与人的 skills 匹配优先；③ 预案检查：incident.type 对应预案存在则执行预案，缺失则提醒“先建最小止血方案”；④ 输出分工表+同步节奏（5 分钟一次）。

**答**：
```javascript
function crisisAssign(incident, people) {
  const hasPlaybook = PLAYBOOKS[incident.type];
  const ranked = people
    .filter(p => p.available)
    .sort((a, b) =>
      (b.seniority + (b.skills.includes(incident.domain) ? 2 : 0))
      - (a.seniority + (a.skills.includes(incident.domain) ? 2 : 0)));
  const commander = ranked[0];
  const executors = ranked.slice(1)
    .sort((a, b) => (b.skills.includes(incident.domain) ? 1 : 0)
      - (a.skills.includes(incident.domain) ? 1 : 0));
  const comms = people.find(p => p.id !== commander.id
    && p.goodAtWriting) ?? people[people.length - 1];
  const recorder = people.find(p => p.id !== commander.id
    && p.id !== comms?.id) ?? ranked[ranked.length - 1];
  return {
    playbook: hasPlaybook ? `执行预案${incident.type}` :
      '⚠️无预案——先建最小止血方案（影响面确认→止损开关→恢复验证）',
    roles: { commander: commander.id,
      executors: executors.map(p => p.id),
      comms: comms?.id, recorder: recorder?.id },
    note: '指挥与执行互斥；对外口径仅comms出口；同步节奏5min',
  };
}
```

**评分点**:
- 资历+域匹配的指挥选择（指挥与执行互斥——定盘优先于动手）。
- 预案缺失提醒（无预案先建最小止血——SOFT-729 准则落地）。
- 沟通与记录独立角色（信息纪律结构化）。

