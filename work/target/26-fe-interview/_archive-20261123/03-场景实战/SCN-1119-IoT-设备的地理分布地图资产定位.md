---
title: [SCN-1119] IoT 设备的地理分布地图（资产定位）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1119：IoT 设备的地理分布地图（资产定位）

**答**：
- 地图：设备地理分布（园区平面图/GIS），聚合展开（密集区域）。
- 状态：点位颜色按状态（在线绿/告警红），点击进详情。
- 联动：地图选区筛选列表（双向联动）。

```javascript
// 设备地图
function deviceMap(devices, zoom) {
  const clustered = aggregatePoints(devices, zoom);    // 1091 网格聚合
  return clustered.map(c => c.type === 'cluster'
    ? { type: 'cluster', count: c.count,
        alerts: c.center && 0 }                        // 聚合内告警计数
    : { type: 'device', id: c.id, color: statusColor(c.status) });
}
function statusColor(s) { return s === 'alert' ? 'red' : 'green'; }
```
