---
title: [DP-081] Mixin 有什么陷阱？为什么演进到 Hook/组合式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-081：Mixin 有什么陷阱？为什么演进到 Hook/组合式？
**答**：
- Mixin：把一组属性/方法混入目标类/组件（`Object.assign`、Vue.mixin、React.createClass 的 mixins）。
- 陷阱：命名冲突静默覆盖、来源不可见（模板里 `this.foo` 不知来自哪个 mixin）、隐式依赖（mixin 之间互相调用方法）、多实例状态纠缠。
- 演进：React 2016 官方宣布"mixins considered harmful"→ HOC/render props → Hooks；Vue2 mixin → Vue3 组合式函数（composables）。
- 本质变化：从"隐式混入属性"变成"显式函数调用 + 显式返回值"，来源与依赖一目了然。

```javascript
// Mixin 的三大陷阱演示
const loggerMixin = {
  log(...args) { console.log('[log]', ...args); },   // 方法A
  name: 'logger',
};
const trackerMixin = {
  log(...args) { console.log('[track]', ...args); }, // 同名方法B：冲突！
  name: 'tracker',
};
class Widget {}
Object.assign(Widget.prototype, loggerMixin, trackerMixin); // 后者覆盖前者，静默丢失
const w = new Widget();
w.log('x');           // [track] x —— loggerMixin.log 无声消失（陷阱1：命名冲突）
console.log(w.name);  // tracker —— 来源不可见（陷阱2）：读代码时不知道 name 来自哪
// 陷阱3：隐式依赖 —— mixin 内调用 this.render()，要求宿主必须实现 render，契约藏在运行时

// Vue2 mixin 同样的问题
// const pageMixin = { data: () => ({ loading: false }), methods: { load() {} } };
// 两个 mixin 都有 loading -> 合并策略碰运气；load 被谁调用 -> 全局搜索

// 演进：Vue3 组合式函数 —— 显式来源、显式依赖、显式返回
// usePageData.js
// export function usePageData(fetcher) {
//   const loading = ref(false);
//   const data = ref(null);
//   const load = async () => { loading.value = true; data.value = await fetcher(); loading.value = false; };
//   return { loading, data, load };   // 返回值即契约
// }
// 组件内：
// const { loading, data, load } = usePageData(() => fetch('/api/list').then(r => r.json()));
// loading 来自哪、重名怎么解决（解构重命名）、依赖是什么 —— 全部显式（陷阱全消）
```
