---
title: [MFW-142] TanStack Start 的 server functions 是怎么工作的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-142：TanStack Start 的 server functions 是怎么工作的？
**答**：
- `createServerFn` 定义一个「服务端专属函数」：编译期把函数体抽到服务端 bundle，客户端生成同 id 的 RPC stub——客户端调用 = POST 到框架生成的端点，等价于 Next 的 Server Actions（Server Actions 是 'use server' 指令，Start 是显式工厂函数）。
- 组成：`validator`（入参 zod 校验，两端共享类型）+ `handler`（服务端逻辑，可访问请求头/cookies）+ 链式 `.client()`（客户端前置逻辑如乐观 UI）。
- 类型流：`fn({ data })` 的入参类型来自 validator，返回类型直接推导——「调用处像本地函数，实际走网络」的全类型 RPC。
- 与 loader 的关系：loader 在服务端可直接调用 server function（进程内），客户端组件也能直接调——一个原语覆盖取数与 mutation。

```ts
// server/products.ts
import { createServerFn } from '@tanstack/react-start';
import { z } from 'zod';

export const createProduct = createServerFn({ method: 'POST' })
  .validator((input: unknown) =>
    z.object({
      name: z.string().min(1),
      price: z.number().positive(),
    }).parse(input),
  )
  .handler(async ({ data }) => {
    // 只在服务端执行：可访问 DB 与密钥
    const session = await getSession(); // 请求上下文注入
    if (!session) throw new Error('UNAUTHORIZED');
    return db.product.create({ data: { ...data, ownerId: session.userId } });
  });

// 客户端组件：像本地函数一样调用，类型完全贯通
import { createProduct } from '../server/products';

function NewProductForm() {
  return (
    <button
      onClick={() => {
        const { data, error } = await createProduct({ data: { name: '键盘', price: 199 } });
        // data 类型 = handler 返回值；error 结构化
      }}
    >创建</button>
  );
}
```
