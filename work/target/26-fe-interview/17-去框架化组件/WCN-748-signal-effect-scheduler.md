---
title: [WCN-748] 笔试：手写 signal effect 的微任务批处理调度器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-748：笔试：手写 signal effect 的微任务批处理调度器

**答**：
- 需求：实现 `createScheduler()` 返回 `{ effect(fn), flush() }`。effect 立即执行一次并收集依赖（简化：直接记录 fn），当依赖 signal 变化时把 fn 排入队列，多个变化只调度一次（通过 queueMicrotask 或手动 flush）；flush 执行所有排队 fn 并清空。
- 要点：用 Set 存待执行 effect 去重；scheduled 标志防止重复入队；effect 首次执行返回清理函数；边界：flush 中再次触发变化要继续处理（循环到空）。

```javascript
function createScheduler() {
  const queue = [], queued = new Set();
  let scheduled = false;
  function schedule(fn) {
    if (queued.has(fn)) return;
    queued.add(fn); queue.push(fn);
    if (!scheduled) { scheduled = true; queueMicrotask(flush); }
  }
  function effect(fn) {
    const wrapped = () => { fn(); };
    wrapped();                                  // 立即执行一次
    wrapped.trigger = () => schedule(wrapped);  // 依赖变化时调用
    return wrapped;
  }
  function flush() {
    scheduled = false;
    let guard = 0;
    while (queue.length) {
      if (++guard > 1000) throw new Error('effect 循环'); // 防死循环
      const fn = queue.shift(); queued.delete(fn); fn();
    }
  }
  return { effect, flush };
}
const s = createScheduler();
let runs = 0;
const e = s.effect(() => { runs++; });
e.trigger(); e.trigger();                       // 连续触发只排一次
s.flush();
console.log('执行次数:', runs);
```

**评分点**：
- Set 去重 + scheduled 标志保证多次变化只调度一次。
- effect 立即执行一次并返回可触发函数，语义完整。
- flush 循环处理到队列空，覆盖执行中再次变化的场景。
- guard 防死循环，具备健壮性。
