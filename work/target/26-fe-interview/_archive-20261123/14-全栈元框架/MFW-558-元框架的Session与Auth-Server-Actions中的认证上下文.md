---
title: [MFW-558] 元框架 Session 与 Auth：Server Components 的认证上下文
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-558：Session 与 Auth：认证上下文

**答**:
- RSC 的认证模式：1) **middleware 粗校验**（session cookie 存在性——重定向登录 RBL-514）；2) **细校验在数据层**（repo/session RBL-554）；3) **Session 存储**：JWT cookie（无状态——签名校验每次）vs session 表（有状态——DB 查询/可吊销）；serverless 的 session 读取（每次请求查 DB——连接成本/RBL-517 KV 缓存 session）。
- cookies() 的语义：动态 API（访问即动态化路由 RBL-510）；读 cookie → 路由动态；「设置 cookie」只能在 Server Action/Route Handler（RSC 渲染期不能 set-cookie——响应头已开始发送 RBL-505 流式约束）。
- Action 里的 auth 上下文：cookies() 读 → session 校验（每个 action 显式——或封装 withAuth 高阶 action）；「权限校验的下沉」（repo 层自动 RBL-554 vs action 显式——分层防御）。
- 追问钩子：为什么「RSC 渲染期不能 set-cookie」是流式架构的必然约束？——RSC 响应是流式的（头先发 body 后流——cookie 属于响应头）；渲染开始 = 头已发 = 头不可改；「副作用的位置约束」：set-cookie 必须在头发送前 = Action/Route Handler（有独立响应头周期）——流式架构把「响应头的可变性」收敛到头周期内，副作用 API 的位置由流的时序决定（RBL-505 背压时序的 API 面）。

```typescript
// Session 三层校验
// middleware.ts：粗校验（存在性）
export function middleware(req) {
  if (!req.cookies.has('session') && req.nextUrl.pathname.startsWith('/app'))
    return NextResponse.redirect('/login');
}
// 数据层：细校验（RBL-554 repo）
export async function getSession() {
  const sid = (await cookies()).get('session')?.value;
  if (!sid) return null;
  const session = await kv.get(`session:${sid}`);        // Edge KV：无 DB 直连
  return session;
}
// Server Action：显式 + 封装
async function withAuth<T>(fn: (session: Session) => Promise<T>): Promise<T> {
  const session = await getSession();
  if (!session) throw new AuthError();
  return fn(session);
}
'use server';
export const updateProfile = (data) => withAuth(async (s) => {
  await db.users.update(s.userId, data);                 // 细粒度权限在 repo
});
```
