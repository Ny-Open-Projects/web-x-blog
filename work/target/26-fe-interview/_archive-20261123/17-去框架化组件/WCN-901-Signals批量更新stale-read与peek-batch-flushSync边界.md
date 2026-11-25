---
title: [WCN-901] Signals 批量更新后立刻读却拿到旧值（stale read）怎么破？peek / batch / flushSync 的边界在哪
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-901：Signals 批量更新后立刻读却拿到旧值（stale read）怎么破？peek / batch / flushSync 的边界在哪

**答**：
- 结论先行：批量（batch）的目的就是「写时标脏、微任务统一 flush」，所以同步读必然读到未提交的新值前的旧值——这是设计取舍，不是 bug。
- 要的是「立刻可见」用同步 API：Preact Signals 的 `.peek()` 跳过依赖追踪直接读最新原始值；Vue `toRef`/原始变量；或显式 `flushSync()` 强制同步提交 effect。
- 要的是「连续写合成一次」用 `batch(fn)`：把多个写包在一个批次里，只在结束时触发一次 effect，避免中间态抖动（大促库存 + 价格同帧更新场景）。
- 注意 peek 不建立依赖：在 effect 里用 peek 读会让响应式「丢依赖」，后续该 signal 变化不再触发，须配合普通读取显式声明依赖。
- 追问钩子：面试官会问「flushSync 会不会破坏批处理导致性能回退」——答：会，所以只在读后必须立刻拿到 DOM 结果的场景（如测量宽度）局部使用，不要在高频路径滥用。

```javascript
// stale read 复现与三种解法（Preact Signals 风格）
import { signal, effect, batch, flushSync } from '@preact/signals-core';
const price = signal(100), count = signal(1);
effect(() => console.log('total=', price.value * count.value));

price.value = 200; count.value = 2;
console.log('sync read:', price.peek() * count.peek()); // 400，立即读到最新

batch(() => { price.value = 300; count.value = 3; }); // 只打印一次 total=900

// 需要在同步块后立刻拿到被 effect 更新后的 DOM：
flushSync(() => { price.value = 400; }); // effect 在此同步执行完
console.log('dom already patched');
```
