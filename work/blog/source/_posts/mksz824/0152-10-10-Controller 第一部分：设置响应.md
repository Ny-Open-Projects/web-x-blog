---
disableNunjucks: true
title: 10-10 Controller 第一部分：设置响应
date: 2026-11-17 10:32:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课正式进入编码过程。第一个要了解的概念是 controller。编码前要先启动项目，因为类型文件是动态生成的，每次有文件修改时这些类型文件会被自动重新生成，给我们更好的 TypeScript 开发体验。现在来到文件夹下，点击 New File 创建一个新的 controller，名称可以称之为 test.ts。

之前说过，controller 负责解析用户的输入，处理后返回相应的结果。初步学习先演示这个过程，第一步只返回结果。从 egg 当中导入一个基类，叫 Controller。接着定义我们自己的类，export default 一个 class，名称叫 TestController，继承这个基类 Controller。这样的继承有一个好处：我们定义的 controller 类会在每一次请求访问到 server 时实例化一个对象，而 TestController 继承了 egg 的 Controller 之后，会在它的方法当中挂载几个属性到 this 上面。

我们创建第一个方法，称之为 index。使用 async 是 egg 的常规做法，这里可能还没有需要 await 的代码，但先这样写着。看挂载的几个属性：第一个是 this.ctx，ctx 是当前请求的上下文，它有很多的属性和方法，是 Context 上下文对象的一个实例。通过它可以拿到框架封装好的、处理当前请求的各种便捷的属性和方法。对 Koa 熟悉的同学应该对它特别亲切，它正是 Koa 的一大特色。在整个应用中，这个上下文对象会一直封装在应用内，供各个模块使用。

第二个是 this.app，也有一系列属性，它是当前应用 Application 对象的实例，通过它可以拿到框架提供的全局对象和方法。第三个是 this.service，看到它就很亲切了，这就是我们在 service 创建当中的一系列类、对象和方法。最后还有 config，是当前应用运行时的配置项。这四大模块是 Egg.js 的核心内容，大家可以认为是四大金刚。现在了解有这么个东西就可以，内部这四个对象的一系列属性和方法会在后面详细讲解。

现在的任务是让它直接返回。ctx 上面有一个 response 对象，代表一个 HTTP 请求的返回，它上面还有一个属性叫 body。写 `this.ctx.response.body = 'Hello World'`。不难发现 response 上面有大量属性：比如 this.ctx.response.status，status 是返回的状态码，和 HTTP code 一一对应，这里希望它返回 200。response 这个类型封装的是 Koa 的返回对象，所有属性可以看它的文档，有很多如 response header、socket、status 等等，可以自己去了解。

当然，每次写这么长的属性会有点不爽，这时可以用一个叫别名的特性：ctx 上面会提供一些快捷属性，可以直接访问 response 内部的属性。不想每次都写 this，可以把 ctx 提取出来。之后直接写 `ctx.body`，它和 response.body 完全等价，写起来比原来轻松很多；status 也一样，`ctx.status = 200`，这样写清爽很多。关于别名，其实也是对 Koa 的一个封装，详细的列表可以去看 response alias 文档，里面有一系列的别名，写起来更快捷。

第一个 controller 就写完了。现在讲它和路由的对应关系。来到 app 目录下面已经创建好的 router.ts 文件。打开后可以看到这个文件的写法是固定的：它是一个函数，函数内有一个参数叫 app，类型是 Application，就是 app.js 的一个内置类型，和 this.app 的类型完全一致，这里是有渊源的。通过这个 app，我们就能拿到框架提供的全局对象和方法。这里拿到 controller 和 router 两个实例，就可以添加路由了。

router 上面有一系列方法，方法名称很多和 HTTP verbs 相对应，比如 get、post、patch、delete。我们创建一个 get：第一个参数是 URL，这里称之为 test；第二个是对应的 controller 处理。有了 controller 的实例，直接写 `controller.test.index`。可以看到它非常便捷，会自动提示生成 controller 的名称和方法。进入 test 当中，有 index 这个方法，这样就完成了一个对应关系。

看一下程序运行的状况：访问 localhost 的 7001，注意是 test 这个路由，刷新后可以看到输出了刚才留下的 hello world 字符串。整个响应就设置完毕了。

这节课简单介绍了 controller 怎样设置响应，以及 controller 和 router 的对应方法。下节课学习在 controller 当中怎样拿到对应的请求，并做一些处理。
