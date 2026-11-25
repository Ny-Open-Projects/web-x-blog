---
title: [MFW-626] 全栈类型安全：从 schema 到 UI 的推理链
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-626：从 schema 到 UI 的推理链

**答**:
- 全栈类型推理链的完整路径：DB schema → ORM 类型（Drizzle inferSelect）→ repo 返回类型 → RSC props → client 组件 props → UI 渲染——「一改全改」的编译期保证（DB 加字段 → repo 类型变 → UI 编译报错处提示遗漏）。
- 推理链的断点与修复：1) 序列化边界（RSC props 的类型 must 可序列化——类型上仍连通但运行时受限 RBL-502）；2) 手动类型断言（`as User`——链断裂：repo 返回 any = 链断；「any 是类型链的天敌」——no-explicit-any 的 lint）；3) API 边界（跨仓 fetch——codegen 补链 RBL-946）。
- 推理链的审计：`any`/`as unknown as` 的扫描（类型逃逸点清单——「推理链的薄弱环节」可视化）；「类型覆盖率」（严格类型的代码占比）。
- 追问钩子：为什么「全栈推理链」的价值在「变更传播」而非「自动补全」？——补全的爽感是表层；核心价值：schema 变更 → 编译错误清单 = 「受影响的 UI 全集」（手工找 = grep/遗漏风险）——「类型的编译期 diff」让变更影响面可见（RBL-649 语义 diff 的类型版）：类型链是「变更传播的自动化追踪器」。

```typescript
// 推理链完整示例
// 1) DB schema
export const products = pgTable('products', { id: serial().primaryKey(), name: text().notNull(), price: numeric() });
export type Product = typeof products.$inferSelect;      // 推导
// 2) repo（返回类型自动）
export const getProduct = (id: number) => db.select().from(products).where(eq(products.id, id));
// 3) RSC props（自动 = Product）
export default async function Page({ params }: { params: { id: string } }) {
  const product = await getProduct(+params.id);
  return <ProductCard product={product} />;              // 类型流到 client
}
// 4) client props（自动）
'use client';
function ProductCard({ product }: { product: Product }) {
  return <span>{product.price}</span>;                   // price: string（numeric）——类型提示
}
// DB 加字段 → Product 类型变 → 编译器列出所有需更新的 UI —— 变更传播自动化
// 审计：类型逃逸扫描
const escapePoints = code.matchAll(/:\s*any\b|as\s+unknown\s+as/g);
```
