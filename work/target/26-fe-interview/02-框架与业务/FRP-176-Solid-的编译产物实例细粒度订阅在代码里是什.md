---
title: [FRP-176] Solid 的编译产物实例：细粒度订阅在代码里是什么形态？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-176：Solid 的编译产物实例：细粒度订阅在代码里是什么形态？

**答**：
- Solid 编译产物是**一次执行**的 setup 函数：`createSignal/createMemo/createEffect` + 直接的 DOM 构建，组件函数只跑一次（不是 render 函数）。
- 模板复用：编译器先把模板转成 `<template>` 元素（或字符串），运行时 `cloneNode` 克隆——DOM 创建成本极低。
- 动态表达式编译成 **getter 传入 helper**：`{count()}` → `insert(el, () => count())` ——insert 内部建 effect 订阅 count，变化时只改这一个文本节点。
- 细粒度的完整含义：订阅建立在**表达式级**，没有组件级重渲的概念——与 Vapor Mode（FRP-138）同思路，但 Solid 从第一天就如此设计。

```javascript
// 简化实现，帮助理解 Solid 产物
// —— 输入 JSX ——
// <div class="card">
//   <h1>{title()}</h1>
//   <button onClick={inc}>+</button>
//   <Show when={visible()} fallback={<p>hidden</p>}>content</Show>
// </div>

// —— 编译产物（简化） ——
const _tmpl$ = /*#__PURE__*/ template(`<div class="card"><h1></h1><button>+</button></div>`);

function App() {
  const [count, setCount] = createSignal(0);   // 组件只执行一次！
  const inc = () => setCount(count() + 1);

  const _el$ = _tmpl$(),                        // cloneNode 克隆模板
        _el$2 = _el$.firstChild,
        _el$3 = _el$2.firstChild,
        _el$4 = _el$.nextSibling;

  // 动态表达式 = getter 传给 helper，helper 内部建 effect
  insert(_el$2, () => title());                 // title 变化 -> 只改这个 h1 的文本
  _el$4.$$click = inc;                          // 事件直接绑定

  // 条件编译为专用组件：内部 effect 监听 when
  createComponent(Show, {
    get when() { return visible(); },           // getter：细粒度依赖
    get fallback() { return _el$5; },
    get children() { return 'content'; }
  });

  return _el$;
}

// —— insert 的实现（订阅发生地） ——
function insert(parent, value) {
  if (typeof value === 'function') {
    createEffect(() => {
      const v = value();                        // 读 signal -> 收集依赖
      // 精准操作：只替换这个位置的文本/节点，不碰兄弟、不碰组件
      replaceText(parent, v);
    });
  } else {
    replaceText(parent, value);
  }
}

// —— 对照：编译期与运行时的分工 ——
// Vue VDOM：编译期标注 patchFlag -> 运行时 diff dynamicChildren（还是有一轮比较）
// Solid   ：编译期直接生成订阅代码 -> 运行时零 diff（表达式即订阅）
// 共同点  ：都靠模板/JSX 的静态可分析性；差异在"标注"与"直译"的程度
```
