---
disableNunjucks: true
title: 10-13 Service 发送 HTTP 请求获取信息
date: 2026-11-17 13:35:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们学习了 Postman 的用法，现在有了犀利的调试工具。这节课言归正传，继续了解 Egg 的基础知识。之前讲了 Router、Controller，Egg 当中还有一个很重要的概念，叫 Service。

Service 不是必须的，你所有的逻辑都可以一股脑地写在 Controller 当中。但当逻辑变得越来越复杂时，势必会造成代码的重复和臃肿，这时候就需要 Service 出来救场了。文档中写明了为什么要使用它：第一，让 controller 中的逻辑更加简洁；第二，保持业务逻辑的独立性，抽象出来的 Service 可以被多个 controller 重复调用；第三，可以将逻辑和展现分离，降低耦合，在 controller 里面编写测试用例也会更加容易。

使用场景有两个。第一个是复杂数据的处理：你要展现的信息有可能需要先从数据库获取，经过一系列规则计算，最后才返回给用户显示。第二个是第三方服务的调用：请求其他第三方的 API，拿到数据后再返回出去。

了解了用途，来一个特殊的需求模拟一下它的用法。我找了一个开源的显示狗图片的 API，就是之前学习 Vue 时用过的 Dog API。现在希望应用中有一个特定的路由，可以返回狗图片的地址。这属于典型的第二个应用场景。API 的 URL 是 breeds/image/random，它会返回 message 和 status 两个信息，我们需要这个数据。

自然要在 service 当中先添加一个文件，这里称之为 dog.ts。有了它以后，首先把基类拿出来，很自然它也在 egg 当中，已经帮你封装好了，叫 Service。我们还需要一个特殊的库在框架内部发送 HTTP 请求。前端我们多次使用了 Axios，它是一个多端通用的工具。Egg 内部其实也封装了一个特殊的方法用来发送 HTTP 请求，文档里叫 HttpClient：这是框架基于 urllib 实现的内置 HTTP client，可以非常便捷地完成任何 HTTP 请求。它有两种访问方式：第一种在 app 上面，app.httpclient 和 app.curl；第二种通过万金油 ctx 也可以拿到，ctx.curl 和 ctx.httpclient。这里我们只发送一个简单的 HTTP GET 请求，想了解更多高级用法可以参看文档，后面我们对这部分知识也会有所涉猎。

开始完成任务。首先 export default class DogService，继承我们导入的基类 Service。创建一个 async 方法，称之为 show。和 Controller 一样，继承了基类后，this 上面也会获得 egg 的几大金刚：this.app、this.ctx、this.config，还有 this.service。我们使用内置在 ctx 上的方法，写 `const response = await this.ctx.curl(url)`。curl 已经存在，有了它就可以轻松发送请求。它有两个参数：第一个是 URL，把地址复制过来；第二个是一系列的 options，决定了发送请求的一些特性。method 不用管，默认是 get。有一项要特别注意，叫 dataType，它决定返回的是什么类型：什么都不加的话返回的是 buffer 类型，我们希望直接返回 JSON，所以写 `dataType: 'json'`。这样就可以成功返回了。

有了数据后直接把它返回出去：`return response`。注意这个 response 不是直接拿到的请求数据，而是又封装了一层，上面有 headers、res 和 status，其中的 data 才是真正需要的数据。这样 Service 就写完了。

有了 Service，就可以在 controller 里进行调用。回到 TestController，添加一个 async 方法叫 getDog。先提取出 ctx，然后 `const response = await service.dog.show()`，方法名都可以自动补全，这时就拿到了对应的 response。有一件事让我不爽：这个 response 没有对应的类型，直接是 any。我希望它获得正确的类型。使用 Axios 时也提过，它肯定会提供一个泛型，可以传入最终返回的类型，curl 也是如此。添加一个 interface 叫 DogResponse，返回有两项：message 是 string 类型，status 也是 string 类型。把 DogResponse 传递到 curl 的泛型当中，response 就能成功获得 DogResponse 这个类型，很方便。

接下来直接返回：`ctx.body = response.message`，也就是图片的地址；status 设置一下，等于 200。Service 和对应的 controller 都写完了，最后添加一个对应的 router：get 方法，URL 写 dog，最后一个参数是对应的 controller，`controller.test.getDog`。来测试最终结果：访问 localhost 的 7001/dog，能看到它成功返回了图片的地址，任务完成。

这节课我们完成了第一个 Service，并且体验到了 Service 的好处：假如有很多 controller 都需要相同的服务，比如获取狗狗图片的地址，它们直接调用这个 Service 就好了，不需要写重复的逻辑。
