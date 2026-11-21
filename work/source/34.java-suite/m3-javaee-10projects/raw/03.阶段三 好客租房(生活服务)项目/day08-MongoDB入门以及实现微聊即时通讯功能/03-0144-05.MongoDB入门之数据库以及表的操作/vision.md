# 画面线理解：05.MongoDB入门之数据库以及表的操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\05.MongoDB入门之数据库以及表的操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:33, 00:53, 01:21, 02:16, 03:20, 04:02, 04:22, 04:32, 04:53, 05:15, 05:42, 06:09, 06:19, 06:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:35:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 MongoDB 中查看、创建、插入、删除数据库和集合（表）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中关于“1.3.2、数据库以及表的操作”的内容，包含查看数据库、切换数据库、创建数据库的命令示例。
画面2：与画面1内容相同，为 PDF 文档的同一页面。
画面3：在 Xshell 终端中，显示 MongoDB 启动后的提示信息，并执行了 `show dbs` 命令，显示了 admin、config、local 三个数据库。
画面4：在 Xshell 终端中，执行了 `use local` 切换数据库，然后执行 `use testdb` 切换到 testdb 数据库。
画面5：在 Xshell 终端中，执行了 `db.user.insert({id:1,name:'zhangsan'})` 插入数据，并执行 `show dbs` 查看数据库。
画面6：在 Xshell 终端中，执行了 `show tables` 和 `show collections` 命令，显示了 user 集合。
画面7：展示 PDF 文档中关于“1.3.2、数据库以及表的操作”的内容，包含查看数据库、切换数据库、创建数据库的命令示例。
画面8：与画面7内容相同，为 PDF 文档的同一页面。
画面9：展示 PDF 文档中关于“查看表”、“删除集合（表）”、“删除数据库”的命令示例。
画面10：与画面9内容相同，为 PDF 文档的同一页面。
画面11：展示 PDF 文档中关于“1.3.3、新增数据”的内容，包含查看表、删除集合、删除数据库的命令示例。
画面12：在 Xshell 终端中，执行了 `db.user.drop()` 删除集合，返回 true，然后执行 `db.dropDatabase()` 删除数据库，返回 false。
画面13：在 Xshell 终端中，执行了 `db.dropDatabase()` 删除数据库，返回 {"dropped": "testdb", "ok": 1}，然后执行 `show dbs` 查看数据库。
画面14：展示 PDF 文档中关于“1.3.2、数据库以及表的操作”的内容，包含查看数据库、切换数据库、创建数据库的命令示例，并在右侧展示了文档中一个用户数据的 JSON 格式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1、2、7、8、9、10、11、14：
```
1.3.2、数据库以及表的操作

#查看所有的数据库
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

#通过use关键字切换数据库
> use admin
switched to db admin

#创建数据库
#说明：在MongoDB中，数据库是自动创建的，通过use切换到新数据库中，进行插入数据即可自动创建数据库
> use testdb
switched to db testdb

#插入数据
> db.user.insert({id:1,name:"zhangsan"})
WriteResult({ "nInserted" : 1 })

#查看表
> show tables
> show collections
user
user

#删除集合（表）
> db.user.drop()
true
#如果成功删除指定集合，则 drop() 方法返回 true，否则返回 false。

#删除数据库
> use testdb  #先切换到要删除的数据库中
> db.dropDatabase()  #删除数据库
{ "dropped" : "testdb", "ok" : 1 }
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
testdb   0.000GB  #数据库自动创建
```

画面3：
```
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use local
switched to db local
```

画面4：
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use local
switched to db local
> use testdb
switched to db testdb
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```

画面5：
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use local
switched to db local
> use testdb
switched to db testdb
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> db.user.insert({id:1,name:'zhangsan'})
WriteResult({ "nInserted" : 1 })
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
testdb   0.000GB
```

画面6：
```
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
user
> show tables
> show collections
