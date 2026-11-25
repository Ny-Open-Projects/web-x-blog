---
title: [NODE-929] 笔试题——实现多服务发布协同看板（发布计划进度）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-929：手写协同看板

**需求与边界**：
- 需求：多服务看板（SCN-OPS-207/924）——① 发布计划进度（各服务阶段——SCN-OPS-207 看板）；② 卡点标注（步骤超时——SCN-OPS-207）；③ 联动状态（依赖服务的灰度健康——SCN-NODE-924）；④ 决策入口（SCN-OPS-253）。
- 边界：① 看板的实时性（事件流——SCN-OPS-207）；② 卡点检测（SCN-OPS-207）；③ 决策的权限（SCN-OPS-253）。

**答**：
```javascript
async function multiServiceBoard(plan) {
  const progress = plan.services.map(s => ({
    app: s.app, stage: s.stage, stuck: isStuck(s, 10 * 60_000),   // 卡点（SCN-OPS-207）
    health: canaryHealth(s),                           // 联动健康（SCN-NODE-924）
  }));
  const stuckAny = progress.some(p => p.stuck);
  if (stuckAny) notifyOwner(progress.find(p => p.stuck));   // 卡点通知（SCN-OPS-207）
  return {
    progress,
    buttons: allowedOps(plan).map(op => ({ action: op, require: op === 'rollback' ? 'oncall-mgr' : null })),   // 权限（SCN-OPS-253）
    audit: executionLog(plan),                         // 审计（SCN-OPS-273）
  };
}
```

**评分点**:
- 进度 + 卡点标注（SCN-OPS-207）。
- 联动健康（SCN-NODE-924）。
- 决策入口权限（SCN-OPS-253）。
- 审计（SCN-OPS-273）。
