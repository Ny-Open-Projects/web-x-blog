---
title: [NODE-441] Node 服务的数据导出（含敏感数据）链路如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-441：数据导出（含敏感数据）链路
**答**:
- 导出 = 数据出域，安全优先：导出权限（字段级——哪些字段允许导出，配额与审批 ARC-439）、导出审计（谁在何时导出了什么范围，ARC-073）、敏感字段默认脱敏（手机号掩码/哈希，NODE-396 规则复用）。
- 链路实现：导出任务（异步 ARC-382 服务端流式生成）→ 产出文件水印（用户 ID 隐写 + 页脚明示，泄露可追责）→ 签名 URL 短时效下载 → 下载记录留痕。
- 一致性：导出快照时间点标注（导出的是"生成时刻"数据，注明时点；大数据量导出用一致性快照（从库 + 单事务/统一时间锚）避免导出过程中数据变化导致不一致）。
- 性能与配额：导出走只读副本 + 限流（NODE-437 错峰）、并发配额（每用户 1 个活跃导出任务）。
- 合规：数据出境（若导出到外部）走 DPA 评估（NODE-436）、用户行使数据权利（个人信息导出）的专项通道（合规要求响应时效）。
```javascript
// 导出任务 + 水印
async function createExport(userId, query) {
  await quota.take(`export:${userId}`, 1);                       // 配额预扣
  const task = await mq.add('export', { userId, query,
    fields: await allowedFields(userId, query),                  // 字段级权限
    watermark: hashUid(userId) });
  return task.id;                                                // 完成 → 水印文件 → 签名 URL → 审计
}
```
