# 09.Spark集群中的角色介绍

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\09.Spark集群中的角色介绍_【海量资源尽在 666java.com】.mp4
- 时长 5分52秒（音频 348s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经把Spark的集群呢就已经搭建起来了那么接下来呢我们一起来了解一下Spark的一些角色那么首先呢我们来看一下Spark的一个架构呢是这样的一个架构那么我们通过我们的一些driver program就是我们的一些驱动程序呢来构建我们的一个Spark的一个contactor上下文然后呢去通过我们的一些集群管理器
[00:28] 然后就去分配我们的任务因为我们前面通过部署就知道那么Spark它的一个集群是一个MS这样的一个架构那么我们会把我们这个任务去提交给master那么真正在做执行的时候并不是master做执行而是谁而是这个worker去做一个执行所以说最终还是需要去提交到我们的worker节点
[00:54] 那么Worker节点就是我们所启动的那个Worker那个进程然后在Worker的进程中我们会启动一个什么的Executor执行器去做一个执行当然了最终我们的任务会以这个Task这样的一个形式去做一个运行了那么需要注意的是这个Executor是一个进程OK好那么这个Catch是在Executor中的一些缓存的一些这样的一些操作OK
[01:22] 好那么这个呢就是它的一些整个的一个架构啊那么下面呢我们对这个架构呢来做一个详细的一个说明那么前面我们也提到那么Spark所采用的这种架构呢是什么呢Must和Slave这样的一种模式那么Must就是集群中的主节点那么Slave呢就是集群中的什么Work这样的一个节点那么OK好那么这个Driver啊Program呢其实就是我们运行这个函数啊Map函数
[01:52] 并且创建了Spark Connect的程序那么后面我们在写代码的时候就会在我们的MEM方法中去做这样的一些创建OK好那么接下来我们来看一下Application那么Application我们其实就指的就是什么应用那么就是我们所编写的一些应用程序那么它包含了我们的一些Driver程序
[02:14] 和集群上的也是Q的那么这个的我们在后面写的过程中大家就能够明白了然后我们的这Cluster Manager那么它就是我们的集群管理器或者说去它的组合的作用就是来获取我们的一些外部的一些服务那么目前是有三种这种服务可以去选择那么第一种就是
[02:38] 18个原生的这种资源管理器那么就是说它不需要去依赖于第三方的一些其他服务那么就可以来跑起来那么这个是默认那么前面我们所搭建的我们这种集群就是采用这种默认的这种资源管理器然后还有通过什么阿帕奇的一个什么SLS去做一个这个集合它是和好多部的什么的MapDios有一个比较良好的这样的一个
[03:06] 兼容的啊这样的一种这个资源调度的一种框架啊那么还有呢就是好多普的这个Yarn去做一个资源管理器也是可以的当然我们一般使用第一种啊就可以了OK好那么还有谁呢就是后面这个WorkNode了就是Work节点它呢就代表着我们可以运行Application的代码的这个节点
[03:29] 那么在我们standalone这种模式中呢就是我们原生的啊资源管理系这种模式下面呢是通过我们的sales文件中所配置的一些work节点这个大家应该有印象吧在我们去搭建集群的时候我们来看一下啊那我们去搭建集群的时候呢是不是我们在我们的slaves这个文件中是不是写了如下的一些内容啊哎呦ok这个呢其实所指向的就是我们的work这样的一个节点
[03:57] 那么这个Executor呢它呢是执行器它呢是为我们的这个在我们这个Work节点上面呢为某个应用而所启动的一个进程那么前面是不是说到过Executor呢是一个进程是一个进程那么这个进程呢主要是负责我们这个任务的一个运行那么并且它也负责将我们这种数据呢去保存到内存呢还是去做保存到磁盘也就是说这种数据的一个落地
[04:27] 那么每个应用都应该有独立的独立的这个executor大家想一下为什么要有独立的executor大家想一下那么原因就是如果说多个应用共用一个executor的话那么一旦这个executor当机的话它所影响到的是不是就不是一个应用了而是有多个应用的影响那么如果每一个应用都有独立的执行器的话那么这个执行器
[04:56] 当机的话是不是仅仅会影响到的是这个应用而不会影响到其他应用这个大家理解了吗OK好那么还有呢最后一个这个这个模块呢叫做什么呢Task它呢就是去呃什么呢呃被送到某一个这个Executor上所工作的这样的一个单元也就是说真正啊干活的呢是这个Task那么Task呢是一个现成去做一个执行啊
[05:22] OK好这个呢就是他的一些架构啊那么通过前面的我们这个集群的一个搭建那么再加上我们对这个架构中的一些这个角色的一些这个讲解那么大家现在应该是对我们这个SPARK的集群有一个相对啊比较深入的这样的一个了解了OK好那么关于我们这个SPARK的一个架构呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Spark 的架构组成及其各角色（Driver Program、Cluster Manager、Worker Node 等）的功能与关系，并演示如何在 Linux 环境下安装配置 Spark。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark 架构图，包含 Driver Program、Cluster Manager 和 Worker Node，以及它们内部的 Executor、Cache、Task 组件。
画面2：聚焦于架构图中的 Cluster Manager，说明其作为集群资源管理器的角色。
画面3：继续展示架构图，同时在下方文字中开始介绍 Spark 架构说明。
画面4：在架构图下方文字中，开始详细介绍 Driver Program、Application、Cluster Manager 的定义和功能。
画面5：继续展示架构图，文字部分已列出 Cluster Manager 的三种资源调度类型（Standalone、Apache Mesos、Hadoop Yarn）。
画面6：继续展示架构图，文字部分已列出 Worker Node 的定义。
画面7：继续展示架构图，文字部分已列出 Executor 的定义。
画面8：继续展示架构图，文字部分已列出 Task 的定义。
画面9：展示架构图，文字部分已完整列出所有组件的定义。
画面10：导航栏切换至“4. 体验 Spark 程序”章节，准备开始实践操作。
画面11：导航栏再次切换至“4.1.1. 普通模式提交任务”小节，准备进行实际操作。
画面12：显示了 Spark 安装配置的 shell 脚本内容，包括解压、配置环境变量、设置 master 主机和端口、创建 slaves 文件并添加节点、复制配置文件、设置 PATH 环境变量等。
画面13：显示了 Spark 启动后的 Web UI 界面，URL 为 http://node1:8080/，显示 Spark Master 在 node1:7077 上运行，有 3 个 Worker 节点在线。
画面14：再次展示架构图，文字部分已完整列出所有组件的定义，准备进入实践环节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面12：
```
#上传Spark-2.4.3-bin-hadoop2.7.tgz压缩包，进行解压
tar -xvf Spark-2.4.3-bin-hadoop2.7.tgz
mv Spark-2.4.3-bin-hadoop2.7 Spark

#修改配置
cd Spark/conf
mv Spark-env.sh.template Spark-env.sh

#在上面添加如下内容
export JAVA_HOME=/usr/local/src/java/JDK 8.0_141  #jdk地址
export SPARK_MASTER_HOST=node1  #指定master的主机名
export SPARK_MASTER_PORT=7077  #master的端口

#修改配置文件
mv slaves.template slaves

#输入如下内容
node1
node2
node3

#将配置文件复制到其它机器
scp -r Spark node2:itcast/
scp -r Spark node3:itcast/

#添加环境变量（3台机器添加）
vim /etc/profile
export SPARK_HOME=/itcast/Spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin

#启动
cd /itcast/Spark/sbin
./start-all.sh
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
架构图结构：
- Driver Program（包含 SparkContext） → Cluster Manager
- Cluster Manager → Worker Node（每个 Worker Node 包含 Executor、Cache、Task）
- Cluster Manager → Worker Node（每个 Worker Node 包含 Executor、Cache、Task）

文字内容：
- Spark 架构使用了分布式计算中 master-slave 模型，master 是集群中含有 master 进程的节点，slave 是集群中含有 worker 进程的节点。
- Driver Program：运行 main 函数并且新建 SparkContext 的程序。
- Application：基于 Spark 的应用程序，包含了 driver 程序和集群上的 Executor。
- Cluster Manager：指的是在集群上获取资源的外部服务。目前有三种类型：
  - Standalone：Spark 原生的资源管理，由 Master 负责资源的分配。
  - Apache Mesos 与 Hadoop MR 兼容性良好的一种资源调度框架。
  - Hadoop Yarn：主要是指 Yarn 中的 ResourceManager。
- Worker Node：集群中任何可以运行 Application 代码的节点，在 Standalone 模式中是通过 slaves 文件配置的 Worker 节点。
- Executor：是在一个 worker node 上为某应用启动的一个进程，该进程负责运行任务，并且负责将数据存在内存或者磁盘上，每个应用都有各自独立的 executor。
- Task：被送到某个 executor 上的工作单元。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

