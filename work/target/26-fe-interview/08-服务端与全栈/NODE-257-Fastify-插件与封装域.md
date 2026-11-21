---
title: [NODE-257] Fastify 插件与封装域？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-257：Fastify 插件与封装域？
**答**:
- 封装域（encapsulation）：fastify.register 创建子域——子域的 decorate/hook 只影响子路由树；父域不可见子域（快照隔离）。
- fastify-plugin：包装插件跳过封装（共享上下文）——装饰需要全局可见时用（如全局 db 装饰器）。
- 装饰器：fastify.decorate('db', pool) 全局；子域 decorate 仅子域——设计上防止全局污染。
- 插件加载顺序：register 是异步的且按域分层——依赖顺序用 await register 或 build 函数式组装。

```javascript
// 封装域示例
import fp from 'fastify-plugin';
// 全局插件（跳过封装）
const dbPlugin = fp(async (app) => { app.decorate('db', new Pool()); }, { name: 'db' });
await app.register(dbPlugin);
// 域内插件（只影响 /admin 路由）
await app.register(async function adminScope(app) {
  app.addHook('onRequest', adminAuth);          // 只对 /admin 生效
  app.decorate('audit', new Auditor());         // 只在 admin 域可见
  app.get('/admin/users', async (req) => app.audit.log(req.user));
}, { prefix: '/admin' });
// 全局拿不到 app.audit —— 封装隔离
```
