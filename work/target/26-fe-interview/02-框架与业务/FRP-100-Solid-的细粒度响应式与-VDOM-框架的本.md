---
title: [FRP-100] Solid 的细粒度响应式与 VDOM 框架的本质区别是什么？编译产物长什么样？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-100：Solid 的细粒度响应式与 VDOM 框架的本质区别是什么？编译产物长什么样？

**答**：
- VDOM 框架（React/Vue）的更新单位是**组件**：数据变 → 组件函数重跑/重渲染 → 生成新 vnode → diff。Solid 的更新单位是**DOM 表达式**：组件函数只跑一次，数据变化直接调用"当初编译时生成的那条 DOM 更新语句"。
- 编译产物对比：Solid 把 `<div>{count()}</div>` 编译成 `const el = document.createElement('div'); insert(el, count)`——count 的 effect 直接写 `el.textContent`，**没有 vnode、没有 diff**。
- 响应式基于 Signals（信号）：`createSignal` 返回 getter/setter，`createEffect` 自动追踪读取的 signal，写入即精准通知——依赖收集发生在**表达式级**而非组件级。
- 性能含义：更新成本 O(受影响的表达式数)，与组件树大小无关；代价是生态/SSR 复杂度与调试（见 FRP-103）。

```javascript
// 简化实现，帮助理解 Solid 的编译产物与细粒度更新
// 源码：<div><h1>Title</h1><p>{count()}</p></div>
// Solid 编译产物（模板 + 表达式级绑定）：
function CompiledComponent() {
  const [count, setCount] = createSignal(0);
  const el = document.createElement('div');
  el.innerHTML = '<h1>Title</h1><p> </p>';       // 静态结构走 innerHTML 模板
  const p = el.querySelector('p');
  // 关键：insert 内部创建 effect，依赖只有 count 这个 signal
  createEffect(() => { p.textContent = String(count()); }); // 表达式级订阅
  return { el, setCount };
}

// 最小 signal 实现：getter/setter + 订阅集合
function createSignal(value) {
  const subs = new Set();
  const read = () => { if (activeEffect) subs.add(activeEffect); return value; };
  const write = (v) => { value = v; [...subs].forEach((e) => e()); };
  return [read, write];
}
let activeEffect = null;
function createEffect(fn) {
  const run = () => { activeEffect = run; fn(); activeEffect = null; };
  run();
}

// 对比 React 同样的组件：setCount 触发的是整个组件函数重跑 + 新 vnode diff
function ReactLikeComponent() {
  // const [count, setCount] = useState(0);
  // return <div><h1>Title</h1><p>{count}</p></div>;  // 每次重建整棵 vnode 树
}
const { el, setCount } = CompiledComponent();
setCount(1);
console.log(el.querySelector('p').textContent); // 1：只动了 p 的文本，h1 完全未参与
```
