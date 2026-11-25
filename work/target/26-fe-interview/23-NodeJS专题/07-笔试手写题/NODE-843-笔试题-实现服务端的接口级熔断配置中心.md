---
title: [NODE-843] 笔试题——实现熔断配置中心（接口级动态参数）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-843：手写熔断配置

**需求与边界**：
- 需求：熔断配置中心（SCN-NODE-669/663）——① 接口级熔断参数（阈值/窗口/半开——per 接口动态配置，SCN-NODE-663 热更）；② 配置校验（参数合理性——SCN-OPS-315 规则）；③ 灰度生效（SCN-OPS-228）；④ 配置审计（SCN-OPS-219）。
- 边界：① 参数热更（breaker 运行中参数更新——SCN-NODE-663 分类目）；② 熔断配置的演练验证（参数合理性实测——SCN-OPS-281）；③ 配置与降级联动（熔断触发降级链——SCN-NODE-778）。

**答**：
```javascript
const breakerConfigs = new Map();                      // 接口 → 熔断参数（动态）
configCenter.on('breaker-config', (newCfg) => {
  for (const [api, cfg] of Object.entries(newCfg)) {
    if (!validBreakerCfg(cfg)) { alert({ type: 'BAD_BREAKER_CFG', api }); continue; }   // 校验（SCN-OPS-315）
    breakerConfigs.set(api, cfg);                      // 热更（SCN-NODE-663）
    breakers.get(api)?.updateParams(cfg);              // 运行中参数更新
    audit({ api, diff: cfg });                         // 审计（SCN-OPS-219）
  }
});
// breaker 读配置（per 接口动态）
function getBreaker(api) {
  const cfg = breakerConfigs.get(api) ?? DEFAULT;
  return breakers.get(api) ?? new CircuitBreaker({ ...cfg });   // SCN-NODE-732
}
```

**评分点**:
- 接口级动态参数（per 接口配置——SCN-NODE-663 热更）。
- 参数校验（SCN-OPS-315）+ 灰度生效（SCN-OPS-228）。
- 运行中参数更新（breaker.updateParams——SCN-NODE-732 联动）。
- 配置审计 + 演练验证（SCN-OPS-219/281）。
