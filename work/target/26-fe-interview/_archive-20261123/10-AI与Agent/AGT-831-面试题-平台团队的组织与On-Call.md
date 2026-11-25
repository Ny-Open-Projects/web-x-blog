---
title: [AGT-831] 平台团队的分工与值班体系（平台组/工具组/模型组/安全组），On-Call 怎么排？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-831：平台团队的分工与值班体系（平台组/工具组/模型组/安全组），On-Call 怎么排

**答**：
- 团队按故障域分工：平台组（运行时/网关，On-Call 主力）、模型组（供应商关系/路由）、工具组（适配器，与业务组共建）、安全组（红队/策略）、数据组（检索/记忆）。On-Call 按 P0/P1 域路由，跨域升级有明确路径。
- 值班卫生：轮值周期 1 周（不超两周）、交接 runbook 化、告警清理（每月删 10% 噪声告警）、复盘闭环（重复告警必须治理）。
- 平台组的特殊纪律：租户请求响应有时限承诺（P0 15min），值班补贴与减负机制（连续值班调休）写进制度，不然 On-Call 会垮。

```javascript
const TEAMS = {
  platform: { domain: 'runtime/gateway', oncall: 'primary' },
  model: { domain: 'vendor/routing' },
  tools: { domain: 'adapters', coBuild: 'business' },
  security: { domain: 'redteam/policy' },
};
function oncallHygiene() {
  return { rotation: '1w', handoff: 'runbook',
    noise: monthlyNoiseReduction(0.1),             // 每月删10%噪声
    repeat: repeatedAlertsMustBeFixed() };
}
```

