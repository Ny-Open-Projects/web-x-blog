---
title: [NODE-899] 笔试题——实现多环境发布差异校验（config + data 双检）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-899：手写双检

**需求与边界**：
- 需求：发布差异校验（SCN-ENG-861/886）——① 配置差异（SCN-ENG-861 漂移）；② 数据差异（迁移状态对齐——SCN-OPS-331 版本表）；③ 依赖服务版本差异（SCN-OPS-254）；④ 差异修复建议。
- 边界：① 预期差异白名单（SCN-ENG-861）；② 差异的阻断级别（硬缺失阻断/软漂移警告——SCN-OPS-229）；③ 差异报告（SCN-OPS-261）。

**答**：
```javascript
async function multiEnvCheck(release) {
  const config = await configSyncCheck(release);       // SCN-886 配置检
  const migrations = await db.migrationStatus();       // 迁移状态（SCN-OPS-331）
  const pendingMigrations = release.migrations.filter(m => !migrations.includes(m.name));   // 迁移未执行
  const depVersions = await dependencyVersions(release);   // 依赖版本（SCN-OPS-254）
  const drift = depVersions.filter(d => d.staging !== d.prod);   // 依赖漂移
  return {
    blocked: config.blocked || pendingMigrations.length,   // 硬阻断（迁移未执行）
    pendingMigrations, drifted: drift,
    softWarn: drift.map(d => `${d.name} 版本不一致（SCN-OPS-254）`),   // 软警告
    report: forReviewBoard({ config, migrations, drift }),   // SCN-OPS-261
  };
}
```

**评分点**:
- 配置 + 迁移 + 依赖三维校验（SCN-ENG-861/OPS-331/254）。
- 硬阻断（迁移未执行）与软警告（依赖漂移）分级（SCN-OPS-229）。
- 报告进评审（SCN-OPS-261）。
- 补齐建议（SCN-886）。
