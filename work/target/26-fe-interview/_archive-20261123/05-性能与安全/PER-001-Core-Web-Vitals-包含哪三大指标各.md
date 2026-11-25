---
title: [PER-001] Core Web Vitals 包含哪三大指标？各自的良好阈值是多少？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-001：Core Web Vitals 包含哪三大指标？各自的良好阈值是多少？

**答**：
- **LCP**（Largest Contentful Paint，最大内容绘制）：衡量加载性能，良好阈值小于 2.5s。
- **INP**（Interaction to Next Paint，交互到下一帧）：衡量交互响应性，良好阈值小于 200ms，2024 年 3 月起正式取代 FID。
- **CLS**（Cumulative Layout Shift，累计布局偏移）：衡量视觉稳定性，良好阈值小于 0.1。
- 实践中直接使用 Google 官方 `web-vitals` 库采集，不必手写全部观测逻辑。

```javascript
import { onLCP, onINP, onCLS } from 'web-vitals';

// npm i web-vitals —— Google 官方指标采集库
onLCP((metric) => sendToAnalytics('LCP', metric)); // 最大内容绘制，良好小于 2.5s
onINP((metric) => sendToAnalytics('INP', metric)); // 交互到下一帧延迟，良好小于 200ms
onCLS((metric) => sendToAnalytics('CLS', metric)); // 累计布局偏移，良好小于 0.1
```
