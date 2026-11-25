---
title: [SCN-722] 错误预算燃尽图怎么设计与呈现？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-722：错误预算燃尽图怎么设计？
**答**：
- 燃尽呈现：横轴时间（30 天窗口）、纵轴剩余预算；理想线（匀速燃尽）与实际线对比——实际线在理想线下方 = 消耗过快；双视图（绝对剩余量 + burn rate）。
- 消耗构成：点开看预算去哪了（哪些事件烧的：故障/劣化/发布抖动），支持按原因拆分堆叠。
- 行动阈值线：预算剩余 50%/25%/0% 三条警示线，触线自动触发对应机制（50% 提醒/25% 限制发布/0% 冻结发布走审批豁免）。
- 预算策略配置：快慢窗口 burn rate 参数可视化配置（改参数走评审，影响告警行为）。
- 追问钩子：预算烧完冻结发布谁有权豁免——豁免需 SRE 委员会审批并自动记录（豁免次数也是健康度信号：频繁豁免说明 SLO 定得不合理或稳定性投入不足）。

```javascript
function budgetBurn(events, window30d) {
  const budget = (1 - SLO.compliance) * window30d.ms;
  let consumed = 0;
  const points = [];
  for (const e of events.sort((a, b) => a.ts - b.ts)) {
    consumed += e.downtimeMs || e.errorCount * e.weight;
    points.push({ t: e.ts, remaining: budget - consumed,
      reason: e.type });                              // 按原因可拆分
  }
  const lines = [0.5, 0.25, 0].map(p => budget * p);  // 行动阈值线
  return { budget, points, lines,
    action: points.at(-1).remaining < 0 ? 'FREEZE' : points.at(-1).remaining < budget * 0.25 ? 'LIMIT' : 'OK' };
}
```
