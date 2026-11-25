---
title: [SOFT-854] 手写 depNotify：依赖变更的分级通知执行（48h 前置/影响面计算/通知模板/漏报追踪）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-854：手写 depNotify：依赖变更的分级通知执行（48h 前置/影响面计算/通知模板/漏报追踪）

**需求与边界**：
- 实现 depNotify(graph, change)：graph 为依赖图（SOFT-838），change 含 { node, daysAhead }。
- 边界要求：① 影响面计算：change.node 的上游闭包（SOFT-838 impactOf）；② 分级：影响面 >2 团队→48h 前置+多通道；≤2→24h 前置+单通道；③ 通知模板生成（三要素 SOFT-573+依赖方专属影响说明）；④ 漏报追踪：前置期不足（daysAhead < 要求）记违规（摩擦复盘输入 SOFT-815）。

**答**：
```javascript
function depNotify(graph, change) {
  const impacted = graph.impactOf(change.node);   // 上游闭包 SOFT-838
  const scale = impacted.length;
  const need = scale > 2 ? 48 : 24;               // 前置小时要求
  const violation = change.daysAhead < need;
  const channels = scale > 2
    ? ['IM群', '邮件', '看板公告'] : ['IM群'];
  const perTeam = impacted.map(team =>
    `- ${team}：你的【${graph.artifactOf?.(change.node, team) ?? '相关交付物'}】受影响`);
  return {
    impacted,
    violation: violation
      ? { level: '漏报违规', note: `前置仅${change.daysAhead}h，要求${need}h——记入摩擦复盘（SOFT-815）` }
      : null,
    template: `【变更通知】${change.node}将变更\n影响面：${scale}个团队\n`
      + perTeam.join('\n') + `\n动作：请评估并回执\n详情：${change.link ?? '（补）'}`,
    channels,
    note: '回执追踪：未回执的依赖方24h后单点提醒' };
}
```

**评分点**:
- 影响面闭包驱动通知范围（SOFT-838 集成）。
- 前置期分级（>2 团队 48h/否则 24h）+ 违规追踪（纪律有牙齿）。
- 通知模板含依赖方专属影响说明（对方视角包 SOFT-559）。

