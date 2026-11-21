---
title: [TS-031] 泛型约束 extends 如何使用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-031：泛型约束 extends 如何使用？
**答**：
- `T extends U` 限定 T 必须满足 U，从而在函数体内安全访问 U 的成员。
- 常用 `T extends keyof Obj` 约束 key 合法性，实现类型安全的取值函数。
- 约束也可以是对象形状、类、构造签名等。
- 约束越精确，函数体内可用的成员越多，推断越准确。

```typescript
interface Lengthwise {
  length: number;
}

function logLength<T extends Lengthwise>(value: T): T {
  console.log(value.length); // 有约束后可安全访问 length
  return value;
}

logLength("hello"); // OK
logLength([1, 2, 3]); // OK
// logLength(123); // 报错：number 没有 length

// keyof 约束：保证 key 一定是 obj 的属性
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: "Tom", age: 18 };
getProp(user, "name"); // string
// getProp(user, "email"); // 报错：不是合法 key
```
