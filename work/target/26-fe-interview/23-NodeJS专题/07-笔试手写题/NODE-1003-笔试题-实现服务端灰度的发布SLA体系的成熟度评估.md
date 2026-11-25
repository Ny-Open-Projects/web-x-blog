---
title: [NODE-1003] 笔试题——实现 SLA 体系成熟度评估（五维评分）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1003：手写成熟度评估

**需求与边界**：
- 需求：SLA 成熟度（SCN-ENG-330/1003）——① 五维评估（承诺/观测/报告/合规/沉淀——SCN-ENG-330 复用）；② 评估的自动采集（SCN-OPS-289）；③ 评估的报告（SCN-OPS-728）；④ 评估的消费（改进——SCN-SLA-1002）。
- 边界：① 评估的映射表（SCN-ENG-330 显式）；② 抽样校验（SCN-ENG-330 过程抽样）；③ 评估的分级（SCN-ENG-330）。

**答**：
```javascript
const SLA_DIMS = {
  promise: { check: 'SLA 定义完整性（SCN-SLA-703）', level: (v) => v >= 0.9 ? 5 : v >= 0.7 ? 3 : 1 },
  observe: { check: '指标采集与达标率（SCN-SLA-740）', ... },
  report: { check: '报告可复核（SCN-OPS-284）', ... },
  compliance: { check: '审计闭环（SCN-SLA-997）', ... },
  knowledge: { check: '沉淀闭环（SCN-SLA-998）', ... },
};
async function slaMaturity() {
  const dims = {};
  for (const [dim, d] of Object.entries(SLA_DIMS)) {
    const v = await autoCollect(d.check);
    dims[dim] = d.level(v);                            // 显式映射（SCN-ENG-330）
  }
  return { dims, weakest: minEntry(dims), improvements: improvementFor(weakest) };   // 木桶（SCN-ENG-330）
}
```

**评分点**:
- 五维评估复用（SCN-ENG-330/OPS-289）。
- 显式映射 + 木桶短板（SCN-ENG-330）。
- 消费改进（SCN-SLA-1002）。
