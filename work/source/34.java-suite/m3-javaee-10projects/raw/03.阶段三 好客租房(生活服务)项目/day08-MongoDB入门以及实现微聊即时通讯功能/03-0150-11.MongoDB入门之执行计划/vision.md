# 画面线理解：11.MongoDB入门之执行计划

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\11.MongoDB入门之执行计划【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:35, 01:57, 02:29, 02:41, 03:35, 03:56, 04:27, 04:50, 05:11, 05:32, 05:54, 06:20, 06:36, 06:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:40:22

1) 这一组画面整体在讲什么（一句话）：
演示 MongoDB 中索引的查看、创建、删除及查询执行计划分析。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 查看数据库中所有索引，输出包含两个索引的结构，分别是 "_id" 和 "age_1_id_-1"，并查询总索引大小为 40960。
画面 2: 查询用户集合中的数据，显示了从 id:117 到 id:136 的文档，包含 username 和 age 字段。
画面 3: 继续显示用户集合中的数据，从 id:137 到 id:196 的文档。
画面 4: 执行 db.user.find().explain()，输出查询计划，显示 "stage": "COLLSCAN"，表示全表扫描。
画面 5: 在画面 4 的基础上，光标在 "COLLSCAN" 上，准备进行修改或说明。
画面 6: 展示 PDF 讲义中关于查询执行计划的说明，包含 "parsedQuery" 和 "winningPlan" 的结构，以及 "COLLSCAN"、"FETCH"、"IXSCAN"、"SHARD_MERGE"、"IDHACK" 等执行阶段的说明。
画面 7: 在终端中输入 db.user.getIndex()，准备查看索引详情，但未完整执行。
画面 8: 继续显示用户集合中的数据，从 id:176 到 id:196 的文档。
画面 9: 执行 db.user.find({_id: ObjectId("5c0bf692bdc7fa321e241a1c")}).explain()，输出查询计划，显示 "stage": "IDHACK"，表示使用了索引查找。
画面 10: 在画面 9 的基础上，光标在 "IDHACK" 上，准备进行修改或说明。
画面 11: 展示 PDF 讲义中关于创建和删除索引的代码，包括 db.user.createIndex({"age":1})、db.user.dropIndex("age_1")、db.user.dropIndexes()。
画面 12: 展示 PDF 讲义中关于索引结构的详细说明，包括 "keyPattern"、"indexName"、"isUnique"、"direction"、"indexBounds" 等字段。
画面 13: 执行 db.user.find({username: 'zhangsan'}).explain()，输出查询计划，显示 "stage": "COLLSCAN"，表示全表扫描。
画面 14: 展示 PDF 讲义中关于复合查询的代码，包括 db.user.find({age: {$gt:100}, id: {$lt:200}}).explain()，并显示对应的查询计划结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
db.user.getIndexes()
[
  {
    "v": 2,
    "key": {
      "_id": 1
    },
    "name": "id",
    "ns": "testdb.user"
  },
  {
    "v": 2,
    "key": {
      "age": 1,
      "id": -1
    },
    "name": "age_1_id_-1",
    "ns": "testdb.user"
  }
]
db.user.totalIndexSize()
40960

画面 2:
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1a"),
  "id": 117,
  "username": "name_17",
  "age": 27
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1b"),
  "id": 118,
  "username": "name_18",
  "age": 28
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1c"),
  "id": 119,
  "username": "name_19",
  "age": 29
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1d"),
  "id": 120,
  "username": "name_20",
  "age": 30
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1e"),
  "id": 121,
  "username": "name_21",
  "age": 31
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a1f"),
  "id": 122,
  "username": "name_22",
  "age": 32
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a20"),
  "id": 123,
  "username": "name_23",
  "age": 33
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a21"),
  "id": 124,
  "username": "name_24",
  "age": 34
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a22"),
  "id": 125,
  "username": "name_25",
  "age": 35
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a23"),
  "id": 126,
  "username": "name_26",
  "age": 36
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a24"),
  "id": 127,
  "username": "name_27",
  "age": 37
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a25"),
  "id": 128,
  "username": "name_28",
  "age": 38
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a26"),
  "id": 129,
  "username": "name_29",
  "age": 39
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a27"),
  "id": 130,
  "username": "name_30",
  "age": 40
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a28"),
  "id": 131,
  "username": "name_31",
  "age": 41
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a29"),
  "id": 132,
  "username": "name_32",
  "age": 42
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a2a"),
  "id": 133,
  "username": "name_33",
  "age": 43
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a2b"),
  "id": 134,
  "username": "name_34",
  "age": 44
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a2c"),
  "id": 135,
  "username": "name_35",
  "age": 45
},
{
  "_id": ObjectId("5c0bf692bdc7fa321e241a2d"),
  "id": 136,
  "username": "name_36",
  "age": 46
}

画面 4:
db.user.find().explain()
{
  "queryPlanner": {
    "plannerVersion": 1,
    "namespace": "testdb.user",
    "indexFilterSet": false,
    "parsedQuery": {
    },
    "winningPlan": {
      "stage": "COLLSCAN",
      "direction": "forward"
    },
    "rejectedPlans": []
  },
  "serverInfo": {
    "host": "fbfba5f54fla",
    "port": 27017,
    "
