---
title: [NODE-928] 笔试题——实现多服务发布拓扑校验（发布计划→拓扑→校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-928：手写拓扑校验

**需求与边界**：
- 需求：发布拓扑校验（SCN-OPS-251/291）——① 发布计划拓扑解析（SCN-OPS-291 计划）；② 拓扑合法性校验（SDK 先行/依赖序——SCN-OPS-251）；③ 拓扑与运行时依赖比对（SCN-OPS-920）；④ 拓扑变更审计（SCN-OPS-273）。
- 边界：① 拓扑的环检测（SCN-BLD-324）；② 拓扑与运行时 diff（SCN-OPS-920）；③ 校验的门禁（SCN-OPS-229）。

**答**：
```javascript
async function topologyVerify(plan) {
  assertNoCycle(plan.steps);                           // 环（SCN-BLD-324）
  const sdkFirst = plan.steps.every(s =>
    s.role !== 'consumer' || plan.steps.some(p => p.app === s.dependsSdk && p.role === 'first'));   // SDK 先行（SCN-OPS-251）
  const runtime = await runtimeDependencyVerify(plan); // 运行时比对（SCN-OPS-920）
  return {
    sdkFirst, runtime,
    pass: sdkFirst && runtime.gate === 'PASS',
    fix: !sdkFirst ? 'SDK 先行——SCN-OPS-251' : null,   // 修复建议
    audit: auditTopologyChange(plan),                  // 审计（SCN-OPS-273）
  };
}
```

**评分点**:
- 环检测 + SDK 先行校验（SCN-BLD-324/OPS-251）。
- 运行时比对（SCN-OPS-920）。
- 门禁 + 审计（SCN-OPS-229/273）。
