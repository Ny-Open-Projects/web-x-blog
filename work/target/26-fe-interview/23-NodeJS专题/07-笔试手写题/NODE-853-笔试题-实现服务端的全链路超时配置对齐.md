---
title: [NODE-853] 笔试题——实现全链路超时配置对齐（配置一致性检查）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-853：手写超时对齐

**需求与边界**：
- 需求：超时配置对齐（SCN-NODE-642）——① 配置收集（各服务超时配置——LB/网关/BFF/服务/DB）；② 一致性校验（上游 ≤ 下游——SCN-NODE-642 预算制）；③ 违规报告（哪层超时 > 上游——白干链路）；④ 对齐建议（自动计算——各级分配）。
- 边界：① 配置来源（各层配置中心收集——SCN-NODE-663）；② 偏差容忍（时钟/网络——±10%）；③ 对齐报告进评审（SCN-OPS-261 材料汇编）。

**答**：
```javascript
async function timeoutAlignment() {
  const chain = [
    { layer: 'lb', timeout: 5000 },                    // LB
    { layer: 'gateway', timeout: 4800 },               // 网关
    { layer: 'bff', timeout: 4500 },                   // BFF
    { layer: 'svc', timeout: 4600 },                   // 服务（>BFF！违规）
    { layer: 'db', timeout: 4700 },
  ];
  const violations = [];
  for (let i = 0; i < chain.length - 1; i++) {
    const [up, down] = [chain[i], chain[i + 1]];
    if (down.timeout > up.timeout)
      violations.push({ upstream: up.layer, downstream: down.layer,
        note: `下游 ${down.timeout}ms > 上游 ${up.timeout}ms——上游放弃后下游白干（SCN-NODE-642）`,
        fix: `将 ${down.layer} 调至 ≤ ${up.timeout}` });   // 对齐建议
  }
  return { chain, violations,
    suggested: suggestBudget(chain, { total: 5000 }) };   // 自动分配（SCN-NODE-642 预算制）
}
```

**评分点**:
- 全链配置收集（LB→DB——SCN-NODE-642 预算制验证）。
- 逐层校验（上游 ≤ 下游）+ 违规报告带修复建议。
- 自动分配建议（SCN-NODE-642）。
- 对齐报告进评审（SCN-OPS-261）。
