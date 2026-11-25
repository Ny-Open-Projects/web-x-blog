---
title: [NODE-022] Express 的中间件模型是怎样的？与 Koa 有何本质区别？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-022：Express 的中间件模型是怎样的？与 Koa 有何本质区别？
**答**：
- Express 中间件是**线性模型**：`(req, res, next)`，通过 `next()` 把控制权交给下一个中间件；如果不调用 `next()` 且不结束响应，请求**悬挂**。
- 与 Koa 的本质区别：Express 中间件拿到的是同一个 `res` 对象直接操作（assign & end），**执行完不会"回来"**——`next()` 之后的代码虽会执行，但拿不到下游的"返回值"，响应状态由下游直接写死；Koa 用 `await next()` 真正形成洋葱（后半个洋葱圈在响应前执行）。
- Express 4 错误中间件必须 `(err, req, res, next)` 四参数签名，且要 `next(err)` 显式传递；异步路由的 Promise reject 在 Express 4 中**不会被捕获**（Express 5 已支持自动捕获），必须 `try/catch` 或 `next(err)`。

```javascript
const express = require('express');
const app = express();

// 线性模型：next() 只进不回
app.use((req, res, next) => {
  console.log('A 进入');
  next();                          // 交给下游
  console.log('A 退出');           // 会执行，但此时响应可能已被下游结束
});

app.use((req, res, next) => {
  console.log('B 进入');
  if (req.path === '/sync-error') throw new Error('sync');       // 同步错误 → 错误中间件
  if (req.path === '/async-error') return Promise.reject(new Error('async')); // Express 4 中不会被捕获！
  res.json({ ok: true });
});

// 错误中间件：必须 4 个参数
app.use((err, req, res, next) => {
  console.error('error middleware:', err.message);
  res.status(500).json({ code: 500, message: err.message });
});

app.listen(3000);
// Express 5 中 async 自动捕获；Express 4 的正确写法：
// app.get('/x', async (req, res, next) => { try { await work(); res.json({}) } catch (e) { next(e) } })
```
