---
title: [NODE-572] Node 服务的 JWT 密钥轮换（无缝换签）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-572：JWT 密钥轮换
**答**:
- 为什么轮换：密钥泄露应急、定期轮换（合规）、算法升级（HS256→RS256——公私钥分离）。
- 双密钥过渡：新密钥签发（新 token 全部用新 kid）+ 旧密钥仅验签（存量 token 过渡期内有效）→ 存量自然过期 → 废旧密钥。JWKS 发布（kid 多把——验签方按 kid 选取，缓存 JWKS + 未知 kid 强刷）。
- 轮换流程：生成新密钥（KMS 托管 NODE-362）→ JWKS 加新 kid → 签发切新 → 观察旧 kid 存量 → 移除旧 kid（等待期 > token 最大有效期）。
- 紧急轮换（泄露）：立即 JWKS 移除旧 kid（所有旧 token 立即失效——会话全踢的代价）或黑名单旧 token（更平滑——按 jti 黑名单批量撤销）。
- 实现细节：kid 在 header 显式、验签失败处理（kid 未知 → 刷 JWKS 重试一次——防缓存滞后）、时钟偏移容忍（nbf/exp leeway 60s——时钟偏差 ARC-537）。
```javascript
// 验签：按 kid 选密钥，未知 kid 刷 JWKS
async function verifyJwt(token) {
  const { kid } = decodeHeader(token);
  let key = jwks.get(kid);
  if (!key) { await refreshJwks(); key = jwks.get(kid); if (!key) throw new UnknownKid(); }
  return jwt.verify(token, key.publicKey, { algorithms: ['RS256'], clockTolerance: 60 });
}
// 签发：jwks.active.sign（kid: v3）——旧 v2 仅 verify，存量过期后移除
```
