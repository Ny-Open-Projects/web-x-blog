---
title: [TS-121] API 返回类型如何从 OpenAPI 自动生成？工程链路是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-121：API 返回类型如何从 OpenAPI 自动生成？工程链路是什么？
**答**：
- 链路：后端产出 OpenAPI 文档（yaml/json）→ `openapi-typescript` 等工具生成 `.d.ts` → 前端按 `paths[...].get.responses["200"]` 索引访问取响应类型。
- 配合生成的 `paths` 类型封装一个强类型 fetch 客户端，URL 与参数、响应全链路类型安全。
- 契约变更时重新跑 codegen，前端编译期立即暴露破坏性改动，CI 中可将其设为门禁。

```json
{
  "scripts": {
    "gen:api": "openapi-typescript https://internal.example/openapi.json -o src/types/api.d.ts"
  }
}
```

```typescript
// 生成文件中的类型形如（节选自 src/types/api.d.ts）
// export interface paths {
//   "/api/users/{id}": {
//     get: {
//       parameters: { path: { id: number } };
//       responses: { 200: { content: { "application/json": { id: number; name: string } } } };
//     };
//   };
// }

import { paths } from "./types/api";

type ResponseOf<P extends keyof paths, M extends keyof paths[P]> =
  paths[P][M] extends { responses: { 200: { content: { "application/json": infer R } } } }
    ? R
    : never;

type User = ResponseOf<"/api/users/{id}", "get">; // { id: number; name: string }

async function apiGet<P extends keyof paths, M extends "get">(
  path: P,
  init?: RequestInit
): Promise<ResponseOf<P, M>> {
  const res = await fetch(path as string, init);
  return res.json();
}

const u = await apiGet("/api/users/{id}"); // 自动推导 User
```
