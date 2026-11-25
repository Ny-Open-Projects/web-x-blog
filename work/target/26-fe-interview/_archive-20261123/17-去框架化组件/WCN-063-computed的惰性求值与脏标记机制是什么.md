---
title: [WCN-063] computed 的惰性求值与脏标记（push-pull）机制是什么？相比纯 pull/push 好在哪？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-063：computed 的惰性求值与脏标记（push-pull）机制是什么？相比纯 pull/pull 好在哪？

**答**：
- 纯 push（写入即重算）：链式 computed 一处写入全链重算，即使下游没人读——浪费。
- 纯 pull（读取才重算）：每次读取都要检查整条依赖链是否过期，代价 O(链长)。
- push-pull：写入阶段只"向下传播脏标记"（O(订阅数)），真正读取时若自身是脏的才重算并清除标记。计算被推迟到有消费者的时刻，且未变化的中间 computed 可通过"值相等"短路（不继续标脏下游）。
- 短路细节：computed 重算后与新值做 Object.is 比较，相等则不通知订阅者——依赖它的 effect 不再触发（这也是"相等性判断"可定制的原因）。
- 版本号方案（如 Preact）：每个 signal 有递增 version，computed 缓存 `(value, version)`，读取时比较上游 version 判断是否过期，比布尔脏标记更精确。

```javascript
let dirty = new Set();

class Computed {
  #fn; #v; #stale = true; #subs = new Set();
  constructor(fn) { this.#fn = fn; }
  get value() {
    if (this.#stale) {
      this.#v = track(this, this.#fn);       // 执行时收集依赖
      this.#stale = false;
    }
    if (activeSub) { this.#subs.add(activeSub); activeSub.#deps.add(this); }
    return this.#v;
  }
  _invalidate() {
    if (this.#stale) return;                 // 已脏则不再传播（去重）
    this.#stale = true;
    for (const s of this.#subs) s._invalidate?.() ?? s();
  }
}
// a.value = 2 时只做 O(订阅数) 的标记；真正 el.textContent 读取 double 时才重算
```
