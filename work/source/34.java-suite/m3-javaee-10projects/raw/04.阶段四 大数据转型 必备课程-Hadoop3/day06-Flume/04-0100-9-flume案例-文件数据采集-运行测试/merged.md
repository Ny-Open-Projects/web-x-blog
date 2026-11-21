# 9-flume案例-文件数据采集-运行测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\9-flume案例-文件数据采集-运行测试【海量资源尽在 ubkz.com】.mp4
- 时长 6分19秒（音频 380s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在讲完三个组件的配置信息之后呢接下来我们把剩余的事情做完来打开我们的这个服务器首先呢我们需要呢进到这个export的flumconfig目录下面我们在这里呢我们来建一个配置文件这个名字呢和我们讲义保持一致我们来看好这里呢叫tel-f.conf
[00:28] 我们也叫这个名字好那么进来之后呢把我们这个配置信息拷贝进来也就是这一段配置信息拷贝的时候小心一点好把它拿过来好粘进去粘完之后呢检查检查一下开头好没有问题好没有问题之后呢大家注意这里的话呢它需要使用till-f命令呢去监控这个文件的一个变化
[01:01] 所以说我们先要去建这么一个文件这个路径我也复制一下我们保存一下保存退出接下来我要去建这么一个文件建这个文件先建一个文件夹make dir粘贴一下创建创建完之后我们来再建一个文件好建完了建完之后接下来我们来看讲义
[01:34] 那说到这里的话呢我们基本上把第一步做完了接下来我们来启动Floom启动Floom的话和之前基本上一样的只是说配置文件呢用我们刚才写过的一个配置文件而且这个杠N呢这个agent的名字呢是agent1这里面要注意好我们来启动来在这里启动的时候要回到Floom的一个主目录好在这里我们来看走好
[02:06] 让他呢在这里等待等待我们的一个输入OK那么等待之后呢接下来我们不要忘了他是来检测我们一个命令的输入而这个命令呢是检测我们文件的一个变化所以说呢我们需要呢在这个文件中呢写点数据哪个文件呢export Service然后呢这里边有一个有一个文件有一个目录这个目录是哪个呢我们刚才写的是一个
[02:36] 这个目录有一个叫我们来看一下有一个叫tell logs我们来进来好在这里边有这么一个文件那接下来呢我们需要向这个文件的写点数据好写点数据之后呢我们刚才这个命令就是tell-f就可以检测到那么我们的flume呢就可以通过这种source来收集那如何向这个文件写数据呢我在这里呢我写一个脚本
[03:05] 写个什么脚本呢我写个脚本然后呢通过这个脚本呢可以不停的向这个文件写数据来我们来看一下讲义好在这呢有这么一个脚本来看一下这个适要脚本这个适要脚本呢是一个我要循环度做这么两句话那么首先呢这个data呢它是一个命令可以获取当前的时间把当前的时间获取完之后呢追加到这个文件sleep 0.5呢
[03:35] 就是每隔0.5秒就会做这么一件事情这是一个循环然后呢接下来我把这句话呢我们复制一下然后放在一个脚本文件中这个脚本文件呢我们可以自己请个名字比如说叫tail-fail.sh好然后呢直接放进来放进来之后呢接下来我们需要做一件事情我们来运行这个脚本它就向这个文件中追加数据一追加数据
[04:05] 那我们的flume呢就能检测到这个数据就能收集数据来我看我们来执行适用脚本怎么执行呢我们用sh tail走稍等它就开始向我们的这个access.log这个文件写数据了写数据呢咱们来观察一下左边这个大家看看这地方有没有变化你看这地方呢它输出了这么一句话它说呢creating hdfs
[04:35] 他说在HDFS的weblogflom-collection下面创建了一个临时文件这个是不是就是正在收集我们刚才的数据呢好 我们来看我们去哪里看呢我们就去我们配置文件的这个目录在node01 8020这个weblogflom-collection看看有没有这么一个文件夹打开我们的HDFS好 在这里我们来刷新一下来看
[05:04] 你发现这个地方已经有了一个weblog我们点开有个Floom Collection进来这是一个年月日进来好再进来你会发现这里边已经收集了一个文件数据而我们的这个脚本的运行呢可能呢再过一段时间呢你看又多出来一个Tempo文件这个Tempo呢是一个临时文件当这个文件它的一些条件满足的时候呢它就会滚动出来一个新文件那这个临时文件呢
[05:33] 它有几个出发条件咱们在设置这个配置文件的时候呢给大家提过我们再回到我们的配置文件在这大家看在这里面呢有一个叫rule sizerule count还有呢rule interval这三个呢只要有一个条件出发那么它就会滚动出一个新文件OK这是一个临时文件再刷新一下你可能呢再过一会儿呢又有一个文件呢出来OK那么
[06:01] 这里呢就证明了我们这个代码是没有问题的我们这个配置也是没有问题的OK那么这个就是从监控一个文件的一个变化然后通过这个文件的变化呢来收集我们想要的数据OK那么关于这个案例呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置Flume Agent，将本地日志文件通过tail-F方式采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示Flume架构图（Source → Channel → Sink → HDFS），并列出实现步骤：1) 写配置文件；2) 配置Source；3) 配置Channel；4) 配置Sink；5) 组合；6) 启动Agent；7) 运行测试。同时展示配置文件中各组件的命名配置：agent1.sources = source1；agent1.sinks = sink1；agent1.channels = channel1。

画面2：
要点：在SourceCRT终端中新建配置文件“tail-file.conf”。

画面3：
要点：在Typora中展示Flume配置文件的完整内容，包含Source、Channel、Sink的详细配置。其中Source配置为exec类型，命令为tail -F /export/servers/taillogs/access_log，绑定到channel1；Sink配置为hdfs类型，路径为hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M，文件前缀为access_log，batchSize为100，fileType为DataStream等。

画面4：
要点：在SourceCRT终端中显示配置文件内容，并执行命令创建HDFS目录和日志文件。

画面5：
要点：在SourceCRT终端中执行命令创建HDFS目录和日志文件，同时在Typora中展示配置文件内容。

画面6：
要点：在Typora中展示Flume配置文件的完整内容，包含Source、Channel、Sink的详细配置。其中Source配置为exec类型，命令为tail -F /export/servers/taillogs/access_log，绑定到channel1；Sink配置为hdfs类型，路径为hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M，文件前缀为access_log，batchSize为100，fileType为DataStream等。

画面7：
要点：在SourceCRT终端中执行命令创建HDFS目录和日志文件，同时在Typora中展示配置文件内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
agent1.sources = source1
agent1.sinks = sink1
agent1.channels = channel1

画面3：
# Describe/configure tail -F source1
agent1.sources.source1.type = exec
agent1.sources.source1.command = tail -F /export/servers/taillogs/access_log
agent1.sources.source1.channels = channel1

# Describe sink1
agent1.sinks.sink1.type = hdfs
agent1.sinks.sink1.channel = c1
agent1.sinks.sink1.hdfs.path = hdfs://node01:8020/weblog/flume-collection/%y-%m-%d/%H-%M
agent1.sinks.sink1.hdfs.filePrefix = access_log
agent1.sinks.sink1.hdfs.maxOpenFiles = 5000
agent1.sinks.sink1.hdfs.batchSize = 100
agent1.sinks.sink1.hdfs.fileType = DataStream
agent1.sinks.sink1.hdfs.writeFormat = Text
agent1.sinks.sink1.hdfs.rollSize = 102400
agent1.sinks.sink1.hdfs.rollInterval = 60
agent1.sinks.sink1.hdfs.round = true
agent1.sinks.sink1.hdfs.roundValue = 10
agent1.sinks.sink1.hdfs.roundUnit = minute
agent1.sinks.sink1.hdfs.useLocalTimeStamp = true

# Use a channel which buffers events in memory
agent1.channels.channel1.type = memory
agent1.channels.channel1.keepAlive = 120
agent1.channels.channel1.capacity = 500000
agent1.channels.channel1.transactionCapacity = 600

# Bind the source and sink to the channel
agent1.sources.source1.channels = channel1
agent1.sinks.sink1.channel = channel1

画面6：
Step 2: 启动 Flume
cd /export/servers/apache-flume-1.6.0-cdh5.14.0-bin
bin/flume-ng agent -c conf -f conf/tail-file.conf -n agent1 -Dflume.root.logger=INFO,console

Step 3: 开发 Shell 脚本时追加文件内容
mkdir -p /export/servers/shells/
cd /export/servers/shells/
vim tail-file.sh

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
架构图：Source → Channel → Sink → HDFS
PPT标题：实现步骤
步骤列表：
1) 写一个配置文件：xxx.conf
2) 配置三个组件的名字
3) 配置Source
4) 配置Channel
5) 将Source, Channel和Sink组合在一起
6) 启动Flume的Agent实例
7) 运行测试

画面3：
PPT标题：2.2.1 Flume配置文件
步骤列表：
Step 1: 下载解压Flume安装包
Step 2: 开发配置文件
Step 3: 启动Flume
Step 4: 上传文件到HDFS
Step 5: Agent级联

画面6：
PPT标题：Step 2: 启动 Flume
Step 2: 启动 Flume
cd /export/servers/apache-flume-1.6.0-cdh5.14.0-bin
bin/flume-ng agent -c conf -f conf/tail-file.conf -n agent1 -Dflume.root.logger=INFO,console

Step 3: 开发 Shell 脚本时追加文件内容
mkdir -p /export/servers/shells/
cd /export/servers/shells/
vim tail-file.sh

5) 不要评价画面美观，不要输出与课程无关的内容。

