---
title: [MFW-174] 登录态怎么贯穿 Middleware、RSC、Server Action 三层？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-174：登录态怎么贯穿 Middleware、RSC、Server Action 三层？
**答**：
- Middleware 层：只做「路由级粗判」——校验 session cookie 是否存在/过期，未登录重定向到登录页；不查数据库（Middleware 运行环境受限且每请求必走，要快）。
- RSC 层：`await cookies()` 读 session token，服务端换取用户信息后做数据级鉴权，未授权返回 error 或渲染受限 UI；读 cookie 会让段变动态，登录后的页面默认就是动态渲染，符合预期。
- Server Action 层：**绝不信任客户端传来的 userId**，每次 Action 内重新从 cookie 鉴权；写操作再加业务级权限校验（是不是资源 owner）。
- 三层共用同一个 session 解析函数，通过 `cache()` 做请求级记忆化，避免一个请求解析多次 session。
- 登出/换绑后要立刻失效旧 token：服务端 session 表 + cookie 双删，并让依赖登录态的缓存 tag 联动失效。

```javascript
import { cache } from 'react';
import { cookies } from 'next/headers';

export const getSession = cache(async () => { // 请求级记忆化：三层共用只解析一次
  const token = (await cookies()).get('session')?.value;
  return token ? await verifySession(token) : null; // 查服务端 session 表
});

export async function deleteOrder(orderId) { // Server Action 内再次鉴权
  'use server';
  const session = await getSession();
  if (!session) throw new Error('UNAUTHORIZED');
  const order = await db.orders.find(orderId);
  if (order.userId !== session.userId) throw new Error('FORBIDDEN'); // 业务级校验
  await db.orders.remove(orderId);
}
```
