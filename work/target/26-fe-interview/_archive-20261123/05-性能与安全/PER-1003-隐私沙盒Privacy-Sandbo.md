---
title: [PER-1003] 隐私沙盒（Privacy Sandbox）对前端埋点的冲击与迁移
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1003：隐私沙盒（Privacy Sandbox）对前端埋点的冲击与迁移

**答**：
- Topics API 取代三方 Cookie 兴趣分类：浏览器本地计算话题，调用方拿到粗粒度兴趣，无个体标识。
- Protected Audience（FLEDGE）：设备端竞价，广告主不再拿用户明细。
- Attribution Reporting：转化归因改为浏览器聚合报告（带噪声、延迟），点击/展示注册后延迟回传。
- 前端迁移：埋点从"标识个体"转向"事件 + 可聚合维度"；归因改接 Attribution API；A/B 实验用 first-party cohort。

```javascript
// Attribution Reporting 注册
function registerConversion(clickId) {
  fetch('/click?tid=' + clickId, {
    attributionReporting: {
      eventSourceEligible: true,     // 允许后续归因
      triggerEligible: false,
    },
  });
}
// 转化端（服务端响应头）：
// Attribution-Reporting-Register-Trigger:
//   {"event_trigger_data":[{"key":"purchase"}],"aggregatable_trigger_data":[...]}
// 前端只需保证关键点击/转化打上注册标记，报告由浏览器延迟回传
```
