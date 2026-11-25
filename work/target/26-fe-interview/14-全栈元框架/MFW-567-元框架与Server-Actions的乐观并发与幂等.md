---
title: [MFW-567] Server Actions 的乐观并发与幂等
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-567：Server Actions 的乐观并发与幂等

**答**:
- Action 的并发语义：client 可并发调多个 action（无全局队列）——同一资源的并发写（两个 tab 同时下单同一商品——库存超卖）——「乐观并发控制」：action 层版本检查（WHERE version = ? / WHERE stock > 0 原子更新）。
- 幂等的必要性：重试/重放（网络层重试或用户双击）→ action 重复执行——「idempotency key」：action 参数含 idempotencyKey（client 生成 UUID）→ server 端去重表（RBL-913 模式）；「下单 action 必须幂等」（重复下单 = 资损）。
- 乐观 UI 与并发的配合：useOptimistic 的本地乐观值在并发下可能交错（两个 tab 的乐观值各自加——server 真值以先 commit 者为准——revalidate 后对齐 RBL-513）。
- 追问钩子：为什么「Action 天然可重放」让幂等从可选变必需？——Action 是 HTTP POST（网络失败 client 重试是标准行为——框架/浏览器层自动）；重试 = 同一 action 再次执行（除非业务幂等 = 重复效果）；传统表单 POST 也重放但用户感知强（页面刷新可察觉）；Action 的静默重放（fetch 层）让重复执行的感知弱化——「静默重放 × 非幂等操作 = 资损」的组合是 Action 架构的必答题。

```typescript
// 幂等 action（去重表）
'use server';
export async function placeOrder(formData: FormData) {
  const idempotencyKey = formData.get('idemKey') as string;
  const existing = await db.orders.findByKey(idempotencyKey);
  if (existing) return { orderId: existing.id, replayed: true };   // 重放返回原结果
  return db.$transaction(async (tx) => {
    const stock = await tx.product.findUnique({ where: { id: sku } });
    if (stock.count <= 0) throw new OutOfStock();          // 乐观并发：原子校验
    const order = await tx.order.create({ data: { idemKey, ... } });
    await tx.product.update({ where: { id: sku, count: { gt: 0 } },
      data: { count: { decrement: 1 } } });                // 原子扣减防超卖
    revalidateTag('cart');
    return { orderId: order.id };
  });
}
// client 侧生成幂等键
const idemKey = useRef(crypto.randomUUID()).current;      // 同一表单生命周期内稳定
<form action={...}>
  <input type="hidden" name="idemKey" value={idemKey} />
</form>
```
