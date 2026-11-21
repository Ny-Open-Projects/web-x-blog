---
title: [TS-170] Pinia/Zustand/Redux 的 action 类型安全有哪三种实现？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-170：Pinia/Zustand/Redux 的 action 类型安全有哪三种实现？
**答**：
- 实现一：可辨识联合 action（Redux 经典），switch 穷尽检查。
- 实现二：泛型 action creator 工厂，action 类型从构造器自动反推，联合自动汇聚。
- 实现三：Zustand/Pinia 式"方法即 action"，state 与方法同源定义，零手写 action 联合。

```typescript
// 实现一：可辨识联合（Redux）
type CounterAction =
  | { type: "increment"; step: number }
  | { type: "reset" };
const reduce = (s: number, a: CounterAction) =>
  a.type === "increment" ? s + a.step : 0;

// 实现二：泛型 action creator，类型与构造器同源
const makeCreator = <K extends string, P extends object>(type: K) =>
  (payload: P) => ({ type, ...payload } as const);
const inc = makeCreator<"increment", { step: number }>("increment");
const actions = { inc } as const;
type AllActions = ReturnType<(typeof actions)[keyof typeof actions]>; // 自动汇聚联合

// 实现三：Zustand 式 store（Pinia 同思想）
import { create } from "zustand";
const useStore = create<{
  count: number;
  increment: (step: number) => void;
}>()((set) => ({
  count: 0,
  increment: (step) => set((s) => ({ count: s.count + step })),
}));
useStore.getState().increment(2); // 调用与类型全联动，无 action 联合要维护
```
