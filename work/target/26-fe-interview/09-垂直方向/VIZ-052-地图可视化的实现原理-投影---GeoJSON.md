---
title: [VIZ-052] 地图可视化的实现原理（投影 / GeoJSON / 下钻）？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-052：地图可视化的实现原理（投影 / GeoJSON / 下钻）？
**答**：地图渲染链路：**GeoJSON**（经纬度几何）→ **投影**（把球面坐标压平成平面坐标，Mercator 适合电商/位置场景，Albers 等积投影适合中国全图着色，避免高纬度面积失真）→ `d3.geoPath(projection)` 生成 SVG path 或 Canvas 绘制 → **choropleth** 着色（区域值映射发散/连续色板）。下钻要点：以 adcode 为键懒加载子级 GeoJSON 并缓存，维护区域栈支持面包屑回退；边界数据源推荐 DataV.GeoAtlas。

```javascript
// GeoJSON 经纬度 -> 投影 -> path；choropleth 着色 + 点击下钻
const projection = d3.geoMercator()
  .center([104, 36]).scale(700).translate([w / 2, h / 2]); // 中心与缩放决定视野
const path = d3.geoPath(projection);
svg.selectAll('path').data(geojson.features).join('path')
  .attr('d', path)
  .attr('fill', d => colorScale(valueMap[d.properties.adcode] ?? 0)) // choropleth
  .on('click', (e, d) => drillTo(d.properties.adcode));  // 点击下钻到子级行政区
// 下钻：adcode 懒加载子级 GeoJSON 并缓存，区域栈 + 面包屑支持回退
```

---

## 八、交互设计（VIZ-053 ~ VIZ-059）
