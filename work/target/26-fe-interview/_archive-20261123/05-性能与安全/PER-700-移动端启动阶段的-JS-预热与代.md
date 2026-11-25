---
title: [PER-700] 移动端启动阶段的 JS 预热与代码分包：哪些代码要预热、怎么度量预热收益？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-700：移动端启动阶段的 JS 预热与代码分包：哪些代码要预热、怎么度量预热收益？

**答**：
- 预热对象分三类：**框架与公共库**（首屏必用，随首包加载）、**高概率下一跳的路由 chunk**（点击前 idle 预取+预编译）、**重计算模块**（如日期/加密库提前 import 触发编译，用时省编译时间）。
- 手段：`<link rel=modulepreload>`（下载+解析预热）、`requestIdleCallback` 里 `import()`（触发下载与编译）、Service Worker precache（二次进入零下载）。
- 收益度量：预热命中率（预取后真被使用的比例，低于 60% 说明预取浪费流量）、首跳接口后首屏耗时对比（预热开/关 A/B）。
- 反面教训：预取过度反而挤占首屏带宽——预热策略要有预算（idle 时最多 2 个 chunk），且按用户路径数据选预热对象而不是拍脑袋。

```javascript

const warmupPlan = {
  eager: ['框架 runtime', '公共 UI 库', '请求层'],               // 随首包
  idlePrefetch: { chunks: ['detail', 'list'], budget: 2,         // idle 最多 2 个
    selector: '按用户路径漏斗数据选高概率下一跳' },
  metrics: { prefetchHitRate: '预取后被使用比例 > 60%，过低即收缩预热清单',
    abMetric: '预热开关 A/B 看首跳->首屏耗时' },
};
function scheduleWarmup(chunks) {
  (window.requestIdleCallback ?? setTimeout)(() => {
    chunks.slice(0, 2).forEach(c => import(`/routes/${c}.js`).catch(() => {})); // 预编译
  }, { timeout: 3000 });
}
// 上报 prefetchHitRate：预取记录 -> 实际路由命中统计 -> 低命中率收缩清单
```
