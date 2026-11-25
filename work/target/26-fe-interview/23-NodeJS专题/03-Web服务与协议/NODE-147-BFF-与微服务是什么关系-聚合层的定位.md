---
title: [NODE-147] BFF 与微服务是什么关系（聚合层的定位）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-147：BFF 与微服务是什么关系（聚合层的定位）？
**答**：
- 分层：客户端 → 网关（通用治理）→ **BFF（业务编排/聚合裁剪）** → 微服务（领域逻辑）；BFF 是微服务数据的"裁缝"，向前端暴露面向场景的接口。
- 三条纪律：① 每端独立 BFF（Web/App/小程序），避免一个 BFF 长成上帝层；② BFF 不写业务规则、不碰核心数据一致性，只编排；③ 微服务禁止绕过 BFF 直接暴露给前端。
- 典型能力：并行聚合 + 慢依赖降级（NODE-048）、字段裁剪（移动端只要 10 个字段不传 100 个）、协议转换（REST→GraphQL）。
- 劣化信号：BFF 里出现 `if 订单金额 > 100` 这类业务规则 = 架构在腐化，及时把规则下沉微服务（NODE-186）。

```javascript
// BFF 编排示例：微服务各管各的表，BFF 聚合裁剪
app.get('/api/mobile/order-detail/:id', async (ctx) => {
  const order = await breaker('order').exec(() => rpc.getOrder(ctx.params.id));
  if (!order) ctx.throw(404);
  const [buyer, track] = await Promise.all([
    cached(`user:${order.userId}`, () => rpc.getUserLite(order.userId), 60), // 裁剪：只要昵称头像
    withTimeout(rpc.getLogistics(ctx.params.id), 300, null),                 // 慢依赖降级为 null
  ]);
  ctx.body = {                       // 移动端字段裁剪：10 个字段而非 100 个
    status: order.status,
    buyer: buyer?.nickname,
    track: track?.latest,
  };
});
```
