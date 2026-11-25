---
title: [MFW-837] ISR 定时失效和按需失效叠加时，最短有效 TTL 怎么算
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-837：ISR 定时失效和按需失效叠加时，最短有效 TTL 怎么算

**答**：
- 结论：任意一次失效都让缓存变陈旧，页面实际新鲜期 = 距最近一次失效的时间；有效新鲜度受 min(定时周期, 按需触发间隔) 约束。
- 落地：把按需失效当作「提前触发下一轮生成」并重新计时；记录 lastInvalidatedAt，下次定时失效 = lastInvalidatedAt + 周期。
- 追问钩子：频繁按需失效会不会让定时失效永不触发？——会，需设兜底上限（max stale），超过强制生成一次。

```javascript
let lastInvalidatedAt = Date.now();
const PERIOD = 60_000;
const MAX_STALE = 300_000;                         // 兜底上限

function onDemandInvalidate() {
  lastInvalidatedAt = Date.now();                   // 按需失效 = 重置计时
}
function nextScheduledAt(now = Date.now()) {
  const byPeriod = lastInvalidatedAt + PERIOD;
  const byMaxStale = lastInvalidatedAt + MAX_STALE;
  return Math.min(byPeriod, byMaxStale);            // 取最近触发点
}
onDemandInvalidate();
console.log(nextScheduledAt() - Date.now() <= PERIOD); // true
// 频繁按需失效 → byPeriod 不断后移，但 MAX_STALE 保证最终生成
```
