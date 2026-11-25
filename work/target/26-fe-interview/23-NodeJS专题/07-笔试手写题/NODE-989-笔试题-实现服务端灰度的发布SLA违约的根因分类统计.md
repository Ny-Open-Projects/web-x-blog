---
title: [NODE-989] 笔试题——实现 SLA 违约根因分类统计（违约归因看板）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-989：手写违约归因

**需求与边界**：
- 需求：违约归因（SCN-SLA-716/989）——① 违约根因分类（发布引发/容量不足/外部依赖——SCN-OPS-716 候选）；② 归因统计（趋势看板——SCN-OPS-716）；③ 归因的消费（改进项——SCN-OPS-227）；④ 归因的人工确认（SCN-OPS-716）。
- 边界：① 候选的置信度（SCN-OPS-716）；② 归因的排除项（SCN-OPS-716）；③ 归因报告（SCN-OPS-728）。

**答**：
```javascript
async function breachAttribution(breach) {
  const candidates = correlate(breach, { changesets: true, capacity: true, deps: true });   // 候选（SCN-OPS-716）
  const classified = groupBy(candidates, c => c.category);   // 分类（发布/容量/外部）
  return {
    classified,
    top: candidates[0],
    humanConfirmed: false,                             // 人工确认前（SCN-OPS-716）
    improvements: candidates[0] ? improvementItem(candidates[0]) : [],   // 改进项（SCN-OPS-227）
    report: forReviewBoard(classified),                // 看板（SCN-OPS-716）
  };
}
```

**评分点**:
- 根因分类（发布/容量/外部——SCN-OPS-716）。
- 人工确认前 + 排除项（SCN-OPS-716）。
- 改进项（SCN-OPS-227）。
