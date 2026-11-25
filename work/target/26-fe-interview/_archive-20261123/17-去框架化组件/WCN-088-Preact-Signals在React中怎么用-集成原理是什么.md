---
title: [WCN-088] Preact Signals 在 React 中怎么用？@preact/signals-react 的集成原理是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-088：Preact Signals 在 React 中怎么用？@preact/signals-react 的集成原理是什么？

**答**：
- 用法：`signal` 创建状态，组件里直接读 `.value`；React 适配器在读取时把组件注册为订阅者，signal 变化自动触发组件重渲染（无需 useState/useSelector）。
- 原理：适配器包装 signal 的读取入口，在渲染期间记录"哪个组件读了哪个 signal"，变化时用 React 内部的调度（或 forceUpdate 语义）精准刷新读取者；依赖追踪复用 signals-core。
- 性能机制：渲染期间 React 会把 JSX 里的 signal 引用原样传给 DOM 层，适配器用"引用相等短路"——signal 未变的节点跳过 diff，实现子树级跳过更新。
- 与 Redux/Zustand 的位置：signals-react 可完全替代 selector 订阅（更细粒度），也可与 React Query 分层（服务器状态归 Query、客户端状态归 signals）。
- 限制：React 严格模式双调用、并发渲染下 effect 时序需要适配层处理；`effect()` 在 React 里要用 `useEffect` + 手动 dispose，或用 `useSignalEffect` 封装。

```jsx
import { signal, computed } from '@preact/signals-react';
import { useSignalEffect } from '@preact/signals-react';

const count = signal(0);
const double = computed(() => count.value * 2);

function Counter() {
  // 直接读 .value：signal 变化自动触发本组件重渲染（无 selector）
  return (
    <>
      <span>{double.value}</span>
      <button onClick={() => count.value++}>+1</button>
      <AutoSave />
    </>
  );
}
function AutoSave() {
  useSignalEffect(() => {          // 生命周期自动 dispose
    localStorage.setItem('count', String(count.value));
  });
  return null;
}
```
