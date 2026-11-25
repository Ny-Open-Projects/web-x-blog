---
title: [NODE-863] 笔试题——实现灰度实例故障自动隔离（per 实例摘流）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-863：手写实例隔离

**需求与边界**：
- 需求：实例级故障隔离（SCN-NODE-776/706）——① per 实例错误率统计（实例维度——SCN-NODE-706）；② 自动摘流（错误率超阈——实例摘流，SCN-NODE-776）；③ 摘流后的恢复探测（SCN-NODE-669）；④ 摘流数量告警（多实例摘流 = 系统性问题——非实例问题）。
- 边界：① 摘流的粒度控制（单实例摘——不整服务摘；SCN-NODE-706 副本粒度语义）；② 摘流实例的诊断（heapdump——SCN-NODE-797）；③ 摘流比例上限（>50% 摘流 = 版本问题回滚——SCN-OPS-234）。

**答**：
```javascript
setInterval(async () => {
  const unhealthy = instances.filter(i => windowErrRate(i) > 0.5);   // per 实例（SCN-NODE-706）
  for (const i of unhealthy) {
    if (i.serving) { i.serving = false; lb.unroute(i); // 摘流（SCN-NODE-776）
      audit({ action: 'INSTANCE_UNROUTE', id: i.id, errRate: windowErrRate(i) });
      triggerDiag(i);                                  // 摘流实例诊断（SCN-NODE-797）
      scheduleHalfOpen(i);                             // 半开探测（SCN-NODE-669）
    }
  }
  const unroutedPct = unhealthy.length / instances.length;
  if (unroutedPct > 0.5) {                             // >50% = 版本问题（SCN-OPS-234）
    alert({ type: 'MAJORITY_UNHEALTHY', action: '触发回滚决策树' });   // SCN-OPS-234
  }
}, 10_000);
```

**评分点**:
- per 实例摘流（SCN-NODE-706 副本粒度）。
- 摘流实例诊断（SCN-NODE-797 一键收集）。
- 摘流比例上限 → 回滚决策（SCN-OPS-234）。
- 半开探测恢复（SCN-NODE-669）。
