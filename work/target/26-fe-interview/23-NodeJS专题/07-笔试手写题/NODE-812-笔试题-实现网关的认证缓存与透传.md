---
title: [NODE-812] 笔试题——实现网关认证缓存（JWT 粗验 + 缓存 + 透传）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-812：手写网关认证

**需求与边界**：
- 需求：网关认证（SCN-NODE-649/701）——① JWT 粗验（签名/过期——alg 白名单 SCN-NODE-785）；② 验证缓存（同 token 短窗验证结果缓存——重复请求免验，SCN-NODE-640）；③ 上下文透传（user/scopes → ALS/下游 header——SCN-NODE-745）；④ 撤销窗口（黑名单——撤销延迟语义，SCN-NODE-649）。
- 边界：① 验证缓存的撤销窗口（缓存 TTL ≤ access 剩余寿命——撤销延迟不放大）；② 缓存键 = token hash（不存原始 token——泄露面）；③ 认证失败的区别响应（过期/无效/撤销——客户端行动不同，SCN-NODE-785）。

**答**：
```javascript
const authCache = new LRUCache({ max: 10_000, ttl: 30_000 });   // 30s 验证缓存（≤access 剩余）
function gatewayAuth() {
  return (req, res, next) => {
    const token = extract(req);
    const key = sha256(token).slice(0, 16);            // token hash 键（不存原始——泄露面）
    let decoded = authCache.get(key);
    if (!decoded) {
      decoded = verifyJwt(token);                      // alg 白名单（SCN-NODE-785）
      if (isRevoked(decoded.jti)) throw new AppError('AUTH-REVOKED');   // 撤销检查
      authCache.set(key, decoded);
    }
    tenantCtx.run({ user: decoded.sub, scopes: decoded.scopes }, next);   // 上下文注入（SCN-NODE-745）
  };
}
```

**评分点**:
- 验证缓存 TTL ≤ access 剩余（撤销延迟不放大——SCN-NODE-649）。
- 缓存键 token hash（泄露面最小化）。
- 撤销检查进缓存 miss 路径（撤销窗口语义完整）。
- ALS 注入（SCN-NODE-745 联动）。
