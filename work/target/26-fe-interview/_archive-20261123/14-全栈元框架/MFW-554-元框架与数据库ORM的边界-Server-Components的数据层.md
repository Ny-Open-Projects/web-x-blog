---
title: [MFW-554] 元框架与 ORM 边界：Server Components 的数据层设计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-554：Server Components 数据层：ORM 边界设计

**答**:
- RSC 直接调 ORM（server 组件里 db.query）——「全栈同仓」的新形态：数据层与 UI 层同进程——边界设计：1) **数据访问层封装**（repository 模式：组件调 repo 函数而非裸 ORM——可测/可换/权限集中）；2) **事务边界**（action 的写操作需事务——跨组件写共享 repo）；3) **连接池治理**（serverless 的连接问题——RBL-517 Edge 版的 Node 版：Next serverless 函数的连接池上限——pgBouncer/HTTP driver）。
- 权限模型：组件里直接 db.query = 无鉴权层（RSC 不是 API——没有 middleware 链）——「数据层鉴权」下沉到 repo（每个 repo 函数内校验 session——RBL-803 的 ORM 版）；「组件直接 ORM」的诱惑 vs 安全。
- 测试边界：repo 单测（mock db）+ 组件集成测试（RBL-549 harness）。
- 追问钩子：为什么「组件里裸写 ORM」是架构债而非开发速度红利？——数据访问散落在组件 = 权限/缓存/事务逻辑无处集中（每个组件自己处理鉴权 = 重复 + 遗漏风险）；repo 层是「数据契约的收口」（缓存 tag 打标/权限/事务的统一层）——「直接调用的爽」vs「契约收口的必要」：RSC 让数据层更近但不是更薄——靠近是为了类型/流式，不是为了让鉴权消失。

```javascript
// repository 层（数据契约收口）
// lib/repo/product.ts
import { cache } from 'react';
export const getProduct = cache(async (id: string, session: Session) => {
  if (!session.canRead('product')) throw new Forbidden();          // 权限收口
  return db.product.findUnique({ where: { id } });                 // ORM
});
// 缓存 tag 集中打标
export async function updateProduct(id, data, session) {
  if (!session.canWrite('product')) throw new Forbidden();
  return db.$transaction(async (tx) => {                           // 事务收口
    const p = await tx.product.update({ where: { id }, data });
    revalidateTag(`product:${id}`);                                // 缓存失效收口
    return p;
  });
}
// 组件侧：只调 repo，不裸写 ORM
export default async function Page({ params }) {
  const session = await auth();
  const product = await getProduct(params.id, session);
  return <ProductView product={product} />;
}
```
