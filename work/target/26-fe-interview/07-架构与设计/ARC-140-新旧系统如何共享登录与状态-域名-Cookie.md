---
title: [ARC-140] 新旧系统如何共享登录与状态（域名/Cookie/Token 桥）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-140：新旧系统如何共享登录与状态（域名/Cookie/Token 桥）？
**答**：
- 域名策略：优先"同主域不同路径"（app.com/new 与 app.com/legacy），Cookie 天然共享；跨子域用 domain=.app.com 的 Cookie；完全不同域名则上 SSO（OAuth 授权码或 CAS），跳转换取票据。
- Token 桥：老系统持有旧会话、新系统用 JWT 时，由网关或桥接服务完成"旧 session → 换发新 JWT"（反之亦然），登录一次两端可用；token 刷新也要双向同步（避免一端刷新另一端失效）。
- 状态共享分清层次：登录态/主题/用户偏好走 Cookie 或共享存储；业务状态不跨系统共享（各自服务端为准），防止隐式耦合。
- 登出一致性：任一端登出要广播失效（统一登出端点 + token 黑名单），否则出现"单端已退全局仍登录"的安全问题。

```typescript
// Token 桥接服务（网关侧核心逻辑）
interface LegacySession { sid: string; userId: string }
interface ModernJWT { token: string; refresh: string; exp: number }

async function exchange(req: Request): Promise<ModernJWT> {
  // 场景 1：老系统用户访问新页面 —— 旧 sid 换发 JWT
  const sid = req.cookies['legacy_sid'];
  if (sid) {
    const session = await legacyStore.verify(sid);            // 验证老会话有效性
    return jwtService.issue({ userId: session.userId, source: 'legacy', ttl: '2h' });
  }
  // 场景 2：新系统用户访问老页面 —— JWT 换取旧会话（或直接透传给老系统的鉴权插件）
  const jwt = req.headers.authorization?.replace('Bearer ', '');
  if (jwt) {
    const claims = await jwtService.verify(jwt);
    const legacySid = await legacyStore.ensureSession(claims.userId);  // 幂等建会话
    setCookie(res, 'legacy_sid', legacySid, { domain: '.app.com' });
    return { token: jwt, refresh: '', exp: claims.exp };
  }
  throw new Unauthorized();
}
// 登出一致性：POST /logout 同时做三件事
// 1. 吊销 JWT（黑名单）2. 删除 legacy session 3. 广播各端踢下线
```
