---
title: [WCN-072] 笔试：手写 Signals 版 Store（嵌套 signal + selector 订阅）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-072：笔试：手写 Signals 版 Store

**题目**：实现 `createStore(initial)`：① 顶层对象每个键变成独立 signal（浅层），键值变化只触发订阅该键的订阅者；② `store.set('key', v)` 更新并通知；③ `useSelector(store, selFn)` 返回 computed，仅当选择结果变化才触发 effect；④ 支持嵌套对象键（`store.set('user.name', x)` 时按顶层 `user` 信号处理）；⑤ 提供整树快照 `store.snapshot()`。

**答**：

```javascript
import { createSignal, computed, effect } from './mini.js';

export function createStore(initial) {
  const signals = new Map();
  const get = (k) => {
    if (!signals.has(k)) signals.set(k, createSignal(initial[k]));
    return signals.get(k);
  };
  // 初始化所有顶层键
  Object.keys(initial).forEach(get);

  return {
    get(k) { return get(k)[0](); },
    set(path, v) {
      const top = path.split('.')[0];           // 嵌套路径归并到顶层信号
      const cur = get(top)[0]();
      if (path.includes('.')) {
        const rest = path.slice(top.length + 1).split('.');
        const next = structuredClone(cur);
        let o = next;
        rest.slice(0, -1).forEach((k) => (o = o[k]));
        o[rest.at(-1)] = v;
        get(top)[1](next);
      } else get(top)[1](v);
    },
    selector(selFn) { return computed(() => selFn(this)); },
    snapshot() {
      return Object.fromEntries(
        [...signals.entries()].map(([k, [read]]) => [k, read()]));
    },
  };
}

// 用法口径
const store = createStore({ user: { name: 'a', age: 1 }, items: [] });
const nameSel = store.selector((s) => s.get('user').name);
effect(() => console.log(nameSel()));       // 只依赖 user.name 所在的顶层信号
store.set('user.age', 2);                   // computed 重算但 name 未变 → 不触发
store.set('user.name', 'b');                // 触发打印 'b'
```

**评分点**：
- 按键懒建 signal（Map 缓存），顶层信号粒度使无关键更新不互相触发。
- selector 是 computed，结果相等短路阻止下游 effect（细粒度订阅的关键）。
- 嵌套路径写入归并到顶层信号并保持不可变更新（structuredClone）。
- snapshot 一致性（同步读取所有顶层信号）。
