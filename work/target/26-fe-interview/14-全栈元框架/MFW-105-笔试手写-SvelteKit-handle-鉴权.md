---
title: [MFW-105] 笔试：手写 SvelteKit 的 handle hook 完成请求级鉴权与审计
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-105：笔试：手写 SvelteKit 的 handle hook 完成请求级鉴权与审计
**答**：实现 `hooks.server.js`：① 解析 Bearer token（API 请求）与 session cookie（页面请求）两种身份源，统一注入 `locals.user`；② `/admin/**` 仅 admin 角色可过，否则 403；③ API 未鉴权返回 401 JSON；④ 记录审计日志（path、userId、耗时）；⑤ 全链路异常返回 500 且不泄漏内部信息。

```ts
// src/hooks.server.ts
import type { Handle } from '@sveltejs/kit';
import { json } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  const t0 = performance.now();
  event.locals.user = null;

  try {
    // 1. 双身份源
    const auth = event.request.headers.get('authorization');
    if (auth?.startsWith('Bearer ')) {
      // API 请求：JWT
      event.locals.user = await verifyJwt(auth.slice(7)); // 失败抛 -> 401
    } else {
      const sid = event.cookies.get('session');
      if (sid) event.locals.user = await getUserBySession(sid);
    }

    // 2. admin 区块
    if (event.url.pathname.startsWith('/admin') && event.locals.user?.role !== 'admin') {
      if (event.url.pathname.startsWith('/api/')) {
        return json({ error: 'forbidden' }, { status: 403 });
      }
      return new Response('Forbidden', { status: 403 });
    }

    // 3. API 未鉴权
    if (event.url.pathname.startsWith('/api/') && requiresAuth(event.url.pathname) && !event.locals.user) {
      return json({ error: 'unauthorized' }, { status: 401 });
    }

    const response = await resolve(event);

    // 4. 审计日志（异步，不阻塞响应）
    const dur = Math.round(performance.now() - t0);
    logAudit({ path: event.url.pathname, userId: event.locals.user?.id, status: response.status, ms: dur })
      .catch(() => {});

    return response;
  } catch (err) {
    // 5. 统一 500：上报但只回脱敏信息
    apm.captureException(err);
    return json({ error: 'internal_error' }, { status: 500 });
  }
};

function requiresAuth(path: string): boolean {
  return !['/api/public', '/api/login', '/api/health'].some((p) => path.startsWith(p));
}
```

**评分点**：
1. 双身份源判断顺序正确（Bearer 优先），两种来源最终统一进 locals.user。
2. admin 校验在 resolve 之前短路，区分 API（JSON 403）与页面（HTML 403）。
3. 审计日志异步发送，不阻塞主链路——阻塞是常见扣分点。
4. catch 兜底返回脱敏 500，且内部堆栈只进 APM 不进响应。
5. requiresAuth 有公开路径白名单意识。
