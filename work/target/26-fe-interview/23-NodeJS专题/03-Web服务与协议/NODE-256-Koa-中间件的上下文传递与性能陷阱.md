---
title: [NODE-256] Koa 中间件的上下文传递与性能陷阱？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-256：Koa 中间件的上下文传递与性能陷阱？
**答**:
- 上下文传递：ctx 上挂业务态（user/traceId/degradeFlags）——但 ctx 是每请求新建对象（NODE-251），字段挂多了有 V8 隐藏类开销；收敛到命名空间（ctx.state = {...}）或 Map。
- 全局变量陷阱：中间件里用模块级变量存请求态 → 并发互踩——跨异步边界用 AsyncLocalStorage（NODE-26x 详述）。
- 中间件顺序陷阱：bodyParser 在权限校验后 → 403 也解析 body（浪费）；耗时中间件放洋葱外层（后置统计准）。
- ctx 序列化成本：日志打印整个 ctx 会展开函数/循环引用——白名单字段输出。

```javascript
// AsyncLocalStorage 跨中间件传 trace
import { AsyncLocalStorage } from 'node:async_hooks';
const als = new AsyncLocalStorage();
app.use((ctx, next) => als.run({ traceId: ctx.get('x-trace-id') ?? newTrace() }, next));
// 任意深层函数（不含 ctx 引用）：
function dbQuery(sql) {
  const { traceId } = als.getStore();          // 上下文自动跟随异步链
  return db.query(sql, { traceId });
}
// 性能：ctx 上只挂 ctx.state.user / ctx.state.traceId；日志白名单：
log.info({ traceId: ctx.state.traceId, path: ctx.path, status: ctx.status }, 'req');
```
