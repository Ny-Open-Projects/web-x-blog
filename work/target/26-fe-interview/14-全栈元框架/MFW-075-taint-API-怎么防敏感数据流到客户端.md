---
title: [MFW-075] React 的 taint API 怎么防止敏感数据被传到客户端？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-075：React 的 taint API 怎么防止敏感数据被传到客户端？
**答**：
- RSC 边界有个隐含风险：任何对象只要能被序列化就能作为 props 传给 Client Component，密码哈希、token 这类字段可能「顺带」漏过去。taint API 把这类对象在框架层标记为**不可跨边界**，传了直接在构建/渲染期报错。
- 两个 API：`taintObjectReference` 污染单个对象引用；`taintUniqueValue` 按值污染（如按 token 字符串本身，防止换壳传递）。
- 放置位置：在数据访问层（如 db 封装、auth 返回处）统一污染，让所有下游自动受保护，而不是每个页面手动防。
- 它是兜底不是替代：最小化数据面（select 精确列）仍是第一道防线。

```ts
// lib/auth.ts
import { taintUniqueValue, taintObjectReference } from 'react';
import type { Session } from './types';

export async function getSession(): Promise<Session> {
  const session = await verifySession(); // { userId, token, email, ... }

  // 1) token 按值污染：无论包在什么新对象里，试图传给客户端都会报错
  taintUniqueValue('不要把 session token 传给客户端组件', session, session.token);

  // 2) 整个内部用户对象按引用污染（示例）
  // taintObjectReference('不要把内部用户对象传给客户端', session.internalUser);

  return session;
}
```

```ts
// lib/data/db.ts —— 数据层统一防线
export async function getUser(id: string) {
  const user = await db.user.findUniqueOrThrow({ where: { id } });
  taintObjectReference('用户敏感对象不可进客户端', user); // 污染整个查询结果
  return user;
}
// page 里 user 仍可在服务端渲染用；一旦 user 被作为 props 传给 'use client' 组件，
// 框架直接抛错，而不是等上线后从 RSC payload 里被人扒出来。
```
