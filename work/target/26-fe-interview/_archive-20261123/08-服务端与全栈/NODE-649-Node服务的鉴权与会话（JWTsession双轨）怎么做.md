---
title: [NODE-649] Node 服务的鉴权与会话（JWT/Session 双轨）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-649：鉴权与会话怎么做？
**答**：
- 双轨选型：JWT（无状态、跨服务传递——签名验证零 IO；代价：撤销难）vs Session（可撤销、服务端权威——代价：集中存储 + 每请求查）；混合主流：短期 JWT（5~15min）+ refresh token（服务端可撤销——撤销粒度在 refresh 层）。
- JWT 安全要点：短过期（泄露窗口最小化）、alg 固定（防 alg:none 攻击——白名单校验）、敏感信息不进 payload（JWT 可解码）、kid 轮换（SCN-FIN-567 token 轮换同源）。
- 会话中间件设计：鉴权与业务解耦（中间件层统一——不散落在 handler）、权限声明式（requirePermission 装饰器——SCN-OPS-643 权限矩阵同源）、未认证的统一响应（401 + 重定向语义）。
- 撤销链路：登出/风控踢下线 → refresh token 黑名单（Redis）+ access token 靠短过期自然失效——撤销延迟 = access 剩余寿命。
- 追问钩子：为什么「JWT 撤销难」要用「短 access + 可撤销 refresh」而不是「JWT 里加黑名单检查」——JWT 黑名单检查 = 每请求查 Redis（回到 session 的 IO 成本，无状态优势全失）；短 access 的撤销延迟最多 15 分钟且 refresh 层可即时拦截——用「时间窗」替代「每请求校验」，撤销语义完整且保留无状态优势。

```javascript
function auth(required = 'user') {
  return async (req, res, next) => {
    const token = verify(req.headers.authorization, { algorithms: ['RS256'] });   // alg 白名单
    if (token.revoked && Date.now() - token.iat > ACCESS_TTL) return res.status(401);
    req.auth = token;
    hasPermission(token, required) ? next() : res.status(403).end();
  };
}
```
