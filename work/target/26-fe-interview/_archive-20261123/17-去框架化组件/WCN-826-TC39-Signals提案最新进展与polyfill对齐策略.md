---
title: [WCN-826] TC39 Signals 提案现在到哪一步了？polyfill 如何与标准 API 对齐？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-826：TC39 Signals 提案现在到哪一步了？polyfill 如何与标准 API 对齐？

**答**：
- 结论先行：Signals 提案已进入 TC39 Stage 2/3 推进阶段，目标是提供语言级 `Signal`、`computed`、`effect` 原语——但浏览器原生支持尚早，现阶段靠 `signal-polyfill` 等对齐实现过渡。
- 提案核心：`Signal.State`（可写源）、`Signal.Computed`（派生）、`Signal.subtle.Watcher`（底层订阅，供框架接入），设计刻意保持「无调度器」——调度交给框架，标准只定义依赖图与读写语义。
- polyfill 对齐策略：用 `signal-polyfill` 包（实现 `Signal.State/Computed`），框架侧适配到自己的 effect 调度；对齐的意义在于「跨框架共享同一 signal 实例」有了统一底座。
- 迁移注意：polyfill 与最终标准可能有 API 细节差异，要封装一层适配隔离，别让业务代码直接依赖底层；用特性探测（`typeof Signal !== 'undefined'`）决定用原生还是 polyfill。
- 追问钩子：面试官会问「标准没有调度器怎么用」——答：这正是设计哲学——标准只管「值与依赖」，`Watch` + 框架自己的微任务队列负责「何时通知、何时渲染」，避免把调度策略写死进语言。

```javascript
// 特性探测：原生 Signal 优先，否则用 polyfill，业务层只依赖统一封装
import { Signal as PolySignal } from 'signal-polyfill';

const S = globalThis.Signal || PolySignal;
const count = new S.State(0);
const doubled = new S.Computed(() => count.get() * 2);

// 标准层只提供 Watch，调度由我们自己的微任务队列负责
let scheduled = false;
const watcher = new S.subtle.Watch(() => {
  if (scheduled) return;
  scheduled = true;
  queueMicrotask(() => { scheduled = false; console.log('render:', doubled.get()); });
});
watcher.watch(doubled);
count.set(2); // → render: 4
```
