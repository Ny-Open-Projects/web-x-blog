---
title: [SCN-713] SLA 看板查询量大（多指标×长跨度）的性能怎么优化？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-713：看板查询性能怎么优化？
**答**：
- 查询分层：默认打开只查核心区指标 + 最近 24h（点数受控）；下钻/放大时间范围才发大查询——「按需加载范围」。
- 物化优先：查询必须命中预聚合物化（分钟/小时/天三级），禁止对原始明细即时聚合；查询 API 校验并拒绝降级到明细的请求。
- 前端优化：图表请求合并（同一时间范围的多指标一次批量查询）；虚拟时间轴（长范围渲染抽点）；SWR 缓存（同范围二次打开秒出）。
- 慢查询治理：查询 P95 预算（核心视图 < 1s），超预算的查询模式进优化清单。
- 追问钩子：用户把时间范围拉到 1 年怎么办——强制降采样到天级物化 + 前端抽点渲染，并提示「长时间范围建议用周报」。

```javascript
const QUERY_RULES = {
  maxPoints: 800,                                    // 单图最大数据点
  materializedOnly: true,                            // 拒绝明细聚合
};
function resolveQuery(range, granularity) {
  const g = granularity ?? autoGranularity(range);   // 24h→5min / 7d→1h / 1y→1d
  const points = range.ms / g;
  if (points > QUERY_RULES.maxPoints)
    throw new Error('RANGE_TOO_FINE');               // 引导降粒度而非硬扛
  return { range, g, materialized: `agg_${g}` };
}
```
