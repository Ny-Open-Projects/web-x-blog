---
title: [WCN-964] 实时行情 / 监控大盘高频数据下 WC 更新怎么批处理
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-964：实时行情 / 监控大盘高频数据下 WC 更新怎么批处理

**答**：
- 结论先行：大盘同时更新成百上千个指标，逐条 set signal 会造成写放大；核心是「采集层批量、渲染层合帧、可视层裁剪」三层过滤。
- 采集层：WebSocket 消息先进队列，按 symbol 聚合（每条只保留最新值），避免同一标的短时间内多次写。
- 渲染层：用 signal 存储「快照对象」而非每个指标一个 signal，一次赋值替换整个快照，下游 computed 按变化字段派生，减少 effect 数量。
- 可视层：只对视口内的卡片订阅高频更新，屏外卡片暂停（IntersectionObserver 控制订阅开关），滚动进入再补最新值。
- 追问钩子：面试官问「怎么保证不丢帧数据」——答：队列聚合允许丢中间值（行情只看最新），但关键事件（成交/告警）走单独不可丢通道，区分「状态数据」与「事件数据」。

```javascript
// 采集层：按 symbol 聚合，只保留最新快照
let buffer = new Map();
function onQuote(sym, price) { buffer.set(sym, price); } // 高频入队
// 渲染层：每帧一次整体赋值
function flush() {
  if (!buffer.size) return;
  snapshot.value = { ...snapshot.value, ...Object.fromEntries(buffer) };
  buffer = new Map();
}
requestAnimationFrame(function loop() { flush(); requestAnimationFrame(loop); });
// 快照 signal + 派生 computed（只重算变化字段的下游）
const snapshot = { value: {}, set(v) { this.value = v; } };
onQuote('AAPL', 190); onQuote('AAPL', 191); // 聚合为 191
```
