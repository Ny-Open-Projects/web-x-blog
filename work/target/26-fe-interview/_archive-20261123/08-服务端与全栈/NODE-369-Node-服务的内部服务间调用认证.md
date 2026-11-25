---
title: [NODE-369] Node 服务间（内部）调用认证如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-369：Node 服务间调用认证
**答**:
- 内部认证 ≠ 信任网络：零信任基线——服务间调用也要认证（mTLS 双向证书 / Service Mesh 自动处理，或应用层 token）。
- 方案谱系：mTLS（网关/mesh 层，应用无感，推荐 K8s 环境）、短期服务令牌（SPIFFE/JWT 服务身份，几分钟过期）、静态密钥（简单但轮换痛苦，兜底方案）。
- 传递用户上下文：内部调用透传身份头（x-user-id + 内部签名防伪造——外部请求网关已剥离这些头，只有网关能注入），下游据此做数据权限（NODE-361）。
- 防御重点：外部流量禁达内部端口（网络策略：内部服务只接受 mesh/gateway 流量）、内部头不可由外部伪造（网关强制剥离）。
- 审计：内部调用也记 trace 与调用方身份（出事能定位到调用链）。
```javascript
// 内部上下文透传 + 防伪造
function internalFetch(url, { user, ...init }) {
  const payload = { uid: user.id, exp: Date.now() + 60e3 };
  const token = signJwt(payload, INTERNAL_KEY, { kid: 'svc' });  // 短时签名
  return fetch(url, { ...init, headers: { 'x-internal-auth': token, 'x-internal-user': user.id } });
}
// 网关强制剥离外部请求的 x-internal-* 头 —— 内部头只能由网关注入
```
