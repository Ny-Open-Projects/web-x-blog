# 07.MongoDB入门之更新数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\07.MongoDB入门之更新数据【海量资源尽在 ubkz.com】.mp4
- 时长 7分29秒（音频 449s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来看一下更新数据前面我们讲过新增那么下面我们来看更新那么更新的数据它的语法呢是这样的一种语法就是db connection然后呢点update前面调用insert现在调用是update这个方法然后呢传入呢有两个参数其实是有可能会有后面这些可选参数吧这两个是必须的参数一个query一个叫update就是说我第一个参数就是说你查询的条件
[00:26] 我根据什么样的一个条件去做查询这个数据查到这个数据然后我再去更新它的什么内容是这样的一个意思就是类似于我们的搜索语句中的update然后后面有个vale什么什么这个就是它的条件OK好那么它的一些可选参数的我们可以看一下那么像第一个叫做upset就是这个意思就是说如果当我们去做更新的时候
[00:54] 如果是否需要去查悟一条新的数据如果数据不存在的时候是否查悟一条新的数据默认的是False就是不落插入如果有必要我们可以把它设置为True那么下面这个参数是指什么呢就是说默认情况下面我们根据这个查询条件那么查询出来的可能会有多条数据那么我们更新了只会更新它的第一条这个数据那么其他是不做更新的如果我们把这个设置为什么的设置为True的话
[01:24] 那么他就会更新我们根据这个条件所查询出来的所有的数据哎OK那么最后一个这个呢是他的一个日志的这个异常的一个级别那这个我们很少去使用往往这两个我们可能会用到哎OK好那我们下面就来演示一下他如何去做一个查找那么我们来看一下现在我们现有的数据是不是这么多啊那我们来看一下如何去做一个更新呢比如说我们来更新啊这个第一条这个数据
[01:53] 我们把它这个年龄呢改成25怎么改呢我们这么来玩是不是通过db.user.update那么update是不是一个方法然后呢前面的这个是一个查询一个字段那么条件是不是就是根据ID等于1对吧然后呢我们在这个位置呢来一个大括号ID冒号1那么这个就代表了它的一个query查询条件那么我们根据这个它来查询我们的数据
[02:21] 那么查询到之后呢我们去做一个修改修改什么呢同样也是一对大括号然后呢使用一个dollar setset什么呢冒号set是一个里面的又是一个大括号就是我们设置什么呢设置age年龄是25ok这样的话呢我们回车那我们可以看到它的一个响应结果呢是这样的这个呢是叫做matches就是一个匹配那么匹配了几条呢匹配了一条数据
[02:51] 对吧然后呢这个是Urban Set就是我们数据不存在的时候是不是要做一个插入那是0没有做插入然后呢这个是Multified就是我们做一个数据的一个修改那么修改几条呢修改一条OK好那么我们来查看一下我们这个数据到底有没有去做一个修改呢我们会发现这个A字是不是已经被修改了修改成25那么OK那么但是有同学在没有去
[03:20] 没有去做学习的时候可能会有一种误以为就是说我们update是不是应该这样去写那么我来把这个改造一下把这个拿掉把这个拿掉来看一下那么是不是就是说前面呢是不是我们是它的一个条件后面的是它的一个更新的一个字段对吧那么我如果这样去写那么会怎么样呢来看一下那么这样去写的话那么我们就会导致一个情况就是
[03:47] 我们会将这条数据的所有的一些这个字段做一个重新的一个覆盖那么也就是说非Age这个字段已经被删除了看到没有什么像NameID已经就没有了因为这样的话其实是做一个字段的一个覆盖所以说我们做我们做我们这个数据做一个更新的时候一定要通过这个什么DollarSet去指定你的哪些字段去做一个修改
[04:15] 这一点啊一定要注意啊一定要注意OK这个啊要注意如果这样去写会删除其他的一些字段这个我们刚刚是不是也演示过了OK好那么接着我们继续往下面看那么如果还有的情况就是当我们去更新一个不存在的字段的时候那么会怎么样呢他会新增这个字段哎OK那么你比如说我们更新一个字段那么我们db.user然后点什么呢update
[04:44] 然后我们条件什么ID冒号2因为冒号1不行了因为1那条数据已经被我们删除了冒号2然后它要更新什么我们来看一下更新$set冒号再来一个大括号然后这个里面要更新比如说更新sex它的性别这个字段设置为1但是我们这个sex性别这个字段
[05:07] 在我们的这个数据中本身是不是就没有你看二这条数据本身是不是就没有那么这个时候它会怎么样呢我们来看一下那么其实我们可以看到它是不是它的修改数也是为1那么也就是说这个数据肯定被修改了对不对但是修改成什么样呢我们来看一下那么会发现它已经新增了这样的一个字段所以这一点大家也要注意了就当我们去修改它的一个
[05:31] 不存在字段的时候呢其实相当于是给他去做一个新增这样的一个字段那其实有些时候呢我们是不是当我们需要给某些这个数据给他新增一些字段的时候是不是就可以采用这种方法来做一个实现啊OK好那么下面我们接着继续看下面这个例子啊就是说当我们去更新一个不存在数据的时候那么默认的是不会去做一个新增数据的那么比如说
[05:59] 那么我现在呢我要去做这样的一个更新更新我的这个ID等于5的这样的一条数据把它的age改成25那么你会发现它这个match是不是匹配是不是就是0那么当我们去做一个这个更新的时候默认情况下面这条数据不存在那么就肯定不会做更新了所以这三个全都是0但是如果我们给它在后面是不是有可选参数
[06:26] 把这个第一个设置为chill的话那么就意味着什么呢来看一下就意味着我们已经呢你可以看到它的匹配数是0但是它的一个新增数是变成了1了也就是说它虽然没有匹配到这个数据但是它可以去做一个新增数据那我们来看一下这个数据有没有被插入呢可以看到这个数据是不是就已经插入进来了它的字段就是有个ID然后呢有一个age好那么这样的话呢就是
[06:56] 我们是不是可以做到当你这个数据不存在的时候我可以帮你去新增这样条数据那么我们最后一个参数最后一个参数来看一下是不是就是在在这个位置在这个位置OK在这个位置好那么给它设置为错那么这个数据就新增好了好那么这个其实就是我们就是我们所讲的这样的一个关于我们的一个就是更新数据的一个操作OK
[07:26] 那么这个update的操作就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

