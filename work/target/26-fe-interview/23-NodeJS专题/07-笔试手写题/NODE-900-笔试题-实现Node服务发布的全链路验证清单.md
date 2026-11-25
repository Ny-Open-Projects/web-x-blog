---
title: [NODE-900] 笔试题——实现发布全链路验证清单（端到端可执行版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-900：手写全链路验证

**需求与边界**：
- 需求：发布验证清单（SCN-NODE-800/OPS-229）——① 端到端检查项（前端→BFF→服务→DB——全链，SCN-NODE-800 扩展）；② 每项自动断言（SCN-NODE-800）；③ 验证结果的发布档案（SCN-OPS-248）；④ 失败项的修复指引。
- 边界：① 全链的覆盖（前端产物/网关/灰度/DB 迁移/依赖——SCN-OPS-261 影响）；② 验证的分级（阻断/建议——SCN-OPS-229）；③ 清单的版本化演进（SCN-ENG-330）。

**答**：
```javascript
const E2E_CHECKS = [
  { name: 'frontend-bundle', run: () => verifyBuildinfo(frontendBuild), level: 'block' },   // SCN-ENG-303
  { name: 'gateway-routing', run: () => verifyGrayRouting(), level: 'block' },   // SCN-NODE-776
  { name: 'bff-aggregation', run: () => testAggregation(), level: 'block' },   // SCN-NODE-813
  { name: 'db-migration', run: () => verifyMigrationState(), level: 'block' },   // SCN-NODE-766
  { name: 'cache-keys', run: () => verifyCacheDims(), level: 'warn' },   // SCN-NODE-805
  { name: 'degrade-path', run: () => verifyDegradeChain(), level: 'block' },   // SCN-NODE-778
];
async function releaseVerification(release) {
  const results = [];
  for (const c of E2E_CHECKS) {
    const ok = await c.run().catch(() => false);
    results.push({ ...c, ok, fix: ok ? null : FIX_HINTS[c.name] });   // 修复指引
  }
  const blocked = results.filter(r => !r.ok && r.level === 'block');
  const archived = releaseArchive(release, results);   // 发布档案（SCN-OPS-248）
  return { pass: !blocked.length, blocked, archived };   // SCN-OPS-229 分级
}
```

**评分点**:
- 全链六项（前端/网关/BFF/DB/缓存/降级）各引用前文编号。
- 阻断/建议分级（SCN-OPS-229）。
- 修复指引 + 发布档案（SCN-OPS-248）。
- 清单版本化（SCN-ENG-330）。
