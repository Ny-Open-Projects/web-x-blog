---
title: [MFW-138] 笔试：手写路由守卫（loader 重定向 + 权限矩阵）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-138：笔试：手写路由守卫（loader 重定向 + 权限矩阵）
**答**：实现可复用的守卫工具 `requireUser(options)` 与 `requireRole(roles)`，供 RRv7 loader 使用：① 未登录 redirect 到 /login 并带 returnTo；② 已登录但角色不符抛 403 Response；③ 支持从 session/Authorization 双来源解析；④ returnTo 有开放重定向防护（只允许站内相对路径）；⑤ 提供 loader 装饰器 `withGuard(loader, guard)` 组合。

```ts
import { redirect } from 'react-router';

type User = { id: string; role: 'user' | 'admin' } | null;

async function resolveUser(request: Request): Promise<User> {
  const auth = request.headers.get('authorization');
  if (auth?.startsWith('Bearer ')) return verifyJwt(auth.slice(7)); // API 场景
  const cookie = request.headers.get('cookie') ?? '';
  const sid = /(?:^|;\s*)session=([^;]+)/.exec(cookie)?.[1];
  return sid ? getSessionUser(sid) : null;
}

// 站内相对路径校验：防 //evil.com 与 /\evil.com 协议相对跳转
function safeReturnTo(raw: string | null): string {
  if (!raw || !raw.startsWith('/') || raw.startsWith('//') || raw.includes('\\')) return '/';
  return raw;
}

export async function requireUser(request: Request): Promise<User> {
  const user = await resolveUser(request);
  if (!user) {
    const url = new URL(request.url);
    throw redirect(`/login?returnTo=${encodeURIComponent(safeReturnTo(url.pathname + url.search))}`);
  }
  return user;
}

export async function requireRole(request: Request, roles: Array<User extends null ? never : User['role']>): Promise<User> {
  const user = await requireUser(request);
  if (!roles.includes(user.role)) {
    throw new Response('Forbidden', { status: 403 }); // RRv7 ErrorBoundary 捕获
  }
  return user;
}

// 装饰器组合：guard 先跑，通过才执行原 loader
type Loader = (args: { request: Request; params: Record<string, string> }) => Promise<unknown>;

function withGuard(loader: Loader, guard: Loader): Loader {
  return async (args) => {
    await guard(args);      // 守卫：可能 throw redirect/Response
    return loader(args);    // 业务
  };
}

// —— 用法 ——
// export const loader = withGuard(
//   async ({ params }) => ({ data: await db.adminData(params.id) }),
//   ({ request }) => requireRole(request, ['admin']),
// );
```

**评分点**：
1. redirect 与 throw Response 的区分正确（401 跳登录、403 报错页）。
2. returnTo 开放重定向防护：拒绝 `//`、反斜杠、非相对路径——很多候选人会漏。
3. 双身份源（Bearer/cookie）解析顺序与容错。
4. withGuard 保证守卫先执行且异常向上传播，loader 不重复鉴权逻辑。
5. redirect 带 returnTo 便于登录后回跳。
