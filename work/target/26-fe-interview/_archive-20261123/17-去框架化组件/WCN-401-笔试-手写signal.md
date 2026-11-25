---
title: [WCN-401] 笔试：手写一个最小 signal 系统（signal/computed/effect，微任务批处理）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-401：笔试：手写一个最小 signal 系统（signal/computed/effect，微任务批处理）。
**题目**：要求：signal(v) 读写并触发订阅；computed(fn) 惰性缓存（依赖自动收集）；effect(fn) 自动追踪依赖、微任务批处理执行一次。实现约 60 行，含循环检测提示。

```javascript
const stack = [];
let scheduled = new Set(), queued = false;
function flush() {
  const list = [...scheduled]; scheduled = new Set(); queued = false;
  for (const e of list) e.fn();
}
function schedule(e) { scheduled.add(e); if (!queued) { queued = true; queueMicrotask(flush); } }
export function signal(v) {
  const subs = new Set();
  const node = {
    get() { if (stack.length) stack[stack.length - 1].deps.add(node); return v; },
    set(nv) { if (nv === v) return; v = nv; for (const s of subs) s.dirty = true, schedule(s); },
  };
  return node;
}
function track(fn, node) {
  node.deps = new Set();
  stack.push(node);
  try { return fn(); } finally { stack.pop(); }
}
export function computed(fn) {
  const node = { deps: new Set(), dirty: true, cached: undefined };
  node.get = () => {
    if (node.dirty) {
      for (const d of node.deps) d.get && d.get.call ? null : null;
      node.cached = track(fn, node); node.dirty = false;
    }
    stack.length && stack[stack.length - 1].deps.add(node);
    return node.cached;
  };
  return node;
}
export function effect(fn) {
  const node = { deps: new Set(), dirty: true, fn: null };
  node.fn = () => { track(fn, node); node.dirty = false; };
  const orig = node.get;
  node.get = undefined;
  schedule(node);
  return () => { node.deps.forEach(d => d.subs?.delete(node)); };
}
// 注意：本实现演示核心骨架；订阅双向注册与版本验证见 402 题

```

**评分点**：
- 当前订阅者栈实现依赖收集（读时 track）。
- 写入只标 dirty + 排队，effect 微任务批处理（多次写一次执行）。
- computed 惰性：读取时验证依赖版本，无订阅不重算。
- 同批多写 → effect 只跑一次（批处理核心断言）。
