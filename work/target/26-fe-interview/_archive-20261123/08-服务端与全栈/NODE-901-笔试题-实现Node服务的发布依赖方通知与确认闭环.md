---
title: [NODE-901] 笔试题——实现发布依赖方通知闭环（通知→确认→归档）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-901：手写通知闭环

**需求与边界**：
- 需求：发布通知闭环（SCN-OPS-864/303）——① 发布前预告（SCN-OPS-303）；② 发布中事件流（SCN-OPS-207）；③ 发布后摘要（SCN-OPS-298 回归）；④ ack 归档（谁确认过——SCN-OPS-220）。
- 边界：① 通知的降噪（SCN-OPS-320）；② 通知的责任路由（SCN-OPS-241）；③ 闭环的完整性检查（通知/ack/归档三态——SCN-OPS-289 审计）。

**答**：
```javascript
async function releaseNotifyLoop(release) {
  await preReleaseNotify(release);                     // 预告（SCN-OPS-864 ack 门）
  releaseEvents.on('*', (e) => notifyWatchroom(e));    // 事件流（SCN-OPS-207）
  const report = await releaseRegressionReport(release);   // 回归报告（SCN-NODE-897）
  await postSummary(report, { to: dependents, broadcast: true });   // 摘要
  const closed = ackedAll(dependents) && archived(report);   // 闭环检查（SCN-OPS-289）
  if (!closed) alert({ type: 'NOTIFY_LOOP_INCOMPLETE' });
  return { closed };
}
```

**评分点**:
- 三阶段通知（预告/事件流/摘要——SCN-OPS-303/207/897）。
- ack 归档闭环检查（SCN-OPS-289）。
- 责任路由（SCN-OPS-241）。
- 降噪（SCN-OPS-320）。
