---
disableNunjucks: true
title: 12-16 egg session 使用外部存储器
date: 2026-11-17 08:30:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

经过源码解读，大家对 Session 的运作方式应该有了新的认识：它巧妙地把信息加密后存进 Cookie，再次访问时解密拿到用户信息，服务器上没有保存任何东西。这种方式刷新了我们对 Session 的常规印象，非常适合小型应用，可以用很低的成本解决持久化和横向扩展问题。

当然它也支持外部存储的形式。这节课就验证并使用外部存储来实现 Session 功能。这种情况下，Cookie 只会存储一个唯一的用户标识符，也就是源码里见过的 externalKey，再次访问时用这个 key 去外部存储里找对应的数据即可。

## 准备工作

编码从一个最简单的模型开始：内存中的存储。为了观测更清楚，先修改一个配置。在 config 的 session 选项里（它与 Cookie 选项共享）有一个 encrypt 选项，会对 Cookie 加密；这里设为 false，让 Cookie 直接返回真实值，方便观察。

下一步在 app 上建立内存存储模型，就是一个简单的 object。先在 index.d.ts 的 Application 里定义这个模型：`sessionMap: Record<string, any>`，初始为空对象。

外部存储器的写法在文档里有说明：设置 `app.sessionStore` 上面的一系列方法即可，比如 get、set、destroy。egg.js 没有为它添加对应的类型定义，所以这里仅作测试，手动用 as any 定义一下。

然后在 sessionStore 上实现三个 async 方法：

- `get(key, maxAge)`：从 `app.sessionMap` 里按 key 取出值并返回；
- `set(key, value, maxAge)`：在 `ctx.session = value` 赋值时被调用，实现就是 `app.sessionMap[key] = value`。测试时把 key 和 value 都打印出来，方便观察；
- `destroy(key)`：把 `app.sessionMap` 中对应的 key delete 掉。

这样，一个简单的内存存储器就实现了。

## 验证

`npm run dev` 启动应用，第一步设置 Session：清掉旧 Cookie，到 login 接口发送请求。由于去掉了 encrypt 加密，返回的 Cookie 都是普通值：key 是我们设置的 session 键名，值是一个 ID 字符串；同时因为默认 sign 为 true，还会伴随生成一个对应的 .sig 签名值，两者一起校验。

再看 console，set 方法被触发了，打印出来的 key 与 Cookie 里完全一致；value 则是上节课分析过的 Session 对象的 toJSON 返回值，除了我们设置的 username，还有 expire、maxAge 两个属性。也就是说，真正的内容储存在内存的 object 里，Cookie 只是把 key 暴露出去。

对照经典的 Session 模型图，这就是我们之前介绍的经典模型：key 存进内存，`sid=xyz123` 这样的标识符返回给客户端。

接下来访问需要权限的接口 get user。发送请求时自动带上刚才创建的 Cookie，可以成功拿到对应的值。此时 console 打印出一行新的 log，是 get 被触发的 key（那串 ID）。这就是服务端拿着 SID 去外部存储里查找，命中后返回对应的值。再次验证了经典模型：使用外部存储时，Session 完全按照经典模型运作。

## 重启测试

重启整个服务器会怎样？先关闭再重启，直接在 users/current 接口发送请求，这时报出错误：登录校验失败。原因是重启后内存中那个 key-value 的 map 已经丢失，对应关系没了，登录状态自然直接消失。这也再次印证了这个数据模型。

## 收尾

这节课验证了源码解读的结果：使用外部存储扩展了 Session 的实现，反过来见证了默认设计（cookie session）的巧妙之处。

留一个课下作业：使用 MongoDB（项目里已经接入了）完成 Session 存储，其实就是修改现有的几个方法，创建一个集合把这些信息存放进去。存入持久化数据库后，服务器挂了再重启，会话信息也不会丢失。

但要意识到：一旦选择把 Session 存入外部存储，就意味着系统强依赖这个外部存储，任何外部存储挂掉后，Session 相关的功能就完全不可用了。

这节课到这里。
