---
title: [V3-215] 手写：用双向链表实现 mini 响应式依赖收集（track/trigger/unlink）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-215：手写：用双向链表实现 mini 响应式依赖收集（track/trigger/unlink）
**答**：实现 `reactive`（Proxy）+ `effect`，依赖用 3.5 式双向链表（Dep.subs 链 + Effect.deps 链互指），要求支持：重复 track 去重、重跑前精准 unlink 失效依赖、触发时只调度存活订阅者。不要求版本计数。
**评分点**：
- Dep 与 Effect 双链互指结构是否正确（prev/next 双向）
- unlink 是否 O(1)（不能遍历 Set）
- 重跑前清理是否只摘除本轮未触达的依赖（增量而非全清）
- 重复依赖不重复建链

```javascript
let activeEffect = null;
function createDep() { return { subs: null, subsTail: null }; }
function link(dep, sub) {
  const node = { dep, sub, prevSub: dep.subsTail, nextSub: null };
  if (dep.subsTail) dep.subsTail.nextSub = node; else dep.subs = node;
  dep.subsTail = node;
  const dTail = sub.depsTail;
  if (dTail) { node.prevDep = dTail; dTail.nextDep = node; }
  else sub.deps = node;
  sub.depsTail = node;
}
function unlink(node) {
  const { prevSub, nextSub, dep, prevDep, nextDep } = node;
  if (prevSub) prevSub.nextSub = nextSub; else dep.subs = nextSub;
  if (nextSub) nextSub.prevSub = prevSub; else if (dep.subsTail === node) dep.subsTail = prevSub;
  const sub = node.sub;
  if (prevDep) prevDep.nextDep = nextDep; else sub.deps = nextDep;
  if (nextDep) nextDep.prevDep = prevDep; else if (sub.depsTail === node) sub.depsTail = prevDep;
}
const targetMap = new WeakMap();
function track(target, key) {
  if (!activeEffect) return;
  let m = targetMap.get(target); if (!m) targetMap.set(target, (m = new Map()));
  let dep = m.get(key); if (!dep) m.set(key, (dep = createDep()));
  if (activeEffect.depsTail && activeEffect.depsTail.dep === dep) return; // 去重
  link(dep, activeEffect);
}
function trigger(target, key) {
  const dep = targetMap.get(target)?.get(key);
  for (let node = dep?.subs; node; node = node.nextSub) {
    if (node.sub !== activeEffect) queueEffect(node.sub);
  }
}
const queue = new Set();
function queueEffect(sub) { queue.add(sub); Promise.resolve().then(flush); }
function flush() { for (const sub of queue) { queue.delete(sub); runSub(sub); } }
function runSub(sub) {
  sub.depsTail = null;
  const prev = activeEffect; activeEffect = sub;
  sub.fn(); activeEffect = prev;
  // 摘除本轮未触达的依赖：从 depsTail 之后截断
  let node = sub.depsTail?.nextDep;
  while (node) { const next = node.nextDep; unlink(node); node = next; }
}
function reactive(obj) { return new Proxy(obj, {
  get(t, k) { track(t, k); return t[k]; },
  set(t, k, v) { t[k] = v; trigger(t, k); return true; },
}); }
function effect(fn) { const sub = { fn, deps: null, depsTail: null }; runSub(sub); return sub; }
// 验证
const s = reactive({ n: 1 });
effect(() => console.log('n =', s.n)); // n = 1
s.n = 2; // n = 2（微任务后）
```
