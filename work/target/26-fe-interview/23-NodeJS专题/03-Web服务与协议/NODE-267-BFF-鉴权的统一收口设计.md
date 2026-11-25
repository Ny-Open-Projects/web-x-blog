---
title: [NODE-267] BFF 鉴权的统一收口设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-267：BFF 鉴权的统一收口设计？
**答**:
- 收口原则：token 校验/刷新/权限注入只在 BFF 入口层做一次，业务 handler 拿到的永远是已解析的 user/permCtx——下游微服务信任 BFF（内网 token 或服务间凭证）。
- 会话模式：前端只持 BFF 会话 cookie（HttpOnly），BFF 持第三方 token——token 不暴露给浏览器（ARC-072 密钥前端架构）。
- 路由声明式鉴权：route 配置带 perm（ARC-068/232 契约同款），中间件统一校验——漏标 CI 检查。
- 刷新与并发：token 刷新的并发去重（单飞）+ 刷新失败温和踢出（ARC-226 fail-closed）。

```typescript
// BFF 鉴权收口
const auth = async (ctx, next) => {
  const session = await getSession(ctx);            // HttpOnly cookie → 会话
  if (!session) return ctx.throw(401);
  const user = await tokenMgr.resolve(session);     // token 校验+缓存（单飞刷新）
  ctx.state.user = user;                            // handler 层只看这个
  ctx.state.permCtx = buildPermSnapshot(user);      // ARC-236 谓词引擎输入
  await next();
};
router.post('/orders', { perm: 'order:create' }, auth, permCheck, handler);   // 声明式
// 下游调用：serviceToken（服务间凭证）而非用户 token——审计带 onBehalfOf: user.id
```
