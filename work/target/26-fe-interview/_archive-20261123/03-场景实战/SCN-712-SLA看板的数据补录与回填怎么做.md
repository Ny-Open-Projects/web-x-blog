---
title: [SCN-712] SLA 数据补录与回填（采集故障后的数据修复）怎么做？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-712：数据补录与回填怎么做？
**答**：
- 补录场景：SDK 故障/上报管道中断导致时段数据缺失——补录后趋势图该时段从「空」变「有」，必须区分「无数据」与「数据为零」（空 ≠ 0 是看板基本功）。
- 回填策略：补录数据带 backfill 标记，图上用虚线/斜纹渲染区分实测；重算 SLO 达标率时补录与实测合并计算（同口径）。
- 排除规则：SDK 故障时段（管道自身故障）不宜计入用户 SLI——故障期间用户确实没受影响，计入会虚低；由「采集健康度」自动判定排除时段。
- 审计：补录操作留痕（谁/何时/补了哪个时段/依据），看板脚注显示「该时段含补录数据」。
- 追问钩子：怎么判定「该排除」——用管道自身可用性数据（上报网关 QPS 骤降 + SDK 心跳缺失）交叉验证，自动化判定 + 人工复核。

```javascript
async function backfill(range, { reason, operator } = {}) {
  const gap = await detectGap(range);                // 缺失时段检测
  const pipelineHealth = await health.query(range);
  const excluded = gap.filter(g => pipelineHealth.downAt(g.start, g.end));  // 管道故障时段排除
  const recoverable = gap.filter(g => !excluded.includes(g));
  await Promise.all(recoverable.map(g => recompute(g)));   // 重算
  await auditLog({ backfill: recoverable, excluded, reason, operator });
  invalidateBoard(range);                            // 看板缓存失效
}
```
