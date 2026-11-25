---
title: [DP-482] 笔试：手写洋葱模型 compose
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-482：笔试：手写洋葱 compose

**答**：实现 Koa 风格的 compose：① `(ctx, next)` 签名的中间件数组 → 洋葱执行（进入顺序 A→B→C，回程 C→B→A）；② next() 多次调用的防护（i 指针检查——同一中间件重复调 next 抛错）；③ 异步支持（Promise 链——await next() 等待内层完成）；④ 空管道与单中间件的边界；⑤ 错误传播（内层抛错 → 外层 catch 可捕获——错误沿洋葱上浮）。写出实现与一个「请求打点」中间件示例。

```javascript
function compose(middlewares) {
  if (!Array.isArray(middlewares)) throw new TypeError('middlewares must be array');
  for (const mw of middlewares) if (typeof mw !== 'function') throw new TypeError('middleware must be function');
  return function (ctx, next) {
    let i = -1;
    function dispatch(j) {
      if (j <= i) throw new Error('next() called multiple times');   // 指针防护
      i = j;
      let fn = middlewares[j];
      if (j === middlewares.length) fn = next;      // 末尾: 交给外部 next
      if (!fn) return Promise.resolve();            // 空管道
      try {
        return Promise.resolve(fn(ctx, () => dispatch(j + 1)));
      } catch (e) { return Promise.reject(e); }     // 同步异常转 rejected
    }
    return dispatch(0);
  };
}
// 打点中间件:
const logger = async (ctx, next) => {
  const t0 = Date.now();
  await next();                                     // 内层完成后
  ctx.log(`${ctx.url} 耗时 ${Date.now() - t0}ms`);  // 回程打点 — 洋葱后半程
};
```

**评分点**：
- i 指针防 next 重复调用（Koa 经典 bug 防护）
- 同步异常转 Promise.reject（统一异步语义）
- 末尾 dispatch 接外部 next（可组合）
- 洋葱回程语义的示例证明（next 后打点）
