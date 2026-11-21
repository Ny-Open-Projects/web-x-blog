# 7-flume案例-目录数据采集-运行测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\7-flume案例-目录数据采集-运行测试【海量资源尽在 ubkz.com】.mp4
- 时长 5分48秒（音频 349s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把第一步做完了那接下来呢我们再做第二步启动一个flume的agent实例怎么去启动呢我们来看打开我们的服务器在这里启动的话也是一个固定的步骤我们先回到我们的主目录在这里这里的话我们运行一个命令我们来看启动flume并flume ng这个是固定的来这个是启动agent实例
[00:30] 后面呢指定一个我们的配置文件的名字这个名字不能写错-n后面跟的是我们agent的名字好那么和这个地方呢表示我最终的信息呢输出到这个我把这些日志信息呢输出到控制台OK我的信息级别呢是一个info级别好我们直接来运行好在这里我们来执行一下走好稍等那么这个时候程序呢就卡在这里阻塞在这里
[01:02] 等着我们向那个目录中的添加文件不要忘了我们的初衷我们的初衷是什么呢我们最初的初衷呢看我画的这个图我们需要监控这个目录的文件变化一旦我向这个目录中的去添加一些文件那么他立刻就对我的文件精彩极那如何向这个目录中添加文件呢我们可以这样做我们可以借助一个工具在这里呢
[01:33] 我这里有一个叫文件上传工具那么在座各位呢可能也有各种一些Linux和Windows之间上传的工具我这是这个叫Square CRTPortable我们来打开看一下稍等这个地方呢他说我这里稍等我这里已经打开过了我先把以前的关掉我再试一下再试一下走稍等他说我已经打开过了
[02:10] 我应该是点下面的一个来我们打开一下稍等点是好我们连一下好连一下之后呢它这个地方我之前已经配过这个地方呢表示你要连接哪个主机这是一个这是一个Windows和Linux之间的传输文件的一个工具这个工具非常多我用的是一个CircleFXOK我们直接连接一下好连接完之后呢那这个时候我们来看连上连上之后呢
[02:39] 这个就是我们的windows下面呢是我们的linux下面是我们的linuxoklinux呢已经加载过来了ok那接下来我要干什么事情呢我们来看我们要进到linux这个我们要监控的这个目录这个目录是exportservice然后在这个里边呢有一个有一个叫什么有一个叫drfile这个目录那接下来我要做一件事情我桌面上有个a.txt
[03:08] 我要把这个A.txt文件呢我拖过来让它给我实现一个监控我来看一下好 我把它拖过来走 拖过来之后呢我刷新一下你会发现这个A.txt变成了A.txt complete这个加了一个complete之后呢就表示我这个文件被Floom已经采集过了Floom采集过了好 采集过了之后呢咱们再看控制台你会发现呢这地方它
[03:38] 它报了一个错误是吧它说那文件没有发现OK这个应该没关系这个应该是我拖的时候呢我可能拖了两次OK那这个地方我们来看的数据采集了没有采集了没有好怎么看呢我们来打开我们HDFS打开HDFS打开之后呢我们在这个根目录下边有个叫spudia为什么要找这个呢是因为我们在写配置文件的时候呢我们指定是在这个spudia去看那个文件
[04:07] 然后这个地方呢费尔斯有个这个年月日进去进去之后有这么一个有这个日期走进去你看他给我们采集了两个文件OK这两个文件呢它的内容呢应该是我A.txt文件的一个内容我打开A.txt走那这个地方你看这里有三行它怎么采集呢我们可以来看一下点开这个来当一下我们来当一下好稍等打开稍等一下
[04:42] 好打开了打开之后我们来查看一下好你看这是第一个文件aabb那第二个文件不用说了就是我们剩余的cc也就是他确实采集了那么问题是他为什么会生成两个文件呢是因为啊我们在配置的时候呢来看我的图我们在配置的时候呢哎我那个我那个图这样我先看这个我配置的时候呢我设了几个一些文动文件的滚动方式有多长时间生成一次呢你看
[05:11] 这里边每隔三秒还有呢文件的大小还有呢这个这个文件的一分的个数这里边呢其实这几个只要有一个触发呢它就会生成一个新文件可能是这个触发了就是说文件达到20个字节我就会生成一个新的文件那么大家呢可以去下面的去自己去把这些条件呢可以调一下然后看它的文件的生成方式OK那么这个说明了我们对于目录的数据的采集呢已经完成了
[05:41] OK那么关于这个从目录中监控文件数据的变化采集数据呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置并启动Flume Agent，将本地文件数据采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示Flume Agent架构图，包含Source、Channel、Sink三个组件，并列出实现步骤：1) 写配置文件；2) 配置Source；3) 配置Channel；4) 配置Sink；5) 启动Agent；6) 运行测试。同时展示配置文件中各组件的配置示例：
al.sources = r1
al.sources.r1.type = spooldir
al.sources.r1.spoolDir = /export/servers/dirfile
al.sources.r1.fileHeader = true
al.channels = c1
al.channels.c1.type = memory
al.channels.c1.capacity = 1000
al.channels.c1.transactionCapacity = 100
al.sinks = k1
al.sinks.k1.type = hdfs
al.sinks.k1.channel = c1
al.sinks.k1.hdfs.path = hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/
al.sinks.k1.hdfs.filePrefix = events-
al.sinks.k1.hdfs.round = true
al.sinks.k1.hdfs.roundValue = 10
al.sinks.k1.hdfs.roundUnit = minute
al.sinks.k1.hdfs.rollInterval = 3
al.sinks.k1.hdfs.rollSize = 20
al.sinks.k1.hdfs.rollCount = 5
al.sinks.k1.hdfs.batchSize = 1
al.sinks.k1.hdfs.useLocalTimeStamp = true
al.sinks.k1.hdfs.fileType = DataStream

画面2：
要点：展示Flume配置文件的Channel部分配置及参数解释，以及启动Flume的命令：
bin/flume-ng agent -f ./conf/spooldir.conf -n al -Dflume.root.logger=INFO,console

画面3：
要点：展示Flume Agent启动后在SecureCRT终端的输出日志，显示Source和Sink组件已成功启动。

画面4：
要点：再次展示Flume Agent架构图，标注了Source、Channel、Sink三个组件及其容量参数（batchSize、transactionCapacity）。

画面5：
要点：展示SecureCRT终端中上传文件的命令提示，以及文件夹中包含的SecureCRT相关配置文件。

画面6：
要点：展示SecureCRT终端的空白界面，无任何操作。

画面7：
要点：展示Windows资源管理器中包含的文件，如ZooKeeper.out、install.log、anaconda-ks.cfg等。

画面8：
要点：展示SecureCRT终端中Flume启动后因找不到指定文件而报错的日志，错误信息为：
Could not find file: /export/servers/dirfile/a.txt (No such file or directory)

画面9：
要点：展示HDFS浏览器界面，路径为/spooldir，显示一个名为“files”的目录。

画面10：
要点：展示HDFS浏览器界面，路径为/spooldir/files，显示两个文件。

画面11：
要点：展示HDFS浏览器中对文件“events-1557455020423”的块信息弹窗，显示其Block ID、Block Pool、Generation Stamp及可用性（分布在node02.Hadoop.com、node03.Hadoop.com）。

画面12：
要点：展示EditPlus文本编辑器，内容为空。

画面13：
要点：展示Flume配置文件中Sink部分的配置，其中hdfs.path配置为：
hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/

画面14：
要点：展示HDFS浏览器界面，路径为/spooldir/files/19-05-10/1020，显示两个文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
al.sources = r1
al.sources.r1.type = spooldir
al.sources.r1.spoolDir = /export/servers/dirfile
al.sources.r1.fileHeader = true
al.channels = c1
al.channels.c1.type = memory
al.channels.c1.capacity = 1000
al.channels.c1.transactionCapacity = 100
al.sinks = k1
al.sinks.k1.type = hdfs
al.sinks.k1.channel = c1
al.sinks.k1.hdfs.path = hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/
al.sinks.k1.hdfs.filePrefix = events-
al.sinks.k1.hdfs.round = true
al.sinks.k1.hdfs.roundValue = 10
al.sinks.k1.hdfs.roundUnit = minute
al.sinks.k1.hdfs.rollInterval = 3
al.sinks.k1.hdfs.rollSize = 20
al.sinks.k1.hdfs.rollCount = 5
al.sinks.k1.hdfs.batchSize = 1
al.sinks.k1.hdfs.useLocalTimeStamp = true
al.sinks.k1.hdfs.fileType = DataStream

画面2：
bin/flume-ng agent -f ./conf/spooldir.conf -n al -Dflume.root.logger=INFO,console

画面8：
Could not find file: /export/servers/dirfile/a.txt (No such file or directory)

画面13：
hdfs://node01:9000/spooldir/files/%y-%m-%d/%H/

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：
架构图：Source → Channel → Sink
结构：Source指向Channel，Channel指向Sink。
表格数据：无。

画面4：
架构图：Source → Channel → Sink
结构：Source指向Channel，Channel指向Sink。
表格数据：无。

画面13：
无PPT标题或架构图。

5) 无。

