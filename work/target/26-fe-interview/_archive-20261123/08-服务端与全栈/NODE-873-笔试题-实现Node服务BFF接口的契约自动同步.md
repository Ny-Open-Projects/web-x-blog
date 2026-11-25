---
title: [NODE-873] 笔试题——实现 BFF 契约自动同步（schema 变更→消费方通知）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-873：手写契约同步

**需求与边界**：
- 需求：契约自动同步（SCN-NODE-677/OPS-873）——① schema diff（SCN-ENG-247）；② 消费方影响分析（谁消费了变更字段——SCN-OPS-291）；③ 消费方通知 ack（SCN-OPS-864）；④ breaking 的版本策略（SCN-NODE-694）。
- 边界：① diff 的分类（add/remove/change——SCN-ENG-308）；② 消费方影响面（消费代码扫描——SCN-OPS-291）；③ 通知的 ack 门（SCN-OPS-864）。

**答**：
```javascript
async function schemaChangeSync(diff) {
  const breaking = diff.removed.length || diff.signatureChanged.length;   // SCN-ENG-308 分类
  const impacted = consumersOf(diff.changedFields);    // 影响分析（SCN-OPS-291）
  for (const c of impacted) {
    await notify({ to: c.ownerRole, payload: { diff, breaking }, ackRequired: breaking });   // ack（SCN-OPS-864）
  }
  if (breaking && !allAcked(impacted))
    return { gate: 'BLOCK_NEW_VERSION_RELEASE', unacked: impacted };   // breaking 未确认阻断（SCN-OPS-864）
  return { synced: true, impacted: impacted.length };
}
```

**评分点**:
- schema diff 分类（SCN-ENG-308）。
- 消费方影响分析（SCN-OPS-291）。
- breaking 未确认阻断（SCN-OPS-864 ack 门）。
- 契约测试联动（SCN-NODE-768 验证）。
