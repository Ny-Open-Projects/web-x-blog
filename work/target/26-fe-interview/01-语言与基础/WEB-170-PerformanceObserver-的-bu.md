---
title: [WEB-170] PerformanceObserver 的 buffer 满了会怎样？怎么不丢早期数据？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-170：PerformanceObserver 的 buffer 满了会怎样？怎么不丢早期数据？
**答**：
- 各类 entry 有缓冲上限（Resource Timing 默认 250 条），满了之后新条目被丢弃——SPA 接口多、页面重时很容易踩。
- 三招：buffered: true 回放观察前已产生的条目；注册后尽快 takeRecords() 清空缓冲；监听 resourcetimingbufferfull 事件并及时 clearResourceTimings()。
- 更稳的方案：SDK 在启动早期就注册 observer 并周期性取走条目，把缓冲当"溢出保险"而不是主通道。
- 丢失检测：对比"理论应上报数"与"实收数"，或利用浏览器给出的 dropped 指标确认。

```javascript
// 采集 SDK 的防丢策略：早注册 + buffered 回放 + 及时清缓冲
const pending = [];
const observer = new PerformanceObserver((list) => {
  pending.push(...list.getEntries().map((e) => e.toJSON()));
});
observer.observe({ type: 'resource', buffered: true }); // 回放已发生的资源条目
// 缓冲将满时立即转移并清空，避免新条目被丢弃
performance.addEventListener('resourcetimingbufferfull', () => {
  pending.push(...performance.getEntriesByType('resource'));
  performance.clearResourceTimings();
});
setInterval(() => { if (pending.length) send(pending.splice(0, 50)); }, 5000);
```
