---
title: [TS-042] keyof 操作符的作用是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-042：keyof 操作符的作用是什么？
**答**：
- `keyof T` 取类型 T 的所有 key 组成的字面量联合类型。
- 对接口取属性名联合，对数字枚举类型特殊：`keyof typeof Enum` 才是成员名联合。
- 与泛型约束 `K extends keyof T` 组合是类型安全取值的标准套路。
- keyof 也是 Pick、Omit、映射类型的基石。

```typescript
interface User {
  id: number;
  name: string;
}

type UserKeys = keyof User; // "id" | "name"

const SortKey = { id: "id", name: "name" } as const;
type SortKey = keyof typeof SortKey; // "id" | "name"

// keyof + 泛型：安全的 setter
function setProp<T, K extends keyof T>(obj: T, key: K, value: T[K]) {
  obj[key] = value;
}

const user: User = { id: 1, name: "Tom" };
setProp(user, "name", "Jerry"); // value 必须是 string
// setProp(user, "name", 123); // 报错
```
