---
title: [NODE-828] 笔试题——实现熔断自动摘流联动（下游挂 → 流量转移）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-828：手写熔断摘流

**需求与边界**：
- 需求：熔断摘流联动（SCN-NODE-669/690）——① 下游熔断 → 该下游流量自动转移（备用下游/降级值——SCN-NODE-669）；② 摘流恢复（下游恢复自动回流——SCN-NODE-669 half-open）；③ 摘流决策记录（SCN-NODE-690 聚合）；④ 摘流风暴防御（多下游同时摘——分级让路，SCN-NODE-585）。
- 边界：① 备用下游的容量校验（主下游流量转给备用——备用扛得住吗，SCN-NODE-699 全局校验）；② 摘流的用户体验（降级标记——SCN-NODE-690）；③ 联动的自动化边界（自动摘流 OK——自动切回需验证，SCN-OPS-259）。

**答**：
```javascript
breaker.on('open', async ({ target }) => {             // 熔断触发 → 自动摘流（SCN-NODE-669）
  const backup = targets[target].backup;
  const capOk = backupCapacity(backup) >= currentLoad(target);   // 备用容量校验（SCN-NODE-699）
  if (!capOk) return degradePartially(target);         // 容量不够：部分降级（SCN-NODE-690）
  router.shift(target, { to: backup });                // 流量转移
  report({ type: 'FAILOVER', target, to: backup });    // 降级标记（SCN-NODE-690）
});
breaker.on('halfOpen', async ({ target }) => {         // 恢复探测通过 → 回流
  const verified = await probeDownstream(target);
  if (verified) { router.shift(target, { to: target }); report({ type: 'FAILOVER_RECOVER' }); }
});
```

**评分点**:
- 熔断 → 自动摘流转移（SCN-NODE-669 联动）。
- 备用容量校验（转移不雪崩备用——SCN-NODE-699 全局）。
- half-open 恢复回流（SCN-NODE-669 语义）。
- 降级标记与聚合（SCN-NODE-690）。
