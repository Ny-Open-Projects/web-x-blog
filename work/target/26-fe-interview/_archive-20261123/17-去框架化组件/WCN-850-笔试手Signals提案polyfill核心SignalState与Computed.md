---
title: [WCN-850] 笔试：手写 Signals 提案 polyfill 核心（Signal.State / Computed / subtle.Watch）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-850：笔试：手写 Signals 提案 polyfill 核心（Signal.State / Computed / subtle.Watch）

**题目**：模拟 TC39 Signals 提案的最小 polyfill。要求实现：① `Signal.State(initial)`：有 `get()`/`set(v)`，set 用 Object.is 去重并标脏下游；② `Signal.Computed(fn)`：惰性求值（首次 get 或依赖变更后再 get 才重算），带脏标记；③ 运行时依赖追踪——全局当前观察者栈，get 时收集依赖、set 时通知下游computed 标脏；④ `Signal.subtle.Watch(callback)`：watch 一个 computed，当其变化时把 computed 加入「待通知队列」，由外部显式调用 `watcher.getPending()` 取出（提案的「无自动调度」语义）；⑤ 循环依赖检测（ effect/computed 读写自己造成环时抛错）。边界：computed 依赖多个源、菱形依赖（a→b→c 和 a→d→c）只触发一次重算。

**答**：

```javascript
let OBSERVER = null;                     // 当前正在求值的 computed
const STATE = Symbol('state');

function makeSignal(fn, isState) {
  const node = {
    [STATE]: { value: undefined, dirty: true, sources: new Set(), observers: new Set(), computing: false },
    get() {
      const st = this[STATE];
      if (OBSERVER) link(OBSERVER, this);
      if (!isState && st.dirty) recompute(this);
      return st.value;
    },
  };
  if (isState) node.set = (v) => {
    const st = node[STATE];
    if (Object.is(st.value, v)) return;
    st.value = v; markDirty(node);
  };
  else node[STATE].fn = fn;
  return node;
}
function link(observer, source) {
  observer[STATE].sources.add(source); source[STATE].observers.add(observer);
}
function recompute(node) {
  const st = node[STATE];
  if (st.computing) throw new Error('循环依赖');
  st.computing = true; OBSERVER = node;
  try { st.value = st.fn(); st.dirty = false; } finally { OBSERVER = null; st.computing = false; }
}
function markDirty(node, seen = new Set()) {
  if (seen.has(node)) return; seen.add(node);              // 菱形依赖去重
  const st = node[STATE];
  if (!st.dirty) { st.dirty = true; st.observers.forEach(o => markDirty(o, seen)); }
}

export const Signal = {
  State: (v) => { const s = makeSignal(null, true); s[STATE].value = v; s[STATE].dirty = false; return s; },
  Computed: (fn) => makeSignal(fn, false),
  subtle: {
    Watch(callback) {
      const pending = new Set();
      return {
        watch(c) { c[STATE].watchers?.add(callback); /* 简化：变化时加入 pending */ c[STATE].onChange = () => pending.add(c); },
        getPending() { const out = [...pending]; pending.clear(); return out; },
      };
    },
  },
};
// 用法：const a = Signal.State(1); const b = Signal.Computed(() => a.get()*2); b.get()===2; a.set(3); b.get()===6;
```

**评分点**：
- 惰性求值 + 脏标记，get 时才重算（computed 核心语义）。
- 运行时依赖追踪（全局 OBSERVER + link 双向记录 sources/observers），set 只标脏下游（正确性）。
- 菱形依赖用 seen 去重、循环依赖用 computing 标志检测（易错边界）。
- Watch 的「外部显式取 pending」体现提案「无内置调度器」设计哲学（对标准的理解深度）。
