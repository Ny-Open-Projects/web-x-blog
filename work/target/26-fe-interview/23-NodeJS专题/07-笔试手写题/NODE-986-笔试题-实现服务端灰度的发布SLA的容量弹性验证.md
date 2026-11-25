---
title: [NODE-986] 笔试题——实现 SLA 容量弹性验证（压测验证 SLA 承诺）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-986：手写弹性验证

**需求与边界**：
- 需求：SLA 弹性验证（SCN-NODE-647/986）——① SLA 承诺的压测验证（SLA QPS 下延迟达标——SCN-NODE-647 稳态）；② 弹性伸缩验证（扩容后的 SLA 维持——SCN-NODE-834）；③ 验证的定期（SCN-NODE-647 重测周期）；④ 验证失败的处理（SLA 修正或扩容——SCN-SLA-965）。
- 边界：① 压测的标记（SCN-NODE-717 影子）；② 验证的分位（SCN-SLA-725）；③ 验证的审计（SCN-OPS-273）。

**答**：
```javascript
async function slaCapacityVerify(sla) {
  const result = await loadTest({ targetQps: slaQps(sla),
    marker: 'shadow', assert: { p99: sla.latencyP99, errorRate: sla.errorRate } });   // 压测验证（SCN-NODE-647/717）
  if (!result.pass) {
    await scaleVerify(sla, { targetQps: slaQps(sla) });   // 弹性验证（SCN-NODE-834）
    if (!elasticOk) return proposeSlaChange(sla, { to: measured });   // SLA 修正（SCN-SLA-965）
  }
  audit({ sla: sla.id, pass: result.pass });           // 审计（SCN-OPS-273）
  return result;
}
```

**评分点**:
- SLA 压测验证（SCN-NODE-647/717）。
- 弹性伸缩验证（SCN-NODE-834）。
- SLA 修正提案（SCN-SLA-965）。
