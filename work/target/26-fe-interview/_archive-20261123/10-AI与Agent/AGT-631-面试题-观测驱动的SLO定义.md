---
title: [AGT-631] Agent 服务的 SLO 怎么定（与常规 API 的 SLO 有何不同）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-631：Agent 服务的 SLO 怎么定（与常规 API 的 SLO 有何不同）

**答**：
- Agent SLO 不是单一可用性：拆成四个独立 SLO——会话建立成功率、轮次完成率（区分业务失败与系统失败）、TTFT P95（感知）、成本上限（单位任务成本预算）。系统失败（超时/网关错）计入 SLO，业务失败（审核拦截/用户取消）不计入但要监控趋势。
- 错误预算玩法相同：预算烧完冻结功能发布只修可靠性；Agent 特有的是「成本预算」也冻结（贵功能先停）。
- SLO 文档带排除项清单：模型供应商故障（降级到备用是否算达成？算，只要轮次完成）、用户主动中断不算失败。

```javascript
const SLO = {
  sessionSetup: { target: 0.995, window: '30d' },
  turnDone:     { target: 0.98, exclude: ['user_cancel', 'moderation'] },
  ttftP95:      { target: 3.0, unit: 's', exclude: ['regen'] },
  costPerTask:  { target: 0.5, unit: 'usd' },   // 成本也是SLO
};
function burnBudget(slo, window) {
  const br = badRatio(window, slo);
  return { burnRate: br / (1 - slo.target),
    frozen: burnRate > 14 && freezeReleases('reliability') }; // 预算烧完冻结
}
```

