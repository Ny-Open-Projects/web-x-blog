---
title: [NODE-496] Node 服务的统一网关认证与会话透传（下游零认证）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-496：统一认证与会话透传
**答**:
- 架构：认证收口网关（JWT/session 统一校验 NODE-376）→ 网关注入可信身份头（x-uid/tenant/gray + 内部签名防伪造）→ 下游零认证（只信任网关注入——网络策略保证外部流量不可达下游 NODE-369）。
- 收益：下游服务不重复实现认证（一处校验全链路受益）、token 算法升级只改网关、下游瘦身。
- 必须守住的防线：内部头剥离（网关强制剥离外部请求的同名头——伪造入口关闭）、下游网络隔离（外部直连下游的路径必须封死——否则透传头可被伪造）、mTLS 或网络策略做身份锚（NODE-369 mesh 配合）。
- 特例处理：需要原始凭证的下游（支付渠道回调验签）——回调路径单独设计（不走统一透传，直接验渠道签名）。
- 会话透传语义：下游拿到的是"已认证的用户上下文"（uid/权限快照版本），下游的细粒度权限仍需自己判（数据级 NODE-484——网关认证 ≠ 授权）。
```javascript
// 网关注入（剥离后重注入）
app.use((ctx, next) => {
  stripInternalHeaders(ctx);                                     // 防伪造：先剥离
  const s = verifySession(ctx);                                  // 统一认证
  ctx.set('x-uid', s.uid); ctx.set('x-tenant', s.tenant);
  ctx.set('x-internal-auth', signInternal({ uid: s.uid, exp: +60e3 })); // 签名防篡改
  return next();
});
// 下游：只认 x-internal-auth 签名有效 + 网络来源 ∈ 网关 IP 段
```
