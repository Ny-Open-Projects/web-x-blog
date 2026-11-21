---
title: [PER-105] SLA/SLO 与错误预算如何驱动工程决策？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-105：SLA/SLO 与错误预算如何驱动工程决策？

**答**：
- 概念链：**SLI**（观测指标，如页面可用率、错误率）、**SLO**（目标，如 99.9% 请求正常）、**SLA**（对外的违约承诺）；前端工程常用 SLO：错误率 < 0.1%、P75 LCP < 2.5s 的会话占比 > 75%。
- **错误预算** = 1 - SLO，是“可以出故障的额度”：预算充足可以激进发版，预算耗尽强制冻结功能迭代、只修稳定性。
- 实践：预算按 28 天滚动窗口计算，burn rate（消耗速度）超 14 倍触发 P0、超 6 倍触发 P1，不必等预算烧完。
- 价值在于把“稳定性 vs 迭代速度”的争论变成数据决策，团队有共同语言。

```javascript
// 错误预算计算器：28 天滚动窗口 + burn rate 告警
function errorBudget({ totalRequests, badRequests, slo = 0.999 }) {
  const allowedBad = Math.floor(totalRequests * (1 - slo)); // 预算额度
  const used = badRequests;
  const remaining = allowedBad - used;

  // burn rate：按当前消耗速度，预算几天烧完
  const dailyBad = badRequests / 28;
  const burnDays = dailyBad > 0 ? remaining / dailyBad : Infinity;

  return {
    budget: allowedBad,
    used,
    remainingPct: (remaining / allowedBad * 100).toFixed(1) + '%',
    burnRate: (dailyBad / (allowedBad / 28)).toFixed(2), // 1 为匀速刚好烧完
    verdict: burnDays < 2 ? 'P0 - 立即冻结功能发布，全员修稳定性'
           : burnDays < 7 ? 'P1 - 暂停非核心迭代，修复 Top 错误'
           : 'HEALTHY - 预算健康，可正常迭代',
  };
}

console.log(errorBudget({ totalRequests: 10_000_000, badRequests: 15_000 }));
// 预算 10000，已用 15000，burnRate 4.2 -> P1
```

## 十七、安全与性能平台化
