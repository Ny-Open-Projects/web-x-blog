---
title: [VIZ-195] 高频题 Top15 速答。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-195：高频题 Top15 速答。
**答**：15 个高频问题一句话核心答案：① Canvas vs SVG？——位图重绘快适合大数据，矢量可交互适合小规模标注；② WebGL 管线？——顶点着色器 → 光栅化 → 片元着色器 → 帧；③ ECharts 大数据？——sampling + large + progressive + dataZoom 窗口；④ setOption 机制？——默认 merge，replaceMerge 控制替换；⑤ 百万点？——WebGL 单 draw call + quadtree 拾取；⑥ 点聚合？——Supercluster 金字塔索引查表；⑦ 坐标系转换？——WGS84→GCJ02→BD09 链式伪随机偏移；⑧ 降采样？——监控 min-max、探索 LTTB、缩略平均；⑨ 脏矩形？——只重绘变化包围盒；⑩ tooltip 原理？——独立 DOM div + formatter + 事件命中；⑪ 主题系统？——Token 三层合并 + registerTheme；⑫ 内存泄漏？——renderer.info + 堆快照找 retainer + dispose 链；⑬ 大屏适配？——scale 等比 + 事件坐标反算；⑭ 联动？——filterStore 总线 + sourceId 防循环；⑮ 性能量化？——P95 帧时长 + long task 占比 + 预算卡口。

```javascript
// 高频速答索引：题目 -> 一句话答案 + 详见题号
const TOP15 = [
  ['Canvas vs SVG', '位图快 vs 矢量可交互，按规模与交互选', 'VIZ-151'],
  ['WebGL 渲染管线', '顶点着色器到光栅化到片元着色器到帧', 'VIZ-022'],
  ['ECharts 大数据优化', 'sampling large progressive dataZoom', 'VIZ-187'],
  ['setOption 机制', '默认 merge，replaceMerge 控制替换语义', 'VIZ-183'],
  ['百万点渲染', 'WebGL 单 draw call 加 quadtree 拾取', 'VIZ-126'],
  ['点聚合', 'Supercluster 金字塔索引，缩放即查表', 'VIZ-146'],
  ['坐标系转换', 'WGS84 到 GCJ02 到 BD09 链式偏移', 'VIZ-144'],
  ['降采样选型', '监控 min-max，探索 LTTB，缩略平均', 'VIZ-129'],
  ['脏矩形', '只重绘变化包围盒', 'VIZ-120'],
  ['tooltip 原理', '独立 DOM div 加 formatter 加事件命中', 'VIZ-122'],
  ['主题系统', 'Token 三层合并加 registerTheme', 'VIZ-168'],
  ['内存泄漏排查', 'renderer.info 加堆快照找 retainer 加 dispose 链', 'VIZ-188'],
  ['大屏适配', 'scale 等比加事件坐标反算', 'VIZ-179'],
  ['跨图联动', 'filterStore 总线加 sourceId 防循环', 'VIZ-139'],
  ['性能量化', 'P95 帧时长加 long task 占比加预算卡口', 'VIZ-150'],
];
```
