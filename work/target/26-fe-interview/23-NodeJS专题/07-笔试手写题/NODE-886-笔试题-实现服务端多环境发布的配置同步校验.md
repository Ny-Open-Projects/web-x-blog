---
title: [NODE-886] 笔试题——实现多环境发布配置同步校验（发布前检查）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-886：手写配置同步

**需求与边界**：
- 需求：发布前配置同步校验（SCN-ENG-237/861）——① 发布所需配置存在性（新版本依赖的配置项——SCN-NODE-663）；② 环境对齐（staging 验证过的配置 prod 已同步——SCN-ENG-237 漂移）；③ schema 校验（SCN-BLD-317）；④ 缺失配置阻断 + 补齐建议。
- 边界：① 配置依赖声明（新版本 required config keys——SCN-BLD-248）；② 配置的灰度同步（SCN-OPS-228）；③ 漂移报告（SCN-ENG-861 联动）。

**答**：
```javascript
async function configSyncCheck(release) {
  const required = release.requiredConfig;             // 版本声明的配置依赖（SCN-BLD-248）
  const missing = required.filter(k => !prodConfig.has(k));   // prod 缺失
  const drifted = diff(prodConfig, stagingConfig, { allow: EXPECTED_DIFFS });   // 漂移（SCN-ENG-861）
  const invalid = required.filter(k => !configSchema.safeParse(prodConfig.get(k)).success);   // schema（SCN-BLD-317）
  return {
    blocked: missing.length || invalid.length,
    missing: missing.map(k => ({ key: k, fix: `在 prod 配置中心添加 ${k}（值参照 staging）` })),   // 补齐建议
    drifted: unexpectedDrift(drifted),
  };
}
```

**评分点**:
- 配置依赖声明校验（SCN-BLD-248）。
- 环境漂移检测（SCN-ENG-861）。
- schema 校验（SCN-BLD-317）。
- 补齐建议（可行动）。
