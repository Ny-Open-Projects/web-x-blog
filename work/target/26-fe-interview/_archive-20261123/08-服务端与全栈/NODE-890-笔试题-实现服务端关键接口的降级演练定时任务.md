---
title: [NODE-890] 笔试题——实现关键接口降级演练定时任务（自动演练）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-890：手写自动演练

**需求与边界**：
- 需求：降级演练自动化（SCN-OPS-269/883）——① 关键接口枚举（核心链路——SCN-联想-833）；② 定时演练（周末低峰——SCN-OPS-269 CI）；③ 演练报告与告警（SCN-OPS-215）；④ 演练债务清单（SCN-OPS-279）。
- 边界：① 演练的摘流（灰度小流量——SCN-OPS-281 范围限定）；② 演练的审批（自动执行限已审核——SCN-联想-833）；③ 演练失败的告警分级（降级不生效 = P0——SCN-OPS-229）。

**答**：
```javascript
cron('0 3 * * 6', async () => {                        // 周末低峰（SCN-OPS-269）
  for (const api of criticalApis()) {                  // 关键接口（SCN-联想-833）
    const drill = drills.for(api);
    if (!drill?.reviewed) { debt.record(api); continue; }   // 债务（SCN-OPS-279）
    const r = await degradeDrill(api, { scope: { pct: 10 } });   // 灰度小流量（SCN-OPS-281）
    reportDrill({ api, ...r, timed: r.degradeWithinMs < 5000 });   // 计时（SCN-OPS-215）
    if (!r.degradeWorks) alert({ type: 'DEGRADE_BROKEN', api, level: 'block' });   // P0（SCN-OPS-229）
  }
});
```

**评分点**:
- 关键接口枚举 + 自动演练（SCN-联想-833/OPS-269）。
- 摘流限定（灰度小流量——SCN-OPS-281）。
- 降级失效 P0 告警（SCN-OPS-229）。
- 演练债务（SCN-OPS-279）。
