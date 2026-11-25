---
title: [NODE-555] Node 服务的发票服务端（开具/冲红/税控对接）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-555：发票服务端
**答**:
- 模型：开票申请（抬头/订单集合/金额构成——可开票金额 = 订单实付 - 已开票，条件校验防超开）、发票记录（状态机：申请→开具中→已开/失败→冲红）。
- 税控对接：税控/电子发票平台 adapter（NODE-552 同构——提交开票/查询/下载）、异步开票（税控队列——任务状态推送 ARC-626）、开具失败处理（税号错误等可修正重开——失败原因结构化）。
- 冲红：退款后冲红（原发票冲红单 → 税控冲红——原发票状态联动）、部分冲红（部分退款按比例冲红——金额拆分规则）、冲红与重开（用户修正信息后重开）。
- 一致性：开票金额与订单对账（发票金额合计 ≤ 订单实付——开票额度表）、发票与退款联动（退款事件 → 待冲红提醒任务）。
- 合规：开票要素校验（税率/抬头规范——合规规则引擎）、发票数据保留（税务留存要求——不可删除，归档策略）。
```javascript
// 开票与额度
async function issueInvoice(app) {
  const usable = await invoiceQuota(app.orderIds);               // 实付-已开
  if (app.amount > usable) throw new InvoiceOverdraw(usable);    // 防超开
  const task = await taxAdapter.submit(app);                     // 税控队列
  await invoiceRepo.create({ ...app, state: 'processing', taxTask: task.id });
}
bus.on('refund.done', e => scheduleRedInvoice(e.orderId));       // 退款冲红任务
```
