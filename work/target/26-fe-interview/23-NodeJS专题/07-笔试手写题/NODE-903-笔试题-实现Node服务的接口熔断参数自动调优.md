---
title: [NODE-903] 笔试题——实现熔断参数自动调优（误触发率反馈）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-903：手写熔断调优

**需求与边界**：
- 需求：熔断参数自动调优（SCN-OPS-276/732）——① 误触发统计（熔断后下游实际健康——误判，SCN-OPS-276）；② 参数调整（阈值过松/过紧——误触发率反馈，SCN-OPS-276）；③ 调优的灰度（参数变更灰度验证——SCN-OPS-228）；④ 调优审计（SCN-OPS-219）。
- 边界：① 误判的判定（熔断后探测下游健康——SCN-NODE-669 half-open 数据）；② 调优的范围（阈值 ±20%——防极端）；③ 调优的观察期（SCN-OPS-276 试用期语义）。

**答**：
```javascript
async function tuneBreaker(api) {
  const stats = breaker(api).stats30d();
  const falseTrips = stats.trips.filter(t => probeHealthy(t.after));   // 熔断后实际健康 = 误判（SCN-OPS-276）
  const fpRate = falseTrips.length / stats.trips.length;
  if (fpRate > 0.3) {                                  // 误判率高：阈值放宽
    const newThreshold = clamp(cfg.threshold * 1.2, cfg.threshold, cfg.threshold * 1.2);   // ±20%
    await grayApply(api, { threshold: newThreshold });  // 灰度验证（SCN-OPS-228）
    audit({ api, from: cfg.threshold, to: newThreshold, fpRate });   // 审计（SCN-OPS-219）
  } else if (fpRate < 0.05 && stats.missedTrips > 0) { // 误判率低但有漏：收紧
    await grayApply(api, { threshold: cfg.threshold * 0.9 });
  }
}
```

**评分点**:
- 误触发统计（熔断后探测健康——SCN-OPS-276）。
- 双向调优（误判放宽/漏判收紧）± 范围约束。
- 灰度验证（SCN-OPS-228）+ 审计（SCN-OPS-219）。
- 观察期语义（SCN-OPS-276）。
