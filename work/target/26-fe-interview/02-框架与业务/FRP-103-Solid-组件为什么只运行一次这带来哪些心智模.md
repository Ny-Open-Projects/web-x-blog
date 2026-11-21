---
title: [FRP-103] Solid 组件为什么只运行一次？这带来哪些心智模型的变化？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-103：Solid 组件为什么只运行一次？这带来哪些心智模型的变化？

**答**：
- 因为没有"重渲染"概念：组件函数在初始化时执行**一次**，产出 DOM 和表达式级 effect；此后数据变化只触发 effect，组件函数体**永远不会再执行**。
- 心智变化 1：**顶层代码 ≠ 每次渲染都跑**。`const v = props.value` 拿到的是**初始快照**（赋值一次就定了），必须写 `props.value`（访问时求值）或包 effect 才能保持追踪——Solid 故意让 props 是 Proxy getter。
- 心智变化 2：**不能用 JSX 表达式"引用"响应式值而不调用**——`<p>{count}</p>` 里 count 若是 signal 会传引用对象，必须 `count()`；忘记调用是 Solid 最常见 bug。
- 心智变化 3：Hooks 不需要依赖数组（effect 自动追踪）、解构 props 会丢响应性（与 Vue 的 toRefs 问题同源）——"框架都不喜欢解构"的深层原因都是**值拷贝破坏追踪链**。

```javascript
// 简化实验，帮助理解"组件只运行一次"的心智模型
let activeEffect = null;
function createEffect(fn) { const run = () => { activeEffect = run; fn(); activeEffect = null; }; run(); }
function createSignal(v) {
  const subs = new Set();
  return [
    () => { if (activeEffect) subs.add(activeEffect); return v; },
    (nv) => { v = nv; [...subs].forEach((e) => e()); },
  ];
}

// Solid 风格组件：函数体只执行一次
let bodyRuns = 0;
function SolidComponent(props) {
  bodyRuns++;
  const el = document.createElement('div');
  // 错误写法：顶层解构/赋值 -> 只捕获初始值
  // const label = props.title;            // 快照，之后不再更新！
  // 正确：保留属性访问，表达式放进 effect
  createEffect(() => { el.textContent = props.title; }); // 追踪 props.title 的 getter
  return el;
}

// 模拟 Solid 的响应式 props：Proxy getter，读时依赖追踪
function createProps(obj) {
  return new Proxy(obj, {
    get(t, k) {
      if (activeEffect) t.__deps?.[k]?.add(activeEffect);
      return t[k];
    },
  });
}
const props = createProps({ title: 'v1', __deps: { title: new Set() } });
const el = SolidComponent(props);
console.log('组件函数执行次数:', bodyRuns); // 1

props.title = 'v2'; // 手动触发订阅（真实 Solid 中 setter 自动通知）
props.__deps.title.forEach((e) => e());
console.log(el.textContent, '| 函数仍只跑了', bodyRuns, '次'); // v2 1
// 对比 React：setProps 会重新调用组件函数 -> bodyRuns 变 2，且 label 若是解构则永远是 v1
```
