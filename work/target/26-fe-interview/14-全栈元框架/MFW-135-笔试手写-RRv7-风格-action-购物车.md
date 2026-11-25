---
title: [MFW-135] 笔试：手写 RRv7 风格的 action + useFetcher 购物车操作
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-135：笔试：手写 RRv7 风格的 action + useFetcher 购物车操作
**答**：实现购物车页：① action 支持 add/remove/update-quantity 三种 intent；② 服务端校验数量与库存；③ 每行删除用 useFetcher（不触发页面导航）；④ 修改数量乐观更新；⑤ action 后 loader 数据自动刷新。

```tsx
// app/routes/cart.tsx
import { Form, useFetcher, useLoaderData, useNavigation, useOptimistic } from 'react-router';
import { startTransition } from 'react';

export async function loader() {
  return { items: await db.cart.items((await auth()).userId) };
}

export async function action({ request }: any) {
  const session = await auth();               // action 先鉴权
  if (!session) throw new Response('unauthorized', { status: 401 });

  const fd = await request.formData();
  const intent = String(fd.get('intent'));

  switch (intent) {
    case 'add': {
      const productId = String(fd.get('productId'));
      const qty = Math.min(Number(fd.get('qty') ?? 1), 99);
      const product = await db.product.findUniqueOrThrow({ where: { id: productId } });
      if (product.stock <= 0) return { ok: false, error: '库存不足' };
      await db.cart.add(session.userId, productId, qty);
      return { ok: true };
    }
    case 'update': {
      const itemId = String(fd.get('itemId'));
      const qty = Math.max(1, Math.min(Number(fd.get('qty')), 99)); // 边界钳制
      await db.cart.updateQty(session.userId, itemId, qty);
      return { ok: true };
    }
    case 'remove': {
      await db.cart.remove(session.userId, String(fd.get('itemId')));
      return { ok: true };
    }
    default:
      throw new Response('bad intent', { status: 400 });
  }
}

export default function Cart() {
  const { items } = useLoaderData<typeof loader>();

  return (
    <ul>
      {items.map((it: any) => <CartRow key={it.id} item={it} />)}
    </ul>
  );
}

function CartRow({ item }: { item: any }) {
  const fetcher = useFetcher();
  const busy = fetcher.state !== 'idle';

  // 乐观数量：update 提交期间显示新值
  const [optimisticQty, setQtyOptimistic] = useOptimistic(
    item.qty, (cur: number, next: number) => next,
  );
  const shownQty = busy && fetcher.formData?.get('intent') === 'update'
    ? optimisticQty : item.qty;

  function changeQty(qty: number) {
    startTransition(async () => {
      setQtyOptimistic(qty);
      await fetcher.submit(
        { intent: 'update', itemId: item.id, qty: String(qty) },
        { method: 'post' },
      );
    });
  }

  return (
    <li>
      {item.name} × {shownQty}
      <button onClick={() => changeQty(shownQty + 1)} disabled={busy}>+</button>
      {/* 局部删除：fetcher.Form 不触发导航，action 完成后 loader 自动重跑 */}
      <fetcher.Form method="post">
        <input type="hidden" name="intent" value="remove" />
        <input type="hidden" name="itemId" value={item.id} />
        <button disabled={busy}>删除</button>
      </fetcher.Form>
    </li>
  );
}
```

**评分点**：
1. action 用 intent 区分多种语义，switch 处理且 default 抛 400。
2. 鉴权在 action 内、数量边界钳制（1~99）、库存校验齐备。
3. 删除行用 fetcher.Form（不导航），能说出 action 后 loader 自动重跑刷新列表。
4. 乐观更新与 fetcher.formData 联动判断（只有 update 期间显示乐观值）。
5. 乐观值经 startTransition 包裹，失败时自动回落真实数据。
