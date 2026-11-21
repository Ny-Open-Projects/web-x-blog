---
title: [MFW-010] Server Actions 是什么？和 API Route（Route Handler）怎么选？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-010：Server Actions 是什么？和 API Route（Route Handler）怎么选？
**答**：
- Server Action 是**服务端异步函数**，加 `'use server'` 后可以直接被客户端组件 import 并像本地函数一样调用——框架自动生成 RPC 端点，无需手写 fetch/接口层。
- 与 API Route 的核心区别：API Route 是**资源端点**（有独立 URL，可供第三方/移动端调用，适合 GET 缓存语义）；Server Action 是**组件树内部的调用通道**（POST，永远不带缓存，面向 UI 变更）。
- 选型经验：**读数据、需要被外部消费 → Route Handler；写数据、表单提交、UI 触发的 mutation → Server Action**。
- Server Action 天然与 React 融合：配合 useActionState/useTransition 自动处理 pending、错误、revalidate。
- 注意边界：Action 里是可信服务端代码，但**输入永远不可信**（鉴权、参数校验、限流都要自己做，Action 不是防火墙）。

```ts
// app/actions.ts
'use server';
import { db } from '@/lib/db';
import { revalidatePath } from 'next/cache';

export async function createOrder(formData: FormData) {
  const sku = String(formData.get('sku'));  // 输入校验自己负责
  const order = await db.order.create({ data: { sku, qty: 1 } });
  revalidatePath('/orders');                // 写后刷新路由缓存
  return { id: order.id };
}
```

```jsx
// app/new-order.tsx（Client）
'use client';
import { useActionState } from 'react';
import { createOrder } from './actions';

export function NewOrderForm() {
  const [state, formAction, pending] = useActionState(
    async (prev, formData) => createOrder(formData),
    null,
  );
  // 像调本地函数一样使用服务端函数，自动 POST 到框架生成的端点
  return (
    <form action={formAction}>
      <input name="sku" placeholder="SKU" required />
      <button disabled={pending}>{pending ? '提交中…' : '创建订单'}</button>
      {state?.id && <p>订单号 {state.id}</p>}
    </form>
  );
}
```
