---
title: [NODE-167] 设计一个 API 开放平台（鉴权/限流/文档/SDK）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-167：设计一个 API 开放平台（鉴权/限流/文档/SDK）？
**答**：
- 四件套：**AppKey/AppSecret 鉴权**（HMAC 签名 + 时间戳防重放，NODE-087）→ **按应用限流**（令牌桶，配额随套餐）→ **自助文档**（OpenAPI 生成 + 在线调试台）→ **多语言 SDK**（同源生成）。
- 泳道隔离：开放流量独立 BFF 与网关路由（NODE-152 open-api 泳道），限流配额独立，故障不波及内部。
- 版本策略：v1 冻结只修 bug，新能力走 v2；废弃提前 6 个月发公告与响应头提示。
- 治理：应用注册/审核/吊销流程、调用量与错误率看板、异常调用自动限流并通知。

```javascript
app.use('/open/v1', async (ctx, next) => {
  const app = await db.app.findUnique({ where: { appKey: ctx.get('x-api-key') } });
  if (!app || app.status !== 'ACTIVE') ctx.throw(401);

  // 签名 = HMAC-SHA256(secret, method + path + timestamp + bodyMd5)
  const ts = Number(ctx.get('x-timestamp'));
  if (Math.abs(Date.now() - ts) > 300_000) ctx.throw(401, 'timestamp drifted'); // 防重放
  if (!verifySig(app.secret, ctx)) ctx.throw(401, 'bad signature');

  const ok = await tokenBucket(`open:${app.appKey}`, app.rateLimit); // 按应用限流
  if (!ok) {
    ctx.status = 429;
    ctx.body = { code: 'RATE_LIMITED', retryAfter: 1 };
    return;
  }
  ctx.state.app = app;
  await next();
});
// 文档：OpenAPI 驱动（NODE-157）+ 沙箱 AppKey 在线调试
// SDK：openapi-typescript + codegen 发 npm，类型与文档同源
```
