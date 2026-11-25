---
title: [NODE-908] 笔试题——实现数据迁移的灰度验证（迁移后读路径验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-908：手写迁移验证

**需求与边界**：
- 需求：迁移灰度验证（SCN-OPS-331/832）——① 迁移后读路径验证（新 schema 读——旧代码兼容，SCN-OPS-832 三层）；② 迁移期间的双写校验（SCN-NODE-793）；③ 迁移完成的准出（验证通过——SCN-OPS-331 门禁）；④ 迁移回滚演练（SCN-NODE-766 down）。
- 边界：① 验证与迁移的分阶段（expand 后验证/migrate 后验证/contract 前验证——三节点）；② 验证失败的处理（暂停 contract——SCN-OPS-348）；③ 验证的成本（抽样——SCN-OPS-331）。

**答**：
```javascript
const MIGRATION_GATES = [
  { after: 'expand', check: () => dualWriteDriftCheck(table, { tolerance: 0.001 }) },   // SCN-NODE-793
  { after: 'migrate', check: () => countReconcile(table) && sampleVerify(table) },   // SCN-OPS-331 对账
  { before: 'contract', check: () => oldVersionReadsNew(sampleRows) },   // SCN-OPS-832 三层
];
async function migrationGates(phase) {
  const gate = MIGRATION_GATES.find(g => g.after === phase || g.before === phase);
  const r = await gate.check();
  if (!r.pass) { pauseMigration(table); return { blocked: true, issues: r.issues }; }   // 暂停（SCN-OPS-348）
  markGatePassed(phase);
  return { pass: true };
}
```

**评分点**:
- 三节点门禁（expand/migrate/contract——SCN-OPS-331）。
- 旧版本读实测（SCN-OPS-832 三层）。
- 失败暂停（SCN-OPS-348 兜底）。
- 双写校验（SCN-NODE-793）。
