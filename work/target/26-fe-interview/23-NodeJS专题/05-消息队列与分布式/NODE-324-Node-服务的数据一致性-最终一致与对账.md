---
title: [NODE-324] Node 服务的数据一致性：最终一致与对账？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-324：Node 服务的数据一致性：最终一致与对账？
**答**:
- 最终一致体系：写路径走 outbox+MQ（NODE-288）保证至少一次；读路径容忍短时不一致（前端乐观更新对齐）。
- 对账兜底：定时对账任务（两侧数据比对）+ 差异修复队列——最终一致的"最后防线"；对账频率按业务敏感度（交易小时级/内容天级）。
- 补偿事务：Saga 模式——正向操作失败走逆向补偿（扣库存失败→退积分）；补偿也要幂等。
- 监控：对账差异率指标——持续非零说明系统设计有 bug 而非偶发。

```javascript
// 对账任务（小时级）
async function reconcile() {
  const local = await db.order.count({ status: 'paid', updatedIn: hour });
  const remote = await payService.count(hour);
  if (local !== remote) {
    const diff = await diffOrders(hour);            // 差异明细
    for (const d of diff) await fixQueue.add('reconcile', d);   // 差异进修复队列
    metrics.inc('reconcile.diff', diff.length);
  }
}
// Saga 补偿
const saga = [
  { do: () => stockService.deduct(sku), undo: () => stockService.restore(sku) },
  { do: () => pointsService.add(uid, pts), undo: () => pointsService.deduct(uid, pts) },
];
// 失败：已完成步骤逆序补偿（每步幂等 NODE-283）
```
