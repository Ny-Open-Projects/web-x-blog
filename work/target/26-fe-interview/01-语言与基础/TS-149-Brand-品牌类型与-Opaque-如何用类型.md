---
title: [TS-149] Brand 品牌类型与 Opaque 如何用类型防混用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-149：Brand 品牌类型与 Opaque 如何用类型防混用？
**答**：
- Brand：`T & { __brand: B }` 制造名义类型，UserId 与 OrderId 都是 number 但互不相容，裸 number 也无法直接通过。
- Opaque 演进：品牌字段换成 unique symbol 键，不可见更难伪造；type-fest 的 Tagged 是官方化实现。
- 成本收益：只在"跨模块流转的标识符"上用（用户 id、订单号、jwt），局部 id 不值得。

```typescript
// Brand 品牌类型
type Brand<T, B extends string> = T & { readonly __brand: B };
type UserId = Brand<number, "UserId">;
type OrderId = Brand<number, "OrderId">;

declare function loadUser(id: UserId): { id: UserId; name: string };
declare function loadOrder(id: OrderId): unknown;

const uid = 1 as UserId;   // 受控铸造点：尽量收敛到专门函数如 makeUserId(n)
const oid = 2 as OrderId;
loadUser(uid);      // OK
// loadUser(oid);   // 报错：OrderId 不是 UserId
// loadUser(1);     // 报错：裸 number 无法通过

// Opaque 演进：unique symbol 键不可见
declare const opaqueBrand: unique symbol;
type Opaque<T, Token> = T & { readonly [opaqueBrand]: Token };
type Jwt = Opaque<string, "Jwt">;
declare const makeJwt: (raw: string) => Jwt; // 只能经构造函数产生，杜绝随手 as
```

## 第三十二章 高阶体操挑战（TS-150 ~ TS-157）
