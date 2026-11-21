# 10.MongoDB入门之数据索引

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\10.MongoDB入门之数据索引【海量资源尽在 ubkz.com】.mp4
- 时长 4分55秒（音频 295s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面我们来看一下MongoDB中的索引那么索引它的一个作用其实不用我们说太多了因为大家都很熟悉了索引的目的其实就是在提升我们查询的效率,对不对如果说你一个查询它需要去扫描整张表那效率肯定是非常低的但有索引之后就不一样了那么肯定效率会很高这个我们就不做详细的一个介绍了因为索引大家都很了解了
[00:27] 这个跟我们数据共同的索引的概念是一样的那我们来看一下它的具体的一些操作那么我们通过一个getindex这样的一个方法就可以来查看我们这张表里面的一个索引我们来看一下那么db.euro.getindex好那么可以看到那么这个是我们当前这张表里面其实它已经
[00:56] 有一个锁引了有一个锁引那么为什么会有锁引呢原因是他默认是不是有个下滑线ID是他的一个主件对吧是主件那么主件往往肯定都是需要锁引的所以他有一个默认的锁引那么在这个里面有些字段我们简单来解释一下那第一个是V代表什么代表的Watson就是版本然后这个是KeyKey其实就是我们所说的锁引那锁引的名字就是下滑线锁引字段这个字段
[01:25] 字段的下环线id其实就是指定的这个字段的名称然后代表着11代表着什么呢是我们正序建一个索引如果是-1的话呃代表是倒序建索引然后呢这个名name的代表着我们这个索引的名字啊所以名字ok然后呢ns呢是他这个命名空间好那么呃这个是我们的一个查查看一个当前表里面的一个索引的一个情况那么下面呢我们可以通过一个credit index
[01:53] 来做一个索引的一个创建比如说我们在这个可以看到credit index age 冒号1代表着什么我们创建一个给 age 这个字段去创建一个索引并且是按照什么的正序去做一个创建ok 那么我们来写一下这个命令url 点什么的credit index叫什么 age然后冒号1那么这样的话我们就可以去做一个创建一个索引
[02:21] 好嘞那么这个所以就创建好了那么我们是不是可以通过前面这个前面这个命令做一个这个查看那我可以看到在这个位置是不是已经查看到我们这个A者这样的一个呃所以了哎好嘞好那么这个是创建这个所以那么还有什么呢删除这个所以比如说我们呃这个所以不需要了把它要删除掉那么可以通过一个drop index去做一个删除根据什么呢根据我们这个名字去做一个删除那么我们来写一下吧
[02:49] 就叫什么的db.url.什么的drop index然后呢我们去指定它的一个名字对吧名字就叫就是age下滑线1是不是就它呀来做一个删除那么现在呢我们是不是就已经把它删掉了来看一下那么现在是不是只留了一个这个索引了哎OK好那么这个呢是做一个索引的一个删除那么还有呢可以去做一个联合索引
[03:17] 那么在我们去使用的mysearch的时候是不是也可以去创建联合索引ok那么我们来看一下联合索引怎么创建呢他也是这样去做一个指定你看前面是不是我们指定了一个字段你只需要给他指定多个字段就可以了好那么咱们把这个来call一下做一个演示就可以了好那么在这来执行一下那么这个
[03:37] 创建索引的意思是指什么呢我们给这个年龄创建一个正序的一个索引我们给这个ID去创建一个倒序的一个索引要注意啊我现在只是去演示它这个语法并不代表着我们真的有这样的一个需求是吧OK好那我来看一下它的一个索引的一个情况那么这个是不是它的第二个这个索引是一个联合的索引那么它的字段是不是有两个字段一个是age一个是ID那么一个是1一个是-1OK一个正序一个倒序
[04:07] 好嘞这个是联合索引那么下面呢还有一个呢是可以去查看这个索引的一个大小OK那么去这样的话他做一个统计做一个统计来看一下那么可以看到整个这个表里面索引的所占的一个什么呢这个大小注意他的单位呢是字节
[04:26] OK是单位是直接这样的一个查看好那么这个呢就是一个索引那么其实我们可以看到在mongo db中创建这个索引是非常简单的对吧但是现在就有个问题了就是我们索引创建好了但是我们在做数据查询的时候这个索引它有没有生效对不对那么这个就是一个问题那么这个我就需要通过我们下面的一个执行计划来做一个查看好那么关于这个索引呢我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

