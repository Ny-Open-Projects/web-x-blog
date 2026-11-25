---
title: [NODE-920] 笔试题——实现发布依赖运行时验证（canary 实际调用了谁）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-920：手写运行时验证

**需求与边界**：
- 需求：运行时依赖验证（SCN-OPS-231/917）——① canary 出站调用捕获（trace——SCN-NODE-645）；② 实际依赖 vs 声明依赖 diff（SCN-OPS-260）；③ 版本验证（依赖的版本——SCN-OPS-917）；④ 未知依赖的告警（未声明依赖——SCN-OPS-260）。
- 边界：① trace 采样的覆盖率（canary 全量——SCN-OPS-203）；② 依赖发现的延迟（首次调用后——预热触发，SCN-联想-895）；③ 未知依赖的处置（注册或移除——SCN-OPS-260）。

**答**：
```javascript
async function runtimeDependencyVerify(release) {
  const spans = await traces.outboundSpans({ version: release.canaryVer });   // 出站捕获（SCN-NODE-645）
  const actual = [...new Set(spans.map(s => s.target))];   // 实际依赖
  const undeclared = actual.filter(d => !release.declaredDeps.includes(d));   // 未声明（SCN-OPS-260）
  const versionMismatch = actual.filter(d => release.declaredDeps[d]?.version !== actualVersion(d));   // SCN-OPS-917
  return {
    actual, undeclared, versionMismatch,
    action: undeclared.length ? 'REGISTER_OR_REMOVE' : 'OK',   // SCN-OPS-260
    gate: !undeclared.length && !versionMismatch.length ? 'PASS' : 'BLOCK',   // SCN-OPS-229
  };
}
```

**评分点**:
- 出站 trace 捕获（canary 全量——SCN-OPS-203）。
- 未声明依赖检测（SCN-OPS-260）。
- 版本 mismatch（SCN-OPS-917）。
- 门禁联动（SCN-OPS-229）。
