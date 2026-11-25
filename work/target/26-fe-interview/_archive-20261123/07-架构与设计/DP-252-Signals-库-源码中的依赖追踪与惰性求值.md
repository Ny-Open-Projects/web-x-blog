---
title: [DP-252] 源码识别：Signals 库（Preact/Solid）源码中的依赖追踪？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-252：源码识别：Signals 库（Preact/Solid）源码中的依赖追踪？
**答**:
- 观察者+依赖追踪：signal 是被观察者，effect/computed 是观察者；读取 signal 时（在 effect 上下文内）自动登记依赖（与 Vue3 同款，DP-201 对比点：无 VDOM、细粒度）。
- 惰性求值：computed 只有被订阅才计算（push-pull 混合：变更 push 标记 dirty，订阅方 pull 时才算）——避免级联全算。
- 备忘录：computed 缓存值 + 版本号比对（依赖未变直接返回旧值）。
- 识别要点：能画"signal → computed → effect"依赖图并说明批量更新（无 requestAnimationFrame 的批处理队列，DP-251 的对比面）。

```javascript
// Signals 源码级简化
let currentObserver = null;
class Signal {
  #val; #subs = new Set(); #version = 0;
  constructor(v) { this.#val = v; }
  get value() { if (currentObserver) { this.#subs.add(currentObserver); currentObserver.deps.add(this); }
    return this.#val; }
  set value(v) { if (v === this.#val) return;
    this.#val = v; this.#version++;
    this.#subs.forEach(s => s.notify()); }         // push：标记 dirty
}
class Computed {
  #fn; #cached; #dirty = true; deps = new Set();
  constructor(fn) { this.#fn = fn; }
  get value() {                                     // pull：订阅方拉取
    if (this.#dirty) {
      const prev = currentObserver; currentObserver = this;
      this.deps.forEach(d => this.rebuild());       // 依赖重登记
      this.#cached = this.#fn(); currentObserver = prev;
      this.#dirty = false;
    }
    return this.#cached;                            // 备忘录
  }
  notify() { this.#dirty = true; this.subs?.forEach(s => s.notify()); }
}
function effect(fn) { const o = { deps: new Set(), notify: fn, subs: new Set() };
  currentObserver = o; fn(); currentObserver = null; return () => /* 解绑 */; }
```
