---
title: [MFW-056] 笔试：手写一个 Server Action 购物车，带乐观更新与失败回滚
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-056：笔试：手写一个 Server Action 购物车，带乐观更新与失败回滚
**答**：实现「加入购物车」完整链路。要求：① 客户端点击后立即在 UI 上数量 +1（乐观更新）；② 调用 Server Action 落库；③ 服务端校验库存，失败时客户端回滚并提示；④ 提交中禁用按钮。

```tsx
// CartButton.tsx
'use client';
import { useOptimistic, useState, useTransition } from 'react';
import { addToCart } from './actions';

export function CartButton({ productId, initialCount }: { productId: string; initialCount: number }) {
  const [count, setCount] = useState(initialCount);
  const [pending, startTransition] = useTransition();

  // 乐观状态：onAction 先渲染乐观值，真实状态到达后覆盖
  const [optimisticCount, applyOptimistic] = useOptimistic(
    count,
    (cur, delta: number) => cur + delta,
  );

  function onClick() {
    startTransition(async () => {
      applyOptimistic(1); // 1. 先渲染 +1
      try {
        await addToCart(productId); // 2. 落库（失败会 throw）
        setCount((c) => c + 1);      // 3. 成功：把真实状态推进
      } catch (e) {
        alert(e instanceof Error ? e.message : '加购失败'); // 4. 失败：乐观值随 transition 结束自动消失
      }
    });
  }

  return (
    <button onClick={onClick} disabled={pending}>
      {pending ? `${optimisticCount} 件（同步中）` : `${count} 件 · 加购`}
    </button>
  );
}
```

```ts
// actions.ts
'use server';
export async function addToCart(productId: string) {
  const session = await auth();
  if (!session) throw new Error('请先登录');
  const p = await db.product.findUniqueOrThrow({ where: { id: productId } });
  if (p.stock <= 0) throw new Error('库存不足'); // 校验失败 -> 客户端回滚
  await db.$transaction([
    db.product.update({ where: { id: productId }, data: { stock: { decrement: 1 } } }),
    db.cartItem.upsert({
      where: { userId_productId: { userId: session.userId, productId } },
      update: { quantity: { increment: 1 } },
      create: { userId: session.userId, productId, quantity: 1 },
    }),
  ]);
}
```

**评分点**：
1. `useOptimistic` 的更新函数必须是纯函数，且乐观值只在 transition 生命周期内生效，能说清「失败自动消失」的机制。
2. 乐观更新与真实状态分离：成功后要把真实 state 推进，否则刷新前数字回跳。
3. 服务端有库存校验 + 事务（decrement 与 upsert 原子化），防超卖。
4. 按钮在 pending 期间禁用，防重复提交。
5. 能主动提到鉴权在 action 内做，不信任客户端。
