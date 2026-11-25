---
title: [RBL-124] 笔试：手写 Bun 版开发代理 server（转发 + 跨域头）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-124：笔试：手写 Bun 版开发代理 server（转发 + 跨域头）
**答**：用 Bun.serve 实现 dev proxy：1) /api/* 请求转发到 http://localhost:8080（保留方法/头/体）；2) 响应注入 CORS 头；3) 非 /api 路径返回静态文件（dist 目录）；4) 上游失败返回 502 且带错误信息；5) 支持 rewrite 规则（/api/user → /users）。

```typescript
const UPSTREAM = 'http://localhost:8080';
const REWRITE: Record<string, string> = { '/api/user': '/users' };

Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);

    // 1) API 代理
    if (url.pathname.startsWith('/api/')) {
      const rewritten = REWRITE[url.pathname] ?? url.pathname.replace(/^\/api/, '');
      const target = `${UPSTREAM}${rewritten}${url.search}`;
      try {
        const res = await fetch(target, {
          method: req.method,
          headers: req.headers,
          body: ['GET', 'HEAD'].includes(req.method) ? undefined : await req.arrayBuffer(),
        });
        // 2) CORS 注入
        const headers = new Headers(res.headers);
        headers.set('access-control-allow-origin', '*');
        return new Response(res.body, { status: res.status, headers });
      } catch (e) {
        return new Response(JSON.stringify({ error: 'upstream failed', detail: String(e) }),
          { status: 502, headers: { 'content-type': 'application/json' } });
      }
    }

    // 3) 静态文件
    const file = Bun.file(`./dist${url.pathname}`);
    return await file.exists() ? new Response(file) : new Response('404', { status: 404 });
  },
});
```
**评分点**：
- 请求方法/头/体透传（GET/HEAD 无体的边界处理）。
- rewrite 与 query 保留。
- CORS 头注入用 Headers 构造（不破坏原头）。
- 上游失败 502 + 错误体（不裸崩）。
- 静态回退 + 404。
