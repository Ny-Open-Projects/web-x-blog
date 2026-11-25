---
title: [WCN-847] 笔试：手写类型安全的 createSignal / computed / effect（TS 类型体操）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-847：笔试：手写类型安全的 createSignal / computed / effect（TS 类型体操）

**题目**：用 TypeScript 实现类型安全的迷你 signal 系统。要求：① `createSignal<T>(initial: T): [() => T, (v: T) => void]`，读写类型一致；② `computed<T>(fn: () => T): () => T`，返回类型从 fn 自动推导，返回只读 getter（不能 set）；③ `effect(fn: () => void | (() => void)): () => void`，允许返回清理函数，返回停止函数；④ `untrack<T>(fn: () => T): T` 保持类型；⑤ 提供 `ReadonlySignal<T>` 与 `Signal<T>` 两个接口，且 `Signal<T>` 不可直接赋给需要「可写」以外语义时类型安全。边界：`createSignal<number>(0)` 不能 set 字符串；computed 的结果类型必须精确推导而非 unknown。给出能被 tsc 通过的实现与「应报错的反例注释」。

**答**：

```typescript
type Cleanup = () => void;
type Equals = (a: unknown, b: unknown) => boolean;

interface ReadonlySignal<T> { (): T }
interface Signal<T> extends ReadonlySignal<T> { set(value: T): void }

let CURRENT: Set<() => void> | null = null;

function createSignal<T>(initial: T, equals: Equals = Object.is): Signal<T> {
  let value = initial;
  const subs = new Set<() => void>();
  const read = (() => {
    if (CURRENT) subs.add(CURRENT);
    return value;
  }) as Signal<T>;
  read.set = (v: T) => { if (equals(value, v)) return; value = v; [...subs].forEach(f => f()); };
  return read;
}
function computed<T>(fn: () => T): ReadonlySignal<T> {
  const out = createSignal(fn());
  effect(() => { out.set(fn()); });               // 依赖变化时重算
  return out;                                     // 返回 Signal<T>，但对外当只读用
}
function effect(fn: () => void | Cleanup): Cleanup {
  let cleanup: void | Cleanup;
  const run = () => { cleanup?.(); CURRENT = new Set(); cleanup = fn(); CURRENT = null; };
  run();
  return () => { cleanup?.(); };
}
function untrack<T>(fn: () => T): T { const c = CURRENT; CURRENT = null; const r = fn(); CURRENT = c; return r; }

const count = createSignal(0);
const doubled = computed(() => count() * 2);       // ReadonlySignal<number>
// count.set('x'); // ❌ tsc 报错：string 不能赋给 number
// doubled.set(5); // 若按只读接口约束应报错（返回类型声明为 ReadonlySignal）
effect(() => console.log('值:', doubled()));
count.set(3);
```

**评分点**：
- 泛型 T 在读写两端一致，`createSignal<number>` 拒绝字符串（类型安全核心）。
- computed 返回类型由 fn 自动推导（不退化成 unknown），且对外暴露只读语义。
- effect 支持 `void | Cleanup` 返回类型并正确调用清理（类型 + 运行时一致）。
- untrack 是泛型透传，不丢失类型（类型体操细节）。
