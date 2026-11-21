---
disableNunjucks: true
title: 11-4 nodejs 连接 mongodb 数据库
date: 2026-11-17 15:17:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上两节课我们介绍了 mongo 命令行和 Robo 3T 图形界面来查看、操作数据。但最终目的是用代码操作数据，这就要用到 MongoDB 官方针对不同语言的 drivers。打开 docs.mongodb.com/drivers，能看到支持的语言图标非常丰富。我们选 Node.js，这个章节有一系列丰富的指南和 fundamentals 文章。我把要点提取出来，带大家把基本语法过一遍，对 MongoDB 会有更深入的认识。

这次仍然用 TS 作为主力语言，用得越多越觉得方便：即使写个简单 Demo，有了定义文件，有时都不用仔细查文档。

第一步创建新项目。我这里已经建了 learn-mongo 文件夹，进入后运行 npm install mongodb --save。注意 mongodb 这个包就是官方提供的 Node.js driver。然后在根目录创建入口文件 index.ts。

代码里先从 mongodb 导入模块，其中有一个叫 MongoClient 的类，用它实例化一个客户端。接下来创建连接 URL。特别注意 MongoDB 采用自己的协议，协议名就叫 mongodb，冒号加两个斜杠，和 http 很像，这是 MongoDB 独有的协议。地址是 localhost（本地已启动），端口号再说一遍是 27017，没改过的话就是它。再强调一遍，要保证 Mongo Server 已经启动。用 new MongoClient(url) 传入 URL 完成实例化。

Node.js driver 的方法名称和 mongo shell 非常类似，所以一开始学 shell 对理解 driver 很有帮助。driver 的方法大量使用 Promise，用 async await 写起来很方便。我们创建一个 async 入口函数 run，里面用 try catch：第一步 await client.connect() 连接数据库；连接后用 client.db() 方法选取要操作的数据库，我们选之前建好的 hello，和 shell 里一样，传一个不存在的库名它会自动新建。

接下来测试数据库是否连通。MongoDB 有个特殊的方法：await db.command()。command 是个新概念，官方叫 database commands，在 shell 里对应 db.runCommand。它用 object 的形式描述我们要在数据库中执行什么操作，每种操作都有对应的 command。看一个复杂例子 find（查询记录）的 syntax 就知道：runCommand 传一个 object，里面有很多 key，find 加各种条件。这个格式太繁琐也不好记，不如直接用实例上的方法方便，所以真实代码中 runCommand 比较少见。这里只介绍一个最简单的 command 来测试连通性：ping。文档说 ping 用于测试 server 是否响应命令，格式非常简单，{ping: 1}。注意它是 object，任何 command 都是 object。最后 console.log('connected', res) 输出结果。

try 之后要记得加 catch，有错误可以抓到并 console.error(e) 打印出来。运行完这些代码要把连接关闭，用 finally，client 上有个 close 方法可以关闭。

入口函数写完了，整个流程是连接、执行命令测试、关闭。运行方式用之前讲过的全局命令 ts-node，可以直接以 TypeScript 方式运行 TS 文件。回车后输出 connected OK，response 返回 ok: 1，说明用 MongoDB driver 连接数据库成功了。

对 MongoDB Node.js 的第一堂学习就到这里，连接成功之后，下节课来学习 CRUD 数据操作。
