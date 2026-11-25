---
title: [TS-005] void 和 undefined 有什么区别？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-005：void 和 undefined 有什么区别？
**答**：
- `void` 表示函数"没有有意义的返回值"，调用方不应使用其返回结果。
- `undefined` 是一个具体的值和类型；`void` 类型的变量只能被赋 `undefined`。
- 特殊规则：目标返回类型是 `void` 时，实现函数可以返回任意值（返回值被忽略），这是为回调写法服务的。
- 所以 `() => void` 并不能约束实现方"真的什么都不返回"。

```typescript
function log(): void {
  console.log("hi");
}

let v: void = undefined; // void 只能被赋 undefined
// v = 1; // 报错

// 回调场景：返回值类型为 void 时，实现可以返回任何值（会被忽略）
type Task = () => void;
const task: Task = () => 123; // 合法，返回值被丢弃
```
