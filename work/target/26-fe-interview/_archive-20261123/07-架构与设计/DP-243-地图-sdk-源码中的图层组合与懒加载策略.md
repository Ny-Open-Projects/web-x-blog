---
title: [DP-243] 源码识别：地图 SDK 源码中的组合模式与瓦片策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-243：源码识别：地图 SDK 源码中的组合模式与瓦片策略？
**答**:
- 组合模式：图层树（map.addLayer(layer)）——layer 可包含子层（group layer），统一 add/remove/show/hide 接口，渲染递归遍历。
- 策略：瓦片加载策略（金字塔 4 分裂、视口优先级队列、LOD 按 zoom 选层）——加载哪个瓦片、何时回收是策略集。
- 对象池/享元：瓦片图片/矢量数据缓存池（LRU + zoom 段回收），避免重复下载（DP-156 代理思想的资源版）。
- 识别要点：能解释"事件拾取：点击 → 屏幕坐标转经纬度 → 命中检测（图层 z 序）"，与 DP-239 canvas 拾取同构。

```javascript
// 图层组合 + 瓦片策略
class Layer { add(l) { this.children.push(l); } remove(l) { this.children = this.children.filter(c => c !== l); }
  render(ctx) { if (this.visible) this.children.forEach(c => c.render(ctx)); } }  // 组合递归
const tileStrategy = {
  pick(viewport, zoom) {
    const tiles = tilesInRange(viewport, zoomForLod(zoom));   // LOD 层级选择
    return tiles.sort(byDistanceToCenter);                    // 视口中心优先
  },
  evict(cache) {                                              // LRU + 层级段回收
    for (const t of cache.keys()) if (t.zoom < currentZoom - 2) cache.delete(t);
  },
};
// map.on('click', e => { const ll = projection.screenToLatLng(e); const hit = hitTest(ll, layersByZ); })
```
