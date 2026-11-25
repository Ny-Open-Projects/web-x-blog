---
title: [NODE-820] 笔试题——实现网关灰度实例健康联动（canary 摘流回退）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-820：手写灰度摘流

**需求与边界**：
- 需求：canary 摘流（SCN-NODE-776/706）——① canary 实例错误率监控（per 实例——SCN-NODE-706 副本粒度）；② 摘流（错误率超阈 → canary 实例摘流，流量回 stable——SCN-OPS-237 降档语义）；③ 恢复探测（半开——SCN-NODE-669）；④ 摘流决策审计（SCN-OPS-273）。
- 边界：① 全 canary 摘光的处理（全部回 stable——灰度自动终止信号，SCN-OPS-237）；② 摘流与哨兵联动（哨兵判定 → 摘流执行——SCN-NODE-798）；③ 恢复的验证（canary 修复后重新灰度——新灰度周期，SCN-OPS-268）。

**答**：
```javascript
setInterval(async () => {
  for (const i of canaryInstances) {
    const errRate = windowErrorRate(i.stats);          // per 实例（SCN-NODE-706）
    if (errRate > 0.5 && i.serving) {
      i.serving = false;                               // 摘流
      traffic.route(i, { to: 'stable' });              // 流量回 stable（SCN-OPS-237 降档）
      audit({ action: 'CANARY_UNROUTE', instance: i.id, errRate });   // 审计（SCN-OPS-273）
      if (canaryInstances.every(c => !c.serving))
        alert({ type: 'GRAY_TERMINATED', note: 'canary 全部摘流——灰度自动终止，回滚决策树（SCN-OPS-234）' });
      scheduleHalfOpenProbe(i);                        // 半开探测（SCN-NODE-669）
    }
    if (!i.serving && probeOk(i)) { i.serving = true; audit({ action: 'CANARY_RECOVER' }); }
  }
}, 10_000);
```

**评分点**:
- per 实例摘流（副本粒度——SCN-NODE-706）。
- 流量回 stable（降档语义——SCN-OPS-237）。
- 全摘自动终止信号（灰度终止 → 决策树——SCN-OPS-234）。
- 半开探测恢复（SCN-NODE-669）。
