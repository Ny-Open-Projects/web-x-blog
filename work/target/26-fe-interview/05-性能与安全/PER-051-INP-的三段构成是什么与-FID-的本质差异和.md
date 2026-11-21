---
title: [PER-051] INP 的三段构成是什么？与 FID 的本质差异和采样陷阱在哪里？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-051：INP 的三段构成是什么？与 FID 的本质差异和采样陷阱在哪里？

**答**：
- INP 覆盖**输入延迟**（Input Delay，事件排队等待主线程）+ **处理时长**（Processing，事件回调执行）+ **呈现延迟**（Presentation，渲染下一帧）三段；FID 只测第一段，所以 FID 好看不代表不卡。
- INP 取页面生命周期内**所有交互**里最差的一次（约等于 P98，取每 50 个交互中最慢的那个），而不是像 FID 只看第一次交互。
- 采样陷阱：web-vitals 库在页面卸载前通过 `sendBeacon` 补报最终值，若用户中途离开且未触发卸载回调会丢样本；单页应用路由切换不会重置观测，需自己按路由归因。
- 优化顺序：先消处理时长里的长任务（拆分、Worker），再降呈现延迟（避免回调里强制同步布局），最后处理输入延迟（预加载交互所需代码）。

```javascript
import { onINP } from 'web-vitals/attribution';

// 带归因的 INP 采集，能看到三段各自耗时和拖慢它的元素
onINP((metric) => {
  const a = metric.attrribution ?? metric;
  sendBeacon('/api/vitals', JSON.stringify({
    name: 'INP',
    value: Math.round(metric.value),
    inputDelay: Math.round(a.inputDelay ?? 0),        // 第一段：排队等待
    processingDuration: Math.round(a.processingDuration ?? 0), // 第二段：回调执行
    presentationDelay: Math.round(a.presentationDelay ?? 0),   // 第三段：渲染下一帧
    element: a.element?.tagName,                      // 哪个元素拖慢的
    event: a.eventType,                               // click / input / keydown
    path: location.pathname,
  }));
}, { reportAllChanges: false }); // 默认只报最终 P98 值，避免样本膨胀
```
