# 画面线理解：10.MongoDB入门之数据索引

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\10.MongoDB入门之数据索引【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:41, 00:53, 01:49, 02:18, 02:28, 02:32, 02:47, 03:34, 03:53, 04:01, 04:06, 04:24, 04:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:39:31

1) 这一组画面整体在讲什么（一句话）：
讲解 MongoDB 中索引的创建、查看、删除及执行计划相关操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义中“1.4. 索引”章节内容，介绍索引的作用和重要性，并展示查看索引的命令 `db.user.getIndexes()`。
画面 2: 在 Xshell 中演示 MongoDB 查询命令，包括 `find()`、`limit()`、`skip()` 和 `sort()` 的组合使用，展示数据分页和排序效果。
画面 3: 在 Xshell 中执行 `db.user.getIndexes()` 命令，查看当前集合的索引信息。
画面 4: 展示 PDF 讲义中“1.4. 索引”章节内容，介绍索引的作用和重要性，并展示查看索引的命令 `db.user.getIndexes()`。
画面 5: 在 Xshell 中执行 `db.user.createIndex({age:1})` 命令，为 `age` 字段创建升序索引。
画面 6: 在 Xshell 中执行 `db.user.getIndexes()` 命令，查看创建索引后的结果，确认新增了 `age_1` 索引。
画面 7: 展示 PDF 讲义中“1.4. 索引”章节内容，介绍删除索引的命令 `db.user.dropIndex('age_1')` 和 `db.user.dropIndexes()`。
画面 8: 在 Xshell 中执行 `db.user.getIndexes()` 命令，查看当前集合的索引信息。
画面 9: 在 Xshell 中执行 `db.user.dropIndex("age_1")` 命令，删除 `age_1` 索引，并再次执行 `getIndexes()` 验证索引已删除。
画面 10: 在 Xshell 中执行 `db.user.createIndex({"age":1, "id":-1})` 命令，创建复合索引。
画面 11: 在 Xshell 中执行 `db.user.getIndexes()` 命令，查看创建复合索引后的结果，确认新增了 `age_1_id_-1` 索引。
画面 12: 展示 PDF 讲义中“1.5. 执行计划”章节内容，介绍查看索引大小的命令 `db.user.totalIndexSize()`。
画面 13: 在 Xshell 中执行 `db.user.totalIndexSize()` 命令，查看当前集合所有索引的总大小，结果为 40960。
画面 14: 展示 PDF 讲义中“1.4. 索引”章节内容，介绍索引的作用和重要性，并展示查看索引的命令 `db.user.getIndexes()`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```text
#分页查询：Skip()跳过几条，Limit()查询条数
db.user.find().limit(1).skip(2) #跳过1条数据，查询2条数据
db.user.find().sort({id:-1}) #按照age倒序排序，-1为倒序，1为正序
```
画面 2:
```text
> db.user.find({$or: [{id:1}, {id:2}]})
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a154"), "id" : 2, "username" : "lisi", "age" : 21 }
> db.user.find()
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a154"), "id" : 2, "username" : "lisi", "age" : 21 }
> db.user.find().limit(1)
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
> db.user.find().limit(1).skip(2)
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a155"), "id" : 3, "username" : "wanqwu", "age" : 22 }
> db.user.find().limit(1).skip(3)
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a156"), "id" : 4, "username" : "zhaoliu", "age" : 22 }
> db.user.find().sort({id:-1})
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a156"), "id" : 4, "username" : "zhaoliu", "age" : 22 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a155"), "id" : 3, "username" : "wanqwu", "age" : 22 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a154"), "id" : 2, "username" : "lisi", "age" : 21 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
```
画面 3:
```text
> db.user.getIndexes()
{
  "v" : 2,
  "key" : {
    "_id" : 1
  },
  "name" : "_id_",
  "ns" : "testdb.user"
}
```
画面 4:
```text
#查看索引
> db.user.getIndexes()
{
  "v" : 2,
  "key" : {
    "_id" : 1
  },
  "name" : "_id_",
  "ns" : "testdb.user"
}
```
画面 5:
```text
> db.user.createIndex({age:1})
{
  "createdCollectionAutomatically" : false,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```
画面 6:
```text
> db.user.getIndexes()
{
  "v" : 2,
  "key" : {
    "_id" : 1
  },
  "name" : "_id_",
  "ns" : "testdb.user"
},
{
  "v" : 2,
  "key" : {
    "age" : 1
  },
  "name" : "age_1",
  "ns" : "testdb.user"
}
```
画面 7:
```text
#创建索引
> db.user.createIndex({'age':1})
{
  "createdCollectionAutomatically" : false,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}

#删除索引
db.user.dropIndex("age_1")
#或者，删除除了_id之外的索引
db.user.dropIndexes()

#创建联合索引
db.user.createIndex({'age':1, 'id':-1})
```
画面 8:
```text
> db.user.getIndexes()
{
  "v" : 2,
  "key" : {
    "_id" : 1
  },
  "name" : "_id_",
  "ns" : "testdb.user"
},
{
  "v" : 2,
  "key" : {
    "age" : 1
  },
  "name" : "age_1",
  "ns" : "testdb.user"
}
```
画面 9:
```text
> db.user.dropIndex("age_1")
{ "nIndexesWas" : 2, "ok" : 1 }
> db.user.getIndexes()
{
  "v" : 2,
  "key" : {
    "_id" : 1
  },
  "name" : "_id_",
  "ns" : "testdb.user"
}
```
画面 10:
```text
> db.user.createIndex({"age":1, "id":-1})
{
  "createdCollectionAutomatically" : false,
  "numIndexesBefore" : 1,
  "numIndexesAfter" :
