---
disableNunjucks: true
title: 12-13 使用 egg-session 实现用户验证功能
date: 2026-11-17 15:27:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课介绍了 Cookie 的机制，这节课来了解会话 Session 以及它在 egg.js 中的实现。虽然项目最终不会采用这种方式做身份验证，但必须理解它的运作机制。

## Session 是概念而非技术

首先要明确：Session 只是一个概念，翻译过来就是"会话"，指在 HTTP 协议中保持用户状态的一种实现机制。它不是某种特定的技术方案，很多方案都能实现 Session，而且它们一般都基于上节课讲的 Cookie 来完成。egg.js 框架内置了 session 插件，可以非常方便地实现对应功能，插件内部使用的是基于 koa 的 koa-session 中间件。

## 写入与校验

要实现的功能和上节课类似：登录（login by email）后把 Session 种下去，在 show 接口里检查 Session 是否存在，存在就返回数据，不存在就返回未登录的错误。

egg.js 在 ctx 上提供了一个特殊属性 `ctx.session`，可以给它设置任意的 key。比如设置 `ctx.session.username = user.username`，Session 就写好了。

接着在受保护的接口里做判断，这里用 show 做实验。第一步从 `ctx.session.username` 把值取出来，然后做 if/else 判断：如果没有 username，说明用户没有登录，往 errors 里添加一个错误类型 `login_validate_fail`（登录验证失败），然后 return `ctx.helper.error`，error type 传刚才添加的 login_validate_fail；如果没问题，就直接返回 success 和对应的 username。

## 测试

在 Postman 里测试，记得先把旧 Cookie 清掉，避免历史请求干扰。用正确的 username 和 password 登录，发送请求后观察响应：服务端种下了一个 Cookie，名字是 `egg_session`（ESSION.SIG 之类的显示其实是 egg_session 及其签名），值是一段经过加密的字符串。这个加密的内部原理下节课通过源码解读，这里只要记住它指代保存的对象即可。Domain、Path、HttpOnly、Secure 都是 Cookie 的默认值，只有 Expires 做了特别设置，有一个默认的过期时间。

拿到这个 Cookie 之后访问 `users/current` 测试接口，请求自动带上了 egg_session 那串加密字符串，后端解密校验通过，确认 Session 没问题，返回正确的数据。然后把 Cookie 删掉再发一次，就能看到错误：error number 101004，登录校验失败，正是刚才写的错误信息。不加 Cookie 时验证逻辑同样工作正常。

Session 还有一系列配置，文档描述得很清楚：除了 key 之外，其余参数和 Cookie 的配置完全一致。key 代表存储 Session 的 Cookie 键值对叫什么名字。

## 网上流传的 Session 模型

既然用起来这么简单，那它的工作原理是什么？翻看网上大多数资料（包括很多对 koa-session 的源码解读），基本都会给你这样一个模型，很多 Java、PHP 实现也确实基于它：

1. 用户登录，向 login 接口 POST username 和 password；
2. 服务端查库比对，正确就返回数据（比如 username 以及一堆其他字段）；
3. 在内部存储或外部存储里创建一个 key-value 结构：key 是随机字符串（比如 xyz123），value 是要保存的数据。存哪里都行，内存、MySQL、Redis 缓存都可以；
4. 响应时返回 `Set-Cookie`，把这个 key 以 `sid=xyz123` 的形式带回客户端；
5. 第二次请求带着这个 Cookie 访问，服务端查询 Session 数据结构里是否有对应的 SID。有，就判定为登录用户，返回数据；没有或 Cookie 根本不存在，就返回未登录错误。

按这个模型，egg.js 默认的 Session 应该存放在某个特殊数据结构里，直觉上一般是内存。

## 验证：不是内存模型

可以这样验证：先重新登录种下 Cookie，再请求一次确认有数据。然后关闭服务器并重启。如果模型成立，重启会把内存里的数据结构抹掉，Session 登录态应该失效，再访问 `users/current` 应该返回未登录。

实际测试的结果是：重启之后访问该接口，依然能返回正确的 data。说明 egg.js 的 session（底层的 koa-session）并没有采用这种传统模型。那它究竟是怎么实现的？下节课一起解读 koa-session 中间件的源码，看看它到底用什么方式实现 Session。
