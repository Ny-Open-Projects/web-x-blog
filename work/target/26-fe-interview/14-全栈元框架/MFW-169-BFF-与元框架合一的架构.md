---
title: [MFW-169] 元框架兼任 BFF 的架构是什么？边界在哪？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-169：元框架兼任 BFF 的架构是什么？边界在哪？
**答**：
- 元框架（Next Route Handlers/Nuxt Nitro/RRv7 loaders）天然能做 BFF：页面取数直达服务端、聚合多下游、裁剪字段、鉴权转发——省掉独立 BFF 层与一次内网跳。
- 合一的收益：类型贯通（前端接口类型即服务端函数签名）、部署单元少、请求级上下文（cookie）直接可用。
- 边界（什么时候拆出独立 BFF）：① 多个前端（App/小程序/Web）共享同一聚合 API——元框架是 Web 专属的，共享层要独立；② 重计算/长连接/WebSocket 集群——SSR 函数无状态短生命周期，不合适；③ 团队边界——BFF 归服务端团队管时拆开更顺。
- 演进路径：起步全合一 → 独立出「平台 API」服务（供多端）+ Web 元框架只做裁剪聚合 → 复杂域（IM/推送）独立服务化。

```ts
// 元框架 BFF 的典型聚合 Handler（Next Route Handler）
// app/api/product-detail/[id]/route.ts
export async function GET(_req: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  // 并行聚合三个下游（SSR/BFF 的核心价值：合并请求 + 裁剪字段）
  const [product, inventory, promo] = await Promise.all([
    fetch(`${process.env.PRODUCT_SVC}/products/${id}`).then((r) => r.json()),
    fetch(`${process.env.INV_SVC}/stock/${id}`).then((r) => r.json()),
    fetch(`${process.env.PROMO_SVC}/active?productId=${id}`).then((r) => r.json()),
  ]);

  // 只吐页面需要的字段：减少传输 + 防内部字段泄漏
  return Response.json({
    name: product.name,
    price: product.price,
    inStock: inventory.count > 0,
    promoText: promo?.banner ?? null,
  });
}
```
