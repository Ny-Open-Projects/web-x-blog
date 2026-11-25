---
title: [VIZ-145] Leaflet / Mapbox GL / Cesium / 高德 JS API 怎么选型？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-145：Leaflet / Mapbox GL / Cesium / 高德 JS API 怎么选型？
**答**：按"数据规模 × 3D 需求 × 合规 × 生态"决策：① **Leaflet**——轻量 40KB、栅格瓦片、插件丰富，适合简单标点，不支持矢量与 3D；② **Mapbox GL / MapLibre**——矢量瓦片 + WebGL，样式自由（style JSON），大规模点位与自定义图层强，国内底图合规注意瓦片源；③ **Cesium**——3D 地球/地形/倾斜摄影/时间轴，数字孪生场景，重且学习成本高；④ **高德/百度**——国内合规 + POI/路径服务齐全，深度定制受限。常见混合方案：高德底图 + ECharts GL 图层，或 MapLibre + deck.gl overlay 共享相机。

```javascript
// 选型决策表 + MapLibre 与 deck.gl 的混合渲染
const CHOICE = (need) => {
  if (need.is3DTerrain || need.photogrammetry) return 'Cesium';        // 3D 地球/倾斜摄影
  if (need.isChinaCompliance && need.poiService) return 'AMap';        // 国内合规 + POI 服务
  if (need.vectorStyle || need.pointCount > 5e4) return 'MapLibre GL'; // 矢量瓦片/WebGL
  return 'Leaflet';                                                    // 轻量标点
};
// MapLibre 底图 + deck.gl overlay：共享相机的大数据图层
import { MapboxOverlay } from '@deck.gl/mapbox';
const map = new maplibregl.Map({ container: 'map', style: styleJson });
map.addControl(new MapboxOverlay({ layers: [
  new ScatterplotLayer({ data: points, getPosition: d => d.coord, radiusMinPixels: 3 }),
  new HexagonLayer({ data: trips, extruded: true }),
]}));
```
