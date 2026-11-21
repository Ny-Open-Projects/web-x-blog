---
title: [WCN-062] Signals 的依赖追踪是怎么实现的？为什么说依赖是"运行时动态"的？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-062：Signals 的依赖追踪是怎么实现的？为什么说依赖是"运行时动态"的？

**答**：
- 核心机制：全局"当前订阅者"指针（computing stack）。effect/computed 执行时把自己压栈，signal 的 getter 被调用时把栈顶订阅者加入自己的 subscriber 集，同时把自己加入订阅者的 deps——双向边建立。
- 动态含义：依赖集不是声明时固定的，而是"上次执行实际读了什么"；分支里的 signal 只在分支被走到时才成为依赖，下次执行前会清空重建依赖集。
- 写入传播：signal 写入 → 标记直接订阅者"脏"（dirty）→ computed 不立即重算，只是向下游传播脏标记；等有人真正读取时才按需重算（push-pull 混合）。
- 去重与顺序：同一 effect 多次被标脏只处理一次（版本号/epoch 判断）；computed 的重算顺序按依赖图拓扑，避免重复计算。
- 边界：getter 之外拿到的值（解构后）不建立依赖；在 untracked 上下文读取不追踪。

```javascript
let activeSub = null;

class Signal {
  #v; #subs = new Set();
  constructor(v) { this.#v = v; }
  get value() {
    if (activeSub) { this.#subs.add(activeSub); activeSub.#deps.add(this); }
    return this.#v;
  }
  set value(nv) {
    if (nv === this.#v) return;
    this.#v = nv;
    for (const s of this.#subs) s.#markDirty();
  }
}

class Effect {
  #deps = new Set(); #dirty = true;
  constructor(fn) { this.#fn = fn; Effect.#queue.add(this); }
  #fn; static #queue = new Set();
  #markDirty() { Effect.#queue.add(this); }   // 微任务批量刷新
  run() {
    for (const d of this.#deps) d.#subs.delete(this); // 重建依赖
    this.#deps.clear();
    const prev = activeSub; activeSub = this;
    try { this.#fn(); } finally { activeSub = prev; }
  }
}
```
