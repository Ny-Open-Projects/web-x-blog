---
title: [MFW-053] Server Action 的安全边界是什么，为什么不能信任客户端传参？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-053：Server Action 的安全边界是什么，为什么不能信任客户端传参？
**答**：
- Server Action 本质是**暴露在公网的 POST RPC 端点**，任何人拿到 action id 都能直接 curl 调用，权限校验必须在 action 函数体内做，靠「页面上没有按钮」保护不了任何东西。
- 参数校验要在服务端重做一遍（zod 等校验 schema），价格、库存、角色这类关键数据一律以服务端数据为准，绝不信客户端传来的金额。
- 返回给客户端的值会进 RSC Payload，用 `experimental_taintObjectReference` 标记敏感对象可从框架层阻断误传。
- 竞态与幂等：网络重试会导致 action 重复执行，写操作要幂等（如带 requestId 去重）。

```ts
'use server';
import { z } from 'zod';

const OrderSchema = z.object({
  productId: z.string().min(1),
  quantity: z.number().int().min(1).max(99),
  requestId: z.string().uuid(), // 幂等键
});

export async function createOrder(formData: FormData) {
  // 1. 鉴权：Action 是公网端点，第一步永远是身份校验
  const session = await auth();
  if (!session) throw new Error('UNAUTHORIZED');

  // 2. 服务端校验，金额/单价绝不来自客户端
  const input = OrderSchema.parse({
    productId: formData.get('productId'),
    quantity: Number(formData.get('quantity')),
    requestId: formData.get('requestId'),
  });
  const product = await db.product.findUniqueOrThrow({
    where: { id: input.productId },
  });

  // 3. 幂等：同一 requestId 只落一次库
  return db.$transaction(async (tx) => {
    await tx.idempotencyKey.create({ data: { key: input.requestId } });
    return tx.order.create({
      data: {
        userId: session.userId,
        productId: input.productId,
        amount: product.price * input.quantity, // 服务端定价
      },
    });
  });
}
```
