---
title: [MFW-557] Edge-DB / Drizzle 在 Server Components：类型化数据层的两种路径
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-557：Edge-DB / Drizzle 的类型化数据层

**答**:
- 两条类型化路径：1) **schema-first 类型生成**（EdgeDB：schema.edb → TS 类型生成（codegen RBL-946 管线）；Prisma：schema.prisma → client 生成）；2) **schema-as-types**（Drizzle：TS 定义 schema——类型从代码推导无生成步骤）。选型：生成路径 = 生成时机/缓存（RBL-742 幂等）；推导路径 = 无生成但 schema 与迁移管理在 TS（迁移工具 drizzle-kit）。
- Server Components 的集成差异：Prisma client 是单例（globalThis 单例防 dev 重复实例——RBL-914 常见坑）；Drizzle 连接轻（无 engine 生成——serverless 更友好）；EdgeDB 的 query builder（边缘计算 .query 链——类型安全的编译产物）。
- 产物边界：ORM client 只进 server bundle（'server' 条件导出 RBL-602——误 import 到 client = bundle 爆炸 + 密钥泄漏 RBL-780）；「server-only 包」守卫（RBL-779）。
- 追问钩子：为什么「Prisma 生成 client 单例」在 dev 是经典内存泄漏点？——dev HMR 每次模块重载都 new PrismaClient()（每个实例一个连接池）→ 连接数爆炸；globalThis 单例（`globalThis.prisma ??= new PrismaClient()`）跨 HMR 复用——「模块级单例在 HMR 下的失效」是热更新语义与单例模式的冲突：HMR 的模块重新执行会重建「模块级」状态——globalThis 是绕过模块生命周期的「跨 HMR 存活层」。

```typescript
// Prisma 单例（HMR 安全）
import { PrismaClient } from '@prisma/client';
const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };
export const prisma = globalForPrisma.prisma ?? new PrismaClient();
if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
// Drizzle：schema-as-types（无生成）
export const products = pgTable('products', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
});
export type Product = typeof products.$inferSelect;      // 类型从表定义推导
// server-only 守卫（防 client import）
// package "server-only": import 时 client 环境抛错
import 'server-only';
import { db } from './db';                               // 强制 server bundle
// 构建期守卫：server bundle 导出面审计（RBL-780）
```
