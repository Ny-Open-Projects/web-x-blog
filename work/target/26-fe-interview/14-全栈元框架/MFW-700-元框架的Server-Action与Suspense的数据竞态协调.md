---
title: [MFW-700] Server Action 与 Suspense 的数据竞态协调
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-700：Action 与 Suspense 的数据竞态

**答**:
- Action 触发 revalidate → Suspense 边界重新渲染的数据竞态：1) **action 提交中 + 页面导航**（action 在执行（写 DB）→ 用户导航离开 → revalidate 触发——action 的 revalidate 在导航后仍生效（server 侧执行完才 revalidate——顺序：action 完成 → revalidate → 缓存失效——即使 client 已离开）；2) 导航后返回：Router Cache 已失效（revalidate 通知——重新拉取）；3) **action 未完成 + 用户导航**（client abort → server 仍执行（RBL-504）→ revalidate 触发——数据已写入但用户没看到——下次访问拿到新数据（最终一致）。
- action 与 Suspense 的时序：action 完成 → revalidateTag → Router Cache 失效 → 受影响 Suspense 边界重新渲染（server push 或下次访问）——「action → revalidate → 边界刷新」的链路。
- 竞态的形态：action A 写 DB → revalidate tag → 同时 action B 读 DB（旧数据——B 在 A 写入前读了）——「写读竞态」：action 间的顺序性（框架不保证 action 串行——业务层处理（乐观锁 RBL-567））。
- 追问钩子：为什么「action 导航后 server 仍执行」是正确的语义？——action 的执行 = 数据写入（用户意图——即使 UI 导航走了也要完成）；abort = UI 层取消（不等待结果）而非 server 取消（数据已写）；「UI 取消 ≠ server 取消」的语义分离：client abort 只取消 UI 等待——server action 继续执行（数据一致性）——RBL-505 的 SSR abort 与 Action abort 的语义差异：SSR abort = 取消渲染（可再生）；Action abort = 不取消执行（不可逆写操作——必须完成）。

```tsx
// Action 导航后的 server 侧继续执行
'use server';
export async function placeOrder(fd: FormData) {
  const order = await db.orders.create({...});           // 用户导航走了也执行
  await emailService.send(order);                        // 后续操作继续
  revalidateTag('orders');                               // 缓存失效（导航后也生效）
  return { orderId: order.id };
}
// client：导航取消 UI 等待（server 继续执行）
'use client';
function Checkout() {
  return <form action={async (fd) => {
    // 用户中途导航 → client abort fetch
    // server 侧 action 继续执行（数据写入 + revalidate）
    const result = await placeOrder(fd);
    router.push('/orders');                              // 正常路径
  }}>
    <button>下单</button>
  </form>;
}
// 竞态：action B 读旧数据（A 未完成写入）
// 解法：业务层的顺序保证（乐观锁 RBL-567）或等待（await A 的结果）
```
