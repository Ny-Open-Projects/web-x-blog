# 3-flume案例-网络数据采集-Flume的配置

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\3-flume案例-网络数据采集-Flume的配置【海量资源尽在 ubkz.com】.mp4
- 时长 10分33秒（音频 634s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 接下来我们来继续我们继续讲这个案例刚才呢我们把Floom安装好那么安装好之后接下来的问题是如何使用Floom让它给我们采集网络数据呢其实使用Floom非常简单我们只需要呢在Floom的conf这个目录下面建一个配置文件就可以了好 那么这个配置文件呢你看 就在这里
[00:29] 这个配置文件里边有很多就是这些建制队这些建制队是来干嘛呢是对我们Flume的组件进行配置的我们回到刚才画的图我们说过这个Flume它的一个实例也就是Urgent有三个组件一个是Source一个是Channel一个是Think那我们在去设计这个配置文件的时候你需要将这三个组件分别进行配置
[00:58] 也就是一句话你要想使用flom就写配置文件然后对三个组件进行配置那怎么去配置呢咱们来先看第一个source咱们刚才说过source是干嘛的呢source是来配置我的数据来自哪里也就是说我要从哪里去收集数据OK那么我们接下来来看一下这个配置文件首先呢我们来看
[01:27] 在配置文件的呢前三行有这么三句话这三句话呢是A1.sources等于RE这给大家解释一下这个A1呢是agent也就是组件的也就是这个实例的名字这个实例的名字这个名字呢待会我们在启动这个flume这个任务的时候呢我们可以给它指定所以这个名字你先别急就是这个名字我们是我们自己来指定的叫什么都行
[01:57] 而这个Ogin的这个实例里边呢它的Sources也就是它的Source这个组件呢它的名字叫RE这个呢就是Source的名字这个名字你也可以随便写啊第二个组件呢是Thinks你看它都加个思意思呢它Source可以有多个Think呢也可以有多个那这里呢只有一个它的名字是KE而Channel呢这个是名字是CE也就是说这三句话呢
[02:27] 其实就干了一件事给我们的三个组件分别起了一个名字OK分别起了名字好起完名字之后呢接下来对这三个组件分别进行配置咱们先看第一个来配置source我把这三句话呢我们来截个图来分别来说明好把它放在我们这里我们来看好这三句话是用来配置我们的source也就是我们这个第一个
[02:57] 那么这个sources呢咱说过它是来标志着我从哪里去收集数据第一个A1是我们agent的一个名字sources那么sources里边有很多的sources我们来配置的是RE这个sourcesRE就是sources的名字那个type呢是类型就是说你要使用哪种类型的一个sources呢我们用的这个sources类型是Netcat
[03:25] 这个netcat是什么意思呢这个netcat呢是source的一种它专门呢是从网络的套接字某一个端口来监听数据这个呢我们不能改这是人家source中已经定义好的它是其中的一个那为了给大家讲清楚这个问题呢我们来可以顺便来看一下我们的这个Apache Flume的一个官方文档在这里有个get starter这个呢
[03:52] 表示的是我们的入门指南我们来看一下稍等好打开之后呢向下翻向下翻这里边呢有一个表格你看这里边有一些组件那么上面是channel我们来看这个source这个呢是全部我们可以使用的一个source也就是我们的source中间这个是类型就是你能使用哪些source呢exec你看这个就是netcat这个是source的一种
[04:24] 这Source一种你看它这里有个描述它这个描述它说这种Source它是一种Netcat类型的风格的TCP事件源你可以这样理解它专门是来监控一个TCP这个通信中数据流OK它可以监控这么一个信息好那么我们用它的正合适所以说这就是Source的类型叫Netcat当然了它还有其他类型
[04:53] 当我们用的时候依次给大家讲解好回到我们刚才的这个图里边我们来看这个是我们的NetCardSource类型我们讲清楚了那接下来呢我们刚才那个案例说怎么说呢说我们需要从某一个端口某一个主机的某一个端口去监听数据所以说呢这个地方有一个叫bund我要绑定一个IP那这个IP呢就是我第三台记载IP我要绑定这个IP
[05:22] 我要绑定这个端口我要从这个主机的这个端口中来监听网络数据所以这三个呢是来配置sauce的从网络中读取从这个主机的这个端口来监听数据OK这是sauce的配置我们讲完了那接下来我们来看第二个channelOKchannel那这个channel怎么配呢这个channel我们来看一下好那么这个地方呢有一个channel
[05:52] 我们把这三号呢也给大家复制一下来放在这个位置好这是配置channel那么channel咱刚才说它起一个什么作用呢它是来去告诉我们你收集的数据暂时存在哪里那所以说呢这个地方呢它有一个叫typea-channels.c-type就是a这个实例它的channels中的第一个c这个channel它的类型是memory这个memory呢
[06:29] 它是一个channel的类型表示我的数据呢是存在内存中的所以说这个数据存在内存中那后面这两个是干嘛呢这两个的话呢它是来标志我这个channel的一个容量而这个capacity呢写的是1000其实1000一个单位这个单位呢咱们后面给大家讲它其实是1000个数据单位就是你这里边最多能存1000个数据
[06:57] 那这个里边有个单位叫event每一个数据呢它被称event所以说1000个数据单位OK还有一个transaction capacity这个表示一次处理的一个数据量是100OK那么这这个关于这个数据量呢它的大小呢我们先知道它是存大小的一个单位OK那么这个呢咱先放着也就是这个channel把它设置完之后呢我们知道
[07:26] 这个数据是存放在内存中的而且呢它的大小呢通过这两个参数来设置哦这就完了那既然呢还有个sync还有个sync我们再来看这个sync呢它是什么意思呢这个sync它表示我们的数据要下沉到哪里来我们来看这里边有这么一句话Aethinksktype我也把它拿一下来我们放在这位置好
[08:00] 这个是来配置think的这句话的作用呢就是我们think的类型呢用的是logger这个logger什么意思呢这个logger呢就是把我们从channel收集的数据呢把它通过一个日志也就是把它放到一个日志系统里面去那我们最终呢可以把这个日志呢打印到我们的控制台那我们就看到一个结果所以说这个表示它的一个think
[08:28] 我们最终的数据呢是存到一个日志系统OK那么这三个呢就配置好了配置好之后呢还缺少一个你需要呢将这Source ChannelSync这三个组件整合在一起所以说我们还需要一个配置来我们来看讲义最后呢有这两句话这两句话的作用呢是将Source ChannelSync之间关联在一起我们来看一下这两句话的一个配置好把这给我站在这里
[09:00] 看第一句话A1.sources.rechannel4也就是说A1它这个source里边re这个source它使用的channel是谁呢是CE那CE其实就是channel的一个名字而这个think呢它这个KE这个think它用的这个channel也是CE也就是说我source用的channel是它我think用的channel也是它那这样子它们三个就关联在一起了OK这是
[09:30] 他们的一个配置所以说我们只需要呢写这么一个配置文件就可以了那这个配置文件呢放在哪里呢我们需要把它放在conf这个目录下面这个名字你随意写来这样子我们来把这个做一下好这是它这个文件的名字叫netcatlogger.config我把这个名字复制一下我们来建一下这个文件好在这里我们呢在这个conf目录我们来
[09:59] 建一个文件好粘一下在这里呢把我们讲义上这些配置信息全部复制过来复制一下稍等好复制过来之后检查一下看看有没有问题好没有问题保存退出那这个呢就配置好了配置好之后呢我们回到讲义我们接下来呢就可以启动我们的flume让它们让它呢给我去工作
[10:30] OK那我们呢先把这个视频呢先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Apache Flume 的 netcat logger 示例，包括编写配置文件、查看官方文档和理解 Flume 架构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Flume 配置文件 netcat-logger.conf 的开头部分，定义了 agent 中的 source、sink 和 channel 名称。
画面 2: 展示了配置文件中 source 组件的配置，包括类型为 netcat、绑定地址和端口。
画面 3: 展示了配置文件中 sink 组件的配置，类型为 logger。
画面 4: 跳转到 Apache Flume 官方 Confluence 页面，显示“Getting Started”部分。
画面 5: 在 Confluence 页面中滚动，显示了 Flume NG 的 Channel 类型列表，包括 memory、file、jdbc 等。
画面 6: 在 Confluence 页面中继续滚动，显示了 Flume NG 的 Source 类型列表，包括 exec、netcat、seq 等。
画面 7: 展示了配置文件中 channel 组件的配置，类型为 memory，容量和事务容量。
画面 8: 展示了配置文件中 source 和 sink 之间的连接关系，即 source.r1.channels = c1。
画面 9: 展示了 Flume 架构图，包含 Source、Channel、Sink 三个组件，以及它们的配置参数。
画面 10: 在架构图中添加了 sink 的配置参数。
画面 11: 展示了在终端中执行命令，准备启动 Flume。
画面 12: 展示了配置文件中 source、sink 和 channel 的配置部分。
画面 13: 展示了终端中执行的命令，用于启动 Flume。
画面 14: 展示了配置文件中 source、sink 和 channel 的配置部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
# 定义这个agent中各组件的名字
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# 描述和配置source组件: r1
a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444

# 描述和配置sink组件: k1
a1.sinks.k1.type = logger

# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 2:
```
export JAVA_HOME=/export/servers/JDK 8.0_141
```

画面 3:
```
# 描述和配置sink组件: k1
a1.sinks.k1.type = logger
```

画面 7:
```
# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
```

画面 8:
```
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 9:
```
1: 从哪里采集 Source
2: 对采集的数据进行临时存储 Channel
3: 将采集的数据存入存储系统 Sink

Agent

a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444

a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
```

画面 10:
```
a1.sinks.k1.type = logger
```

画面 11:
```
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

画面 13:
```
a1.sinks = k1
a1.channels = c1
# 描述和配置source组件: r1
a1.sources.r1.type = netcat
a1.sources.r1.bind = 192.168.174.120
a1.sources.r1.port = 44444
# 描述和配置sink组件: k1
a1.sinks.k1.type = logger
# 描述和配置channel组件, 此处使用是内存存储的方式
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# 描述和配置source channel sink之间的连接关系
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9: 架构图显示了 Source、Channel、Sink 三个组件，Source 指向 Channel，Channel 指向 Sink。
画面 5: 表格列出了 Channel 类型，包括 memory、file、jdbc 等。
画面 6: 表格列出了 Source 类型，包括 exec、netcat、seq 等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

