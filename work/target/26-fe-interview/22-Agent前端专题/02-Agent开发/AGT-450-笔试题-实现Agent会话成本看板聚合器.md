---
title: [AGT-450] 笔试题——实现成本看板聚合（多维切片+分位数+异常检测）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-450：手写成本聚合器：按功能/模型/用户切片、P50/P95、突增异常检测

**需求与边界**：
- 输入：用量流水（[{feature, model, userId, taskId, cost, tokens, ts}]）、维度选择；输出：聚合报表+异常告警。
- 边界要求：① 多维切片（功能/模型/用户/天）；② 分位数（P50/P95——长尾可见）；③ 环比突增检测（日成本环比 >2x 告警）；④ 重试浪费单列（retry 标记的成本）。

**答**：
```javascript
function costReport(rows, { dims = ['feature', 'model'], day }) {
  const slice = (r) => dims.map(d => r[d]).join('/');
  const groups = groupBy(rows, slice);
  const report = map(groups, (g, key) => {
    const costs = g.map(x => x.cost).sort((a, b) => a - b);
    return {
      key,
      total: sum(g, 'cost'),
      p50: quantile(costs, 0.5), p95: quantile(costs, 0.95),
      taskCount: new Set(g.map(x => x.taskId)).size,
      tokens: sum(g, 'tokens'),
      retryWaste: sum(g.filter(x => x.retry), 'cost'),   // 重试浪费单列
    };
  });
  // 环比突增检测（按天总量）
  const daily = groupBy(rows.filter(r => dayOf(r.ts) === day), slice);
  const prev = await prevDay(dims);
  const alerts = map(daily, (g, key) => {
    const today = sum(g, 'cost');
    const yesterday = prev[key] ?? 0;
    return yesterday > 0 && today > yesterday * 2
      ? { key, today, yesterday,
          type: 'spike', ratio: today / yesterday }
      : null;
  }).filter(Boolean);
  return { report: sortBy(report, 'total').reverse(),
    alerts,
    topWaste: sortBy(report, 'retryWaste').reverse().slice(0, 5) };
}
// 报表视图：总成本榜 / P95 长尾榜 / 重试浪费榜 / 突增告警。
```

**评分点**:
- 多维切片 + 分位数（P50/P95）+ 任务去重计数——长尾与结构性浪费可见。
- 环比 2x 突增告警（绝对值小的时候不算——有 yesterday>0 保护）。
- 重试浪费独立统计（retryWaste）与 Top 浪费榜——归因到可行动项。
- 报表按总成本排序输出（决策友好）。
