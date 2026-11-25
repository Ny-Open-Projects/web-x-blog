---
title: [NODE-602] Node 服务的告警抑制与根因定位（依赖拓扑联动）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-602：告警抑制与根因
**答**:
- 依赖抑制：DB 挂 → 所有依赖 DB 的服务告警一起炸——拓扑驱动抑制（依赖图 NODE-427：告警服务 X → 检查 X 的依赖是否已告警 → 已告警则抑制下游告警，只留根因）。
- 根因候选排序：告警触发时按拓扑+指标联动定位（根因 = 拓扑上游 + 时间最早的异常——传播方向推断）、自动下钻（NODE-432 维度嫌疑排序——平台执行）。
- 抑制的边界：不能过度抑制（真独立故障被误抑制——抑制条件保守：强依赖且时间强关联才抑制）、抑制透明（被抑制的告警仍可见——折叠呈现"被 DB 故障抑制的 12 条告警"）、抑制解除（根因恢复 → 被抑制告警自动恢复确认）。
- 实现：告警事件总线（告警 → 拓扑分析器 → 抑制决策 → 通知引擎——NODE-430 IM 机器人只收根因+摘要）、人工打破抑制（值班判断"不是 DB 的锅"——一键恢复全部）。
- 观测：抑制准确率（被抑制告警中真实由根因引起的比例）、MTTD 改善（抑制后定位提速的证据）。
```javascript
// 拓扑抑制
alerts.on('new', async (a) => {
  const upstream = await depGraph.upstream(a.svc);
  const rootCauses = upstream.filter(u => activeAlerts.has(u) && timePrecedes(u, a));
  if (rootCauses.length) return suppress(a, { cause: rootCauses[0] });   // 折叠呈现
  return notify(a);
});
```
