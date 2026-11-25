---
title: [SCN-154] 地图页是转化核心页但首屏慢，地图 JSAPI 2MB、切片上百个，如何优化首屏加载？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-154：地图页是转化核心页但首屏慢，地图 JSAPI 2MB、切片上百个，如何优化首屏加载？
**答**：
- 最大头是"按需初始化"：地图不在首屏可视区就延迟初始化，JSAPI 用动态 import 在需要时加载，首屏 JS 体积直接减掉 2MB。
- 初始化后切片按可视范围 + 缩放级别加载，移动/缩放时做切片预取；静态底图选栅格瓦片按需，矢量瓦片量大但交互体验好，按产品形态取舍。
- 覆盖物（marker）多时不能全量打点：视口裁剪 + 聚合（cluster），几千个 marker 一次性 addLayer 会卡死主线程。
- 定位、周边搜索等附加服务与地图初始化并行 Promise.all，别串行排队。

```javascript
// 地图首屏优化：延迟初始化 + 动态加载 JSAPI + 视口切片预取
export function useLazyMap(containerRef, { center }) {
  useEffect(() => {
    const el = containerRef.current;
    const io = new IntersectionObserver(async ([entry]) => {
      if (!entry.isIntersecting) return;
      io.disconnect();
      // 动态 import：JSAPI 不进主包
      const AMap = await loadJSAPI('https://webapi.amap.com/maps?v=2.0&key=KEY');
      const map = new AMap.Map(el, { center, zoom: 13, viewMode: '2D', showBuildingBlock: false });
      // 初始只加载可视范围切片：设置 limitBounds 防止预加载远处切片
      map.setLimitBounds(map.getBounds());
      // 移动结束做视口数据加载 + 周边预取下一屏
      map.on('moveend', () => {
        loadMarkersInView(map);                        // 视口裁剪 + 聚合
        prefetchTiles(map.getBounds().offset(0, map.getHeight())); // 相邻屏预取
      });
      loadMarkersInView(map);
    }, { rootMargin: '200px' });                       // 差一点进视口就开始准备
    io.observe(el);
    return () => io.disconnect();
  }, []);
}

// marker 聚合：几千个点聚合渲染，而不是逐点 addMarker
function loadMarkersInView(map) {
  const bounds = map.getBounds();
  const points = store.getStores().filter(s => bounds.contains([s.lng, s.lat]));
  AMap.MarkerCluster && map.addCluster(points, { gridSize: 60 }); // 网格聚合
}
```
