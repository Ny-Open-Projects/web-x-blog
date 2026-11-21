# 4-flume案例-网络数据采集-启动flume

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\4-flume案例-网络数据采集-启动flume【海量资源尽在 ubkz.com】.mp4
- 时长 7分21秒（音频 442s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 把这个Floom配置完之后呢接下来我们就可以启动我们的FloomOK 怎么启动呢首先呢 我们需要有一个命令这个命令呢 我们可以查看一下我们的这个Floom官方文档来 点开点开之后呢 向下翻在这里呢 它说呢你要去启动的话呢 有这么一个示例你看 有个binbin下面有个Floom ng这个Floom ng呢 其实是Floom的一个版本
[00:30] OK后面呢跟上一些指定一些配置文件比如说这个地方一个杠F指定呢我们康复目录下边的某个配置文件那这个配置文件呢刚才咱们配置过后面呢这个地方呢是来指定我们的这个信息呀它的一个显示级别这地方显示一个debug级别而且把这个信息收集的信息显示到哪里呢显示我们的控制台上后面这个杠N呢
[01:00] 表示我们的一个agent的一个名字类似于这么一个命令那接下来我们来看我们的命令那在这里我们这里呢bin.flomng这是一个启动一个bin下面一个程序OK我们启动agent实例这个呢-cconf-f呢它是指定我们的一个刚才写的那个配置文件在conf目录下面有个netcat-logged-conf这个呢
[01:29] 是我们刚才配置了三个组件后面这个杠n呢它指定的是一个urgent的一个名字这个a1那这个a1呢你看我刚才的配置文件中是不是都是a1 a1.a1.这个a1就来自这里所以这个名字可以随便起但是必须和配置文件这个名字一致好那后面有一个杠这个叫rootlogger这个表示呢我最终显示的是一个infer级别的信息
[01:58] 把这个信息显示到控制台OK好那我呢把这个命令来执行一下我们来看一下好在哪里执行呢我们需要进到我们的上一集找到这个我们的主目录下面然后在这里好我再复制一下把它复制好复制完了走我们来执行走稍等好执行到这个位置的时候注意我们的程序呢就在这里卡住了它干嘛呢
[02:31] 它正在监听我们这个主机的这个端口监听这个端口有没有数据过来但是现在很显然我们是没有数据的那接下来呢我们是不是得用另外一台主机给它发送数据OK那么大家可以回想回想我们刚才画的一个图现在我是在这个mini2这台主机上我需要有另外一台主机给我发信息过来那怎么发呢我们在这里呢
[03:00] 我们可以使用一个TerranetTerranet命令OK通过这个呢来模拟数据的一个发送那么我们需要准备另外一台主机比如说Node02需要安装一个Terranet我们来试一下在这个110这台主机呢我们来yum-y install然后呢我们来装个Terranet稍等让它安装好安装完成安装完之后呢
[03:36] 我们这里边就可以使用这个命令叫Telnet这个Telnet怎么用呢后面跟上你的主机的IP或者主机名然后呢后面跟上你要发送的数据的一个端口我们的端口是多少呢我们的端口是是几呢是五个四那我们来这样做一下12345好我来发数据那这个时候呢它在这里等待你输入数据比如说我输一个hello
[04:05] 那我回车吧回车之后我们来看这里边有没有收到我们的数据你看到没有在这个地方呢它就有变化了它就收到了一个数据这个数据呢它里边说个event这个event呢其实是我们数据的一个单位我再发一个来比如说我再发一个我发一个发一个这个我再发一个吧发一个你好走咱们来看这个地方它又收到event那这个地方呢
[04:35] 你看有个hider有个body这个body呢其实这里边存放的其实就是我刚才的你好而且它这个地方是一个16进制你看后边是一个你好好那么说明我们的Floom确实是不是采集到了我们的日志数据啊好在这里呢我给大家呢解释一下这个event啊因为呢我们后边呢会多次使用这个关键字来我们来看一下打开我们的画图那么这里边呢我们这个里边有个组件叫channel
[05:05] 这个channel呢怎么去理解呢我把这个channel给大家放大一点大家注意我专门画这个channel放大一点拿过来拿过来这个channel呢就是一个管道一个通道好在这个channel里边呢其实它存放的是我们采集到的数据那我们采集到的数据呢其实采集一次呢它有一个数据这个数据呢
[05:47] 被称为一个一个的event这个数据被称为一个一个的event你踩了一条数据它其实就是event它就是event而这个event它被分成两部分那么这个event前面这个部分被称为hide也就是它的头部信息把它调小一点12这个是头部信息
[06:26] 而后面这个呢是我们采集到数据的一个正文也就是真实的数据这个呢叫body叫body把它放在这里好这个叫body那么当我们这个channel收集完数据之后呢其实在这个channel的内部它是由一个一个的event组成的OK这些数据呢event就像一个胶囊一样白加黑胶囊OK这是它的一个数据的特点所以说你会看到我们收集数据的时候呢这个地方你看hider
[07:00] 这里边数据是空的那body呢这里边放的是它的一个字节数组字节数据OK这是它的一个数据特点好那我们呢有了这个概念之后呢我们就可以在这个基础上呢做一些更丰富的一些案例好那么关于呢我们这个案例呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置并启动 Apache Flume Agent，通过一个简单的日志采集案例演示环境搭建和命令行操作。

2) 按时间顺序列出每张画面的要点：
   画面1：展示 Apache Flume 官方文档中关于 Source 和 Sink 组件的实现类列表，用于说明 Flume 的核心组件。
   画面2：显示课程 PPT 页面，内容为“Step 3: 启动配置文件”和“Step 4: 安装 Telnet 准备测试”，并附带启动命令和 Telnet 安装命令。
   画面3：在画面2基础上，鼠标光标移动到命令行区域，准备执行命令。
   画面4：在画面3基础上，鼠标光标在命令行区域停留，准备执行命令。
   画面5：切换到 SecureCRT 终端，显示 Flume 配置文件中定义的源和目标关系：a1.sources = r1 和 a1.sinks = k1。
   画面6：在画面2基础上，鼠标光标在命令行区域停留，准备执行命令。
   画面7：在 SecureCRT 终端中执行启动命令后，显示 Flume 启动日志，包括环境变量加载、Hadoop 库路径设置和 SLF4J 多绑定警告。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
   画面1：
   Component | Type | Description | Implementation Class
   --- | --- | --- | ---
   Source | syslogudp |  | SyslogUDPSource
   Source | org.apache.flume.source.avrolegacy.AvroLegacySource |  | AvroLegacySource
   Source | org.apache.flume.source.thriftLegacy.ThriftLegacySource |  | ThriftLegacySource
   Source | org.apache.flume.source.scribe.ScribeSource |  | ScribeSource
   Source | custom type as FOOV |  | (custom FOOV)
   Sink | hdfs | Writes all events received to HDFS (with support for rolling, bucketing, HDFS 200 append, and more) | HDFSEventSink
   Sink | org.apache.flume.sink.hbase.HBaseSink | A simple sink that reads events from a channel and writes them to HBase. | org.apache.flume.sink.hbase.HBaseSink
   Sink | org.apache.flume.sink.hbase.AsyncHBaseSink |  | org.apache.flume.sink.hbase.AsyncHBaseSink
   Sink | logger | Logs events at INFO level via configured logging subsystem (log4j by default) | LoggerSink
   Sink | avro | Sink that invokes a pre-defined Avro protocol | AvroSink

   画面2：
   Step 3: 启动配置文件
   指定采集方案配置文件，在相应的节点上启动flume agent
   先用一个最简单的例子来测试一下程序环境是否正常
   启动agent去采集数据
   bin/flume-ng agent -c conf -f conf/netcat-logger.conf -n a1 -Dflume.root.logger=INFO,console
   • -c conf 指定flume自身的配置文件所在目录
   • -f conf/netcat-logger.conf 指定我们所描述的采集方案
   • -n a1 指定我们这个agent的名字
   Step 4: 安装 Telnet 准备测试
   在node02机器上安装telnet客户端，用于模拟数据的发送
   yum -y install telnet
   telnet node03 44444 # 使用telnet模拟数据发送

   画面5：
   a1.sources = r1
   a1.sinks = k1

   画面7：
   Info: Sourcing environment configuration script /export/servers/apache-flume-1.8.0-bin/conf/Hadoop-env.sh
   Info: Including Hadoop libraries found via /export/servers/Hadoop-3.1.1/bin/Hadoop for Hive access
   Info: Including Hive libraries found via /export/servers/Hadoop-3.1.1/bin/Hadoop for Hive access
   + exec /export/servers/JDK 8.0_141/bin/java -Xmx20m -Dflume.root.logger=INFO,console -cp /export/servers/apache-flume-1.8.0-bin/conf:/export/servers/apache-flume-1.8.0-bin/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/tools/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/common/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/hdfs/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/yarn/lib/*:/export/servers/Hadoop-3.1.1/share/Hadoop/mapreduce/lib/*:/export/servers/Hadoop-3.1

