# 4.6 Flink安装配置

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.6 Flink安装配置_【海量资源尽在 666java.com】.mp4
- 时长 9分44秒（音频 584s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来学习Flink的安装和配置那么Flink运行呢一般分为三种模式即Local模式Standalone模式和On-Yarn模式这个On-Yarn模式中的Yarn其实就是Hadoop体系里边的一个资源管理平台那么Flink的整个运行环境可以在这一台这个资源管理平台上来运行那么我们今天呢主要给大家介绍Local和Standalone模式那么Local的话我们可以把本地
[00:28] 就是我们Flink程序在下载到我们本地的windows操作系统里边那么我们在启动起来之后呢我们的开发的程序直接在这上面来运行就可以了那么standalone呢我们可以把它配置成一个局群的有一个job manager或者有多个这种task manager那么通过这种方式来把我们的测试环境搭建起来
[00:51] 那我们现在可以看一看我们如何来进行安装和配置那首先第一步的话是我们需要下载程序这个下载程序的过程也比较简单我们先从我们比如说我们百度里边直接搜索到我们Flink它的一个官网而在它官网的左侧的有一个菜单这个菜单呢其实就叫download我们下面还可以有一个中文版的这个字我们点击中文版就可以看到在这个地方是一个下载那进入下载的时候我们看到当前的这个版本呢也有Apache Flink的1.9.1
[01:20] 我们点开它之后呢我们可以下载Apache Flink 1.9.1的这样的一个下载的bin的一个目录的bin的一个包那么这个包呢叫做Flink-1.9.1-bin-scala下划线2.12的一个tgz这个目录这个文件我们把它进行下载那么下载的过程呢我们就不多讲了下载完了之后比如说在我们当前Windows操作系统里边我们可以使用这个解压压缩包
[01:50] 把这个文件给它解压出来那么解压之后呢就是有一个Flink-1.9.1这个目录了那么在这个目录里边有这么几个文件夹一个是B目录B目录下是我们当前Flink它的一些可执行的一些程序比如说比较有用的一个可执行程序就是我们的start cluster这个BT文件或者一个stop cluster这个BT的文件
[02:16] 如果是我们本地来执行的情况下我们可以直接点击startcluster.bad那它是我们直接就运行了我们的Flink的程序我们把它下载下来解压之后我们没有做任何的一个操作那我们看直接是在我们浏览器里面输入localhost 8080那此时我们就可以看到Flink它的一个管理页面了而这个管理页面里边我们可以看一看
[02:46] 我们从左侧里边是它的菜单栏这个菜单栏里边有一个overview实际上是指的是我们的这个叫什么呢呃一个全景的啊当前的有什么样的一些任务那么下边的话是我们的job就是我们执行的任务包括我们可以执行的正在执行的和完成执行的已完成的一些任务那么task manager里边我们可以看到我们当前这台机器啊
[03:14] 这个这个Flink的这个机群是有一个task manager这个task manager呢是我们呃因为我们是用local方式来执行的嘛那么他只有一个task manager我们job manager呢是我们整个的整个local的这个机群或者我们当前的这台服务器Flink服务器他的一些配置包括我们服这个local manager的一些啊就是job manager的他的一个内存的一些大小啊
[03:41] 或者说是我们的一个堆内存的大小还有包括它显它执行过程中的一些日志我们可以从这里边也可以看到它我们的一个输出的一些日志到底是什么呢那么还有一个比较重要的就是我们可以直接在这里边提交我们的叫吧比如说我们点击这新添加一个叫不我们就可以提交进去提交进去之后我们就可以执行了那这是我们在本地执行安装程序的一个过程
[04:11] 下面我们来看一看我们的这个Flink Standalone这种模式是如何来进行安装部署的那么Standalone模式呢顾名思义就是在本地集群中执行这种调度那么这种集群呢它其实不依赖于外部的比如说像Yarn这种调度机制那么此时呢我们需要对这些配置文件呢做一些简单的一些修改我们预计使用当前服务器充当我们的Job Manager和我们的这个Task Manager
[04:40] 那么一般情况下需要多台机器但是在我们的当前这个演示环境里边我们使用了一台机器来作为我们的job manager和task manager那么如果要进行安装的这种HA的这种高负载的情况我们需要提前对我们的LOOKIPER进行一下安装我们前面其实已经安装了这个LOOKIPER对吧那么我们现在先看一下我们如何来在我们的服务器上来安装我们的Flink stand-alone
[05:09] 那我现在已经把我们Flink程序给它下载下来了那下一步的话我需要对它进行一个解压啊trzxf的一个Flink啊然后这个加这个压缩包那么我们在压解压的过程中我们可以看到哎它解压已经解压完了解压还挺快那么我们进入到我们的这个Flink这个目录里边这个目录里边和我们刚才在window的环境里边是一样的因为我们的都是下载的是同一个包嘛
[05:37] 那我需要配置一下我们的一些配置文件我们进入我们的config目录里边那么这个config目录里边有三个文件是需要我们注意的第一个是我们的flinkconfig我们vimflinkconfig那首先我们需要配置的是我们的一个job manager它的一个地址那么这当前这个地址呢就是172.17.0.143那
[06:08] 下一步的话我们需要配置我们当前这个集群它的端口有一个叫rest的pot我们把它注释给去掉然后rest address注释也给去掉那么我们的这个Flink集群的端口是8081然后我们的地址呢是0.0.0
[06:34] 那这个0.0.0.0的意思是说我们任何一台机器都能够访问到它那下一步我们要配置我们这个机群它的我们看一下这个Task Manager也就是说我们有Job Manager还有一个Task Manager我们在这个地方是配置的Task Manager的一个插槽是2默认的时候情况是1然后我们的并行度我们设置为4默认的时候也是1
[07:08] 我们把它保存下来紧接着我们要vrim我们的master这个文件这个文件里边我们看到它实际上是叫localhost一个8080对吧那么我们不用对它进行修改我们可以再修改我们的slaveslave的话现在只有一个localhost我们要再添加两个那么我们直接在这儿我们添加我们的localhost现在情况下其实就是三个localhost了那么我们把它保存
[07:39] 那么我们下一步就可以执行我们的叫做Flink的启动了我们进入到第一目录下我们看到有一个start cluster的这个sh文件我们执行ok那此时的话一个job manager启动起来了然后三个task manager也启动起来了我们在我们的浏览器上来打开172.17.0.143然后8081
[08:21] OK我们的这个远程的这个standalone的这个集群已经已经启动起来了那么我们可以看到我们的总共的task的插槽是六个然后呢我们task manager呢是有三个也就是说我们task manager刚才配置的情况下我们配置了task manager三个然后每一个的插槽是两个所以说总共的这个插槽就是六个那和他的这种界面上和我们
[08:48] 在local的实际上是一样的对吧我们都可以看到当前执行的是什么我们的task manager此时task manager就有三个了我们记不记得我们当前对于我们本地的话它其实只有一个但是我们在服务器上我们运行了三个task manager也就是sleep而我们job manager呢实际上是只有一个对吧那其他的功能是一样的我就可以添加一个我们的jar 包就是把我们的程序给添加上去让它来执行
[09:16] 这是我们整个安装我们的这个standalone的这个模式那么安装standalone的这个模式来讲的话大家注意一点的时候就是我们的配置那么这个配置里边我们用了啊我们的IP地址来进行配置然后呢我们还把我们的这个什么呢把我们端口给它打开了然后在slave文件的时候我们添加了三个slave文件这样的话是我们整个安装的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下下载、解压并配置 Apache Flink 1.9.1 的 Standalone 模式，并启动集群以访问 Web Dashboard。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Flink 官方文档中关于安装配置的章节，说明了 Flink 有 Local、Standalone、On Yarn 三种运行模式，并给出了下载 Flink 1.9.1 的 wget 命令。
画面 2: 展示了 Apache Flink 官网的下载页面，确认了 Flink 1.9.1 是最新的稳定版本，并列出了可供下载的文件。
画面 3: 展示了下载的 Flink 1.9.1-bin-scala_2.12.tgz 文件在 Windows 资源管理器中的位置。
画面 4: 展示了 Flink Web Dashboard 的“Running Jobs”页面，但内容为空。
画面 5: 展示了 Flink Web Dashboard 的“Job Manager”页面，准备提交新作业。
画面 6: 在 Linux 终端中，显示了已下载的 Flink 1.9.1-bin-scala_2.12.tgz 文件，并执行了 tar 命令解压。
画面 7: 展示了 Flink 配置文件 Flink-conf.yaml 的部分内容，包括 JobManager 和 TaskManager 的堆内存设置。
画面 8: 展示了 Flink-conf.yaml 文件中关于 Kerberos 安全配置的部分。
画面 9: 在终端中，显示了正在执行的命令，但内容为空。
画面 10: 在终端中，执行了 start-cluster.sh 命令，启动了 Flink Standalone 集群。
画面 11: 展示了浏览器访问本地 IP 地址 172.17.0.143:8081 的页面，但显示的是一个商业网站的首页。
画面 12: 展示了 Flink Web Dashboard 的“Overview”页面，显示了可用任务槽位和运行作业状态。
画面 13: 展示了 Flink 官方文档中关于修改环境变量和配置文件 Flink-conf.yaml 的说明。
画面 14: 展示了 Flink-conf.yaml 文件中关于 JobManager 和 TaskManager 的 IP 地址、端口、堆内存等配置项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
[root@node2-vmb6 opt]# cd /opt
[root@node2-vmb6 opt]# wget -c http://mirrors.tuna.tsinghua.edu.cn/apache/Flink/Flink-1.9.1/Flink-1.9.1-bin-scala_2.12.tgz
```
画面 6:
```bash
[root@node2-vmb6 opt]# tar xf Flink-1.9.1-bin-scala_2.12.tgz
```
画面 7:
```yaml
# The heap size for the JobManager JVM
jobmanager.heap.size: 1024m

# The heap size for the TaskManager JVM
taskmanager.heap.size: 1024m

# The number of task slots that each TaskManager offers. Each slot runs one parallel pipeline.
taskmanager.numberOfTaskSlots: 1

# The parallelism used for programs that did not specify and other parallelism.
parallelism.default: 1
```
画面 8:
```yaml
# Flink Cluster Security Configuration

# Kerberos authentication for various components: Hadoop, ZooKeeper, and connectors
# may be enabled in four steps:
# 1. configure the local xdb.conf file
# 2. provide Kerberos credentials (either a keytab or a ticket cache w/ kinit)
# 3. Make the credentials available to various JAAS login contexts
# 4. configure the connector to use JAAS/SASL

# The below configure how Kerberos credentials are provided. A keytab will be used instead of
# a ticket cache if the keytab path and principal are set.
# security.kerberos.login.use-ticket-cache: true
# security.kerberos.login.keytab: /path/to/kerberos/keytab
```
画面 10:
```bash
[root@node2-vmb6 bin]# ./start-cluster.sh
Starting cluster.
Starting standalone session daemon on host node2-vmb6.yyy.
```
画面 13:
```bash
1) 修改环境变量，vi /etc/profile,添加以下内容
export FLINK_HOME=/opt/Flink-1.9.1/
export PATH=$FLINK_HOME/bin:$PATH

2) 修改配置文件 Flink-conf.yaml,
cd /opt/Flink-1.9.1/conf
vim Flink-conf.yaml

# 主要修改的位置有：
jobmanager.rpc.address: 172.17.0.143
taskmanager.numberofTaskSlots: 2
parallelism.default: 4
```
画面 14:
```yaml
# JobManager 的IP地址
jobmanager.rpc.address: 172.17.0.143

# JobManager 的端口号
jobmanager.rpc.port: 6123

# JobManager JVM heap 内存大小
jobmanager.heap.size: 1024m

# TaskManager JVM heap 内存大小
taskmanager.heap.size: 1024m

# 每个 TaskManager 提供的任务 slots 数量大小，默认为1
taskmanager.numberOfTaskSlots: 1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.5 安装配置”，内容包括“Flink 的运行一般分为三种模式：Local、Standalone、On Yarn”。
画面 13: PPT 标题为“1.5 安装配置”，内容包括“1) 修改环境变量，vi /etc/profile,添加以下内容”和“2) 修改配置文件 Flink-conf.yaml”。
画面 14: PPT 标题为“1.5 安装配置”，内容包括“# 主要修改的位置有：”和“# JobManager 的IP地址”等配置项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

