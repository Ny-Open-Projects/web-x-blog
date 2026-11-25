---
title: [WCN-832] Signals 的 TypeScript 类型体操：如何设计类型安全的 computed / effect？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-832：Signals 的 TypeScript 类型体操：如何设计类型安全的 computed / effect？

**答**：
- 结论先行：Signal 的 TS 设计目标是「读出来是什么类型、写进去也约束成什么类型，派生链类型不丢失」——核心是泛型 `Signal<T>` + `computed` 用返回类型推导 + 只读信号类型分离。
- 基础类型：`interface Signal<T> { (): T; (v: T): void; value: T }`（函数重载形式）或 `get()/set(v)` 形式；关键是 `T` 在读写两端保持一致。
- 只读派生：`computed<T>(fn: () => T): ReadonlySignal<T>`——返回类型去掉 `set`，从类型层面禁止对派生值写入（防止破坏单向数据流）。
- 类型体操要点：`untrack<T>(fn: () => T): T` 保持类型；`batch` 是泛型透传；`effect(fn: () => void | Cleanup)` 允许返回清理函数；`selector` 订阅用 `K extends keyof T` 约束键。
- 进阶：条件类型/映射类型生成「把对象每个字段变成 signal」的 `DeepSignal<T>`，用于深层响应式场景，但要注意递归深度与 TS 编译性能。
- 追问钩子：面试官会问「computed 的 T 怎么推导」——答：靠函数返回类型 `() => T` 让 TS 自动推导，无需手写；复杂场景可用 `ReturnType<typeof fn>` 显式标注。

```typescript
type Cleanup = () => void;
interface ReadonlySignal<T> { get(): T }
interface Signal<T> extends ReadonlySignal<T> { set(v: T): void; value: T }

declare function signal<T>(initial: T): Signal<T>;
declare function computed<T>(fn: () => T): ReadonlySignal<T>;
declare function effect(fn: () => void | Cleanup): () => void;
declare function untrack<T>(fn: () => T): T;

const count = signal(0);          // Signal<number>
const label = signal('hi');       // Signal<string>
const doubled = computed(() => count.get() * 2); // ReadonlySignal<number>
// doubled.set(5); // ❌ 编译错误：派生信号只读

const stop = effect(() => {
  console.log(doubled.get(), label.get());
  return () => console.log('cleanup'); // 类型允许 void | Cleanup
});
// count.set('x'); // ❌ 编译错误：类型不匹配
count.set(3); stop();
```
