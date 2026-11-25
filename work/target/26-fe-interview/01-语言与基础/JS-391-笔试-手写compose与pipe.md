---
title: [JS-391] 笔试：手写 compose / pipe（含异步支持）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 语言基础]
type: 笔试题
---

## JS-391：笔试：手写 compose / pipe

**答**：实现：① `compose(...fns)`：从右向左执行（f(g(h(x)))）；② `pipe(...fns)`：从左向右；③ 两者都支持异步函数（任一环节返回 Promise 则整个链 Promise 化）；④ `composeWith(dispatch)`：中间件式（Koa 洋葱模型），next() 传递。写出实现。

```javascript
function compose(...fns) {
  if (!fns.length) throw new TypeError('compose requires at least one fn');
  return (x) => fns.reduceRight((acc, fn) => acc.then(fn), Promise.resolve(x));
  // 统一 Promise 化: 同步函数被 then 包装后仍是正确值, 且异步自动支持
}

function pipe(...fns) {
  return (x) => fns.reduce((acc, fn) => acc.then(fn), Promise.resolve(x));
}

// 洋葱模型 (Koa)
function composeMiddleware(mws) {
  return (ctx) => {
    let i = -1;
    function dispatch(j) {
      if (j <= i) return Promise.reject(new Error('next() called multiple times'));
      i = j;
      const mw = mws[j];
      if (!mw) return Promise.resolve();
      return Promise.resolve(mw(ctx, () => dispatch(j + 1)));
    }
    return dispatch(0);
  };
}

// 用法
const process = pipe(
  (s) => s.trim(),
  async (s) => (await fetch(`/api/q?s=${s}`)).json(),
  (d) => d.items,
);
```

**评分点**：
- reduce/reduceRight + Promise.resolve 统一异步支持的技巧
- compose 右结合方向正确（易错点）
- 洋葱模型的 i 指针防 next() 重复调用（Koa 经典）
- 空函数列表抛错的防御
