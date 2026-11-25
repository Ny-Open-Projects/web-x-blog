---
title: [PER-285] isInputPending API 是什么？切片循环里怎么用它防止输入饥饿？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-285：isInputPending API 是什么？切片循环里怎么用它防止输入饥饿？

**答**：
- `navigator.isInputPending({ includeContinuous: false })`：同步查询"是否有待处理的用户输入（点击/按键）"，让长计算能在**处理前**主动检查用户是否在等待——不必等事件排队后才被动让出。
- 与 yield 的配合：切片循环每步先查 isInputPending——有输入立即让出（用户优先），没输入继续算。比"固定每 N ms 让出"更聪明：空闲时少让出（总耗时低），忙时马上让（INP 保住）。
- 参数：includeContinuous 默认 false 只看离散输入（click/keydown）；true 包含 pointermove/scroll 等连续输入——开 true 会让让出过于频繁，一般不开。
- 兼容：Chrome 支持，Safari/Firefox 未实现——必须降级为"固定预算让出"（isInputPending 不存在时用 time budget），两条路径都要有。

```javascript
async function processWithInputPriority(items) {
  const pending = () => navigator.isInputPending?.({ includeContinuous: false }) ?? false;
  let i = 0;
  while (i < items.length) {
    if (pending()) { await scheduler.yield(); continue; }   // 用户在等：马上让出
    const start = performance.now();
    do { step(items[i++]); }
    while (i < items.length && performance.now() - start < 30 && !pending());
    if (i < items.length) await scheduler.yield();          // 预算用尽也让出
  }
}
// 无 isInputPending 的浏览器自动退化为纯时间预算切片（pending() 恒 false）
```
