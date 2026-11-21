---
title: [FRP-101] Svelte 的编译产物与运行时框架有何不同？"编译时框架"如何做响应式？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-101：Svelte 的编译产物与运行时框架有何不同？"编译时框架"如何做响应式？

**答**：
- Svelte 在**编译期**把组件编译成无框架运行时的 JS：模板里每个可能变化的表达式被分析后生成 `$$invalidate` 调用——变量赋值语句（`count = 1`）被编译为"赋值 + 标脏 + 调度更新"。
- 响应式靠**编译期静态分析**：`let count` 被标记为响应式变量（因为被模板引用），所有对它的赋值点自动插入更新代码；Svelte 5 引入 runes（`$state/$derived/$effect`）后与 Solid 的 signals 模型趋同。
- 产物形态：组件是 `create_fragment(ctx)`，内含 `create/mount/update/destroy` 四段纯 DOM 操作函数，update 里就是精确的 `p.textContent = ctx.count` 这样的语句。
- 与 Solid 的差别：Solid 运行时保留 signal 订阅（动态依赖图）；Svelte 4 的依赖在**编译期写死**（无运行时依赖收集），产物更"扁平"，但动态性受限（Svelte 5 补上了运行时 signal）。

```javascript
// 简化实验，帮助理解 Svelte 风格的编译产物
// 源码（Svelte）：
// <script>let count = 0; const inc = () => count = count + 1;</script>
// <button on:click={inc}>{count}</button>

// 编译产物（简化）：
function create_fragment(ctx) {
  let button, t, mounted;
  return {
    create() {
      button = document.createElement('button');       // 直接建 DOM，无 vnode
      t = document.createTextNode('0');
      button.appendChild(t);
    },
    mount(target) {
      target.appendChild(button);
      mounted = true;
      button.addEventListener('click', ctx.inc);       // 事件绑定编译期生成
    },
    // update：只包含编译期分析出的"会变的表达式"
    p(newCtx) {
      if (newCtx.count !== ctx.count) t.data = newCtx.count; // 精确到节点/字段的更新语句
      ctx = newCtx;
    },
    destroy() { button.remove(); },
  };
}

function SvelteCompiledComponent() {
  const ctx = { count: 0 };
  const inc = () => { ctx.count = ctx.count + 1; $$invalidate(); }; // 赋值被改写
  const fragment = create_fragment(ctx);
  const updater = () => fragment.p({ count: ctx.count });
  function $$invalidate() { updater(); }               // 编译器插入的标脏+调度
  void inc;
  return fragment;
}

const frag = SvelteCompiledComponent();
frag.create(); frag.mount(document.body);
console.log('运行时框架运行期需要携带的代码量：vnode/diff/scheduler');
console.log('Svelte 产物：create/mount/p/destroy 四段纯 DOM 语句，无 diff 引擎');
```
