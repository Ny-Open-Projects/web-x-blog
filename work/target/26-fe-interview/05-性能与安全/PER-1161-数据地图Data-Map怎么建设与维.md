---
title: [PER-1161] 数据地图（Data Map）怎么建设与维护
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1161：数据地图（Data Map）怎么建设与维护

**答**：
- 内容：数据分类目录 × 存储位置 × 责任人 × 保留期 × 流向（上下游）——一张图回答"什么数据在哪里"。
- 建设：从字段注册表自动推导（事件→存储表→下游 ETL→报表），人工补充缺失环节。
- 维护：每次数据架构变更（新表/新下游）强制更新数据地图，CI 校验注册表与地图一致性。
- 用途：DSAR 定位、泄露影响评估、监管问询答复的基础设施。

```javascript
// 数据地图节点与边
const DATA_MAP = {
  nodes: {
    'events.lcp': { owner: 'fe-platform', level: 1, retention: 30 },
    'orders.amount': { owner: 'commerce', level: 2, retention: 1095 },
  },
  edges: [
    { from: 'events.*', to: 'warehouse.events', transform: 'agg' },
    { from: 'orders.*', to: 'crm.export', transform: 'pseudonymized' },
  ],
};
function traceFlow(field) {
  const outs = DATA_MAP.edges.filter(e => e.from.startsWith(field.split('.')[0]));
  return { field, flows: outs.map(e => e.to),
    level: DATA_MAP.nodes[field]?.level ?? 'unknown' };
}
```
