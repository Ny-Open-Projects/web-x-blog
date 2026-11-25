---
title: [NODE-865] 笔试题——实现双活单元数据校验（切流后对账）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-865：手写单元对账

**需求与边界**：
- 需求：双活切流对账（SCN-NODE-852/682）——① 切流期间的写入双校验（单元切换窗口的数据——SCN-NODE-852 故障切换）；② 单元间数据同步校验（跨单元复制——SCN-OPS-195）；③ 差异修复（SCN-OPS-227 善后）；④ 切流回滚的数据一致性（SCN-OPS-277）。
- 边界：① 对账键（orderId——SCN-FIN-552）；② 对账窗口（切流时间窗——SCN-NODE-852）；③ 对账的自动化（定时——SCN-NODE-682 分片）。

**答**：
```javascript
async function unitReconcile(afterFailover) {
  const window = failoverWindow(afterFailover);        // 切流窗口（SCN-NODE-852）
  const mine = await primaryUnit.orders(window);       // 主单元
  const replica = await backupUnit.orders(window);     // 备单元（SCN-OPS-195 同步）
  const diff = reconcilePair(mine, replica);           // SCN-FIN-552 匹配
  for (const d of diff) {
    if (d.kind === 'REPLICA_MISSING' && d.autoFixable)
      await backupUnit.replay(d.record);               // 自动补（幂等——SCN-NODE-655）
    else await enqueueDiffTicket(d);                   // 人工池
  }
  if (diff.length) blockFailoverComplete();            // 差异未清阻塞切流完成（SCN-OPS-227）
  return { diff: diff.length, autoFixed: diff.filter(d => d.autoFixable).length };
}
```

**评分点**:
- 切流窗口对账（SCN-NODE-852）。
- 自动补 + 人工池分流（SCN-NODE-655/OPS-259）。
- 差异未清阻塞切流完成（SCN-OPS-227 善后）。
- 单元间同步校验（SCN-OPS-195）。
