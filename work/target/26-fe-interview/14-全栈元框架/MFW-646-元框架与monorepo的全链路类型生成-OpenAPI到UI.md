---
title: [MFW-646] OpenAPI 到 UI 的类型生成管线
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-646：OpenAPI 到 UI 类型生成

**答**:
- OpenAPI codegen 的管线（外部 API 的类型补链 RBL-946）：1) **schema 源**（后端 OpenAPI spec——contract 单源）；2) codegen（openapi-typescript → 类型 + client（fetch wrapper 类型化）；3) 幂等校验（RBL-742：提交的类型 = 重新生成的——漂移检测 CI）；4) 类型集成（RSC 的 fetch 类型化——fetch wrapper 泛型化）。
- 生成管线的坑：1) **spec 与实现漂移**（后端代码改了 spec 没更新——spec 校验（实现与 spec 的契约测试——后端 CI）+ codegen 幂等双防线）；2) 生成体积（大 spec → 数万行类型——tsc 慢：按 tag 分域生成）；3) nullable 语义（OpenAPI nullable vs TS optional——codegen 的语义翻译陷阱）。
- 与 RSC 的集成：fetch wrapper（类型化 fetch——`api.get('/products/{id}', { params: { id: 1 } })` 返回类型自动推导）；「RSC 中类型化 fetch」= 推理链从外部 API 补全。
- 追问钩子：为什么「OpenAPI codegen 的幂等校验」在多团队协作中特别重要？——spec 是后端维护、类型是前端消费——「spec 改了类型没重新生成」= 前端类型过期（静默错：字段改名后运行时 undefined——类型还显示有）；幂等校验 = CI 对账（生成的 ≠ 提交的 → 红）；「跨团队的契约对账」的机械化：幂等校验把「沟通成本」变成「CI 成本」（后端改 spec → 前端 CI 红 → 自动 PR 提醒 regen）。

```typescript
// codegen 管线
// package.json scripts:
//   "codegen": "openapi-typescript ./openapi.json -o ./types/api.d.ts"
// CI 幂等校验（RBL-742）
// pnpm codegen && git diff --exit-code ./types/api.d.ts   ← 有 diff = 未提交最新生成
// 类型化 fetch wrapper
import { paths } from './types/api';
export async function apiFetch<P extends keyof paths>(
  path: P, init?: { params?: paths[P]['get']["parameters"]['path'] }
): Promise<paths[P]['get']['responses'][200]['content']['application/json']> {
  const url = fillPath(path as string, init?.params);
  return fetch(url).then(r => r.json());
}
// RSC 使用（类型直推）
const product = await apiFetch('/products/{id}', { params: { id: '42' } });
// product: paths['/products/{id}']['get']['responses'][200] —— 全自动
```
