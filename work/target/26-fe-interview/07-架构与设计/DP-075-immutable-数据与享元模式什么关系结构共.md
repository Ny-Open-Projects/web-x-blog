---
title: [DP-075] immutable 数据与享元模式什么关系？结构共享如何实现？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-075：immutable 数据与享元模式什么关系？结构共享如何实现？
**答**：
- 不可变数据：任何修改都返回新对象、原对象永不变——React/PureComponent、 redux 时间旅行的基础。
- 享元视角：新版本对象**共享**未变化的子结构（内部状态），而不是整树深拷贝——这叫持久化数据结构/结构共享。
- 实现路径：Trie/HAMT（Immutable.js）、路径复制+冻结（Immer 的 draft + Proxy）。
- 判等优化：引用相等即可判定"未变化"（`===` 比较），这是 memo/shouldComponentUpdate 高效的原因。

```javascript
// 手写路径复制：改一个节点，只复制该路径，兄弟分支共享（享元/结构共享）
function updateIn(obj, path, value) {
  if (path.length === 0) return value;
  const [key, ...rest] = path;
  const clone = Array.isArray(obj) ? [...obj] : { ...obj }; // 浅复制当前层
  clone[key] = updateIn(clone[key], rest, value);           // 只沿修改路径递归
  return clone;
}
const state = Object.freeze({
  user: { name: 'Tom', settings: { theme: 'light', lang: 'zh' } },
  orders: [1, 2, 3],
});
const next = updateIn(state, ['user', 'settings', 'theme'], 'dark');
console.log(next.user.settings.theme);      // dark —— 表面上"已修改"
console.log(state.user.settings.theme);     // light —— 原对象不可变
console.log(next.orders === state.orders);  // true —— 未变化分支被共享（享元）
console.log(next.user === state.user);      // false —— 变化路径被复制

// Immer 的做法：Proxy draft + 写时复制（Copy-on-Write）
// import { produce } from 'immer';
// const next2 = produce(state, (draft) => { draft.user.settings.theme = 'dark'; });
// next2.orders === state.orders // true —— 同样结构共享

// 判等优化的收益：组件只需引用比较
function shouldUpdate(prev, next) {
  return prev !== next; // 结构共享下，引用相等即可跳过整棵子树的渲染
}
console.log(shouldUpdate(state.orders, next.orders)); // false —— 不重渲染
```
