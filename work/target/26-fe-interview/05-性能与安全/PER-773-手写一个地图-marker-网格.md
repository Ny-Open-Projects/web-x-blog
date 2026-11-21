---
title: [PER-773] 手写一个地图 marker 网格聚合器：网格聚类、聚合点展开与视野增量更新
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-773：手写一个地图 marker 网格聚合器：网格聚类、聚合点展开与视野增量更新

**答**：
- 实现：按当前 zoom 计算网格尺寸（zoom 每升 1 网格减半），marker 投影到网格取代表点（第一个或质心）；视野变化（moveend）时只重算可见网格；聚合点点击展开（zoom+1 或弹出列表）。
- 要点：聚合在数据层（纯计算）与渲染层（画点）分离；增量更新——上次视野内已聚合的网格不重算（缓存 key：zoom+grid）；marker 数量大时聚合计算进 Worker（> 2000 点）。
- 边界：聚合点数量文本实时更新；重叠网格边界 marker 抖动（网格 key 稳定算法：固定世界坐标网格而非屏幕网格）。
- 评分点：世界坐标网格与增量缓存。

```javascript

class MarkerCluster {
  constructor(markers, { worker } = {}) { this.markers = markers; this.worker = worker; }
  clustersFor(bounds, zoom, cache) {
    const gridSize = 256 / Math.pow(2, zoom);                    // 世界坐标网格
    const key = `${zoom}:${boundsKey(bounds)}`;
    if (cache.has(key)) return cache.get(key);                   // 增量缓存
    const cells = new Map();
    for (const m of this.markers) {
      if (!inBounds(m, bounds)) continue;                        // 只算可见
      const gx = Math.floor(m.lng / gridSize), gy = Math.floor(m.lat / gridSize);
      const cell = cells.get(`${gx}:${gy}`) ??= { count: 0, lng: 0, lat: 0, members: [] };
      cell.count++; cell.lng += m.lng; cell.lat += m.lat;
      cell.members.push(m.id);
    }
    const out = [...cells.values()].map(c => ({
      lng: c.lng / c.count, lat: c.lat / c.count, count: c.count,
      expandable: c.count > 1, ids: c.members,
    }));
    cache.set(key, out);
    return out;
  }
}
// 渲染层只画聚合点（count>1 画数字气泡，=1 画原 marker），点击 expandable 聚合点 zoom+1
```
