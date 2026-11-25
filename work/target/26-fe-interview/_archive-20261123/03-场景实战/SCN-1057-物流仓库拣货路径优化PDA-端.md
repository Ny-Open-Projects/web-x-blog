---
title: [SCN-1057] 物流仓库拣货路径优化（PDA 端）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1057：物流仓库拣货路径优化（PDA 端）

**答**：
- 拣货：订单合并拣货（波次），路径优化（按库位顺序排序拣货任务）。
- PDA：扫码确认（防拣错）、缺货即时上报（库存联动）。
- 效率：拣货路径长度对比（优化前后 KPI）。

```javascript
// 拣货路径
function pickPath(tasks, layout) {
  return tasks.sort((a, b) =>
    layout.order(a.location) - layout.order(b.location));   // 库位序
}
function pickConfirm(task, barcode) {
  if (barcode !== task.sku) return { ok: false, reason: '商品不匹配' };
  return api('/pick/confirm', { taskId: task.id });
}
// 缺货：pickShort(task) -> 库存系统即时锁定替换
```
