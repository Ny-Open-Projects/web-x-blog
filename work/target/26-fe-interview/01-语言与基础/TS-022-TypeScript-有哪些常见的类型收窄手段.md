---
title: [TS-022] TypeScript 有哪些常见的类型收窄手段？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-022：TypeScript 有哪些常见的类型收窄手段？
**答**：
- `typeof`：收窄原始类型，注意 typeof null 是 "object" 需要额外排除。
- `instanceof`：收窄类实例；`in`：收窄属性存在性，适合对象联合。
- 真值判断、相等/不等判断（配合字面量类型）、数组 includes 也能收窄。
- 收窄只在当前控制流分支内有效，不改变原声明类型。

```typescript
function describe(input: string | number | Date | null) {
  if (input === null) return "空值"; // 相等判断收窄
  if (typeof input === "string") return input.toUpperCase(); // typeof 收窄
  if (typeof input === "number") return input.toFixed(2);
  if (input instanceof Date) return input.toISOString(); // instanceof 收窄
  return "未知";
}

function hasName(obj: { name?: string } | { id: number }) {
  if ("name" in obj) return obj.name; // in 收窄
  return `id=${obj.id}`;
}
```
