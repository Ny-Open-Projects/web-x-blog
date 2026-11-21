---
title: [NODE-156] 如何用 Prisma 构建类型安全的 DB 层？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-156：如何用 Prisma 构建类型安全的 DB 层？
**答**：
- 核心：`schema.prisma` 是唯一事实源 → `prisma generate` 产出精确 TS 类型 → **表结构变更即编译期报错**，字段拼错/类型不符在 CI 就拦截。
- 查询类型随 select 收窄：只 select 部分字段时返回类型自动只有这些字段；`Awaited<ReturnType<...>>` 可反向提取类型给下游。
- 事务类型安全：`$transaction(async (tx) => ...)` 里 tx 拥有同样的类型约束。
- 配套纪律：迁移走 `prisma migrate`（SQL 入库 review）；复杂查询用 `$queryRaw` tagged template（参数化防注入，NODE-127）。

```typescript
// schema.prisma → npx prisma generate
// model Order { id String @id  userId String  status OrderStatus  amount Int }

const listOrders = (userId: string) =>
  prisma.order.findMany({
    where: { userId, status: 'PAID' },        // 枚举值拼错 → 编译失败
    select: { id: true, amount: true, createdAt: true },
    orderBy: { createdAt: 'desc' },
    take: 20,
  });

type OrderRow = Awaited<ReturnType<typeof listOrders>>[number]; // 类型反向提取

const result = await prisma.$transaction(async (tx) => {
  const o = await tx.order.update({           // 事务内同样类型安全
    where: { id }, data: { status: 'PAID' },
  });
  return o;
});
```
