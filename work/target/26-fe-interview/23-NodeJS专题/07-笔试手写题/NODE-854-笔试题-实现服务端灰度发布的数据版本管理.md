---
title: [NODE-854] 笔试题——实现数据版本管理（schema 版本 + 读写兼容）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-854：手写数据版本

**需求与边界**：
- 需求：数据版本管理（SCN-OPS-331/205）——① schema 版本戳（每条数据带 schemaVer）；② 版本迁移读（旧版本数据 → 迁移函数链——SCN-OPS-646）；③ 写路径版本化（写当前版本——SCN-OPS-331 expand）；④ 版本兼容矩阵（各代码版本 × 各 schema 版本——SCN-OPS-211）。
- 边界：① 迁移链的注册（SNAP_MIGRATIONS——SCN-OPS-646）；② 版本兼容矩阵的校验（CI——SCN-OPS-829 门禁）；③ 版本戳与灰度标记联动（SCN-NODE-670）。

**答**：
```javascript
// 数据带 schema 版本戳
await db.insert('orders', { ...order, schemaVer: 2 });
// 读路径迁移链（SCN-OPS-646）
const MIGRATIONS = { 1: (d) => ({ ...d, status: 'legacy' }), 2: (d) => d };
function readOrder(row) {
  let data = row;
  for (let v = row.schemaVer; v < CURRENT_SCHEMA_VER; v++)
    data = MIGRATIONS[v](data);                        // 逐版本迁移（SCN-OPS-646）
  return data;
}
// 写路径：当前版本（SCN-OPS-331 expand）
async function writeOrder(order) { return db.insert({ ...order, schemaVer: CURRENT_SCHEMA_VER }); }
// 兼容矩阵校验（CI——SCN-OPS-829）
for (const codeVer of RELEASED_VERSIONS)
  for (const schemaVer of [1, 2])
    assert(canRead(codeVer, schemaVer), `${codeVer} 不能读 schema ${schemaVer}——SCN-OPS-829 门禁`);
```

**评分点**:
- schema 版本戳 + 迁移链（SCN-OPS-646）。
- 写当前版本 / 读迁移（SCN-OPS-331 expand-contract）。
- 兼容矩阵 CI 校验（SCN-OPS-829 门禁）。
- 与灰度标记联动（SCN-NODE-670）。
