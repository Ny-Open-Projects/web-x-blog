---
title: [NODE-044] Prisma、TypeORM、Sequelize 如何对比选型？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-044：Prisma、TypeORM、Sequelize 如何对比选型？
**答**：
- **Prisma**：schema 单一真源 + 生成强类型 Client，TS 体验最佳、迁移工具成熟；代价是不够灵活（复杂 SQL 要 `$queryRaw`）、运行时多一层查询引擎。新项目 + TS 首选。
- **TypeORM**：装饰器实体 + Active Record/Data Mapper 双模式，功能全（关系、事务、迁移、订阅者）；但类型推断弱、文档质量参差、历史坑较多。适合深度定制与 NestJS 生态。
- **Sequelize**：老牌、生态稳定、文档丰富；TS 支持靠手写 interface，体验一般。存量项目维护居多。
- 面试口径：**类型安全与 DX 选 Prisma，NestJS 重度定制选 TypeORM，存量维护 Sequelize**；共享 SQL 场景或强控制需求可以直接上 Knex/原生驱动。

```typescript
// Prisma：schema 驱动 + 强类型查询
// prisma/schema.prisma
// model User {
//   id    Int     @id @default(autoincrement())
//   email String  @unique
//   posts Post[]
// }
// model Post {
//   id       Int    @id @default(autoincrement())
//   title    String
//   author   User   @relation(fields: [authorId], references: [id])
//   authorId Int
// }

import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

// 关联查询 + 类型自动推导，author 拼写错误在编译期就报红
const usersWithPosts = await prisma.user.findMany({
  where: { email: { endsWith: '@example.com' } },
  include: { posts: { where: { title: { contains: 'Node' } }, take: 5 } },
});

// 事务：交互式事务（同一上下文内多步原子操作）
await prisma.$transaction(async (tx) => {
  await tx.account.update({ where: { id: fromId }, data: { balance: { decrement: amount } } });
  await tx.account.update({ where: { id: toId }, data: { balance: { increment: amount } } });
  await tx.transferLog.create({ data: { fromId, toId, amount } });
});
```

```javascript
// TypeORM：装饰器实体（对比参考）
// @Entity() class User { @PrimaryGeneratedColumn() id; @Column() email; @OneToMany(() => Post, p => p.author) posts; }
// await repo.find({ relations: ['posts'], where: { email: Like('%@example.com') } });
// Sequelize：模型 + 语法糖
// await User.findAll({ include: Post, where: { email: { [Op.endsWith]: '@example.com' } } });
```
