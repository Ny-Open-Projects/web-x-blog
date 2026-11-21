# 11-flume案例-flume级联-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\11-flume案例-flume级联-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 时长 8分11秒（音频 492s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 讲完这个集联的模型之后呢接下来我们就分布实施这个案例好来看一下我们的讲义这里呢我们需要分几步呢122345我们需要做五步咱们先看第一步第一步的话呢我们需要在node02这台机子上安装一个flow因为我们把两个agent呢放在不同的主机上那你node03有你node02是不是也得有啊好
[00:28] 怎么安装呢我们可以把第三台机子上已经配好的这个Flume发送到我们的Node02上来我们来做这个事情好非常简单打开我们的服务器在这里呢我们回到上一集SCP Apache Flume然后呢这个地方呢我们应该加个-R参数因为我们复制的是一个文件夹复制到哪里呢复制到Node02这台机子上而且是当前目录
[00:58] pwd 走稍等好 复制完了之后呢接下来我们来继续看好 那么这个时候呢我们需要在node02上配置我们的flom也就是说我们还是需要再写一个配置文件这个配置文件叫名字叫till ever ever logger那我们就按照这个名字来写吧好 在哪里写呢我们需要在node02上记住是node02别搞错了回到这个node02
[01:30] 就是100这台机子上稍等一下好在这里呢我们需要export Service apache flow好在这里面有个configure目录configure目录我们在这里呢需要去新建一个文件好新建文件就这个文件这个文件里边呢我们把我们的这个对三个组件的配置信息啊全部复制过来复制完之后我们做一个简单的分析好拿过来
[02:01] 粘在这里好拿过来之后呢我们来看一下这里边它的一些信息看记住这是node02那么sauce sync channel是三个别名然后呢咱先看sauce先看我刚才画的一张图那么对于node02来讲它的sauce是不是还是来自一个文件的一个命令的结果togarf所以说它的sauce是esc它的channel是memory它的sync是everok来看一下
[02:31] 那这个地方呢sauce type是esc它来监测什么呢它来监测这个还是这个文件它的一个信息那现在这个文件是不是还不存在记着我们待会要创建这个文件好那么这个这个地方它说它的channel是ce就这句话应该是放在最后说这句话你可以把它删掉把它一个删掉OK好了那么接下来这个地方呢
[02:58] 是接下来是什么呢接下来是我们的channel我们先看channel吧好channel的话呢我们用的是memory对吧我们用memoryOKchannel它的容量是1000translocation呢是100OK这个也没有什么太多问题再看sync关键是我们的sync我们的sync呢注意我们的sync它的type呢是ever也就是说我们下一集我们的这个我们的数据呢要给谁呢
[03:27] 给我们的下一个agent所以说这个地方是ever好ever完之后呢大家注意如果你的think是ever我们刚才说过了你还要配置两个东西一个是host name一个是pot也就是说你要去指定你把这个数据发给哪个主机哪个端口大家一定要注意这个地方呢我的IP是174174要跟你自己的IP来设我把这里呢
[03:56] 也改成174稍等否则它是连不上的OK改成174好改完之后呢那接下来再看最后一个最后两行呢就是将它们连在一起source定的channel是cesync定的这个channel也是ceOK那么这个呢就配置完毕了好配置完毕配置完毕之后呢我们来保存退出OK好那么这个做完之后呢接下来我们继续看
[04:26] 想想看我们还需要干嘛呢我们第三步像这个这个我们还需要在node02上呢干嘛呢去建一个文件夹这个文件夹叫tilslogs并且呢在这个文件夹的下面上创建一个文件什么意思呢你看刚才呢我说这个目录在node02上不存在的这个文件也不存在我们可以手动创建一下了也非常简单你看直接呢make dr把这句话粘进来
[04:55] 好把后面的干掉好然后呢再touch一个再粘过来粘了两次来touch一下再粘一下怎么了粘两次ok把这个后面的也去掉吧来我们要创建这么一个文件来走那是不是就完成了就在node02上有这么一个文件我要监控这个文件好完了之后咱们继续再看这是第三步第四步呢我们需要配置node03node03
[05:26] 也需要去写一个config文件叫EverHDFS Config这个名字尽量一致因为后面在启动这个Floom的时候它都是以这个名字为准好那我们接着回到node03别搞错了node03我刚才是node02node03在这里在这里的话我们apache floom在这里我们进到进到conf然后在这里
[05:56] 我们来建一个文件好在这里呢我们要去把node03的一个三个组件的配置也复制一下来复制好然后粘贴好粘贴完之后呢我们来看一下这里的配置在看之前呢我希望大家再看一下我刚才画的图node03的三个组件呢source是evil而memory呢这个channel是memorysync是hdfs待着如果你的source填的是evil
[06:30] 你还需要绑定IP和端口为什么呢我们刚才看了一个官方文档你看这个EVER SOUCE它需要BEND和PORT绑定IP和端口OK那所以说我们来看这个配置来看一下好在这里的话呢我们从上到下看一下吧这个地方是别名没什么好看的而这个SOUCE EVER要绑定一个IP和端口注意这里的IP和端口一定要和Node02
[07:00] 我这里指定的这个来向下看指定的这个hostname和钻口要一致否则它的数据是连不通的好有了这个之后呢我们来继续向下看那这里边呢还有呢它会在把这个地方是这个地方它还会把这个数据呢放到这个这个我们的HDFS这个目录HDFS放在这里待会呢我们就这个目录呢去查看是否能生成我们定用的文件信息
[07:30] 好那这些信息呢基本上我们都分析过了这个文件的滚动周期啊滚动的一些大小啊等等好最后呢这个地方呢还有一个什么还有一个啊这是channel还有一个呢把它们串在一起OK这个也没有什么太多新的东西OK整个的话呢这个配置文件里边最值得大家看的就是这个sauce注意它用的是EverSauce别的都和之前是一样的OK那我就配好了
[07:58] 好 拍好之后呢接下来我们来看好 那我们做到第四步了第五步呢我们需要去顺序启动来启动我们的程序那这样我们先把这个视频呢先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在两台节点（node02 和 node03）上配置 Flume，实现从 node02 采集日志并转发到 node03，最终将数据写入 HDFS。

2) 按时间顺序列出每张画面的要点：
   画面1：展示 Flume Agent 的架构图，node02 上的 Source（exec）通过 memory Channel 连接到 Sink（avro），并标注“收集文件的数据 tail -F access_log”。
   画面2：PPT 页面显示“Step 1: Node02 安装 Flume”和“Step 2: Node02 配置 Flume”，并给出在 node02 上执行的命令：cd /export/servers && scp -r apache-flume-1.8.0-bin node02:$PWD。
   画面3：PPT 页面显示“Step 2: Node02 配置 Flume”，并给出在 node02 上执行的命令：cd /export/servers/apache-flume-1.8.0-bin/conf && vim tail-avro-logger.conf。
   画面4：PPT 页面显示“Step 3: 开发脚本向文件中写入数据”和“Step 4: Node03 Flume 配置文件”，并给出在 node03 上执行的命令：cd /export/servers/apache-flume-1.8.0-bin/conf。
   画面5：在 SourceCRT 中编辑配置文件，内容为：
   # Name the components on this agent
   a1.sources = r1
   a1.sinks = k1
   a1.channels = c1
   # Describe/configure the source
   a1.sources.r1.type = exec
   a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
   a1.sources.r1.channels = c1
   # Describe the sink
   ##sink露说腔vro胸一贴枚莘茎脣脣
   a1.sinks.k1 = k1
   a1.sinks.k1.type = avro
   a1.sinks.k1.channel = c1
   a1.sinks.k1.hostname = 192.168.174.120
   a1.sinks.k1.port = 4141
   a1.sinks.k1.batch-size = 10
   # Use a channel which buffers events in memory
   a1.channels.c1.type = memory
   a1.channels.c1.capacity = 1000
   a1.channels.c1.transactionCapacity = 100
   画面6：在 SourceCRT 中编辑配置文件，内容与画面5相同，但光标位于 a1.sinks.k1.type = avro 行。
   画面7：在 SourceCRT 中执行命令 mkdir /export/servers/taillogs/，并显示成功创建目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
   画面2：
   cd /export/servers
   scp -r apache-flume-1.8.0-bin node02:$PWD
   画面3：
   cd /export/servers/apache-flume-1.8.0-bin/conf
   vim tail-avro-logger.conf
   画面4：
   cd /export/servers/apache-flume-1.8.0-bin/conf
   画面5：
   # Name the components on this agent
   a1.sources = r1
   a1.sinks = k1
   a1.channels = c1
   # Describe/configure the source
   a1.sources.r1.type = exec
   a1.sources.r1.command = tail -F /export/servers/taillogs/access_log
   a1.sources.r1.channels = c1
   # Describe the sink
   ##sink露说腔vro胸一贴枚莘茎脣脣
   a1.sinks.k1 = k1
   a1.sinks.k1.type = avro
   a1.sinks.k1.channel = c1
   a1.sinks.k1.hostname = 192.168.174.120
   a1.sinks.k1.port = 4141
   a1.sinks.k1.batch-size = 10
   # Use a channel which buffers events in memory
   a1.channels.c1.type = memory
   a1.channels.c1.capacity = 1000
   a1.channels.c1.transactionCapacity = 100
   画面7：
   mkdir /export/servers/taillogs/

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
   画面1：架构图中，Source（exec）指向 Channel（memory），Channel（memory）指向 Sink（avro）。
   画面2：PPT 标题为“分析”，内容为“第一个agent负责收集文件当中的数据，通过网络发送到第二个agent当中去，第二个agent负责接收第一个agent发送的数据，并将数据保存到hdfs上面去”。
   画面3：PPT 标题为“分析”，内容与画面2相同。
   画面4：PPT 标题为“Step 3: 开发脚本向文件中写入数据”和“Step 4: Node03 Flume 配置文件”。

5) 不要评价画面美观，不要输出与课程无关的内容。

