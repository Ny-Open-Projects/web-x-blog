---
title: [NODE-878] 笔试题——实现依赖降级矩阵自动触发（熔断→降级→摘流）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-878：手写降级联动

**需求与边界**：
- 需求：降级自动触发链（SCN-NODE-669/778/828）——① 熔断触发（SCN-NODE-669 open 事件）；② 降级执行（策略级联——SCN-NODE-778）；③ 流量转移（备用下游——SCN-NODE-828）；④ 全链事件（触发→执行→恢复——SCN-OPS-670 可观测）。
- 边界：① 触发的去抖（同下游 5 分钟内不重复触发——SCN-OPS-276）；② 降级链的预算（SCN-NODE-778 级联预算）；③ 恢复验证（SCN-NODE-669 half-open）。

**答**：
```javascript
breaker.on('open', async ({ target }) => {             // SCN-NODE-669 触发
  if (recentlyTriggered(target, 5 * 60_000)) return;   // 去抖（SCN-OPS-276）
  const chain = degradationMatrix[target];             // 策略级联（SCN-NODE-778）
  for (const s of chain.strategies) {
    const out = await tryStrategy(s, target);
    if (out) { report({ type: 'AUTO_DEGRADE', target, strategy: s.name }); break; }   // SCN-NODE-690
    if (s.next === 'reroute') await failover(target);  // 流量转移（SCN-NODE-828）
  }
});
breaker.on('closed', ({ target }) => {                 // 恢复（SCN-NODE-669 half-open）
  report({ type: 'AUTO_RECOVER', target });
  restoreChain(target);                                // 降级回滚（SCN-NODE-778）
});
```

**评分点**:
- 熔断→降级→转移三级联动（SCN-NODE-669/778/828）。
- 去抖防御（SCN-OPS-276）。
- 恢复回滚降级（half-open——SCN-NODE-669）。
- 全链事件可观测（SCN-OPS-670）。
