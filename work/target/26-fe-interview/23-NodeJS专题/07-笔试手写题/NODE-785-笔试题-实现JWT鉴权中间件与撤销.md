---
title: [NODE-785] 笔试题——实现 JWT 鉴权中间件（alg 白名单 + 撤销检查）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-785：手写 JWT 鉴权

**需求与边界**：
- 需求：JWT 鉴权（SCN-NODE-649）——① alg 白名单（防 alg:none——SCN-NODE-649）；② 撤销检查（refresh 黑名单——撤销延迟 = access 剩余）；③ kid 轮换（密钥轮换——SCN-FIN-567）；④ 权限声明式（requirePermission——SCN-OPS-609）。
- 边界：① payload 不含敏感（可解码——SCN-NODE-698）；② 时钟偏差容忍（exp/iat ±30s——多服务时钟差）；③ 鉴权与租户上下文合并（ALS 注入——SCN-NODE-745）。

**答**：
```javascript
function auth(required = 'user') {
  return (req, res, next) => {
    const token = (req.headers.authorization ?? '').replace('Bearer ', '');
    let decoded;
    try {
      decoded = jwt.verify(token, getKeyByKid(req.headers['x-kid']), {   // kid 轮换（SCN-FIN-567）
        algorithms: ['RS256'],                           // alg 白名单（防 alg:none）
        clockTolerance: 30,                              // 时钟偏差容忍
      });
    } catch (e) {
      return res.status(401).json({ code: e.name === 'TokenExpiredError' ? 'EXPIRED' : 'INVALID' });
    }
    if (isRevoked(decoded.sub, decoded.jti))             // refresh 黑名单（撤销链——SCN-NODE-649）
      return res.status(401).json({ code: 'REVOKED' });
    if (!hasPermission(decoded.scopes, required))        // 声明式权限（SCN-OPS-609）
      return res.status(403).end();
    tenantCtx.run({ ...tenantCtx.getStore(), user: decoded.sub, scopes: decoded.scopes }, next);   // ALS 注入
  };
}
```

**评分点**:
- alg 白名单（防 alg:none——SCN-NODE-649）。
- kid 轮换（密钥轮换——SCN-FIN-567）。
- 撤销链（refresh 黑名单——撤销延迟语义）。
- ALS 注入合并租户上下文（SCN-NODE-745）。
