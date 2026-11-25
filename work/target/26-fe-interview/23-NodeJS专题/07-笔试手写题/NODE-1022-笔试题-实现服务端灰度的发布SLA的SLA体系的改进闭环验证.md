---
title: [NODE-1022] 笔试题——实现 SLA 改进闭环验证（改进效果的量化验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1022：手写闭环验证

**需求与边界**：
- 需求：改进验证（SCN-SLA-1002/1017）——① 改进的量化验证（指标变化 vs 目标——SCN-OPS-227 验证）；② 对照要求（SCN-NODE-717 对照）；③ 未达成的处理（SCN-OPS-227 重开）；④ 验证的报告（SCN-OPS-248）。
- 边界：① 量化的验证（SCN-OPS-227）；② 对照（SCN-NODE-717）；③ 报告（SCN-OPS-248）。

**答**：
```javascript
async function verifyImprovement(imp) {
  const delta = await metrics.compare(imp.metric, imp.due, '-30d');   // 量化（SCN-OPS-227）
  const ok = delta.achieved && delta.controlled;       // 对照（SCN-NODE-717 流量/版本切片）
  if (!ok) { reopenImprovement(imp); return { verified: false, delta }; }   // 重开（SCN-OPS-227）
  await closeImprovement(imp, delta);
  archiveImprovement(imp, delta);                      // 报告（SCN-OPS-248）
  return { verified: true, delta };
}
```

**评分点**:
- 量化验证 + 对照（SCN-OPS-227/NODE-717）。
- 未达成重开（SCN-OPS-227）。
- 报告（SCN-OPS-248）。
