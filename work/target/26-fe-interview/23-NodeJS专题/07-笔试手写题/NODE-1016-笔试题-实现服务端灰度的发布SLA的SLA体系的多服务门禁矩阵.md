---
title: [NODE-1016] 笔试题——实现 SLA 体系多服务门禁矩阵（SLA 门禁扩展）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1016：手写多维扩展

**需求与边界**：
- 需求：多服务 SLA 门禁（SCN-OPS-922/1016）——① 四维扩展（+SLA 达标/预算/降级对齐——SCN-SLA-991）；② 矩阵并行（SCN-NODE-729）；③ 总判定（SCN-OPS-229）；④ 报告（SCN-OPS-261）。
- 边界：① 各维复用（编号引用）；② 豁免（SCN-OPS-229）；③ 报告（SCN-OPS-261）。

**答**：
```javascript
const EXTENDED_GATES = {
  ...GATE_DIMENSIONS,                                  // SCN-NODE-922 四维
  slaCompliance: async (r) => ({ ok: recentCompliance(r.sla) >= 0.95, level: 'block' }),   // SCN-SLA-991
  slaBudget: async (r) => ({ ok: errorBudget(r.slo, 30).remaining > 0, level: 'block' }),   // SCN-OPS-944
  slaDegrade: async (r) => ({ ok: degradeAligned(r.sla), level: 'warn' }),   // SCN-1010
};
// 组合到 multiDimGate（SCN-NODE-922）——七维门禁矩阵
```

**评分点**:
- 四维 → 七维扩展（SCN-NODE-922/SLA-991/944/1010）。
- 复用 + 豁免 + 报告（SCN-NODE-729/OPS-229/261）。
