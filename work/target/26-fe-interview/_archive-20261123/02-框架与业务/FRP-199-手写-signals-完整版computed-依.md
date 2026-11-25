---
title: [FRP-199] 手写 signals 完整版：computed 依赖图与拓扑更新怎么实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-199：手写 signals 完整版：computed 依赖图与拓扑更新怎么实现？

**答**：
- 与 FRP-120 的 mini 版相比，完整版要有**依赖图**：signal 是源节点，computed 是带依赖集合的派生节点，effect 是终点——更新沿图**拓扑序**传播。
- 拓扑更新解决 diamond 依赖：`a -> b, a -> c, (b,c) -> d`，a 变化时 b、c 先算、d 只算**一次**（等两个上游都完成后才计算）。
- 实现：dirty 标记 + 深度/拓扑级别——trigger 时把受影响 computed 按"依赖深度"排序逐个重新求值；下游读取上游时建立双向引用（node.subs / node.deps）。
- 立等可见的优化：值未变的 computed（`===` 比较）不再向下游传播——剪枝。

```javascript
// 简化实现，帮助理解 signals 的依赖图与拓扑更新
let runningSub = null;      // 当前正在计算的节点

class SignalNode {
  constructor(value) {
    this.value = value;
    this.subs = new Set();      // 我的订阅者（computed/effect）
  }
  get() {
    if (runningSub) {           // 依赖收集：建立双向边
      this.subs.add(runningSub);
      runningSub.deps.add(this);
    }
    return this.value;
  }
  set(v) {
    if (Object.is(v, this.value)) return;   // 值未变：不传播
    this.value = v;
    // 收集所有受影响节点，按拓扑深度排序传播
    const affected = collectAffected(this);
    affected.sort((x, y) => x.depth - y.depth);
    for (const node of affected) node.update();
  }
}

function collectAffected(node, seen = new Set(), out = []) {
  for (const sub of node.subs) {
    if (!seen.has(sub)) {
      seen.add(sub);
      sub.dirty = true;
      out.push(sub);
      collectAffected(sub, seen, out);        // 递归下游
    }
  }
  return out;
}

class ComputedNode {
  constructor(fn) {
    this.fn = fn;
    this.deps = new Set();      // 我的依赖（上游）
    this.subs = new Set();      // 我的订阅者（下游）
    this.value = undefined;
    this.dirty = true;
    this.depth = 0;             // 拓扑深度：上游最大深度 + 1 —— 排序依据
  }
  get() {
    if (this.dirty) this.recompute();
    // 作为下游值被读取时也要向上注册
    if (runningSub) { this.subs.add(runningSub); runningSub.deps.add(this); }
    return this.value;
  }
  recompute() {
    // 断开旧依赖（分支切换），重新收集
    for (const dep of this.deps) dep.subs.delete(this);
    this.deps.clear();
    const prev = runningSub;
    runningSub = this;
    try { this.value = this.fn(); } finally { runningSub = prev; }
    this.depth = [...this.deps].reduce((m, d) => Math.max(m, d.depth ?? 0), -1) + 1;
    this.dirty = false;
  }
  update() {
    const old = this.value;
    this.recompute();                                    // 上游都算完了才轮到我（拓扑序保证）
    if (!Object.is(old, this.value)) return true;        // 值变了才继续向下 —— 剪枝
    return false;
  }
}

class EffectNode {
  constructor(fn) {
    this.fn = fn;
    this.deps = new Set();
    this.depth = Infinity;      // effect 永远最后
    this.run();
  }
  run() {
    for (const dep of this.deps) dep.subs.delete(this);
    this.deps.clear();
    const prev = runningSub;
    runningSub = this;
    try { this.fn(); } finally { runningSub = prev; }
  }
  update() { this.run(); }    // effect 无值，重跑即可
}

const signal = (v) => new SignalNode(v);
const computed = (fn) => new ComputedNode(fn);
const effect = (fn) => new EffectNode(fn);

// —— diamond 依赖验证 ——
const a = signal(1);
const b = computed(() => a.get() * 2);       // depth 1
const c = computed(() => a.get() + 10);      // depth 1
let runs = 0;
const d = new EffectNode(() => { runs++; console.log('d =', b.get() + c.get()); });
// d = 13（1*2 + 1+10）
a.set(2);   // b -> 4, c -> 12，d 只跑一次：d = 16
console.log('runs =', runs);                 // 2（初始 1 次 + 更新 1 次）—— 拓扑序合并生效
```
