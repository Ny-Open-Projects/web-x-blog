---
title: [WEB-279] BFF 层是干什么的？解决什么问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 架构]
type: 面试题
---

## WEB-279：BFF 层是干什么的？解决什么问题？

**答**：
- BFF（Backend For Frontend）：为特定前端形态（Web/App/小程序）定制的聚合层，前端团队用 Node 维护。
- 解决三类问题：聚合裁剪（多个微服务的数据拼成页面一次返回，砍掉冗余字段）、协议适配（内部 RPC 转 HTTP/JSON）、鉴权与会话（客户端只面对 BFF，HttpOnly cookie 在 BFF 兑换成内部 token）。
- 收益：端与后端解耦，后端接口稳定，页面需要的「形状」随需求快速变；SSR 也天然放 BFF。
- 代价与治理：多一层运维与故障面，需要链路追踪、超时熔断、限流；团队边界要清晰（谁写 BFF）。

```javascript
// BFF 聚合示例：页面一次拿到头图+价格+库存
app.get('/api/product-page/:id', async (req, res) => {
  const [info, price, stock] = await Promise.all([
    rpc('product-service', 'info', req.params.id),
    rpc('price-service', 'get', req.params.id),
    rpc('stock-service', 'check', req.params.id),
  ]);
  res.json({ title: info.title, image: info.image, price: price.value, inStock: stock.ok });
});
```
