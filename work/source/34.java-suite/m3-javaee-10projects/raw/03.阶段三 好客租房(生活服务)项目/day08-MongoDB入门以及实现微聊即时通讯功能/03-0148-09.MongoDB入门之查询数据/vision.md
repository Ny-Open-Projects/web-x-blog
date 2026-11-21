# 画面线理解：09.MongoDB入门之查询数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\09.MongoDB入门之查询数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:19, 01:45, 02:13, 03:15, 03:36, 03:52, 04:11, 04:52, 05:46, 06:26, 07:01, 07:27, 08:23, 08:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:38:41

1) 这一组画面整体在讲什么（一句话）：
讲解 MongoDB 查询数据的方法，包括基本查询、条件查询、分页查询、排序查询以及索引的作用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“1.3.6、查询数据”章节，介绍 MongoDB 查询语法格式 `db.user.find([query], [fields])`，并说明 `query` 和 `fields` 参数的含义。
画面 2: 展示 PDF 文档中“条件查询”表格，列出“等于”、“小于”、“小于或等于”、“大于”四种操作的格式、范例和对应的 RDBMS 类似语句。
画面 3: 展示终端命令行，执行了四条 `db.user.insert(...)` 命令向数据库插入测试数据。
画面 4: 展示 PDF 文档中“1.4、索引”章节，列出多个 MongoDB 查询示例，包括查询全部数据、查询特定字段、查询特定 ID、查询年龄范围、分页查询、排序查询等。
画面 5: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 6: 展示终端命令行，执行了 `db.user.find()` 查询所有数据，并显示了返回的文档列表。
画面 7: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 8: 展示终端命令行，执行了 `db.user.find({id:1})` 查询特定 ID 的数据，并使用 `.pretty()` 方法格式化输出。
画面 9: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 10: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 11: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 12: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 13: 与画面 4 内容相同，为 PDF 文档中“1.4、索引”章节的示例代码。
画面 14: 展示 PDF 文档中“1.3.6、查询数据”章节，介绍删除数据的命令 `db.user.remove()`，并说明 `deleteOne` 和 `deleteMany` 的使用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```text
1.3.6、查询数据
MongoDB 查询数据的语法格式如下：
db.user.find([query], [fields])
• query：可选，使用查询操作符指定查询条件。
• fields：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值，只需省略该参数即可（默认省略）。
如果你需要以易读的方式求取数据，可以使用 pretty() 方法。语法格式如下：
db.col.find().pretty()
```

画面 2:
```text
条件查询：
| 操作 | 格式 | 范例 | RDBMS中的类似语句 |
| :--- | :--- | :--- | :--- |
| 等于 | {<key>:<value>} | db.col.Find({"by":"黑马程序员"}).pretty() | where by = '黑马程序员' |
| 小于 | {<key>:{$lt:<value>}} | db.col.Find({"likes":{$lt:30}}).pretty() | where likes < 30 |
| 小于或等于 | {<key>:{$lte:<value>}} | db.col.Find({"likes":{$lte:30}}).pretty() | where likes <= 30 |
| 大于 | {<key>:{$gt:<value>}} | db.col.Find({"likes":{$gt:30}}).pretty() | where likes > 30 |
```

画面 3:
```text
> use testdb
switched to db testdb
> db.user.insert({id:1,username:'zhangsan',age:20})
WriteResult( { "nInserted" : 1 } )
> db.user.insert({id:2,username:'lisi',age:21})
WriteResult( { "nInserted" : 1 } )
> db.user.insert({id:3,username:'wangwu',age:22})
WriteResult( { "nInserted" : 1 } )
> db.user.insert({id:4,username:'zhaoliu',age:22})
WriteResult( { "nInserted" : 1 } )
```

画面 4:
```text
实例：
1 #加入测试数据
2 db.user.insert({id:1,username:'zhangsan',age:20})
3 db.user.insert({id:2,username:'lisi',age:21})
4 db.user.insert({id:3,username:'wangwu',age:22})
5 db.user.insert({id:4,username:'zhaoliu',age:22})
6
7 db.user.find()  #查询全部数据
8 db.user.find({},{id:1,username:1})  #只查询id与username字段
9 db.user.find().count()  #查询数据条数
10 db.user.find({id:1})  #查询id为1的数据
11 db.user.find({age:{$lt:21}})  #查询小于等于21的数据
12 db.user.find({age:{$lte:21}, id:{$gte:2}})  #and查询，age小于等于21并且id大于等于2
13 db.user.find({$or:[{id:1},{id:2}]})  #查询id=1 or id=2
14
15 #分页查询：Skip()跳过几条，Limit()查询条数
16 db.user.find().skip(1).limit(2)  #跳过1条数据，查询2条数据
17 db.user.find().sort({id:-1})  #按照age倒序排序，-1为倒序，1为正序
```

画面 6:
```text
> db.user.find()
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a154"), "id" : 2, "username" : "lisi", "age" : 21 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a155"), "id" : 3, "username" : "wangwu", "age" : 22 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a156"), "id" : 4, "username" : "zhaoliu", "age" : 22 }
> db.user.find({id:1})
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
> db.user.find({id:1}).pretty()
{
  "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"),
  "id" : 1,
  "username" : "zhangsan",
  "age" : 20
}
> db.user.find({age:{$lt:21}})
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a153"), "id" : 1, "username" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0bf1d0dbc7fa321e24a154"), "id" : 2, "username" : "lisi", "age" : 21 }
```

画面 14:
```text
1.3.6、查询数据
MongoDB 查询数据的语法格式如下：
db.user.find([query], [fields])
• query：可选，使用查询操作符指定查询条件。
• fields：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值，只需省略该参数即可（默认省略）。
如果你需要以易读的方式求取数据，可以使用 pretty() 方法。语法格式如下：
db.col.find().pretty()
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
