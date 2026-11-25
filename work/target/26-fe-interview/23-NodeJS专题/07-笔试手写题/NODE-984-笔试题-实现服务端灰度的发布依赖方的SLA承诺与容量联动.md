---
title: [NODE-984] 笔试题——实现 SLA 与容量联动（承诺与实际的动态对齐）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-984：手写 SLA 容量联动

**需求与边界**：
- 需求：SLA 容量联动（SCN-SLA-975/984）——① 容量变化 → SLA 评估（扩缩容后 SLA 重估——SCN-NODE-834）；② SLA 变化 → 容量要求（SCN-SLA-975）；③ 联动的巡检（SCN-SLA-975）；④ 联动的审计（SCN-OPS-273）。
- 边界：① 容量数据源（SCN-NODE-765）；② SLA 变更流程（SCN-SLA-965）；③ 联动的告警（SCN-SLA-975）。

**答**：
```javascript
scaleEvents.on('scaled', async (svc, newInstanceCount) => {
  const sla = slaOf(svc);
  const newCap = instanceCapacity(newInstanceCount);   // SCN-NODE-765
  const required = slaQps(sla);
  if (newCap < required) {
    alert({ type: 'SLA_AT_RISK', svc, newCap, required,
      fix: '扩容或降级 SLA（SCN-SLA-965 流程）' });    // 联动（SCN-SLA-975）
    await proposeSlaChange(svc, { to: newCap });       // SLA 变更提案（SCN-SLA-965）
  }
});
```

**评分点**:
- 容量变化 → SLA 重估（SCN-NODE-834/765）。
- SLA 变更提案（SCN-SLA-965）。
- 告警（SCN-SLA-975）。
