---
title: [TS-196] 如何实现类型安全的 ORM select（字段 → 返回行）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-196：如何实现类型安全的 ORM select（字段 → 返回行）？
**答**：
- fields 是表字段元组，返回行类型映射 `K[number]`，没选的列不出现在结果类型上。
- 泛型约束 `K extends readonly (keyof T)[]` 同时完成字段名补全与错字拦截。
- 进阶方向：保持元组顺序的返回行、where 列约束联动、update 仅允许已选键。

```typescript
interface UserTable {
  id: number;
  name: string;
  email: string;
  passwordHash: string;
}

type SelectedRow<T, K extends readonly (keyof T)[]> = {
  [F in K[number]]: T[F];
};

declare function select<T, K extends readonly (keyof T)[]>(
  table: string,
  fields: K,
): SelectedRow<T, K>[];

const rows = select<UserTable>("user", ["id", "name"]);
rows[0].id;    // number
rows[0].name;  // string
// rows[0].email;                 // 报错：没选的列不在结果类型上
// select("user", ["id", "nope"]); // 报错：nope 不是 UserTable 字段
// select("user", []);            // 空选集类型为 {}，可加 K["length"] extends 0 拦截
```
