---
title: [NODE-110] Koa 的 ctx 属性代理是如何实现的（defineGetter 原理）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-110：Koa 的 ctx 属性代理是如何实现的（defineGetter 原理）？
**答**：
- `ctx.status` → `response.status`、`ctx.url` → `request.url`：本质是在 context 原型上 **defineProperty 委托**（Koa 源码用已废弃的 `__defineGetter__/__defineSetter__`，等价于 delegates 库）。
- 委托分三类：request 的只读委托（url/header/method）、response 的 getter+setter 双向委托（body/status/type）、以及 `ctx.request`/`ctx.response` 自身引用。
- 价值：业务代码 `ctx.body = data` 一行等价 `ctx.response.body = data`，读写心智统一。
- 面试追问点：为什么 body 必须 setter（写穿透到 response）、url 为什么只读（请求行不可变）。

```javascript
function delegate(proto, target, name) { // 双向委托：body/status 这类可写的
  Object.defineProperty(proto, name, {
    get() { return this[target][name]; },
    set(v) { this[target][name] = v; },
    configurable: true,
  });
}
function access(proto, target, name) {   // 只读委托：url/header 这类请求期不变的
  Object.defineProperty(proto, name, {
    get() { return this[target][name]; },
    configurable: true,
  });
}

const proto = {}; // 即 Koa context.js 导出的原型对象
access(proto, 'request', 'url');
access(proto, 'request', 'header');
delegate(proto, 'response', 'status');
delegate(proto, 'response', 'body');

// 验证：ctx.body 写入实际落到 ctx.response.body
const ctx = { __proto__: proto,
  request: { url: '/a?b=1', header: {} },
  response: { status: 200, body: undefined } };
ctx.body = { ok: 1 };
console.log(ctx.response.body, ctx.url); // { ok: 1 } '/a?b=1'
```
