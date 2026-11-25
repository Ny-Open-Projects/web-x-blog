---
title: [TS-176] 如何用模板字面量从 API 路径生成请求方法映射？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-176：如何用模板字面量从 API 路径生成请求方法映射？
**答**：
- 链路：路径去掉冒号 → 按 "/" 切段 → 各段 Pascal 化拼接 → 映射类型 as 重映射成 `fetchXxx` 方法名。
- 中间类型（Split/Pascal）写在小工具类型里，as 子句里内联组合。
- 场景：纯静态的 API 客户端生成、按路径补全方法名。

```typescript
type ApiPaths = "/users" | "/users/:id" | "/users/:id/posts";

type Split<S extends string> = S extends `${infer A}/${infer B}`
  ? A extends "" ? Split<B> : [A, ...Split<B>]
  : [S];

type Pascal<T extends string[]> = T extends [infer F extends string, ...infer R extends string[]]
  ? `${Capitalize<F extends `:${infer W}` ? W : F>}${Pascal<R>}`
  : "";

type Api = {
  [P in ApiPaths as `fetch${Pascal<Split<P>>}`]: (
    params: Record<string, string>,
  ) => Promise<unknown>;
};

type ApiName = keyof Api; // "fetchUsers" | "fetchUsersId" | "fetchUsersIdPosts"
// fetchUsersId({ id: "1" }) —— 方法名由路径自动生成，编辑器直接补全
```
