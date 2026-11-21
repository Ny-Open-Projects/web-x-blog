---
disableNunjucks: true
title: 17-3-4 JSON Server 实现 JWT 验证 - 实现路由保护
date: 2026-11-17 12:04:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

为了给 mock server 的不同路由添加权限管理，上节课讲解了 JSON Web Token 的基本原理并用代码实现了第一部分，生成 token。这节课完成第二部分：把 token 验证添加到对应的路由上。

先看场景。我在 `db.json` 里添加了 `works` 节点，mock server 会返回用户的作品，真实接口里也有对应的一个。这个路由需要权限保护，只有登录用户才能访问自己的作品。但现在它随便就返回数据了，这节课就来完成保护这个路由的过程。

## verifyToken 函数

mock-server 里现在有 `createToken`，自然要有对应的函数来解开它，叫 `verifyToken`，参数是要验证的 token 字符串：

```js
function verifyToken(token) {
  return jwt.verify(token, SECRET_KEY)
}
```

`jwt.verify` 是 JWT 提供的方法，第一个参数是 token，第二个是 secret key（和创建时用的同一个，复制过来即可）。

## 添加权限中间件

给 server 添加一个中间件，让它在正式处理路由逻辑之前验证权限：

```js
server.use('/works', (req, res, next) => { ... })
```

`server.use` 有两个参数：第一个是对应的路由，不添加就是对所有路由起作用；这里对特定路由 `/works` 起作用。真实的后端有很多接口需要验证，想把更多路由纳入权限管理，可以把 URL 写成正则等，添加多种 URL 的配置，这里演示就加一个。

第二个参数是回调函数，参数依次是 request、response 和 next。`next` 很关键：它是执行下一个处理的方法，验证通过后靠它放行。

先准备失败时的返回，和真实接口做到一模一样：

```js
const errorResponse = {
  errno: 12001,
  message: '登录校验失败',
}
```

## 中间件逻辑

我们的信息存在一个特定的 header 里，叫 `authorization`。从 request headers 上拿下来：

```js
const authHeader = req.headers.authorization
```

**第一种情况**：如果它等于 undefined，说明根本没传，直接返回错误并 return，return 让处理提前结束，路由不会再往下执行：

```js
if (authHeader === undefined) {
  res.jsonp(errorResponse)
  return
}
```

**第二种情况**：header 有值，用 try-catch 验证：

```js
try {
  const verifyTokenResult = verifyToken(authHeader.split(' ')[1])
  next()
} catch (error) {
  res.jsonp(errorResponse)
}
```

注意 authHeader 不能直接传入 verifyToken，我们用的是特殊格式的值：`Bearer` 加空格加一串 token。这是硬性规定（规范），所以要先用空格 `split`，取后面的部分 `[1]`。验证没问题就调用 `next` 进行下一步；如果验证过程抛出错误（token 是假的或已失效），catch 到后直接返回 errorResponse。

## 验证三种情况

访问 `localhost:3000/api/works`：

1. **不传 authorization**：点击 Send，直接返回「登录校验失败」，拿不到真正的数据；
2. **传正确的 token**：添加 authorization header（用之前生成的还没过期的 token），Send 后验证通过、调用 next 放行，返回正常数据，而且自定义的返回格式也保留着，data.list 里是对应的作品数据；
3. **传错误的 token**：把 token 删掉几位再 Send，同样返回「登录校验失败」，try 里抛出错误进入 catch，返回 errorResponse。

整个过程完成，mock server 的权限配置就绪。其实不知不觉中，我们实现了一个 JSON Web Token 的简单实现版本。通过这个实现，大家应该能更清楚它的原理：非常简单，主要是 `jwt.sign` 和 `jwt.verify` 这一对相对的过程。

到这里，我们已经能完全掌握使用 JSON Server 完成路由权限验证了。
