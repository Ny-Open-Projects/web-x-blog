---
title: [MFW-757] Server Actions 的 Composed Actions
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-757：Server Actions 的 Composed Actions

**答**:
- Composed Actions：1) **action 内调用其他 server 函数**（非直接调 action——调用的是普通 server 函数（同文件/同模块——不产生新的 HTTP 请求）；2) **编排模式**：主 action 编排子操作（子操作是普通 async 函数——不是 'use server' 标注的 action——内函数直接调用无 HTTP 开销；3) 'use server' 的文件级语义（文件标注 = 所有导出都是 action——文件内非导出函数是普通函数（可被 action 调用——不被暴露为端点）。
- 编排 vs 直接暴露：编排 action = 一个端点调用多个内部函数（单 HTTP 请求）；直接暴露 = 多个端点（client 分别调用——多次请求）；「编排的原子性」：单事务多操作（RBL-722）/编排 action 的优势。
- 权限边界：编排 action 的 auth 检查（在编排层校验一次——内部函数信任编排层（不做重复 auth——减少开销但保持安全——内函数不暴露所以无直接调用风险）。
- 追问钩子：为什么「'use server' 文件内的非导出函数不是 action」是设计关键？——文件级 'use server' = 所有**导出**函数成为 action（可被 client 调用——HTTP 端点）；非导出 = 普通函数（无 HTTP 端点——仅 server 内部使用）；「导出的边界 = 安全边界」：非导出函数不被暴露 → 编排 action 可以安全地调用内部函数（无需在内部函数重复 auth——调用者已被编排层鉴权）；「action 的暴露面控制」：导出即端点、非导出即内部——文件的导出面就是安全面。

```typescript
// actions.ts —— 文件级 'use server'
'use server';
// 导出 = action（HTTP 端点）
export async function placeOrder(data: OrderInput) {
  const session = await auth();                          // 编排层 auth
  if (!session.canBuy) throw new Error('Unauthorized');
  // 编排：调用内部函数（非导出——不是 action）
  const order = await _createOrder(session.userId, data);      // 内部函数
  await _updateInventory(data.sku, data.qty);            // 内部函数
  await _awardPoints(session.userId, data.total);        // 内部函数
  return { orderId: order.id };
}
// 非导出 = 普通函数（无 HTTP 端点——安全）
async function _createOrder(userId: string, data: OrderInput) {
  return db.order.create({ data: { ...data, userId } });
}
async function _updateInventory(sku: string, qty: number) {
  return db.inventory.update({ where: { sku }, data: { count: { decrement: qty } } });
}
async function _awardPoints(userId: string, total: number) {
  return db.points.create({ data: { userId, amount: total * 0.01 } });
}
```
