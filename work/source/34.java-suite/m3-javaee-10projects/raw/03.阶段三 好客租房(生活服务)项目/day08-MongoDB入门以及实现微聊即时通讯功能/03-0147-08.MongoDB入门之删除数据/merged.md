# 08.MongoDB入门之删除数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\08.MongoDB入门之删除数据【海量资源尽在 ubkz.com】.mp4
- 时长 4分45秒（音频 285s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面我们来看一下删除数据就是数据的删除那么我们可以通过remote这个方法来做数据的删除具体语法是这样的通过db.connection.remote去做一个删除然后我们可以看到它的一个参数就是一个query,就是查询条件根据什么样的条件去做删除我们的数据那么在下面有两个可选的参数那么一个叫just one那么这个是指什么呢
[00:29] 就是说如果我们把它设置为错的话那么只会删除一个是一条数据就是匹配的一条数据如果不设置的话默认是false然后是删除匹配所有匹配的一个数据比如说什么意思呢就是说我通过这个条件我匹配了有十条数据默认情况下面我是把这十条数据全部都删除但是如果你把这个
[00:52] 参数给它设置为chore的话它只会删除第一条就这个意思那么第二个这个跟上面一样就不说了就是一个抛出异常的一个级别这个我们就一般很少用好的我们来看一下那么具体的一个使用来看一下那么我们这么来玩吧然后我们来看一下我们去做一个db点什么呢url点一个remote根据一个条件什么条件呢比方说年龄都是25的这个条件去做一个删除
[01:21] 那么我们现在有几条数据是不是两条来看一下它是否能够删除两条你会发现是不是两条数据已经被删除了OK那么我们来查一下是不是只有剩下这两条数据了OK好那么我们接下来为了演示方便我们插入四条数据去做一个演示把它拷贝一下到我们这个位置来插入那么现在我们应该就会有有这么多数据了这样的话我们就演示起来就会方便一些了
[01:49] 好了我们接着继续往下面看那么如果我们把后面这个参数给它设置为设置为chew的话那么它呢只会删除一条你比如说我们现在年龄年龄为22的是不是有两条啊哎呦有啊年龄22有三条啊然后呢我们去给它做一个匹配比如说来看一下啊去做一个删除的时候如果我们匹配这个22那么如果我回车它一定会删除我们的三条数据对不对但是呢我在后面给它设置为一个chew
[02:17] 就代表着说我只删除你匹配掉数据的第一条然后呢可以看到是不是他只删除掉一条啊那么显然是不是把这第一条是不是给他删除了我们来看一下是不是呢来看一下哎呃是不是把第一条就删除掉了哎OK好那么这个是这样的一个操作啊那么如果我们想想把所有的数据做一个删除的话那我们可以使用这样的一个方式就是叫remoteremote什么呢把这个
[02:45] 把这个后面这个参数设置为False因为默认就False了所以把它删掉然后呢把这个参数呢给它拿掉就是说我们没有参数直接去做一个删除就代表着所有的数据可以看到这边已经删除掉五条数据了对不对OK好那么这个呢是它的一些基本的操作当然了在我们的这个MongoDB在新版本中它为了一些简化的一个操作呢官方推荐使用那种Delete这个操作
[03:13] 叫什么delete one和delete money去做一些这个操作那我们还是把这个去插入进来吧那我们做一些简单的一些这个演示啊现在呢我们是不是已经就有了有四条数据了来一个什么呢url点一个friend去查找可以看到是不是有四条数据那么下面我们来看一下通过这个delete one怎么去做一个查找呢是不是通过这个dbdb.url.delete
[03:42] delete什么的delete one是不是就是去删除一条数据比如说我们删除这个年龄age年龄是22的数据那么看一下它会删除几条呢来看一下是不是只会删除掉一条对不对那么来看一下删除掉哪条呢是不是把这一条是不是删除了往我那条数据删除了OK当然你也可以使用这种方式就是delete这个money显然就是
[04:12] 删除匹配多条那么跟我们讲义上面写的一样就是如果delete这个many的话那么没有条件代表什么呢是不是就会删除所有的数据OK这样的话那数据就会被删除了那么我们使用这种方式也可以你也可以使用设置为后面一个true和false来指定是删除一条还是多条
[04:34] 其实这种写法就delete1这种写法呢其实是更加的方便一点的对不对OK好那么关于我们数据的删除呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 MongoDB 中删除操作的多种方法，包括根据条件删除、删除单条记录、删除所有记录，并对比不同删除方法的语法和效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 db.collection.remove() 方法的语法和参数说明，包含代码示例。
画面 2: 在 Xshell 中执行 db.user.update() 更新年龄为 25 的记录，然后执行 db.user.remove(age:25) 删除匹配的记录，显示删除结果。
画面 3: 继续在 Xshell 中执行 db.user.find() 查询所有记录，确认删除操作后的数据状态。
画面 4: 在 Xshell 中执行 db.user.remove(age:25) 删除年龄为 25 的记录，显示删除结果。
画面 5: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 6: 在 Xshell 中执行 db.user.remove(age:22, true) 删除年龄为 22 的记录，显示删除结果。
画面 7: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 8: 在 Xshell 中执行 db.user.remove(age:22, true) 删除年龄为 22 的记录，显示删除结果。
画面 9: 继续在 Xshell 中执行 db.user.remove() 删除所有记录，显示删除结果。
画面 10: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 11: 在 Xshell 中执行 db.user.deleteMany({}) 删除所有记录，显示删除结果。
画面 12: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 13: 在 Xshell 中执行 db.user.deleteMany({}) 删除所有记录，显示删除结果。
画面 14: 展示 PDF 文档中关于 db.collection.remove() 方法的语法和参数说明，包含代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
db.collection.remove(
  query,
  {
    justOne: <boolean>,
    writeConcern: <document>
  }
)

参数说明：
• query: (可选) 删除的文档的条件。
• justOne: (可选) 如果设置为 true 或 1, 则只删除一个文档, 如果不设置该参数, 或使用默认值 false, 则删除所有匹配条件的文档。
• writeConcern: (可选) 指定抛出的级别。

实例：
> db.user.remove(age:25)
WriteResult({ "nRemoved" : 2 }) #删除了2条数据

加入几条测试数据
db.user.insert({id:1,username: "zhangsan",age:20});
db.user.insert({id:2,username: "lisi",age:21});
db.user.insert({id:3,username: "wangwu",age:22});
db.user.insert({id:4,username: "zhaoliu",age:22});

画面 5:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

画面 14:
db.collection.remove(
  query,
  {
    justOne: <boolean>,
    writeConcern: <document>
  }
)

参数说明：
• query: (可选) 删除的文档的条件。
• justOne: (可选) 如果设置为 true 或 1, 则只删除一个文档, 如果不设置该参数, 或使用默认值 false, 则删除所有匹配条件的文档。
• writeConcern: (可选) 指定抛出的级别。

实例：
> db.user.remove(age:25)
WriteResult({ "nRemoved" : 2 }) #删除了2条数据

加入几条测试数据
db.user.insert({id:1,username: "zhangsan",age:20});
db.user.insert({id:2,username: "lisi",age:21});
db.user.insert({id:3,username: "wangwu",age:22});
db.user.insert({id:4,username: "zhaoliu",age:22});

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
标题: 1.3.6. 查询数据
内容:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

画面 14:
标题: 1.3.6. 查询数据
内容:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

