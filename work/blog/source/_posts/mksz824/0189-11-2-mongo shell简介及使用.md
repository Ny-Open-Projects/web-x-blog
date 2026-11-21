---
disableNunjucks: true
title: 11-2 mongo shell简介及使用
date: 2026-11-17 17:09:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们成功启动了 MongoDB 的本地服务，现在要解决怎么和数据进行交互。MongoDB 提供了一个命令行程序，可以在 Shell 界面下管理和操作数据；如果 SSH 远程连接服务器，它也是管理或查看 MongoDB 数据的重要工具。

还记得下载的可运行程序 bin 文件夹里，除了启动服务用的 mongod，还有几个程序，其中一个叫 mongo，就是对应的管理程序，是一个基于 JavaScript 的交互式 Shell。官方文档叫 the mongo shell，interactive JavaScript interface。因为已经加进了 PATH，直接运行即可。

输入 mongo 启动，注意必须先启动了 MongoDB 实例才能连接成功。启动后先 cls 清屏，然后学几个命令。

第一个命令 show dbs，查看当前实例的所有数据库。db 是 database 的简称，有多个所以加 s。它会列出当前实例包含的所有数据库，可以看出一个 MongoDB 实例可以包含多个数据库。admin、config、local 都是启动实例时自动创建的内置数据库。

第二个命令 db，打印当前所在的数据库。当前在 test，这是默认创建的。但它为什么没出现在 show dbs 里？因为 test 中还没有任何数据，等你给它添加数据后，它就会出现在 show dbs 列表中。

切换数据库用 use 命令加数据库名。use admin 后显示 switch to db admin，再打 db 就确认我们在 admin 里。use 还能直接新建数据库：use hello 会创建一个叫 hello 的新数据库并切换过去，打 db 输出 hello。

进入数据库后就要看数据了。MongoDB 里有个和关系型数据库"表"对应的概念，叫集合 collections，用 show collections 查看。新建的数据库没有任何集合。

接下来插入数据。在特定 collection 中插入数据的语法非常像 JavaScript，其实底层就是 JS。db 指当前数据库（hello），后面点上一个 collection 名称，不存在时会自动新建。我们用 user，然后调用方法。插入的方法有 insert、insertMany、insertOne，顾名思义，先用 insertOne。它的参数是要插入的一个 document（文档），可以插入一个 object 对象或 JSON 数据，比如 {name: 'Viking'}。执行后输出 acknowledged: true，还显示了 insertedId 对应的 ObjectID，说明插入成功。

查找数据用 db.user.find()，不加任何条件就是查找所有数据。执行后能看到刚才那条 name 为 Viking 的记录，还自动加了 _id 字段，它是标识唯一性的特殊标识符。按条件查找也一样：find 接受一个查询对象作为参数。多插入一条 {name: 'Lily'} 后 user.find() 有两条，用 {name: 'Viking'} 条件就只查出一条，条件生效了。

更新数据用 db.user.update()，第一个参数是查找条件（更新哪一条，比如 Viking 这条），第二个是更新成什么值（name 改成 Lucy）。之后再查，值变成了 Lucy 和 Lily。删除数据用 db.user.deleteOne({name: 'Lucy'})，delete 有 many 和 one，删一条用 deleteOne。输出 acknowledged: true、deletedCount: 1，再 find 只剩一条了。

Shell 操作就介绍这么多，目的是让大家对 mongo shell 有个简单印象：有这么一个程序，可以在 Shell 里用类似 JS 的语法管理数据库。后面在程序中操作数据不会用这个比较难用的 Shell，MongoDB 数据库操作的内容会一点点扩充。想提前了解的同学可以去看官方文档和 API，每个 API 下面都有更多方法，到时我们会一一讲解。
