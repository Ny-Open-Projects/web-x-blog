---
title: [NODE-988] 笔试题——实现 SLA 报告可复核（数据快照+分析代码）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-988：手写可复核

**需求与边界**：
- 需求：SLA 报告可复核（SCN-OPS-284/982）——① 报告的可复核包（快照+口径+代码——SCN-OPS-284）；② 口径版本（SCN-SLA-710）；③ 复核的验证（重算比对——SCN-OPS-284）；④ 复核的消费（争议仲裁——SCN-SLA-714）。
- 边界：① 口径版本化（SCN-SLA-710）；② 数据快照（SCN-OPS-728）；③ 重算的一致性（SCN-SLA-710）。

**答**：
```javascript
async function slaReplicationPack(report) {
  return {
    config: report.calVer,                             // 口径版本（SCN-SLA-710）
    dataSnapshot: report.dataRev,                      // 快照（SCN-OPS-728）
    analysisCode: ANALYSIS_CODE_VER,                   // 分析代码
    expectedHash: sha256(report.results),              // 期望结果
    verify: async (third) => {                         // 第三方重算（SCN-OPS-284）
      const recomputed = await third.recompute(report.dataSnapshot, report.calVer);
      return sha256(recomputed) === report.expectedHash;   // 重算比对
    },
  };
}
```

**评分点**:
- 可复核包四要素（SCN-OPS-284）。
- 口径版本化（SCN-SLA-710）。
- 第三方重算（争议仲裁——SCN-SLA-714）。
