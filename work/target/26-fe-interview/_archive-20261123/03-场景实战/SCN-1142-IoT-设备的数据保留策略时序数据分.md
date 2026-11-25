---
title: [SCN-1142] IoT 设备的数据保留策略（时序数据分层）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1142：IoT 设备的数据保留策略（时序数据分层）

**答**：
- 分层：原始 1s 数据留 7 天 → 1m 聚合留 90 天 → 1h 聚合留 2 年（存储成本控制）。
- 查询路由：按查询范围自动路由到对应层（7 天内查原始，更久查聚合）。
- 导出：长区间导出走聚合层（提示精度）。

```javascript
// 数据分层
function dataTier(from, to) {
  const days = (to - from) / 86400_000;
  if (days <= 7) return { layer: 'raw', granularity: '1s' };
  if (days <= 90) return { layer: '1m', granularity: '1m' };
  return { layer: '1h', granularity: '1h',
    note: '长区间查询使用聚合层' };
}
```
