---
title: [WCN-843] 笔试：手写跨框架共享 signal 的「统一适配器」（React/Vue/Solid 三端）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-843：笔试：手写跨框架共享 signal 的「统一适配器」（React/Vue/Solid 三端）

**题目**：实现一个框架无关的 `createSharedSignal(initial)`，返回对象含 `get()`、`set(v)`、`subscribe(fn)`（fn 接收新值，返回退订函数）、`value` getter。要求：① set 时用 `Object.is` 比较，值相同不通知；② subscribe 返回的退订函数可重复调用且幂等；③ 提供三个桥接函数：`toReact(s)` 返回 `{ subscribe, getSnapshot }`（供 useSyncExternalStore）、`toVue(s, customRef)` 返回 Vue ref、`toSolid(s)` 返回 `[read, write]` 风格访问器。边界：订阅回调抛错不能阻断其他订阅者；空订阅者不报错。

**答**：

```javascript
function createSharedSignal(initial) {
  let value = initial;
  const subs = new Set();
  const api = {
    get() { return value; },
    get value() { return value; },
    set(v) {
      if (Object.is(value, v)) return;              // 相等短路
      value = v;
      for (const fn of [...subs]) {                 // 拷贝遍历，防止回调中增删
        try { fn(value); } catch (e) { queueMicrotask(() => { throw e; }); }
      }
    },
    subscribe(fn) {
      if (typeof fn !== 'function') return () => {};
      subs.add(fn);
      let active = true;
      return () => { if (active) { active = false; subs.delete(fn); } }; // 幂等退订
    },
  };
  return api;
}

// 桥接层
function toReact(s) {
  return { subscribe: (cb) => s.subscribe(() => cb()), getSnapshot: () => s.get() };
}
function toVue(s, customRef) {
  return customRef((track, trigger) => ({
    get() { track(); return s.get(); },
    set(v) { s.set(v); trigger(); },
  }));
}
function toSolid(s) {
  return [() => s.get(), (v) => s.set(v)];
}

const shared = createSharedSignal(0);
const unsub = shared.subscribe(v => console.log('React/Vue/Solid 都收到:', v));
shared.set(1); shared.set(1); // 只通知一次（相等短路）
unsub(); unsub();            // 幂等
```

**评分点**：
- 相等性用 `Object.is` 短路，避免无效通知（正确性）。
- 回调遍历用副本 + try/catch 隔离，防止互相影响与遍历中修改集合（健壮性）。
- 退订函数幂等（active 标志），符合 useSyncExternalStore 契约（细节）。
- 三个桥接函数语义正确（getSnapshot 必须返回缓存值、Vue 手动 track/trigger）（框架理解）。
