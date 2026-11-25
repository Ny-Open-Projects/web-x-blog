---
title: [TS-117] 如何让 API 路径字符串自动推导查询参数类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-117：如何让 API 路径字符串自动推导查询参数类型？
**答**：
- 模板字面量匹配 `?` 之后的查询串，`k=v&` 循环递归解析出每个键。
- 每个键映射为 string 组成参数对象，与 TS-060 的路径参数思路同源但解析目标是 query。
- 把 `QueryOf` 与 `RouteParams` 叠加，就能得到"一个 URL 字符串推导全部请求参数"的完整方案。

```typescript
type QueryToObj<Q extends string> =
  Q extends `${infer K}=${string}&${infer Rest}`
    ? { [P in K]: string } & QueryToObj<Rest>
    : Q extends `${infer K}=${string}`
      ? { [P in K]: string }
      : unknown;

type QueryOf<S extends string> =
  S extends `${string}?${infer Q}` ? QueryToObj<Q> : unknown;

type Q1 = QueryOf<"/api/users?page=1&size=20">;
// { page: string } & { size: string }

declare function fetchApi<S extends string>(url: S, query: QueryOf<S>): void;

fetchApi("/api/users?page=1&size=20", { page: "1", size: "20" }); // OK
// fetchApi("/api/users?page=1&size=20", { page: "1" });          // 报错：缺少 size
// fetchApi("/api/users?page=1", { page: 1 });                    // 报错：必须是 string
```
