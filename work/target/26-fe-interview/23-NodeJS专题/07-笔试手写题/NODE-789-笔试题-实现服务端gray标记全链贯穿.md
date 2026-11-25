---
title: [NODE-789] 笔试题——实现灰度标记全链贯穿（网关→BFF→下游→MQ）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-789：手写灰度贯穿

**需求与边界**：
- 需求：灰度标记贯穿（SCN-OPS-216/NODE-670）——① 网关重写（SCN-OPS-216 权威）；② BFF ALS 注入 + 出站透传（axios interceptor——SCN-NODE-670）；③ MQ 消息携带（SCN-NODE-746 outbox 带 header）；④ 遗漏审计（入口有标记出口没出——链断哨兵，SCN-NODE-670）。
- 边界：① 网关重写优先（客户端传值不信任——SCN-OPS-216）；② 下游版本路由联动（标记 → 实例路由——SCN-NODE-776）；③ 定时任务的标记继承（任务发起时的标记固化——SCN-NODE-730）。

**答**：
```javascript
// 网关（权威重写——SCN-OPS-216）
gateway.use((req, res, next) => {
  req.headers['x-gray-bucket'] = computeGrayBucket(req.user);   // 重写（不信任客户端）
  next();
});
// BFF：ALS 注入 + 出站透传 + 遗漏审计
als.run({ gray: req.headers['x-gray-bucket'] }, next);
axios.interceptors.request.use(cfg => {
  const gray = ctx.getStore()?.gray;
  if (gray) cfg.headers['x-gray-bucket'] = gray;
  return cfg;
});
axios.interceptors.response.use(r => r, (e) => {       // 链断哨兵（SCN-NODE-670）
  if (ctx.getStore()?.gray && !e.config.headers['x-gray-bucket'])
    alert({ type: 'GRAY_CHAIN_BROKEN', url: e.config.url });
  throw e;
});
// MQ：outbox 携带（SCN-NODE-746）
await tx.insertOutbox(topic, payload, { headers: { 'x-gray-bucket': ctx.getStore().gray } });
```

**评分点**:
- 网关权威重写（不信任客户端——SCN-OPS-216）。
- ALS 注入 + interceptor 透传 + 链断哨兵（遗漏审计——SCN-NODE-670）。
- MQ outbox 携带标记（异步链路——SCN-NODE-746）。
- 下游版本路由联动（SCN-NODE-776）。
