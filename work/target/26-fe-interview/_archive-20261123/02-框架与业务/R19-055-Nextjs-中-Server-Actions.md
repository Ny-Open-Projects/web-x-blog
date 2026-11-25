---
title: [R19-055] Next.js 中 Server Actions 怎么写？如何刷新数据？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-055：Next.js 中 Server Actions 怎么写？如何刷新数据？
**答**：
- `'use server'` 文件或函数内定义 Server Action，客户端可以直接 import 并调用，像 RPC 一样。
- Server Action 在服务端执行，天然安全地访问数据库与密钥，请求体自动序列化。
- 数据更新后调用 revalidatePath 或 revalidateTag 让 Next 的缓存失效，页面重新渲染。
- 通常与 useActionState、redirect 组合完成表单闭环。

```jsx
// app/actions.js
'use server';

import { revalidatePath } from 'next/cache';
import { db } from '@/lib/db';

export async function deletePost(id) {
  await db.post.delete({ where: { id } });
  revalidatePath('/posts'); // 让 /posts 的缓存失效并重渲染
}
```
