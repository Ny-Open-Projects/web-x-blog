---
title: [AV-389] 协作冲突的语义层处理（除 CRDT 外的规则）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-389：协作冲突的语义层处理（除 CRDT 外的规则）

**答**：
- CRDT 保证数据收敛，不保证业务正确：如"删除被引用的图形"需语义校验。
- 规则集：操作前引用检查（对象存在/权限/锁）、服务端二次校验（防恶意）。
- 锁：显式编辑锁（谁在编辑这个对象 UI 提示）减少冲突发生。

```javascript
// 语义校验层
function validateOperation(op, doc) {
  const shape = doc.shapes.get(op.id);
  if (!shape && op.type !== 'create')
    return { ok: false, reason: '对象不存在（已被删除）' };
  if (shape?.lockedBy && shape.lockedBy !== op.userId)
    return { ok: false, reason: `被 ${shape.lockedBy} 锁定` };
  if (op.type === 'delete' && shape?.referencedBy?.length)
    return { ok: false, reason: '被其他对象引用' };
  return { ok: true };
}
```
