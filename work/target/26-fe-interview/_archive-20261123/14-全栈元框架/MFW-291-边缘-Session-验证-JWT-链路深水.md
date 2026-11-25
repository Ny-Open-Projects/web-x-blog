---
title: [MFW-291] 边缘 JWT 校验链深水（jwks 缓存/kid 轮换/时钟偏移）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-291：边缘 JWT 校验链深水

**答**:
- JWKS 获取：边缘无持久态——公钥集拉取后缓存（isolate 内 KV + Cache API 双层；TTL 5min + kid 未命中强制刷新一次——轮换零窗口）
- kid 轮换协议：token header.kid 选公钥——新 kid 未在缓存 → 刷 JWKS 再验（一次额外请求，缓存更新后归零成本）
- 时钟偏移：nbf/exp 校验留 ±30s leeway（边缘节点与签发端时钟漂移——误杀合法 token 是可用性事故）
- 算法锁定：只允许 RS256/ES256（alg: none 攻击与算法混淆——拒绝列表不如允许列表）

```javascript
async function verifyInEdge(token) {
  const { kid, alg } = decodeHeader(token)
  if (!['RS256','ES256'].includes(alg)) throw new Error('alg not allowed')  // 允许列表
  let keys = await getCachedJwks() ?? await fetchAndCacheJwks()             // 5min TTL
  let key = keys[kid] ?? (await forceRefresh(), keys = cache())[kid]        // 轮换 miss → 强刷
  return jwtVerify(token, key, { clockTolerance: 30 })                      // 偏移容忍
}
```
