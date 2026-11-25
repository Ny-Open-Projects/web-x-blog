---
title: [NODE-911] 笔试题——实现依赖熔断的循环防御（A→B→A 熔断环）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-911：手写熔断环防御

**需求与边界**：
- 需求：熔断循环防御（SCN-NODE-669/ENG-202）——① 熔断传播检测（A 熔断导致 B 熔断——图传播，SCN-NODE-824）；② 熔断环检测（A→B→A——SCN-ENG-202 循环）；③ 环的打破（关键路径单边不熔断——降级优先，SCN-NODE-690）；④ 传播告警（SCN-NODE-824）。
- 边界：① 熔断传播的建模（依赖图 + 熔断状态——SCN-NODE-824）；② 环的预防（依赖分层——SCN-ENG-202 CI）；③ 传播的演习（SCN-OPS-281 注入验证传播）。

**答**：
```javascript
function cascadeBreakerCheck(breakerStates, depsGraph) {
  const openSet = [...breakerStates.filter(s => s.state === 'open').map(s => s.target)];
  const cascade = propagate(openSet, depsGraph);       // 传播预测（SCN-NODE-824）
  const cycle = findCycleInOpen(cascade);              // 熔断环（SCN-ENG-202）
  if (cycle)
    return { cycle, action: 'BREAK_CYCLE', fix: `关键路径单边降级优先（SCN-NODE-690）——不熔断 ${cycle[0]}` };
  alert({ type: 'CASCADE_RISK', cascade });
}
// 预防：依赖分层 CI（SCN-ENG-202 no-circular）+ 注入演习（SCN-OPS-281）
```

**评分点**:
- 熔断传播预测（SCN-NODE-824 依赖图）。
- 熔断环检测（SCN-ENG-202 循环）。
- 环打破（降级优先——SCN-NODE-690）。
- 演习验证（SCN-OPS-281）。
