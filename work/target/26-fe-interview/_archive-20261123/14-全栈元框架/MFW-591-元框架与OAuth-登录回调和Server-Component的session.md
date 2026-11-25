---
title: [MFW-591] OAuth 登录回调与 Server Component 的 session
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-591：OAuth 回调与 RSC session

**答**:
- OAuth 流程在元框架的落点：1) **发起**（route handler：/api/auth/login → 302 到 provider + state 参数（CSRF 防——state 存 cookie 比对））；2) **回调**（/api/auth/callback → code 换 token → 建 session → set-cookie → redirect）；3) **RSC 读 session**（cookies() → session 校验 RBL-558）。
- 回调的坑：1) **state 验证**（回调的 state 与 cookie 中 state 比对——CSRF：不比对 = 登录 CSRF 攻击）；2) **token 存储**（access token 存哪：session 表（server 可刷新）+ refresh token 加密 cookie；「token 不进 client」RBL-803）；3) 回调的竞态（重复回调/并发登录——幂等 RBL-567）。
- session 的续期：滑动过期（访问刷新过期时间——RSC 渲染期不能 set-cookie！RBL-558——刷新只能在 Action/route handler——「静默续期」方案：middleware 里 set（Next middleware 可 set-cookie RBL-514））。
- 追问钩子：为什么 OAuth 的「token 交换」必须放 route handler 而不能放 client？——code + client_secret 是敏感凭据：client_secret 进 client bundle = 任何人可冒充应用换 token；「机密操作在 server」是 OAuth 的基础安全模型（PKCE 是 client 场景的替代——无 secret 但仍需 server 配合）——边界划分（RBL-803）在 OAuth 上的具体化：code 换 token 的往返必须在 server 侧。

```typescript
// 发起：route handler
// app/api/auth/login/route.ts
export async function GET() {
  const state = crypto.randomUUID();
  const res = NextResponse.redirect(
    `https://provider.com/oauth?client_id=${CLIENT_ID}&state=${state}&redirect_uri=${CALLBACK}`);
  res.cookies.set('oauth_state', state, { httpOnly: true, maxAge: 600, sameSite: 'lax' });
  return res;
}
// 回调
export async function GET(req: Request) {
  const url = new URL(req.url);
  const state = url.searchParams.get('state');
  const cookieState = req.headers.get('cookie')?.match(/oauth_state=([^;]+)/)?.[1];
  if (state !== cookieState) return new Response('CSRF', { status: 403 });   // state 比对
  const code = url.searchParams.get('code');
  const tokens = await exchangeCode(code);               // server 侧换 token（secret 在 server）
  const session = await createSession(tokens);           // session 表 + set-cookie
  return NextResponse.redirect('/app');
}
```
