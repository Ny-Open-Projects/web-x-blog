---
title: [PER-1195] 如何处理"数据 inaccuracies"（数据准确性权）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1195：如何处理"数据 inaccuracies"（数据准确性权）

**答**：
- 要求：用户可更正不准确的数据（GDPR Art.16）；更正需传播到所有下游（派生表/缓存/第三方）。
- 实现：更正入口 → 验证身份 → 更正主数据 → 触发下游更正任务（同 DSAR 编排 1155）→ 完成回执。
- 难点：聚合/统计不回改（历史报表保持快照），只改可识别个人的当前数据。
- 留痕：更正前后值审计（脱敏存证），防止抵赖与误操作。

```javascript
// 数据更正编排
async function correctData(uid, field, newValue) {
  await verifyIdentity(uid);
  const before = await db.user.get(uid, field);
  await db.user.update(uid, { [field]: newValue });
  const downstream = traceFlow(`user.${field}`).flows;    // 1161
  await Promise.all(downstream.map(d => dispatch(d,
    { type: 'correct', uid: hash(uid), field, value: newValue })));
  logAudit(hash(uid), `correct:${field}`, 'GDPR Art.16');
  return { ok: true, before: maskField(field, before), downstream: downstream.length };
}
```
