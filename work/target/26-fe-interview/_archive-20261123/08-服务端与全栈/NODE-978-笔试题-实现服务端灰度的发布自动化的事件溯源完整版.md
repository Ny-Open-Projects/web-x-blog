---
title: [NODE-978] 笔试题——实现发布自动化事件溯源完整版（事件流+投影+重放）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-978：手写事件溯源完整

**需求与边界**：
- 需求：事件溯源完整版（SCN-OPS-271/713）——① 事件流（SCN-OPS-271）；② 投影（读模型——SCN-NODE-713）；③ 重放（时间旅行——SCN-OPS-271）；④ 快照（SCN-OPS-271）。
- 边界：① 投影的重建（SCN-NODE-845）；② 事件的 schema 演进（SCN-NODE-713）；③ 重放的成本（后台——SCN-NODE-667）。

**答**：
```javascript
// 事件流 → 投影 → 重放（SCN-OPS-271 + NODE-713/845 组合）
const es = createEventSourcedOrchestrator();           // SCN-OPS-296
es.subscribeProjection('release-boards', projection);  // 读模型（SCN-NODE-845）
es.replayTo(n);                                        // 时间旅行（SCN-OPS-271）
es.snapshot();                                         // 快照加速（SCN-OPS-271）
```

**评分点**:
- 事件溯源完整组合（SCN-OPS-271/296 + NODE-713/845）。
- 投影 + 重放 + 快照（SCN-NODE-845/OPS-271）。
- schema 演进（SCN-NODE-713）。
