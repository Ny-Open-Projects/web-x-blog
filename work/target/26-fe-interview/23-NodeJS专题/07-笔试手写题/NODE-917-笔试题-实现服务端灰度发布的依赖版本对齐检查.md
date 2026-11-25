---
title: [NODE-917] 笔试题——实现灰度发布依赖版本对齐检查（canary 依赖）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-917：手写依赖对齐

**需求与边界**：
- 需求：canary 依赖对齐（SCN-NODE-844/844）——① canary 依赖的 canary 版本检查（接口依赖声明——SCN-NODE-844 DAG）；② 依赖未就绪的处理（回 stable——SCN-NODE-844）；③ 依赖版本矩阵（SCN-OPS-211）；④ 对齐的审计（SCN-OPS-273）。
- 边界：① 依赖声明的来源（发布计划——SCN-OPS-291 影响面）；② 依赖的运行时校验（canary 实际调用版本——SCN-OPS-231）；③ 对齐的 CI（SCN-OPS-229）。

**答**：
```javascript
async function canaryDepsCheck(release) {
  const deps = release.apiDeps;                        // 接口依赖（SCN-NODE-844 DAG）
  const unready = deps.filter(d => !canaryActive(d));  // 依赖未就绪
  if (unready.length) {
    audit({ release: release.id, unready });           // 审计（SCN-OPS-273）
    return { ready: false, unready,
      action: '依赖未就绪——回 stable（SCN-NODE-844）或先发布依赖（SCN-OPS-291 影响面）' };
  }
  const runtimeCheck = await verifyRuntimeVersions(deps);   // 运行时版本（SCN-OPS-231）
  return { ready: runtimeCheck.ok, matrix: compatMatrix(release, deps) };   // SCN-OPS-211
}
```

**评分点**:
- 依赖 DAG 声明校验（SCN-NODE-844）。
- 未就绪回 stable（SCN-NODE-844）或先发依赖（SCN-OPS-291）。
- 运行时版本验证（SCN-OPS-231）。
- 兼容矩阵（SCN-OPS-211）。
