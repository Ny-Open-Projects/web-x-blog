---
disableNunjucks: true
title: 12-10 使用 mongoose-sequence 插件完成 ID 自增
date: 2026-11-17 12:24:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

前几节课我们已经可以完成数据的加密、对比和隐藏。按说接下来应该是鉴权了：login 之后用什么方式验证用户的权限。但在鉴权开始之前，先要对数据库做一个简单的改造，并通过这个过程学习 mongoose 中的新内容：插件。

用过关系型数据库的同学都知道，比如 MySQL 有个特殊字段叫 auto increment。建表时一般给 ID 添加这个属性，用 auto increment 关键字执行对应任务：给每条新记录的 ID 自动递增，起始值是 1，这样就能通过不同的 ID 区分不同的数据。

Mongo 里我们之前学过，每创建一条记录时会使用一个随机的 ObjectID 类型的数据作为特殊标识符，还多次强调过它不是 string 类型，而是 MongoDB 自带的 ObjectID 类型。但这个随机字符串比较长，不好记忆和使用。所以现在想在 MongoDB 中也实现类似 MySQL auto increment 的效果：每创建一条新数据就插入一个对应的 ID，是数字，可以自增。

为了完成这个效果，要借助 mongoose 的新概念：插件。mongoose 插件的概念和 egg.js 的插件在含义上异曲同工，都是完成特定功能的一个模块。mongoose 插件有个特定场景：为了重用 schema 上的逻辑而设立，让多个 schema 方便地共享相同的逻辑。schema 大家都还记得吧，initUserModel 的时候遇到它：schema 是个构造函数，它的实例上有很多方法，可以在调用不同方法时完成对应的处理。

简单看一下。进入 userSchema 打点，会出现一系列方法：post、pre、removeListener、setMaxListeners 等等，会发现它是一个基于事件的处理机制。在官方文档上看一个写好的插件：它是一个 function，内部把 schema 传进来后调用 schema 的 post 方法，post 就是每次执行完这个查询以后触发的回调。这个插件的作用是在 find 和 findOne 之后给文档添加一个特殊字段 loadedAt，等于当前时间。有了这个函数，就可以在 schema 实例上使用 plugin 方法把它加载进去。这样多个 schema 就能很好地共享相同的逻辑了：示例里 gameSchema 和 playerSchema 都通过这种方式添加了每次查找后的 loadedAt 字段。

插件可以在 schema 中这样使用，也可以全局使用：直接导入 mongoose，在 mongoose 上调用 plugin 方法。

为了完成自增任务，我们找到一个非常好用的 mongoose 插件 mongoose-sequence，它是用得最多的对应插件，帮我们很容易地创建自增字段。文档讲了很多高级用法我们暂时用不到，只要实现一个自增 ID 就行，直接写代码。大家自己安装：npm install --save mongoose-sequence，我这里已经装完。然后来到 model 的 User.ts 把它引进来。

特别注意：它是 CommonJS 模块，默认导入要写成 import * as 的方式，这点之前说过。AutoIncrementFactory 是一个工厂函数，从 mongoose-sequence 引入后需要通过工厂函数创建对应的自增插件函数：const autoIncrement = AutoIncrementFactory(...)，调用工厂函数需要传入一个 connection。我们的 connection 在 app 上，是通过 egg-mongoose 插件添加上去的，写 this.app.mongoose。通过 factory 创建出插件函数后，就可以调用 schema.plugin() 方法，把函数传进去，这样就配置好了。

它还有更多 options。mongoose-sequence 给我们提供两个参数：第一个叫 incField（increment field），指代哪个字段是自增字段，我们这里肯定是 id，默认也是 id；第二个叫 id，是给这个 schema 的自增创建一个特殊的标识，避免和其他 schema 的自增插件相混淆。比如我们还有其他数据结构也要创建自增插件，那 id 就起另一个名称，这里写 userIdsCounter。

添加完成后就可以在数据中测试了。我把原来的数据删除了一些，看看新数据会怎么样。直接用 viking@123.com 点 Send，这是一个 user create 接口。可以看到多了一条记录，id 等于 2，因为我之前创建过一条数据，是自增的。再测一次：viking@234.com 创建，期望值应该是 3。结果新创建的数据 id 就是 3，自增成功了，最后的这个特性也实现了。

这节课有两个知识点：第一，先提出需求，我们需要一个自增的简单字段；然后讲了 mongoose plugin 的概念，插件其实就是一个可重用的函数，可以用 schema.plugin 方法在多个 schema 之间重用；最后讲解了解决方案，使用 mongoose-sequence 完成了对应需求。这节课的任务就完成了。
