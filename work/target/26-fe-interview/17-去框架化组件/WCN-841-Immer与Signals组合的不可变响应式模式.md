---
title: [WCN-841] Immer + Signals 组合的「不可变响应式」模式怎么做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-841：Immer + Signals 组合的「不可变响应式」模式怎么做？

**答**：
- 结论先行：Signals 默认「可变 + 细粒度」，但有时需要「不可变语义」（时间旅行、与 React 生态集成、结构共享）——Immer 用 `produce` 让你以「mutable 写法」生成不可变新对象，再写入 signal，兼顾 DX 与不可变收益。
- 组合方式：`const state = signal(initial); update(recipe) { state.value = produce(state.value, recipe); }`——Immer 只克隆被修改的路径（结构共享），未变部分引用不变，配合 signal 的相等性检查可跳过无关更新。
- 为什么有用：① 时间旅行/撤销——每次 produce 产生一个新快照可直接存历史；② React 生态——不可变值便于 `useSyncExternalStore` 与 memo 比较；③ 避免「原地改对象但 signal 引用没变导致不更新」的坑。
- 注意点：Immer 生成的 draft 不能逃逸出 recipe（不要在 recipe 里异步保存 draft）；大对象每次 produce 仍有结构共享开销；与深层 signal（deep-signal）是两种不同路线，别混用。
- 追问钩子：面试官会问「Immer 和 deep-signal 选哪个」——答：要不可变语义/时间旅行选 Immer；要字段级细粒度订阅、避免整对象替换选 deep-signal；按需求取舍。

```javascript
import { signal } from '@preact/signals-core';
import { produce } from 'immer';

const state = signal({ user: { name: 'A' }, todos: [{ id: 1, done: false }] });
// 用 Immer 的 mutable 写法生成不可变新对象
function update(recipe) {
  const next = produce(state.value, recipe);
  if (next !== state.value) state.value = next; // 引用变了才触发更新
}
update(d => { d.user.name = 'B'; });             // 只克隆 user 路径
update(d => { d.todos[0].done = true; });         // 只克隆 todos 路径
console.log(state.value.user.name);              // B
// 快照历史：每次 update 的 state.value 都是不可变快照，可直接存
```
