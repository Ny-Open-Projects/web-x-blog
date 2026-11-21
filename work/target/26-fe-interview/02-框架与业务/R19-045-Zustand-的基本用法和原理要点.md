---
title: [R19-045] Zustand 的基本用法和原理要点？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-045：Zustand 的基本用法和原理要点？
**答**：
- create 创建一个全局 Hook，组件通过选择器订阅 store 的切片，只有选中的切片变化才重渲染。
- 无 Provider 包裹，天然规避 Context 全量更新的问题；selector 用引用相等比较。
- 原理核心是 store 里的 listeners 集合 + useSyncExternalStore 订阅外部 store。
- 内置中间件：persist 持久化、devtools 调试、immer 不可变更新。

```jsx
import { create } from 'zustand';

const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}));

function Counter() {
  // 只订阅 count 切片，reset 等无关更新不会引起本组件渲染
  const count = useCounterStore((s) => s.count);
  const increment = useCounterStore((s) => s.increment);

  return (
    <>
      <p>{count}</p>
      <button onClick={increment}>加一</button>
    </>
  );
}
```
