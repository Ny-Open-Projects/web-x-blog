---
title: [MFW-100] 笔试：手写一个 SvelteKit 登录（form action + session cookie）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-100：笔试：手写一个 SvelteKit 登录（form action + session cookie）
**答**：实现 `/login` 页面的登录链路：① `+page.server.js` 的 login action 校验账密；② 成功后发 httpOnly session cookie 并 redirect 到原页；③ 失败 fail 返回错误信息；④ `hooks.server.js` 里解析 cookie 注入 `locals.user`；⑤ 登录页未登录可访问、其他页未登录跳登录。

```js
// src/routes/login/+page.server.js
import { fail, redirect } from '@sveltejs/kit';
import { v4 as uuid } from 'uuid';

export const actions = {
  async login({ request, cookies, url }) {
    const form = await request.formData();
    const email = String(form.get('email') ?? '');
    const password = String(form.get('password') ?? '');

    if (!email || !password) {
      return fail(400, { errors: { form: '请填写完整' }, email });
    }
    const user = await verifyUser(email, password); // 内部含慢哈希比对
    if (!user) {
      return fail(401, { errors: { form: '账号或密码错误' }, email });
    }

    const sessionId = uuid();
    await db.session.create({ data: { id: sessionId, userId: user.id, expiresAt: addDays(new Date(), 7) } });
    cookies.set('session', sessionId, {
      path: '/',
      httpOnly: true,          // 防 JS 读取，防 XSS 窃取
      sameSite: 'lax',         // 防 CSRF 基线
      secure: true,            // 仅 HTTPS
      maxAge: 60 * 60 * 24 * 7,
    });
    redirect(303, url.searchParams.get('redirect') ?? '/'); // 303 防表单重提交
  },
};
```

```js
// src/hooks.server.js —— 每请求解析 session
export const handle = async ({ event, resolve }) => {
  const sid = event.cookies.get('session');
  event.locals.user = sid
    ? await db.session.findUnique({ where: { id: sid }, include: { user: true } })?.user ?? null
    : null;
  return resolve(event);
};

// src/routes/+layout.server.js —— 数据侧透出
export const load = async ({ locals }) => ({ user: locals.user });
```

```js
// src/routes/+layout.js —— 全局路由守卫
export async function load({ url, parent }) {
  const { user } = await parent();
  const PUBLIC = ['/login', '/register'];
  if (!user && !PUBLIC.includes(url.pathname)) {
    redirect(302, `/login?redirect=${encodeURIComponent(url.pathname)}`);
  }
}
```

**评分点**：
1. cookie 三件套齐全（httpOnly/sameSite/secure）并能说出各自防什么。
2. 成功 redirect 用 303 而非 302（POST 后重定向语义 + 防重提交）。
3. session 校验在 hooks.server.js 每请求执行，locals.user 贯穿 action/load。
4. fail(401) 返回结构化错误，登录页可回显且不丢已输入的 email。
5. redirect 参数有白名单/校验意识更佳（防开放重定向）。
