---
title: [R19-124] 如何在 React 应用接入 web-vitals 性能上报？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-124：如何在 React 应用接入 web-vitals 性能上报？
**答**：
- 标准指标五件套：LCP（首屏）、INP（交互响应性，React 长任务最敏感）、CLS（布局偏移）、TTFB、FCP。
- onXxx 回调里拿 metric，用 sendBeacon 上报（页面卸载也不丢）。
- 上报维度带上路由与用户标识，才能按页面聚合出劣化榜单。
- INP 差通常是长任务：回看 R19-097 的 useDeferredValue 与代码分割。

```javascript
// vitals.ts —— web-vitals 标准指标 + 上报埋点
import { onLCP, onINP, onCLS, onTTFB, onFCP } from 'web-vitals';
import { getUserId } from './auth';

function sendToAnalytics(metric) {
  // sendBeacon 不阻塞卸载，页面关闭也能发出去
  navigator.sendBeacon('/api/vitals', JSON.stringify({
    name: metric.name,          // LCP / INP / CLS / TTFB / FCP
    value: metric.value,
    rating: metric.rating,      // good / needs-improvement / poor
    id: metric.id,              // 同一会话去重
    route: location.pathname,
    userId: getUserId(),
  }));
}

onLCP(sendToAnalytics);   // 首屏最大元素渲染时间
onINP(sendToAnalytics);   // 交互响应性，React 长任务最敏感
onCLS(sendToAnalytics);   // 布局偏移，关注图片与骨架屏
onTTFB(sendToAnalytics);
onFCP(sendToAnalytics);
```
