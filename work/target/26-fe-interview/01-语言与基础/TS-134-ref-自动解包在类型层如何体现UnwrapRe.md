---
title: [TS-134] ref 自动解包在类型层如何体现？UnwrapRef 有哪些坑？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-134：ref 自动解包在类型层如何体现？UnwrapRef 有哪些坑？
**答**：
- reactive 包裹的对象会"深度解包"内部 ref，类型层对应 `UnwrapRef<T>`：`Ref<number>` 变成 `number`。
- 坑一：数组/Map/Set 内的 ref 不解包，类型与运行时都仍是 Ref。
- 坑二：UnwrapRef 递归展开类实例，破坏封装并曾引发循环类型爆栈，Vue 3.5 引入 UnwrapRefSimple（带内部惰性标记）修复。
- 想原样持有对象（不解包、不深度代理）用 shallowRef。

```typescript
import { reactive, ref, shallowRef } from "vue";

class Counter {
  count = 0;
  inc() { this.count++; }
}
const counterRef = ref(new Counter());
const state = reactive({ counter: counterRef, n: ref(1) });

state.counter.count; // 类型是 number：UnwrapRef 把 Ref<Counter> 解包成 Counter
state.n;             // 类型是 number，不是 Ref<number>

// 坑一：数组内不解包
const list = reactive([ref(1)]);
list[0]; // 仍是 Ref<number>，需要 list[0].value

// 坑二：UnwrapRef 对类实例深度递归展开，Vue 3.5 起 reactivity 内部改用
// UnwrapRefSimple 规避循环引用导致的编辑器卡死/类型爆栈

// 解法：shallowRef 不解包也不深度代理
const raw = shallowRef(new Counter());
raw.value.inc(); // Counter 原样持有
```
