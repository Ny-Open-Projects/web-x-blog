---
title: [ARC-283] 灰度与 AB 平台的数据埋点要求如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-283：灰度与 AB 平台的数据埋点要求如何设计？
**答**：
- 分析不可信的常见原因：埋点缺失上下文。灰度/实验埋点要求：**每条事件必须带版本指纹+实验分桶快照**（用户当刻所在的所有实验组），否则分析口径错乱。
- 快照机制：SDK 维护"分桶上下文"（版本、实验 map、灰度比例、环境），任何埋点事件自动附加；实验变量变化时刻记录"曝光事件"（assignment event），分析按 assignment 起算——没有曝光事件，转化没法归因。
- 时序纪律：曝光事件先于行为事件落库（保证归因窗口正确），SDK 保证 assignment 同步打点不被批量上报延迟（ARC-076 批量上报要给 assignment 开白名单直发）。
- 数据校验：曝光量 vs 分桶配置量对账（SRM），缺失曝光事件的用户进不了分析集，占比过高说明埋点链路坏了。

```typescript
// 分桶上下文自动附加
function track(event, props = {}) {
  const enriched = {
    ...props,
    build: window.__BUILD__,
    exp: experimentContext.snapshot(),        // { checkoutB: 'B', newFeed: 'control' }
  };
  if (event === 'experiment:assignment') return beacon.sendNow(enriched);  // 曝光直发，不进批量队列
  return queue.push({ event, ...enriched });  // 其余事件批量
}
// 平台分析：以 assignment 为起点，窗口内行为事件按 exp map 归组
```
