---
title: [WCN-085] Solid 的细粒度渲染原理是什么？为什么说"组件函数只运行一次"？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-085：Solid 的细粒度渲染原理是什么？为什么说"组件函数只运行一次"？

**答**：
- 编译期拆分：Solid 编译 JSX 时，把每个含响应式读取的表达式提取为独立的"作用域计算"（render effect），运行时每个表达式各自创建 effect，读取 signal 时自动追踪。
- 组件函数只在首次渲染执行一次，产出真实 DOM 与一批 effect；之后状态变化只运行受影响表达式的 effect，不存在"重跑组件"概念。
- 控制流也编译化：`<For>`/`<Show>` 编译为 keyed/非 keyed 的专用更新器，`For` 只对新增/删除项操作，同 key 项复用节点。
- 与 Svelte 的区别：Svelte 把响应性编译为 `invalidate` 赋值语句（依赖是编译期静态确定的），Solid 是运行时追踪（依赖动态）；Solid 更接近"运行时 signals + 编译期定位更新点"。
- 代价：组件只跑一次意味着不能把 props 解构后当快照用（解构即脱离追踪），需 `props.x` 访问保持响应；这是 Solid 最著名的坑。

```jsx
// Solid JSX → 编译产物（示意）
function Counter() {
  const [n, setN] = createSignal(0);      // 组件体只执行一次
  return <div>
    <span>{n()}</span>                     // 编译为: effect(() => span.textContent = n())
    <button onClick={() => setN(n() + 1)}>+1</button>
  </div>;
}
// setN 后只有第一个 effect 运行；组件函数不再执行
```
