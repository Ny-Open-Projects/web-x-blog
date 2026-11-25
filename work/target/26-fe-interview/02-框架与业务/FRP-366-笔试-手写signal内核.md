---
title: [FRP-366] 笔试：手写 signal 内核（读时订阅 + 批量传播）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-366：笔试：手写 signal 内核

**答**：实现最小 signal 库：① `signal(v)` 返回读写函数（Solid 风格：调用读、传参写）；② `effect(fn)`：fn 内读 signal 自动订阅（读时订阅），写触发重跑；③ 批量传播：`batch(fn)` 内多次写只触发一次 effect；④ effect 嵌套栈支持（外层 effect 读内层 signal 正确归属）；⑤ 无循环保护（effect 内写自己读的 signal 告警）。写出实现。

```javascript
let active = null;                 // effect 栈
const stack = [];
let batchDepth = 0, queued = new Set();

function signal(value) {
  const subs = new Set();
  const read = () => {
    if (active) { subs.add(active); active.deps.add(subs); }   // 读时订阅
    return value;
  };
  const write = (nv) => {
    if (Object.is(value, nv)) return;
    value = nv;
    if (batchDepth > 0) { subs.forEach(s => queued.add(s)); return; }   // 批处理: 攒
    subs.forEach(s => s.run());
  };
  read[Symbol.toPrimitive] = read; read.set = write;
  return read;
}

function effect(fn) {
  const e = {
    deps: new Set(),
    run() {
      cleanup(e);                                  // 先清旧依赖(分支重连)
      stack.push(active); active = e;
      try { fn(); } finally { active = stack.pop(); }
    },
  };
  e.run();
  return () => cleanup(e);
}
function cleanup(e) { for (const subs of e.deps) subs.delete(e); e.deps.clear(); }

function batch(fn) {
  batchDepth++;
  try { fn(); }
  finally {
    if (--batchDepth === 0) { const q = queued; queued = new Set(); q.forEach(s => s.run()); }
  }
}
// 用法
const count = signal(1);
const name = signal('a');
effect(() => console.log(count(), name()));    // 读时自动订阅
batch(() => { count.set(2); name.set('b'); }); // 只触发一次 effect
```

**评分点**：
- 读时订阅（active effect 栈 + deps 双向登记）
- cleanup（分支依赖重连的正确性）
- batch 深度计数与延迟传播（一次通知）
- 循环写告警的认知
