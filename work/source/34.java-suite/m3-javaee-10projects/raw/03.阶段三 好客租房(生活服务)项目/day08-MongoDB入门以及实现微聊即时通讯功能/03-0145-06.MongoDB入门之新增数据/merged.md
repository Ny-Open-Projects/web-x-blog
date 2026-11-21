# 06.MongoDB入门之新增数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\06.MongoDB入门之新增数据【海量资源尽在 ubkz.com】.mp4
- 时长 3分20秒（音频 200s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来看新增数据那么在Mongol B中呢我们已经知道啊它所存储的这种结构呢是一种JSON的结构那么我们把它称之为叫做BSON那么全称呢是Bajonate JSON哎呦OK好,那么我们来看一下它如何去做一个数据的一个插入那么它使用的命令呢或者它的语法呢是这样的叫DB点
[00:23] connect name就是我们的表名然后点insert去做这样的一个插入document就是我们的数据OK那么在mago db中插入数据有两个方法或者说两个命令一个叫做insert一个叫做save这两个效果是一样的我们分别来做演示一下那么首先我们需要去选择我们所要操作的数据库比如说test db然后我们去做一个db.url比如说这个url是我的表名当然你不叫url叫aa
[00:52] 叫 bb 都可以那么由于我们查读的是一个用户的数据所以我们这个表名叫 user然后我们来一个什么的 insert然后在这个里面我们去输的是一个 json 的字符创比如说 id 冒号冒号这个要用英文的然后来一个 name比如说叫什么张三ok然后还有比如说叫 age
[01:21] 年龄比如说20ok好这样的话我们数据是不是就有差误了当然我们前面说过还有一个命令叫C5啊它效果呢是一样的C5然后呢我们把这改成2然后呢这个张三我们改成李四李四然后年龄改成22岁ok走好那么你可以看到数据是不是同样能够去差误成功啊好那么这个数据我们差误成功了但是这个数据我们怎么样去做一个查找呢
[01:49] 它是通过这样的命令叫做db点什么呢选择我们这张表是不是db点user然后呢fend去做一个查找查找什么呢没有任何条件没有条件查找就代表什么呢查找所有的数据这个表里面的所有的数据啊来看一下那么现在我们是不是就可以去查找出啊这样的一个数据出来了那么把我们这两条数据全部都查询出来了哎呦ok好那么呃当然了在有些时候啊我们去做我们测试的时候
[02:19] 创建一个数据库是不是得先要插入我们的一个数据那么有些时候我没必要去写这么多这么多字段我能不能这样来写来看一下那么我直接做一个insert我什么都不写就写一个大括号一对大括号代表的是不是也是一条数据但是我这条数据它并没有任何的字段这样能插入成功吗来看一下
[02:41] 那么我们其实会发现它依然是能够查目成功的那么有没有这行数据呢其实你会发现是不是有这条数据它是不是只有一个字段就是我们下滑下这个ID那么这个在前面我们是不是也说过下滑下ID其实就是我们这个数据的一个唯一的标识它的类型是object ID这种类型OK它的值呢
[03:00] 对的就是里面的这个值这个值ok好那么这个就是我们所要给大家讲的就是插入数据的一个这样的一个操作你可以选择insert你可以选择save这种操作那么我们一般更常用的是这个insert这个操作好那么关于新增数据的这个操作我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

