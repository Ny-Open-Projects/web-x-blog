---
disableNunjucks: true
title: 12-14 koa session 源代码分析第一部分
date: 2026-11-17 16:28:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课开始解读 koa-session 的源码。这是一个比较复杂的源码解读项目，这里深入浅出地解释几个关键部分，即便简化后也要分两节课完成。

## 带着问题读源码

读源码的方法是"带着问题找答案"。从上节课的使用来看，操作 Session 无非两步：一是从 `ctx.session` 上获取属性，二是给 `ctx.session` 的属性赋值，通过这两个途径完成 Session 的获取和设置。

由此可以推测两点实现思路：第一，需要扩充 context 对象，往上添加一个 session 属性；第二，每次请求过程中都要拿到对应的 Session 值，所以应该有一个中间件，在每次请求时从某个存储取得值，复制到一个特殊变量上供用户使用。koa-session 的整个中间件就是围绕这两个任务展开的。

## 入口：index.js

把源码 clone 下来，入口文件是 index.js。它导出一个 function，前面的参数初始化、限制判断之类的代码与主逻辑无关，跳过。能看到两个关键点：一是扩充 context 对象的那一行，完成"在 context 上扩展 session 属性"这个目的；二是返回一个真正的中间件函数，里面做了一系列处理。

先搞清楚 context 扩展的逻辑，跳转到对应代码。这里有一个熟悉的方法 `Object.defineProperty`，作用对象是 context，要定义的属性就是 session，因为我们平时就是用 `ctx.session` 赋值取值的。扩展时使用了 getter 和 setter。这节课的任务是看"设置"如何完成，也就是调用 `ctx.session = xxx` 时触发的 setter；获取（getter）留到下节课。

## Symbol 与 ContextSession

setter 里调用的是 `this[CONTEXT_SESSION].set(...)`，所以要弄清 CONTEXT_SESSION 是什么。往上看定义，它是一个 Symbol。之前扩展 egg 对象时用过 Symbol：Symbol 可以看成对象上的一个 key，比字符串强的地方是每个都独一无二。把它理解为对象上的一个特殊属性名即可。

于是 setter 的逻辑可以还原为：先判断下方一个带下划线的属性（`_CONTEXT_SESSION`）是否存在，存在就直接 return；不存在就实例化 ContextSession 类，把返回的对象赋给它，最后返回出去。所以 `ctx.session` 背后的实体就是 ContextSession 的实例，调用 `ctx.session = ...` 实际是调用这个实例上的 set 方法。

## set 与 create

ContextSession 是另一个文件，整体是一个大的 class，其他属性不管，直奔 set 方法。set 的逻辑很短：先判断 val 是否等于 null（我们的场景不是），然后判断 `typeof val === 'object'`，我们写的 `ctx.session = { username: 'viking' }` 是对象，条件为 true，于是调用 `this.create(val, this.externalKey)`。

顺着 set 进入 create 方法。刨去 debug 和参数判断这些附加逻辑，核心是 `this.session = new Session(this, val)`：把值传递给另一个类。源码里有两个类，一个是 ContextSession，另一个就是 session.js 里的 Session。

直接看 Session 的 constructor，它就是一个平实的对象：设置一系列前面带下划线的私有属性，把 sessionCtx 赋给内部属性，保存 ctx 和 externalKey，然后对传入的 object 做 for-in 一一赋值（中间有两个针对特殊情况的判断，不影响主线）。

到这里路线图走完了：`this.session` 等于 Session 实例化的结果，包含 username=viking 这些业务字段，以及若干私有属性。赋值本身完成了。

## 保存：commit 与 save

但 Session 需要保存。回到最上面的中间件，看它怎么发挥作用。中间件 async function 里第一步获取当前的 session store（就是刚才分析过的 ContextSession 实例）；第二步是外部存储的初始化判断，与取值相关，下节课再看；然后 try 执行后续逻辑。特别注意这里有一个 finally：如果 options.autoCommit 等于 true（默认就是 true，看源码可确认），就执行 `await session.commit()`。

commit 顾名思义和保存有关。跳到 commit 方法，前面一堆判断跳过，最终调用的是 `this.save`。save 里先取了一些值，然后调用 `this.session.toJSON()`，把 Session 实例转成 JSON。toJSON 的实现很简单：做一次 forEach，过滤掉不需要的属性（比如带下划线的私有属性、isNew 之类），剩下的逐项返回，最后返回一个 JSON 字符串。

接着是一系列判断，同样略过。重点看外部存储相关逻辑之前的默认路径：`json = opts.encode(json)`，对 JSON 做 encode，默认实现就是 Base64。也就是说，最初设置的数据经过 Base64 编码后得到一个字符串，最终通过 `this.ctx.cookies.set(key, json)` 写出去。其实就是把这个值通过 Set-Cookie 响应头保存在客户端。

再注意一点：因为上节课讲过 ctx.cookies 有 encrypt 加签能力，所以最终返回的不是明面上的 Base64，而是经过加密处理的结果，安全地存进了 Cookie。

## 结论

至此 set 流程完毕：每次 `ctx.session = 某个值` 时，经过一系列逻辑，最终是发送一个 Set-Cookie 响应头，把保存的值先 Base64 再加密，写到客户端。它默认并没有采用内存存储或第三方存储，而是直接把值保存进 Cookie 本身。这也就解释了上节课"重启服务器登录态依然有效"的现象。

koa-session 源码解析第一部分到这里，赋值流程已经搞清楚了，下节课看取值是怎么完成的。
