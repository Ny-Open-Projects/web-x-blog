# 05.MongoDB入门之数据库以及表的操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\05.MongoDB入门之数据库以及表的操作【海量资源尽在 ubkz.com】.mp4
- 时长 6分38秒（音频 399s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来看一下MongoDB中的数据库啊以及表的这个操作啊那么在MongoDB中啊它其实跟我们的传统的数据库也是一样首先呢我们要去先有什么呢先有我们的数据库啊数据库然后呢在数据库的内部呢再有多张表啊多张表啊也是这种相同这种概念啊就是表然后呢在表里面呢
[00:25] 再会有我们的一行一行的数据啊它是这样的一个意思啊所以呢这个概念跟我们传统的一些mySQL啊是一样的啊ok所以呢接下来呢我们先来看的是它的数据库以及它这个表的一些相关的一些操作那么前面呢我们其实可以看到它的第一个这个命令是不是就是秀一个DBS来查看它的所有的数据库那么我们来看一下
[00:49] 那么刚刚我们是不是已经执行过了是不是默认有三个数据库OK好那么下面我们就可以通过这种user这种关键字来切换我们的数据库的操作就是说我们具体的一些后续的一些CRUD的操作那你必须得选中一个数据库你可以选中admin也可以选择什么local去做一些这种执行也就是说你必须要选中数据库所以我们要从user去做一个选择比如说我们user什么呢local
[01:17] 然后是不是就可以切换到我们这个Local也就是说通过这个U的关键字去做一个数据库的一个切换OK好那么下面我们就来看一下如何去创建一个数据库那么因为前面是三个都是它的一些默认的数据库我们一般操作不要基于这个数据库做操作那么我们都是自己去创建数据库去做一些这个操作所以我们来看一下如何去创建数据库那么在MongoDB中数据库的创建其实是做一个自动的创建的
[01:46] 就是说当我们需要去切换到这个数据库然后进行插入数据的时候就可以帮我们自动去创建一个数据库也就是说我们不需要去手动创建数据库OK比如说接下来我们创建一个我们的数据库叫做testdbOK那么怎么创建先去做一个切换叫testdb但是这个数据库
[02:09] 我们本身是不是不存在对不对但是他依然是可以切换到我们这个数据库然后我们来看一下是为一个DBS你会发现这个数据库并没有为什么没有呢原因是我们并没有向这个数据库中去插入数据如果我们给他插入数据这个数据库就会被自动的一个创建那我们来看一下他如何去插入数据我们先写这样的一个命令后面我们会再去详细去讲他插入数据的命令
[02:38] 那么我们通过db点什么呢我们的这个表db的表表名呢我们就直接来写一个url吧因为我们插入这个用户的数据啊叫什么呢insert啊insertinsert什么呢插入一条数据前面我们说过它的数据呢都是一些这个json结构的这种文档啊所以呢我们就这样来写是不是一个大括号就是一个json然后来一个id比如说是1然后呢有一个叫name对吧name可以叫比如叫
[03:06] 叫什么呢叫张三哎OK假设我们这个这个数据呢只有两个字段好那么我们回车这个时候呢我们来提示提示我们说这个数据呢已经有插入成功了然后呢我们再来看一下我们的数据库是不是可以看到是不是已经多了一个数据库叫做testdb那么这个数据库是不是就帮我们自动的是不是就创建好了哎OK所以说在mongo db中啊这个数据库的创建是自动的哎所以呢我们只需要去插入数据那么数据库就会自动
[03:36] 创建好OK好那么刚刚我们所讲的这个命令呢我们先不做过多的一个讲解后面我们会详细的再说OK好那么是不是可以看到创建好了对吧那么这个呢就是我们的数据库的这个操作啊那么我们下面来看一下我们的这个表的一些相关的操作那么我们可以通过一个show一个什么呢show一个叫tablestables来查看我们这张表
[04:05] 我们这个库里面所有的表那么当前我们这个数据库是这个testdb那么在这个数据库下面只有一张表就这个usr这张表所以就把它打印出来了ok好那么大L也可以通过什么稍微connections去做一个查看因为前面我们提到过在mago db中我们把它把这个表table其实称之为一个connectionok那么通过它也可以去做一个查看好那么我们来测试一下
[04:34] so一个so一个clangson好那么拿到的是不是打印串是不是也是这个user是一样的效果其实我们更习惯的是使用它因为我们之前用的比较多的比方像mycircle它也是这样的一个命令OK好那么我们如何去删除一张表呢通过这样的一个命令就是db.usergroup作去做一个这个删除
[05:03] OK那么db.unit.drop去做一个删除好那么这张表就会被删除掉了我们来看一下show一个tables那么是不是就没有表了没有一张表了OK好那么这个是我们的删除表的一个操作OK那么如果我们这个drop这个方法它返回chew就代表着删除成功了如果这个返回false就是代表什么代表着我们就删除就是
[05:31] 这个表其实已经不存在了我们来看一下你看它返回了一个False因为这个表本身它不存在了所以它是否删除成功呢其实是返回了False的OK好 那么我们来看一下这个数据库怎么创建数据库怎么创建呢数据库是那么你要删除哪个数据库要先切换到这个数据库比如说我们先切换到我们这个TestDB那么现在本身是不是就是在这个TestDB上面对吧然后呢我们再去敲一个mini就是DB
[06:00] 给Drop database去做一个删除就可以了我们来敲一个命令db 什么的,drop database然后去做一个删除走那么这个数据库就删除了是有一个什么的dbs可以看到那么我们刚刚所创建的testdb这个数据库是不是也被删除掉了哎呀ok就通过一个这样的一个命令去做一个删除那么其实我们可以看到他这个
[06:26] 方法明是不是很容易去做一个理解对吧这不是不就做一个删除哎OK好这个就是我们关于我们的这个数据库以及这个表的一些相关的操作好那么这个我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
Enable MongoDB's free cloud-based monitoring Service, which will then receive and display
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

