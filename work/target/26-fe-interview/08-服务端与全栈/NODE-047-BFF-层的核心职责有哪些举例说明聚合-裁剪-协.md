---
title: [NODE-047] BFF 层的核心职责有哪些？举例说明"聚合、裁剪、协议转换"？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-047：BFF 层的核心职责有哪些？举例说明"聚合、裁剪、协议转换"？
**答**：
- **聚合**：把多个下游接口的数据拼成一个页面级响应（并行请求 + 超时降级）。
- **裁剪与适配**：只返回端上需要的字段（省流量）、字段改名与结构重排（匹配前端组件 props）、单位/时区/枚举值转换。
- **协议转换**：下游 gRPC/内部 RPC/老接口 → 统一 REST/JSON；错误码归一。
- 附加职责：鉴权会话、限流熔断、埋点注入、A/B 分流、安全过滤（越权字段剔除，如不透传下游返回的手机号给无权限端）。

```javascript
// 商品详情页 BFF：聚合 + 裁剪 + 协议转换
async function fetchJSON(url, timeoutMs = 800) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), timeoutMs);   // 每个下游独立超时
  try {
    const res = await fetch(url, { signal: ctrl.signal });
    if (!res.ok) throw new Error(`upstream ${res.status}`);
    return await res.json();
  } finally { clearTimeout(timer); }
}

router.get('/page/product/:id', async (ctx) => {
  const { id } = ctx.params;
  const uid = ctx.state.user?.uid;

  // 聚合：商品、价格、库存 并行请求
  const [product, price, stock] = await Promise.allSettled([
    fetchJSON(`${PRODUCT_RPC}/v1/goods/${id}`),       // 下游是内部 RPC，经网关代理
    fetchJSON(`${PRICE_API}/price?gid=${id}`),
    fetchJSON(`${STOCK_API}/stock?gid=${id}`),
  ]);

  // 降级：核心数据失败才报错，附属数据失败给默认值
  if (product.status !== 'fulfilled') ctx.throw(502, '商品服务不可用');

  ctx.body = {
    // 裁剪：只给移动端需要的字段，重排为组件友好结构
    goods: {
      id: product.value.id,
      title: product.value.itemName,          // 字段改名：itemName → title
      cover: product.value.images[0]?.url,    // 取首图，不透传整个图片数组
      price: price.status === 'fulfilled'
        ? { current: price.value.amount, formatted: `¥${(price.value.amount / 100).toFixed(2)}` } // 分转元
        : { current: null, formatted: '价格暂不可见' },   // 协议降级
      inStock: stock.status === 'fulfilled' ? stock.value.count > 0 : true,
    },
    // 安全：下游返回的 seller 手机号绝不透传
  };
});
```
