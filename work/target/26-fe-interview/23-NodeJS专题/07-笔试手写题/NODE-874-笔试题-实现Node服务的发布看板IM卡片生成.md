---
title: [NODE-874] 笔试题——实现发布看板 IM 卡片生成（发布/灰度状态）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-874：手写发布卡片

**需求与边界**：
- 需求：发布 IM 卡片（SCN-OPS-325/207）——① 发布状态卡片（阶段/指标/决策记录——SCN-OPS-207 看板数据）；② 灰度日报卡片（SCN-OPS-325）；③ 可交互按钮（放量/回滚确认——SCN-OPS-253 权限校验）；④ 卡片刷新（状态回写——SCN-联想-634 卡片状态流转）。
- 边界：① 按钮权限（点击者校验——SCN-OPS-253）；② 卡片降噪（合并——SCN-OPS-612）；③ 状态回写幂等（SCN-NODE-655）。

**答**：
```javascript
function releaseCard(release) {
  return {
    title: `发布 ${release.app} v${release.version}`,
    stage: release.gray.stage + '%',
    verdicts: release.sentinel.verdicts,               // SCN-NODE-798 哨兵
    decisions: release.fsm.log.slice(-3),              // 决策记录（SCN-OPS-292）
    buttons: release.allowedOps.map(op => ({           // 权限过滤按钮（SCN-OPS-253）
      action: op, confirm: op === 'rollback' })),
    links: { board: releaseBoardUrl(release.id) },
  };
}
async function onCardAction(releaseId, action, user, cardToken) {   // SCN-联想-634 状态回写
  if (!hasReleasePermission(user, action)) throw new AppError('PERM_DENIED');   // 权限（SCN-OPS-253）
  const r = await execute(action, releaseId, { by: user });   // 幂等（SCN-NODE-655）
  await updateCard(releaseId, stateSummary(releaseId));   // 卡片刷新（SCN-联想-634）
  return r;
}
```

**评分点**:
- 卡片数据聚合（哨兵/决策/阶段——SCN-OPS-207/325）。
- 按钮权限校验（SCN-OPS-253）。
- 状态回写幂等 + 卡片刷新（SCN-NODE-655/联想-634）。
- 降噪（SCN-OPS-612）。
