---
title: [SCN-261] 地图首屏优化——地图 JSAPI 的加载与初始化提速？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-261：地图是转化核心页但首屏慢，地图 JSAPI 怎么提速？

**答**:
- 加载策略：SDK 按需异步加载（动态 script 注入，不阻塞页面解析）、入口预取（列表页 prefetch 地图 SDK——用户点击进地图页时已就绪）、SDK 瘦身（按需模块：只要地图+点标记就不引全量插件）。
- 初始化提速：容器先渲染（地图容器布局先稳定——防止 SDK 加载后容器尺寸变化抖动）、初始视野预设（先渲染低精度底图+骨架，SDK ready 后精化）、瓦片预取（初始视野的瓦片提前预热）、配置复用（key/配置常量化避免重复申请）。
- 数据与渲染分层：首屏只渲染核心 marker（可视区聚合），非核心图层（热力/轨迹）延迟初始化；marker 数据走独立接口（地图框架加载与业务数据并行）。
- 监控：地图 SDK 加载耗时/初始化耗时/首帧 marker 渲染耗时三个指标独立埋点——定位慢在哪个环节（SDK 下载 vs 初始化 vs 数据）。

```javascript
// 入口预取 + 动态加载
const loadMap = once(async () => {
  await injectScript(`//api.map.com/v3?key=${KEY}`);
  return initMap(container, { viewMode: '2D' });  // 2D 更快
});
listPage.on('idle', () => loadMap().catch(() => {}));  // 预取
// 初始化：容器先稳定 → 低精度底图 → marker 数据并行
const [map, markers] = await Promise.all([
  loadMap(), fetchMarkers(bbox) ]);
map.add(markersToCluster(markers));       // 可视区聚合渲染
// 指标：sdkLoad / init / firstMarkers 三段埋点。
```
