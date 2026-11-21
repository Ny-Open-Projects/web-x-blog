---
title: [ARC-062] BFF 层的职责边界如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-062：BFF 层的职责边界如何设计？
**答**：
- BFF 只做三件事：聚合（多个下游接口拼一个页面级接口）、裁剪（去掉前端不需要的字段）、协议转换（下游 RPC/老协议 → 前端友好 JSON）。
- BFF 不做业务逻辑：业务规则在领域服务，BFF 写了业务规则就会随端增多而腐烂。
- 每端一个 BFF（web/wap/app）或按域拆分，团队归属与前端一致，接口契约由前端定义。

```typescript
// BFF：商品详情页聚合接口 —— 聚合 + 裁剪 + 协议转换，无业务逻辑
import type { FastifyInstance } from 'fastify';

export default async function (app: FastifyInstance) {
  app.get('/api/bff/product/:id', async (req) => {
    const { id } = req.params as { id: string };
    // 并行聚合三个下游（网关/RPC/旧接口）
    const [base, inventory, promotion] = await Promise.all([
      rpc.product.getBaseInfo(id),
      rpc.inventory.getStock(id),
      restApi.get(`/legacy/promotions?sku=${id}`),        // 协议转换：旧接口 → 新结构
    ]);
    return {
      // 裁剪：前端只需要展示字段，不下发内部成本、审计字段
      title: base.title,
      price: promotion.finalPrice ?? base.msPrice,
      stockState: inventory.quantity > 0 ? 'IN_STOCK' : 'SOLD_OUT',  // 转成前端枚举
      tags: promotion.labels.map(l => ({ text: l.text, color: l.css })), // 协议适配
    };
  });
}
```
