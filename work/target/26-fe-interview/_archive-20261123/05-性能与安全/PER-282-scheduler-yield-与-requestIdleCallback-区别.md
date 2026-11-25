---
title: [PER-282] scheduler.yield、scheduler.postTask、requestIdleCallback 三者怎么选？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-282：scheduler.yield、scheduler.postTask、requestIdleCallback 三者怎么选？

**答**：
- `scheduler.yield()`：让出主线程后**以原优先级续排**（continuation 不降级），专治"长任务切片"，最贴近"我要把一件事分多次做完"的语义。首选。
- `scheduler.postTask(cb, {priority})`：显式调度新任务，可选 user-blocking/user-visible/background 优先级与 delay、signal；适合"延后但不急"的独立任务（如非首屏数据拉取、埋点批量）。
- `requestIdleCallback(cb, {timeout})`：浏览器空闲时才跑（timeout 兜底最晚跑），适合真正的"边角料"（日志上报、预计算、预热）。缺点：无优先级保证、Safari 长期不支持（需 polyfill）、回调里只有 deadline 没有优先级。
- 选型口诀：拆长任务用 yield；排队用 postTask；可丢的杂务用 idle；都不行再 setTimeout（注意 4ms 钳制与最低优先级）。

```javascript
// 三者的典型分工
async function heavyPipeline(data) {
  const chunks = split(data, 100);
  for (const c of chunks) {
    process(c);
    await scheduler.yield();                       // ① 切片：保优先级续排
  }
}
scheduler.postTask(() => prefetchNextPage(), { priority: 'background', delay: 1000 }); // ② 低优排队
requestIdleCallback((deadline) => {                // ③ 空闲杂务：可丢
  while (deadline.timeRemaining() > 0 && queue.length) flushLogOne();
}, { timeout: 2000 });                             // 2s 内必须跑，防饿死
// 兼容：yield 降级 postTask；postTask 降级 MessageChannel；idle 降级 setTimeout
```
