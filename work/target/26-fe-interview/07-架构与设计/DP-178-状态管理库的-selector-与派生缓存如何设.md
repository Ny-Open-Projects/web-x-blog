---
title: [DP-178] 状态管理库的 selector 与派生缓存如何设计？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-178：状态管理库的 selector 与派生缓存如何设计？（高频）
**答**：
- selector = CQRS 读模型（DP-137）+ 享元（相同输入共享计算结果）：组件订阅"派生视图"而不是原始 state，减少无关渲染。
- 三级缓存设计：单 selector 记忆化（输入相等短路）→ 组合 selector（上游变了下游才重算，依赖图）→ 全局缓存表（按 key 共享，跨组件复用）。
- 关键细节：输入相等判断用浅比较（reselect 默认），嵌套对象必须由上游保证引用稳定（配合 immutable 结构共享，DP-075）。

```javascript
// 一级：单 selector 记忆化（reselect createSelector 复刻）
function createSelector(...fns) {
  const resultFn = fns.pop();
  let lastArgs = null, lastResult;
  const equality = (a, b) => a === b;                          // 默认引用相等
  return (...args) => {
    const deps = fns.map((fn) => fn(...args));
    const hit = lastArgs && deps.every((d, i) => equality(d, lastArgs[i]));   // 输入全等才短路
    if (!hit) { lastArgs = deps; lastResult = resultFn(...deps); }            // 否则重算并缓存
    return lastResult;                                         // 享元：同输入同结果对象
  };
}
// 二级：组合 selector（依赖图：上游变才重算）
const selectItems = (state) => state.cart.items;
const selectKeyword = (state) => state.ui.keyword;
const selectVisibleItems = createSelector(selectItems, selectKeyword,
  (items, kw) => items.filter((i) => i.name.includes(kw)));    // items 或 kw 变才重算
const selectTotal = createSelector(selectVisibleItems,
  (visible) => visible.reduce((s, i) => s + i.price * i.qty, 0));   // 上游不变直接复用
// 三级：全局缓存表（跨组件共享同一 selector 实例）
const selectorCache = new Map();
export const getSelector = (key, factory) => {
  if (!selectorCache.has(key)) selectorCache.set(key, factory());
  return selectorCache.get(key);                               // 组件A/B 共用同一份缓存
};
// 订阅派生值而非原始 state：无关字段变更不触发本组件
useSyncExternalStore(store.subscribe, () => selectTotal(store.getState()));
```
