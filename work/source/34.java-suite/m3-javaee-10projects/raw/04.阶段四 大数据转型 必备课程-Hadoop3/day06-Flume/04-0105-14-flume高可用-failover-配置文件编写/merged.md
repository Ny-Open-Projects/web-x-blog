# 14-flume高可用-failover-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\14-flume高可用-failover-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 时长 9分25秒（音频 566s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在讲完这个案例的模型之后呢接下来我们来实现这个案例来看讲义首先第一步的话呢我们需要安装Floam因为我们是要搞Floam集群那么三台主机呢都要安装Floam而我们的Node02和Node03已经安装好了接下来我们给第一台机子安装Floam怎么做呢非常简单我们呢可以把第二台的Floam
[00:29] 直接拷贝到第一台就可以了scp-r apache-flom然后拷贝到node01这个主机pwd 走稍等拷贝完之后还有一个东西我们要拷过去就是这个文件夹这个文件夹下面有一个shell脚本还有一个文件我们也拷进去来 这样的话scp-log
[01:01] 前面加个-r然后呢拷贝到我们的还是node01这个当前的目录下走好拷贝完之后呢我们来看一下node0 exportexport service87好下面好再回到这里看看这里边有一个till logsok那么这个呢就拷贝完了好拷贝完了之后呢接下来我们来开始进行配置
[01:33] 那配置的话呢因为有三台主机都有Float我们一个一个来配先配置Node01Node01呢看我这个图Node01呢它需要去我们的文件中呢采集新的数据然后把这个数据呢通过Sync发送给Node02和Node03所有这个配置呢我们来看一下在这个Node01它的conf目录下面呢建一个urgent的conf文件我们来看一下
[02:05] 打开在这里我们来在这个UportCD的APAC conf这个目录然后呢我们agent2进的conf进来把这个配置文件直接拿过来来复制粘贴好粘贴完之后呢我们来分析一下这里的参数啊首先这个就不用说了是名字但是你看这个地方有一个很特别的东西
[02:39] 在启动flume的时候给urgent起了一个名字关键是这个syncsync4后面跟两个也就是说我们的这里的node01呢这个flume的sync呢有两个一个是k1一个是k2为什么有两个呢还是看这张图你看这个node01收到的结果呢可以给node02也可以给node03那么说明它的sync是不是有两个OK那既然咱再向下看
[03:08] 这个地方有一个叫sync groups这个呢其实就是sync组相当于呢两个sync组成了一个组这个组的名字叫GE好那接下来我们再看这个再看这个source这个source呢因为是从文件呢去获取增量数据它需要去监控一个命令的输出所以说呢这个地方呢是exec我们的这个type呢是exec表示监控一个命令就这个命令它来监控这个文件的变化
[03:38] 而前面这个呢我们可以把它删掉因为后面呢应该有配置我看一下在后面应该有配置我就那这样啊我还要加上去因为它后面应该是把它提前了OK这是签到的配置我们用的是CE好那接下来呢我们再继续哦稍等稍等稍等我再粘一下不小心把它删掉了再把它粘一次好过来好过来之后呢我们刚才看到哪里呢
[04:08] 我们刚才看到这个位置那接下来再向下看我们这里还有一个什么呢还有一个channel这个channel的话呢这个地方channel是一个type memory这个就不用说了对吧那这个地方呢是放在内存里边这是它的一个容量OK那下面呢还有一个问题你看这个sync有两个那在这里呢它先去配第一个也就是KE这个KE呢它这个地方呢这个类型呢用的是r
[04:38] 为什么用的是EVOR呢因为我们呢需要将这个数据呢发送到下一个agent所以说这个sync是EVOROK那么还有呢这个地方要要去指定一个hostname和port这个hostname表示我要发给谁我这个数据呢要发给node02这个主机我的端口是52020大家注意这是这是node02这个目的地它的一个配置那还有一个sync呢
[05:07] 还有一个think我们要设置think2来 向下走这个地方呢它的channel还是ce而第二个think呢它的类型也是ever表示我要发送给下一机的agent好 那这个地方呢有个node03表示呢我要发给node03这个主机也是这个端口也就是说它既配了node02这个agent也又配了node03好 那么接下来还有一个这个地方呢有一个叫think组
[05:36] G点sync4那这地方是指定是K1和K2OK最后呢这个地方呢最后这个地方呢指定的是这个sync组里边的一些参数比如说呢这个type呢表示一个failover这个failover呢叫故障转移就是说当我一个sync出现问题的时候呢另外一个主机呢会立刻进行替补达这个高可用的目的好那这里面还有一个叫priority
[06:05] 这个是什么意思呢这个表示每一个sync的一个犬值这个犬值是什么意思呢你比如说有两个sync有两个那这两个的话呢我这个数据到底是发给node02还是node03呢大家注意这个时候就看谁的犬值高犬值高的优先去接收这个数据所以说呢这个priority是犬值那这个node02它的犬值高它就优先接收数据而node03呢只能等待
[06:35] 如果哪一天node02挂掉了那么这个时候呢它就会把数据发给这个sync也就是node03最后一个最大惩罚时间就是如果说一个机子挂掉之后呢在这个时间这里呢它不能再接受新的数据OK这是它的一个配置OK我们把它保存一下那看完这个node01之后呢接下来我们来再看node02和node03的配置我们来看一下好咱们下一下饭
[07:04] 咱们先看node02在node02的conf下面呢需要建立这么一个文件来我们来看一下需要建立这么一个文件叫collector收集器的意思打开这个我们来进入apacheconf这个目录我们来新建一个collectorconf好把这个数据呢拿过来复制一下好 粘贴好 咱们从上到下看一下首先呢这个地方呢没什么好看的
[07:39] 这个channel memory而这个source是一个ever这个地方要绑定自己的一个IP和端口这个端口一定要和node01的端口一致好后面这个地方呢表示我的数据是放在hdfs有个文件夹叫flume下面一个failover大家以后记住待会呢会看到这个文件夹的出现好这个基本上呢其他的配置呢都是我们见过的这个文件的类型啊
[08:08] 写入的格式啊文本呢还有滚动的一些周期啊等等OK那这个呢我们就保存退出咱们接下来呢再看看node03node03进到conf在node03下呢我们再来node03呢我们也去建一个collector.conf好在这里走一下把这个内容呢粘贴进来把这个内容粘贴进来OK复制粘贴
[08:42] 好 粘贴之后呢我们来看一下这个node03呢它这个地方呢channel也是memory它的source也就是它的源呢是接收上一级的一个sync所以说是everal好 它绑定自己的node03502050 520 20好 后面呢是它sync的一些这个一些设置它也是hdfs它要在flume failover下面呢去创建一些文件和文件夹好 那么这个也配置好了
[09:12] 那么到此为止呢我们就把整个的Floom集群呢给大家配置好了那么其实就是三个配置文件三个配置文件好那么配置完之后呢我们先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在多节点环境中配置Flume NG Agent，实现日志数据的采集、传输与故障转移。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 展示了Flume NG Agent配置文档，说明将node03的Flume安装包和日志目录复制到node01，并配置agent.conf。
画面2: 展示了SecureCRT中Flume的文件传输进度，显示多个HTML文件已传输完成。
画面3: 与画面1内容相同，展示Flume配置文档。
画面4: 展示了在Typora中编辑agent.conf文件，同时SecureCRT中显示了文件传输进度。
画面5: SecureCRT界面空白，准备输入命令。
画面6: SecureCRT中显示了agent.conf文件的配置内容，包括source、channel、sink的设置。
画面7: SecureCRT界面空白，准备输入命令。
画面8: SecureCRT中显示了agent.conf文件的配置内容，继续配置sink1和sink2。
画面9: SecureCRT中显示了agent.conf文件的配置内容，配置了failover机制。
画面10: SecureCRT中显示了在node02上执行命令，将taillogs目录复制到node01。
画面11: SecureCRT中显示了agent.conf文件的配置内容，配置了sink写入HDFS。
画面12: SecureCRT中显示了在node03上执行Flume服务的停止命令。
画面13: 展示了在Typora中编辑collector.conf文件，配置了source、channel、sink。
画面14: 展示了Flume架构图，说明node01采集数据并发送到node02或node03，实现failover。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
cd /export/servers
scp -r apache-flume-1.8.0-bin/ node01:$PWD
scp -r shells/ taillogs/ node01:$PWD
```
画面4:
```
#agent1 name
agent1.channels = c1
agent1.sources = r1
agent1.sinks = k1 k2
```
画面6:
```
agent1.sources.r1.channels = c1
agent1.sources.r1.type = exec
agent1.sources.r1.command = tail -F /export/servers/taillogs/access_log
```
画面8:
```
agent1.sinks.k1.type = avro
agent1.sinks.k1.hostname = node02
agent1.sinks.k1.port = 52020
agent1.sinks.k2.type = avro
agent1.sinks.k2.hostname = node03
agent1.sinks.k2.port = 52020
```
画面9:
```
agent1.sinkgroups.g1.processor.type = failover
agent1.sinkgroups.g1.processor.priority.k1 = 10
agent1.sinkgroups.g1.processor.priority.k2 = 1
agent1.sinkgroups.g1.processor.maxpenalty = 10000
```
画面10:
```
[root@node02 servers]# cd taillogs
[root@node02 taillogs]# ls
access_log tail-file.sh
[root@node02 taillogs]# cd ..
[root@node02 servers]# scp -r taillogs/ node01:$PWD
```
画面11:
```
a1.sinks.k1.type=hdfs
a1.sinks.k1.hdfs.path = hdfs://node01:8020/flume/failover/
a1.sinks.k1.hdfs.fileType=DataStream
a1.sinks.k1.hdfs.writeFormat=TEXT
a1.sinks.k1.hdfs.rollInterval=10
a1.sinks.k1.channel=c1
```
画面13:
```
#set Agent name
a1.sources = r1
a1.channels = c1
a1.sinks = k1
```
画面14:
```
需求:
1:node01去采集一个文件的新增数据
2:node01采集数据之后发送给node02
或node03的flume的Agent
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14: 架构图显示了node01的Agent指向node02和node03的Agent，标注了failover。node01的Agent配置为Source: exec, Channel: memory, Sink: avro。node02和node03的Agent配置为Source: avro, Channel: memory, Sink: hdfs。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

