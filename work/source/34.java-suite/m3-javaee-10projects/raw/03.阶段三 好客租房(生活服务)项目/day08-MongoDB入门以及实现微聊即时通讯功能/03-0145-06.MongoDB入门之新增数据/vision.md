# 画面线理解：06.MongoDB入门之新增数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\06.MongoDB入门之新增数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:41, 00:46, 01:17, 01:24, 01:39, 01:42, 01:45, 02:04, 02:06, 02:07, 02:13, 02:41, 02:45, 03:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:36:23

1) 这一组画面整体在讲什么（一句话）：
演示在 MongoDB 命令行中如何创建数据库、插入和更新文档数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 MongoDB 启动日志，提示未启用访问控制，并提供启用免费监控的命令。
画面 2: 执行 `use testdb` 命令，切换到 testdb 数据库。
画面 3: 在命令行中输入 `db.user.insert({id:1,name:'zhangsan',age:20})`，准备插入数据。
画面 4: 执行插入命令，返回 WriteResult({"nInserted": 1})，表示插入成功。
画面 5: 执行 `db.user.save({id:2,name:'lisi',age:22})` 命令，更新文档。
画面 6: 执行 save 命令，返回 WriteResult({"nInserted": 1})，表示更新成功。
画面 7: 画面内容与画面 6 相同，无新操作。
画面 8: 执行 `db.user.find()` 命令，查询并显示所有文档。
画面 9: 画面内容与画面 8 相同，无新操作。
画面 10: 画面内容与画面 8 相同，无新操作。
画面 11: 画面内容与画面 8 相同，无新操作。
画面 12: 执行 `db.user.insert({})` 命令，插入一个空文档。
画面 13: 执行 insert 命令，返回 WriteResult({"nInserted": 1})，表示插入成功。
画面 14: 显示 PDF 文档内容，其中包含关于插入和更新数据的 MongoDB 语法说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
> use testdb
switched to db testdb

画面 3:
> db.user.insert({id:1,name:'zhangsan',age:20})

画面 4:
> db.user.insert({id:1,name:'zhangsan',age:20})
WriteResult({ "nInserted" : 1 })

画面 5:
> db.user.save({id:2,name:'lisi',age:22})

画面 6:
> db.user.save({id:2,name:'lisi',age:22})
WriteResult({ "nInserted" : 1 })

画面 8:
> db.user.find()
{ "_id" : ObjectId("5c0be790d49eaaa20d4140e3"), "id" : 1, "name" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0be7a0d49eaaa20d4140e4"), "id" : 2, "name" : "lisi", "age" : 22 }

画面 12:
> db.user.insert({})

画面 13:
> db.user.insert({})
WriteResult({ "nInserted" : 1 })

画面 14 (PDF 文档内容):
1.3.3. 新增数据
在MongoDB中，存储的文档结构是一种类似于json的结构，称之为bson（全称为 Binary JSON ）。
插入数据
#方法：db.COLLECTION_NAME.insert(document)
> db.user.insert({id:1,username:'zhangsan',age:20})
WriteResult({ "nInserted" : 1 })
> db.user.save({id:2,username:'lisi',age:22})
WriteResult({ "nInserted" : 1 })
> db.user.find()  #查询数据
{ "_id" : ObjectId("5c0be0024b318926e01fd6e"), "id" : 1, "username" : "zhangsan", "age" : 20 }
{ "_id" : ObjectId("5c0be0134b318926e01fd6e"), "id" : 2, "username" : "lisi", "age" : 22 }

1.3.4. 更新数据
update() 方法用于更新已存在的文档。语法格式如下：

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: PDF 文档标题为“1.3.3. 新增数据”和“1.3.4. 更新数据”，内容包含 MongoDB 插入和更新数据的命令示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
