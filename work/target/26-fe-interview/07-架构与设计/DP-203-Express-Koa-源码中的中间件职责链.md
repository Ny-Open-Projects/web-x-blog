---
title: [DP-203] 源码识别：Express/Koa 源码中的中间件职责链？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-203：源码识别：Express/Koa 源码中的中间件职责链？
**答**：
- Express：回调式职责链——next() 显式移交，中间件按注册顺序线性执行；错误中间件 (err, req, res, next) 是链尾的错误分支。
- Koa：async 职责链（洋葱模型）——compose 把中间件数组折成嵌套 Promise，await next() 前后各是"进入/离开"切面，天然支持后置逻辑（计时、响应头）。
- 源码核心就是 compose 的递归 dispatch：`dispatch(i) = Promise.resolve(fn(ctx, () => dispatch(i+1)))`——面试能默写就赢了。
- 识别要点：Express 链是"接力棒"（单向不回头），Koa 链是"洋葱"（双向穿透），对应职责链的两种形态。

```javascript
// Koa compose 源码级简化
function compose(middleware) {
  return function (ctx) {
    let index = -1;
    return dispatch(0);
    function dispatch(i) {
      if (i <= index) return Promise.reject(new Error('next() called multiple times')); // 防重复 next
      index = i;
      const fn = middleware[i];
      if (!fn) return Promise.resolve();
      return Promise.resolve(fn(ctx, () => dispatch(i + 1)));   // 洋葱：进入 → 递归 → 离开
    }
  };
}
// Express 对比：app.use((req, res, next) => { /* 前置 */ next(); /* 只有同步返回后，无法拦截响应 */ });
// Koa 洋葱的后置能力：
app.use(async (ctx, next) => {
  const start = Date.now();
  await next();                                        // 下游执行完才走这里
  ctx.set('X-Response-Time', `${Date.now() - start}ms`);  // 后置切面
});
```
