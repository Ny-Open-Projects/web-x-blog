# 画面线理解：09.Spark集群中的角色介绍

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\09.Spark集群中的角色介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:25, 01:26, 01:28, 01:46, 02:04, 02:35, 03:20, 03:22, 03:44, 03:46, 03:48, 03:55, 05:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:22:54

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
tar -xvf spark-2.4.3-bin-hadoop2.7.tgz
mv spark-2.4.3-bin-hadoop2.7 spark

#修改配置
cd spark/conf
mv spark-env.sh.template spark-env.sh

#在上面添加如下内容
export JAVA_HOME=/usr/local/src/java/jdk1.8.0_141  #jdk地址
export SPARK_MASTER_HOST=node1  #指定master的主机名
export SPARK_MASTER_PORT=7077  #master的端口

#修改配置文件
mv slaves.template slaves

#输入如下内容
node1
node2
node3

#将配置文件复制到其它机器
scp -r spark node2:itcast/
scp -r spark node3:itcast/

#添加环境变量（3台机器添加）
vim /etc/profile
export SPARK_HOME=/itcast/spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin

#启动
cd /itcast/spark/sbin
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
  - Standalone：spark 原生的资源管理，由 Master 负责资源的分配。
  - Apache Mesos 与 hadoop MR 兼容性良好的一种资源调度框架。
  - Hadoop Yarn：主要是指 Yarn 中的 ResourceManager。
- Worker Node：集群中任何可以运行 Application 代码的节点，在 Standalone 模式中是通过 slaves 文件配置的 Worker 节点。
- Executor：是在一个 worker node 上为某应用启动的一个进程，该进程负责运行任务，并且负责将数据存在内存或者磁盘上，每个应用都有各自独立的 executor。
- Task：被送到某个 executor 上的工作单元。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
