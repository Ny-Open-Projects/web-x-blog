---
title: [FRP-048] 编译时优化与运行时优化有何区别？Svelte 是怎么做的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-048：编译时优化与运行时优化有何区别？Svelte 是怎么做的？

**答**：
- 运行时框架（React/Vue）：产物包含框架本体，运行时做依赖收集/diff/调度；优点灵活（JSX/动态模板），代价是运行时开销 + 框架体积。
- 编译时框架（Svelte）：编译器分析组件，把响应式声明**编译成直接读写 DOM 的命令式代码**，没有 diff、没有虚拟 DOM、几乎零运行时；代价是模板受限于编译期能分析的形式（动态性差）、组件多时输出代码量增长。
- Vue3 是折中：保留运行时 diff，但编译期用 patchFlag/静态提升把 diff 范围压到"仅动态部分"——运行时与编译时协同。
- 趋势：React 19 的 React Compiler（自动 memo 化）、Vue Vapor 模式（无虚拟 DOM）都在向"编译期多干活"靠拢。

```html
<!-- 一一对应：Svelte 组件源码（模板语法与 HTML 同构），编译产物思路见下一段 -->
<!-- Svelte 组件源码 -->
<script>
  let count = 0;
</script>

<button on:click={() => count++}>
  {count}
</button>
```

```javascript
// —— Svelte 编译产物（近似还原）：没有 vnode，没有 diff ——
// 简化实现，帮助理解编译时框架的产物形态
function Button(root) {
  // 直接拿到 DOM 引用
  const button = root.appendChild(document.createElement('button'));
  const text = button.appendChild(document.createTextNode(''));

  button.addEventListener('click', () => {
    count++;          // 只改变量
    $$invalidate();   // 生成的更新函数：直接改 text.data
  });

  function $$invalidate() {
    text.data = count; // 直接操作 DOM，跳过 diff —— 这就是编译时优化
  }

  $$invalidate();
  return { destroy() { button.remove(); } };
}

// 对比 React 同样功能的运行时开销：
//   JSX 创建 vnode 树 -> reconcile diff -> commit 操作 DOM
// Svelte：事件回调里一行 text.data = count
// 结论：编译器在构建期"烧录"了更新路径，运行时不再推导
```
