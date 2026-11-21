---
title: [NODE-031] 中间件执行顺序题：写出下列 Koa 代码的输出并解释？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-031：中间件执行顺序题：写出下列 Koa 代码的输出并解释？
**答**：
- 规则：`await next()` 前是"进入"（按注册顺序），之后是"退出"（逆序）；**response 中间件应放在最后注册但最先看到 body**……实际规则是"注册顺序 = 前半段执行顺序"。
- 输出：`A1 B1 C1 C2 B2 A2`，body 为 `'C'`。高频变体：去掉中间 C 的 `await next()` → C 后面的 C2 仍执行（同一函数内），但 B2/A2 **不会执行吗？**——会执行！C 未调用 next 只是跳过了"C 内部之后"没有更内层；B2/A2 属于外层回溯，正常执行。但若 C 的 next 是 `next()` 未 await，则 C2 会在 B 之前抢先执行（顺序错乱）。

```javascript
const Koa = require('koa');
const app = new Koa();

app.use(async (ctx, next) => {
  console.log('A1'); await next(); console.log('A2');
});
app.use(async (ctx, next) => {
  console.log('B1'); await next(); console.log('B2');
});
app.use(async (ctx, next) => {
  console.log('C1'); ctx.body = 'C'; await next(); console.log('C2'); ctx.body = 'C2'; // 后写覆盖
});

app.listen(3000);
// 输出：A1 B1 C1 C2 B2 A2，最终 body 是 'C2'

// 变体 1：C 不调用 next() → 输出 A1 B1 C1 C2 B2 A2 仍相同（只是没有更内层），
//         但若 C 之后还有 D 中间件，D 永远不会执行。
// 变体 2：C 中 next() 不加 await → C1 后立即回溯 B2 A2，C2 最后执行（顺序倒挂）。
// 变体 3：B 抛异常 throw new Error() → C 系列不执行，错误沿 A 的 try/catch 冒泡。
```
