---
title: [BLD-334] 笔试题——实现构建体系综合控制台（BLD 收束）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-334：手写构建控制台（BLD 收束）

**需求与边界**：
- 需求：整合 BLD 系列能力——① 流水线视图（阶段耗时/hook 剖析——SCN-BLD-300）、② 产物视图（体积报告/diff/重复检测——SCN-BLD-296/298）、③ 正确性视图（hash 稳定性/增量一致性/manifest 校验——SCN-BLD-295/332/306）、④ 治理视图（预算/Ratchet/插件注册表——SCN-ENG-291/331）、⑤ 信任视图（buildinfo/provenance——SCN-BLD-303/322）。
- 边界：① 各视图复用前文实现（引用编号）；② 控制台只聚合不做决策（与 OPS-333 同原则）；③ BLD 能力地图收束（291~333 索引）。

**答**：
```javascript
function buildConsole(buildId) {
  const build = buildStore.get(buildId);
  return {
    pipeline: {
      profiling: hookProfiler(build).report(),         // SCN-BLD-300 hook 剖析
      telemetry: telemetryAggregate(build.samples),    // SCN-BLD-312 聚合
    },
    artifact: {
      sizes: sizeReport(build.manifest, build.baseline, build.budgets),   // SCN-BLD-296
      duplicates: detectDuplicates(build.stats),       // SCN-BLD-298 双实例
      syntax: scanSyntaxArtifacts(build.bundle, build.targets),   // SCN-BLD-310 语法残留
    },
    correctness: {
      hashStability: moduleIdStability(bundler, project),   // SCN-BLD-311
      manifest: verifyManifest(build.manifest, dist),  // SCN-BLD-306
      buildinfo: verifyBuildinfo(build.buildinfo, dist),   // SCN-BLD-303
    },
    governance: {
      ratchet: ratchetFile, budgets: build.budgets,    // SCN-ENG-291/265
      plugins: pluginGovernance(registry, measured),   // SCN-BLD-331
    },
    trust: { provenance: verifyProvenance(build.provenance, pubKey) },   // SCN-BLD-322
    note: '只聚合不做决策——与 OPS-333 同原则',
  };
}
// BLD 能力地图（291~333 全链索引）
const BLD_MAP = {
  pipeline: ['291-minibundler', '300-profiling', '316-worker-pool', '324-critical-path'],
  artifact: ['296-sizes', '298-duplicates', '307-critical-css', '310-syntax', '318-sprite', '319-font'],
  correctness: ['295-hash-stability', '299-golden', '306-manifest', '311-module-id', '332-incremental'],
  governance: ['301-lock', '308-drift', '313-degrade', '314-trend', '331-plugins'],
  trust: ['303-buildinfo', '320-csp', '322-provenance', '327-memory', '328-export-diff'],
};
```

**评分点**:
- 五视图聚合（流水线/产物/正确性/治理/信任）全链引用前文。
- 只聚合不决策（单一事实源——SCN-OPS-333 同原则）。
- BLD 能力地图收束（291~333 全链索引）。
- ②04-工程化与构建收官（ENG 133 + OPS 133 + BLD 134 = 400 张）。
