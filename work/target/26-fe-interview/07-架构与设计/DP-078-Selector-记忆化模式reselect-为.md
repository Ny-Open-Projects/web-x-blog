---
title: [DP-078] Selector/记忆化模式：reselect 为什么能做性能优化？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-078：Selector/记忆化模式：reselect 为什么能做性能优化？
**答**：
- 记忆化：缓存纯函数的输入→输出映射，同输入直接返回缓存——以空间换时间。
- reselect 思路：selector 是"从全局 state 派生视图数据"的纯函数，输入是 `(state, props)`，输出引用相等则组件跳过渲染。
- 关键：**依赖未变时返回同一引用**（结构共享），这就是 React.memo 生效的前提。
- 前端同源：Vue 的 computed（依赖变化才重算）、useMemo、lodash.memoize。

```javascript
// 手写 memoize（单层 key + 自定义解析器）
function memoize(fn, resolver = (...a) => JSON.stringify(a)) {
  const cache = new Map();
  const memo = (...args) => {
    const key = resolver(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
  memo.cache = cache; // 暴露缓存：支持手动清理（对照 lodash.memoize）
  return memo;
}
const expensiveFilter = memoize((list, keyword) =>
  list.filter((it) => it.name.includes(keyword))
);
const data = Array.from({ length: 10000 }, (_, i) => ({ id: i, name: `item-${i}` }));
expensiveFilter(data, 'item-9');   // 真实计算一次
expensiveFilter(data, 'item-9');   // 命中缓存

// reselect 风格：多级 selector + 依赖未变返回同引用
function createSelector(...fns) {
  const last = { deps: null, result: null };
  return (...args) => {
    const deps = fns.slice(0, -1).map((fn) => fn(...args)); // 计算依赖
    const compute = fns[fns.length - 1];
    if (last.deps && deps.every((d, i) => d === last.deps[i])) {
      return last.result;                                    // 依赖引用全等 -> 直接复用
    }
    last.deps = deps;
    last.result = compute(...deps);
    return last.result;
  };
}
const getState = (state) => state.items;
const getKeyword = (_, keyword) => keyword;
const getVisibleItems = createSelector(
  getState, getKeyword,
  (items, kw) => items.filter((it) => it.name.includes(kw)) // 只在依赖变化时重算
);
const state1 = { items: data };
console.log(getVisibleItems(state1, 'item-1') === getVisibleItems(state1, 'item-1')); // true 同引用
// 组件 memo(getVisibleItems(state, kw)) —— 引用相等，跳过重渲染
```
