---
title: [OPT-044] 真实用户监控（RUM）数据和实验室数据为什么会打架？以哪个为准？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-044：真实用户监控（RUM）数据和实验室数据为什么会打架？以哪个为准？

**答**：
- 差异来源五个：**采样人群**（RUM 混入低端机/弱网）、**采集方式**（Lighthouse 模拟加载 vs 真实用户中断行为）、**统计口径**（Lab 单次值 vs RUM P75）、**缓存状态**（Lab 冷启动 vs 用户热缓存）、**第三方与 A/B**。
- 经典打架场景：Lab 全绿但 RUM 的 LCP P75 4s——通常是真实用户网络差或 LCP 元素是接口渲染的图片，Lab 没覆盖。
- 决策原则：**看趋势与归因用 Lab，定验收与预警用 RUM**；两者打架先查口径（P75 vs 均值、href 是否同版本）。
- 对齐方法：Lab 也按 RUM 用户分布选设备/网络档位，让两者可比。

```javascript
// 一一对应：RUM 与 Lab 双通道采集同一组指标，字段对齐后才能对比归因
// rum.js —— 上报字段与 Lighthouse 一一对齐
function reportOnce(entryName, value) {
  navigator.sendBeacon('/api/rum', JSON.stringify({
    metric: entryName,
    value: Math.round(value),
    // 对齐 Lab 的维度，否则对比无意义
    formFactor: matchMedia('(pointer: coarse)').matches ? 'mobile' : 'desktop',
    effectiveType: navigator.connection?.effectiveType, // RUM 独有：真实网络
    deviceMemory: navigator.deviceMemory,               // RUM 独有：真实设备档位
    buildId: document.documentElement.dataset.build,    // 与 Lab 测的版本对齐
  }));
}
new PerformanceObserver((list) => {
  const lcp = list.getEntries().at(-1);
  reportOnce('LCP', lcp.startTime); // Lab 用 numericValue，RUM 用真实时间，同名对齐
}).observe({ type: 'largest-contentful-paint', buffered: true });
// 分析时：按 buildId 分组取 P75 与同版本 Lighthouse 值比，差值 >1s 去查
// effectiveType/deviceMemory 分布——多半是某档用户被 Lab 档位遗漏
```
