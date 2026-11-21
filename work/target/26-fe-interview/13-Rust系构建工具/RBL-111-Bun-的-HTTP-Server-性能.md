---
title: [RBL-111] Bun 内置 HTTP server 为什么快？与 Node 的差异？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-111：Bun 内置 HTTP server 为什么快？与 Node 的差异？
**答**：
- Bun.serve 直接在 Zig 层处理 TCP/HTTP 解析，请求对象零拷贝（无 JS 对象逐字段构造的中间层），框架层（express 那种抽象）可完全绕过。
- 对比 Node http：Node 的 ServerResponse/IncomingMessage 构建有 JS 层开销；Bun 的 Request/Response 遵循 Web 标准 API（fetch 形态），实现更薄。
- 数据量级：官方基准 hello world 场景 Bun 每秒请求数可达 Node 数倍；但真实业务瓶颈多在业务逻辑与数据库，差距会被稀释。
- 生态差异：Node 生态有 express/fastify 等成熟框架与中间件；Bun 原生风格更像 worker/fetch handler（Hono 等轻框架适配好）。
- 适用：边缘函数风格 API、高吞吐简单路由；复杂中间件生态依赖的项目留在 Node。
- 追问钩子：Web 标准 API（fetch/Request/Response/streams）成为运行时公共契约，是跨运行时代码可移植性的关键。

```typescript
// bun server.ts —— 无框架直接跑
Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);
    if (url.pathname === '/api/user') {
      const user = await db.query('select * from users limit 1');
      return Response.json(user);   // Web 标准 Response
    }
    return new Response('404', { status: 404 });
  },
});
```
