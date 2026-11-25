---
title: [WCN-735] 用 Signals 实现跨组件的派生状态缓存（select/reselect 模式）怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-735：用 Signals 实现跨组件的派生状态缓存（select/reselect 模式）怎么设计？

**答**：
- 结论：computed 本身就是细粒度缓存——依赖不变则不重算；对于「参数化 selector」（如按 id 取对象），用 per-key 的 computed 缓存 Map，避免为不同参数建同一个 computed。
- 用 WeakMap 以源对象为 key 缓存派生结果，保证同一源 + 同一参数复用；提供 cache.clear 在源整体替换时失效。
- 追问钩子：selector 结果被大量组件订阅，源更新时如何避免重复计算 N 次？考察「共享 computed 单例」。

```javascript
function createParamSelector(source, fn) {
  const cache = new Map();                          // key -> computed
  return (key) => {
    if (!cache.has(key)) {
      cache.set(key, computed(() => fn(source.value, key)));
    }
    return cache.get(key).value;
  };
}
const source = signal({ 1: { name: 'A' }, 2: { name: 'B' } });
const getName = createParamSelector(source, (obj, id) => obj[id]?.name);
console.log(getName(1), getName(2));               // 每个 id 独立缓存
```
