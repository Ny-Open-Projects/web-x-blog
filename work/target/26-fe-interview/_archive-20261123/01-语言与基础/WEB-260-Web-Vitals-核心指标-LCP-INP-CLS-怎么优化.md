---
title: [WEB-260] Web Vitals 核心指标 LCP/INP/CLS 怎么优化
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 性能]
type: 面试题
---

## WEB-260：Web Vitals 核心指标 LCP/INP/CLS 怎么优化

**答**：
- LCP < 2.5s（最大内容渲染）：LCP 元素通常是首屏大图/标题。优化——预加载 LCP 资源（preload）、图片设 fetchpriority=high、服务端渲染首屏、CDN 就近。
- INP < 200ms（交互到下一帧绘制）：优化——拆长任务（调度切片）、减少输入处理中的同步计算、事件处理器尽早让出主线程（用 scheduler.yield / setTimeout 分帧）。
- CLS < 0.1（累计布局偏移）：优化——图片视频写死宽高比、动态插入内容预留占位、字体 font-display: optional/swap + size-adjust、广告位固定容器。
- 采集：web-vitals 库上报真实用户数据（RUM），实验室工具（Lighthouse）仅作回归参考。

```javascript
import { onLCP, onINP, onCLS } from 'web-vitals';
const send = (m) => navigator.sendBeacon('/perf/vitals', JSON.stringify(m));
onLCP(send); onINP(send); onCLS(send);
```

**评分点**：
- 三个指标阈值与含义准确
- 每个指标给出对应优化手段
- 提到 RUM vs 实验室差异
