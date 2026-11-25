---
title: [TS-010] unknown 与 any 的区别是什么？unknown 如何安全使用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-010：unknown 与 any 的区别是什么？unknown 如何安全使用？
**答**：
- `unknown` 可以接收任何值（与 any 相同），但使用前必须先收窄或断言。
- unknown 不能直接访问属性、不能直接调用，只能赋值给 `unknown` 或 `any`。
- 适合用在不可信数据的入口：JSON.parse 结果、第三方回调参数、catch 的 error。
- typeof、instanceof、in、自定义守卫等收窄手段对 unknown 全部适用。

```typescript
function safeParse(json: string): unknown {
  try {
    return JSON.parse(json);
  } catch {
    return undefined;
  }
}

const value = safeParse('{"name": "Tom"}');
// value.name; // 报错：unknown 不能直接访问属性
if (typeof value === "object" && value !== null && "name" in value) {
  console.log((value as { name: string }).name); // 收窄 + 断言后可用
}
```
