---
title: [DP-359] 适配器模式实战：第三方 SDK 统一封装
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-359：适配器模式：SDK 统一

**答**：
- 适配器的价值：第三方 SDK 的差异（各埋点 SDK 的 track 签名不同）用适配器抹平——业务只依赖统一接口，换 SDK 不改业务
- 实战结构：统一接口（Analytics { track, identify }）+ 各 SDK 适配器（GATracker/SensorsTracker 实现同接口）+ 工厂按配置选择
- 双写期适配：迁移期同时上报两家（适配器组合——数据校验双跑）——适配器天然支持过渡
- 适配器的「语义翻译」：SDK 的事件模型不同（GA 的 category/action vs 神策的 event/props）——适配器做语义映射（映射表可测）
- 深水点：适配器的「能力降级」——SDK 缺失某能力（实时推送）时适配器返回「不支持」而不是静默丢数据——能力探测协议

```javascript
// 统一接口
export class Analytics {
  #impl;
  constructor(impl) { this.#impl = impl; }
  track(event, props) {
    if (!this.#impl.capabilities.includes(event.type))
      return { ok: false, reason: 'unsupported' };   // 能力降级协议
    return this.#impl.track(event, props);
  }
}
// GA 适配器
class GAAdapter {
  capabilities = ['pageview', 'click'];
  track(e, p) { gtag('event', e.name, { event_category: e.type, ...p }); }
}
// 双写迁移: new Analytics([new GAAdapter(), new SensorsAdapter()]) — 组合适配器
```
