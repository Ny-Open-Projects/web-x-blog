# 画面线理解：07.MongoDB入门之更新数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\07.MongoDB入门之更新数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:40, 01:47, 03:09, 03:46, 04:01, 04:26, 05:11, 05:24, 05:58, 06:46, 07:03, 07:21, 07:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:37:14

1) 这一组画面整体在讲什么（一句话）：
讲解 MongoDB 中 update() 方法的语法、参数及实际操作示例，包括更新已存在文档、更新不存在字段、以及设置 upsert 参数。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“1.3.4. 更新数据”章节，介绍 update() 方法用于更新已存在的文档，并列出语法格式。
画面 2: PDF 文档中展示 update() 方法的参数说明，包括 query、update、upsert、multi、writeConcern，并附有示例代码。
画面 3: Xshell 终端中展示在 testdb 数据库中执行 insert、save、find 操作，插入并更新了两条用户记录。
画面 4: Xshell 终端中执行 db.user.update({id:1},{$set:{age:25}}) 更新用户 zhangsan 的年龄为 25，并通过 find 验证更新结果。
画面 5: Xshell 终端中再次执行 db.user.update({id:1},{$set:{age:25}})，结果与上一画面相同，确认更新成功。
画面 6: Xshell 终端中执行 db.user.update({id:1},{$set:{age:25}})，结果与前几画面相同，确认更新成功。
画面 7: PDF 文档中展示更新不存在字段的示例，代码为 db.user.update({id:2},{$set:{sex:1}})，并说明更新后会新增字段。
画面 8: Xshell 终端中执行 db.user.update({id:2},{$set:{sex:1}})，成功为用户 lisi 新增 sex 字段，并通过 find 验证。
画面 9: Xshell 终端中执行 db.user.update({id:2},{$set:{sex:1}})，结果与上一画面相同，确认更新成功。
画面 10: Xshell 终端中执行 db.user.update({id:2},{$set:{sex:1}})，结果与前几画面相同，确认更新成功。
画面 11: Xshell 终端中尝试更新 id:5 的记录（不存在），并设置 upsert 为 true，成功插入新记录，并通过 find 验证。
画面 12: PDF 文档中展示更新不存在的字段时，如果设置 upsert 为 true，则会新增数据，代码为 db.user.update({id:3},{$set:{sex:1}},true)。
画面 13: PDF 文档中展示更新不存在的字段时，如果设置 upsert 为 true，则会新增数据，代码为 db.user.update({id:3},{$set:{sex:1}},true)。
画面 14: PDF 文档中再次展示 update() 方法的参数说明，包括 query、update、upsert、multi、writeConcern，并附有示例代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
update() 方法用于更新已存在的文档。语法格式如下：
```

画面 2:
```
multi: <boolean>,
writeConcern: <document>
```

画面 2 参数说明:
```
query: update的查询条件，类似sql update查询where后面的。
update: update的更新条件，一些更新的操作符（如.inc.）等，也可以理解为sql update查询set后面的。
upsert: 可选，这个参数的意思是，如果不存在update的记录，是否插入objNow，true为插入，默认是false，不插入。
multi: 可选，mongodb 默认是false 只更新找到的第一条记录，如果这个参数为true，就把按条件查出多条记录全部更新。
writeConcern: 可选，抛出异常的级别。
```

画面 3:
```
> use testdb
switched to db testdb
> db.user.insert({id:1,name:"zhangsan",age:20})
WriteResult( { "nInserted" : 1 } )
> db.user.save({id:2,name:"lisi",age:22})
WriteResult( { "nInserted" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }
> db.user.insert({})
WriteResult( { "nInserted" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }
{ "_id" : ObjectId("5c0be7ddd49eaaa20d4140e5"), "id" : 3, "name" : "zhangsan", "age" : 20 }
```

画面 4:
```
> db.user.update({id:1},{$set:{age:25}})
WriteResult( { "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 25 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }
{ "_id" : ObjectId("5c0be7ddd49eaaa20d4140e5"), "id" : 3, "name" : "zhangsan", "age" : 20 }
```

画面 5:
```
> db.user.update({id:1},{$set:{age:25}})
WriteResult( { "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 25 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }
{ "_id" : ObjectId("5c0be7ddd49eaaa20d4140e5"), "id" : 3, "name" : "zhangsan", "age" : 20 }
```

画面 6:
```
> db.user.update({id:1},{$set:{age:25}})
WriteResult( { "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 25 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }
{ "_id" : ObjectId("5c0be7ddd49eaaa20d4140e5"), "id" : 3, "name" : "zhangsan", "age" : 20 }
```

画面 7:
```
#注意：如果这样写，会删除其他所有的字段
> db.user.update({id:1},{$set:{age:25}})
WriteResult( { "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 } )
> db.user.find()
{ "_id" : ObjectId("5c0be0024b318926e0c1f6dc"), "id" : 1, "username" : "zhangsan", "age" : 25 }
{ "_id" : ObjectId("5c08c0134b318926e0c1f6dd"), "id" : 2, "username" : "lisi
