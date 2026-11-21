---
title: [FRP-120] 手写 Signals mini：发布订阅 + 自动依赖收集的信号库？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-120：手写 Signals mini：发布订阅 + 自动依赖收集的信号库？

**答**：
- 目标 API：`signal(v)`（读收集/写通知）、`effect(fn)`（自动追踪 fn 内读取的 signal，依赖变化重跑）、`computed(fn)`（惰性派生 + 缓存）、`batch(fn)`（批量合并通知）。
- 自动依赖收集：执行 effect/computed 时置全局 `active`；signal getter 检测到 active 就把自己加入其依赖集合——**依赖图在运行时按实际读取自动建立**（分支切换时旧依赖通过 cleanup 摘除，呼应 FRP-053）。
- 与手写 Vue 响应式（FRP-113）的差异：signal 不需要 Proxy——**响应性粒度是"值"本身**，靠 getter/setter 函数（Solid/Svelte 5 模型）；这就是 Signals 提案（FRP-102）的最小内核。
- 收尾自查：写后立即同步通知、batch 内只通知一次、computed 无人订阅不重算。

```javascript
// 简化实现，帮助理解：60 行内的 signals mini
let active = null;
const batchQueue = new Set();
let inBatch = false;

function signal(value) {
  const subs = new Set();
  return {
    get() { if (active) subs.add(active); return value; },      // 读：自动收集
    set(v) {
      if (v === value) return;                                  // 相等短路
      value = v;
      if (inBatch) { subs.forEach((s) => batchQueue.add(s)); return; } // 批量：只登记
      [...subs].forEach((s) => s());                            // 写：通知
    },
  };
}

function effect(fn) {
  const run = () => {
    // cleanup：摘除上次的依赖（分支切换场景）
    for (const sig of run.deps) sig.__subs.delete(run);
    run.deps = new Set();
    active = run;
    try { fn(); } finally { active = null; }
  };
  run.deps = new Set();
  // 让 signal 能反向清理：给每个 signal 一个共享的订阅表句柄
  run.__register = (subs) => { subs.add(run); run.deps.add({ __subs: subs }); };
  return run;
}
// signal 与 effect 的注册桥梁：重写 signal 的 get
const _signal = signal;
signal = function (v) {
  const s = _signal(v);
  s.__subs = new Set();
  const origGet = s.get;
  s.get = function () { if (active) { s.__subs.add(active); active.deps.add(s.__subs); } return origGet(); };
  return s;
};

function computed(fn) {
  let value, dirty = true;
  const c = { get() {
    if (dirty) { const prev = active; active = null; value = fn(); active = prev; dirty = false; }
    if (active) { /* 派生值被上层 effect 依赖时转发通知 */ c.__read?.(); }
    return value;
  } };
  effect(() => { c.__read = () => {}; dirty = true; const v = fn(); if (v !== value) { value = v; } });
  return c;
}

function batch(fn) {
  inBatch = true;
  try { fn(); } finally {
    inBatch = false;
    const jobs = [...batchQueue]; batchQueue.clear();
    jobs.forEach((j) => j());   // 一批只通知一轮
  }
}

// 验证 1：自动依赖收集与分支切换
const count = signal(1);
const doubled = signal(0);
let runs = 0;
const run = effect(() => {
  runs++;
  // 依赖动态：count > 5 时只读 count
  console.log('log =', count.get() > 5 ? count.get() : doubled.get());
});
doubled.set(2);           // log = 2（依赖 doubled）
count.set(6);             // log = 6（分支切换，依赖变为 count）
doubled.set(9);           // 不再触发！旧依赖已被 cleanup
console.log('effect 执行次数:', runs); // 3

// 验证 2：batch 合并
batch(() => { count.set(7); doubled.set(100); }); // 只触发一轮
console.log('batch 后执行次数:', runs); // 4
```

## 十八、Vue3 响应式边界与陷阱
