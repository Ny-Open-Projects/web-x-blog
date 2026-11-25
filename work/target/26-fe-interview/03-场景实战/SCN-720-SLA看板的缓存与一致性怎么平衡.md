---
title: [SCN-720] 看板的查询缓存与数据一致性怎么平衡？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-720：缓存与一致性怎么平衡？
**答**：
- 缓存层级：查询 API 结果缓存（按 range+granularity+版本键）→ 前端 SWR → 图表组件级缓存。TTL 按「数据段是否还在流动」分：当前小时不缓存（分钟级更新）、历史小时强缓存。
- 失效机制：数据回填/口径变更/物化重算时按版本键失效——版本键 = 指标口径版本 + 数据修正版本，避免按时间盲目失效。
- 一致性承诺：同一看板内多面板一次批量查询（同快照），保证面板间数字一致（单面板各自查可能出现 A 面板 99.98% B 面板 99.99% 的打架）。
- 边界标注：缓存命中响应带 dataAsOf，前端展示——一致性与新鲜度都显式化。
- 追问钩子：为什么「当前小时不缓存」——值班盯的是当前 burn rate，缓存 1 分钟都可能掩盖突增；历史数据 immutable 才能放心强缓存。

```javascript
function cacheKey(metric, range, g) {
  return [metric, range, g, metricVersion(metric), dataRevision(metric, range)].join('|');
}
const ttlFor = (range) => range.end >= currentHour()
  ? 0                                   // 流动数据不缓存
  : 24 * 3600_000;                      // 历史 immutable 强缓存
// 批量一致性：一次快照
async function boardSnapshot(keys, range) {
  const rev = revisionAt(keys, range);  // 同一修订版本
  return Promise.all(keys.map(k => query(k, range, { rev })));
}
```
