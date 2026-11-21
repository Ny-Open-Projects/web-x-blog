---
title: [TS-040] Partial 在业务中的典型应用场景是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-040：Partial 在业务中的典型应用场景是什么？
**答**：
- 最典型是"更新函数"：`update(id, patch: Partial<User>)` 只传要改的字段。
- 与表单草稿、配置合并、默认值覆盖等场景天然契合。
- 配合 Required 可以做"部分转完整"的中间态建模。
- 深层对象用 DeepPartial（见 TS-059）。

```typescript
interface User {
  id: number;
  name: string;
  age: number;
  email: string;
}

declare const users: Map<number, User>;

function updateUser(id: number, patch: Partial<User>): User {
  const user = users.get(id)!;
  const updated = { ...user, ...patch };
  users.set(id, updated);
  return updated;
}

updateUser(1, { name: "新名字" }); // 只传需要修改的字段
updateUser(1, { age: 20, email: "new@example.com" });

// 默认值合并也是 Partial 的常见用法
function createConnection(options: Partial<{ host: string; port: number }> = {}) {
  const config = { host: "localhost", port: 6379, ...options };
  return config;
}
```
