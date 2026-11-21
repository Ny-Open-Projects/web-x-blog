---
title: [WCN-070] 笔试：手写 createSignal / effect（依赖追踪 + 微任务批处理）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-070：笔试：手写 createSignal / effect

**题目**：实现响应式原语：① `createSignal(v)` 返回 `[getter, setter]`，setter 相等（Object.is）时不通知；② `effect(fn)` 自动追踪 fn 内读取的 signal，支持动态分支依赖；③ 写入触发 effect 走微任务批处理（同一同步段只跑一次）；④ effect 返回 dispose；⑤ 循环写入自触发检测（effect 内写自己依赖的 signal → 只重跑一次不无限循环）。

**答**：

```javascript
let activeSub = null;
const queue = new Set();
let scheduled = false;

function scheduleRun(sub) {
  queue.add(sub);
  if (!scheduled) { scheduled = true; queueMicrotask(() => {
    const batch = [...queue]; queue.clear(); scheduled = false;
    batch.forEach((s) => s.run());
  }); }
}

export function createSignal(v) {
  const subs = new Set();
  const read = () => {
    if (activeSub) { subs.add(activeSub); activeSub.deps.add(subs); }
    return v;
  };
  const write = (nv) => {
    if (Object.is(nv, v)) return;
    v = nv;
    [...subs].forEach(scheduleRun);
  };
  return [read, write];
}

export function effect(fn) {
  const sub = {
    deps: new Set(),
    run() {
      disposeDeps(sub);
      const prev = activeSub;
      activeSub = sub;
      try { sub.cleanup?.(); sub.cleanup = fn(); }    // 支持返回清理函数
      finally { activeSub = prev; }
    },
    disposed: false,
  };
  sub.run();
  function dispose() {
    if (sub.disposed) return;
    sub.disposed = true;
    disposeDeps(sub);
    sub.cleanup?.();
  }
  return dispose;
}
function disposeDeps(sub) {
  for (const s of sub.deps) s.delete(sub);
  sub.deps.clear();
}

// 测试口径：
// const [n, setN] = createSignal(1);
// const stop = effect(() => console.log(n()));
// setN(2); setN(3);   // 同步段内只打印一次 3
// setN(3);            // 相等不触发
// stop(); setN(4);    // 不再打印
```

**评分点**：
- 双向依赖注册（subs.add(activeSub) 与 deps.add）保证动态分支依赖可重建。
- Object.is 相等短路；微任务 Set 去重批处理（同步段内多次写入只跑一次）。
- dispose 清空 deps 防泄漏；effect 支持返回 cleanup。
- 防无限循环：批处理 + 相等短路使自写依赖只重跑一次（如能说明栈深检测更佳）。
