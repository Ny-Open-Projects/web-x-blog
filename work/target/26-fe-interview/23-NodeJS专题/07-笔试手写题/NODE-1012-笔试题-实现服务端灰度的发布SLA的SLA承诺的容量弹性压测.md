---
title: [NODE-1012] 笔试题——实现 SLA 弹性压测验证（扩容后 SLA 维持）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1012：手写弹性压测

**需求与边界**：
- 需求：弹性压测（SCN-NODE-986/834）——① SLA QPS 压测（SCN-NODE-647 稳态）；② 扩容响应验证（HPA 触发→扩容→SLA 维持——SCN-NODE-834）；③ 分段计时（SCN-OPS-215）；④ 失败的处置（SLA 修正或扩容上限调高——SCN-SLA-965）。
- 边界：① 压测的影子标记（SCN-NODE-717）；② 分位断言（SCN-SLA-725）；③ 审计（SCN-OPS-273）。

**答**：
```javascript
async function elasticSlaTest(sla) {
  const base = await loadTest({ qps: slaQps(sla) * 0.8, marker: 'shadow' });   // 基线（SCN-NODE-717）
  const surge = await loadTest({ qps: slaQps(sla) * 2, marker: 'shadow' });   // 2× 峰值
  const scaled = await waitForScale({ target: slaQps(sla) * 2 });   // HPA 扩容验证（SCN-NODE-834）
  const segments = { base, surge, scaledIn: scaled.scaleInMs };   // 分段（SCN-OPS-215）
  const pass = surge.p99 <= sla.latencyP99 && scaled.ok;
  if (!pass) return proposeSlaChange(sla, { to: measured(surge) });   // SCN-SLA-965
  audit({ sla: sla.id, pass });                        // 审计（SCN-OPS-273）
  return { pass, segments };
}
```

**评分点**:
- 基线 + 峰值 + 扩容三段验证（SCN-NODE-647/834）。
- 分段计时 + 分位断言（SCN-OPS-215/725）。
- 失败处置（SCN-SLA-965）。
