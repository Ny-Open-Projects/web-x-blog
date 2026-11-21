# 4.5 Flink架构原理

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.5 Flink架构原理_【海量资源尽在 666java.com】.mp4
- 时长 3分58秒（音频 238s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来学习一下Flink的一个架构Flink作为一个实时流计算引擎或者叫流计算的一个框架或者叫流计算的一个平台那么它本身呢有三个组件组成的一个叫Job Client一个叫Job Manager还有一个是Task Manager那么我们来看一看我们这张原理图首先我们的开发者他把我们的整个Flink程序开发完之后呢
[00:30] 他用一种客户端的方式来提交我们的程序那么这个客户端呢有可能是说我们后台的一个Flink的啊一个可执行的一个程序还可以我们通过Flink的页面Flink的管理页面来提交我们的程序那他由jobclient发送我们的程序之后他实际上把程序发给到了我们的一个jobmanager而jobmanager收到程序他会
[00:58] 返回给我们的jobclient说你提交成功了那紧接着就是jobmanager他要做的事情他把程序呢把整个的Flink的一个任务提交给我们的task manager因为我们Flink程序是要处理数据的嘛但是处理数据需要有中间的协调者这个协调者就是我们的一个jobmanager那还有具体的任务的执行者其实就是一个task manager
[01:25] Task Manager他在提交程序之后呢他会定时的向我们的Job Manager发布或者说汇报我们整个任务的一个执行情况那Job Manager最终来对他进行一个汇总也就是说我们在这张图里面有两个Task Manager有可能还有更多的三个四个这种Task Manager他在执行完结果之后他会把相应的数据提交给我们的Job ManagerJob Manager汇总之后
[01:55] 把结果返回给Job Client这是完成了一个整个的一个数据流的一个处理的一个过程那么我们看一看下面的这张图整个的一个流程图我们的Flink Program也就是说我们左侧的这一部分这个部分来讲的话它包含了我们的程序代码程序代码通过客户端那么
[02:17] 本身客户端的话会把我们整个程序划分成一个可执行的或者说是有一个叫做有像无环图第一级的一个图那么这个图的话本身它会把整个的状态也好还是我们的一些整个的运行的过程呢发送给我们的job manager那么job manager根据这张图把我们的任务分配给不同的worker也就是task managertask manager他会
[02:47] 处理具体的任务他本身他的任务处理结果之后呢他会把数据返回给job managerjob manager再返回给我们的啊前端的job client啊告诉我们整个的系统数数据当前这个数据已经处理完了而这个数据来讲的话这个整个的这个系统呢他可能会在我们的啊自己的一台机器上一个机群里边独立的机群或者说在亚运上
[03:15] 或者是说我们在云服务器上来执行部署那在这里边的话啊下面这其实就是对我们的啊整个过程的一个解释吗program code就是我们在这儿的一个job client它的是承载的或者说它执行的就是program code那么job client的话它具体的是任务的一个执行起点它负责接收的我们程序的代码然后创建我们的这个数据流交给我们的job manager
[03:43] 最终来讲的话最终会在我们的task manager里边来执行这是我们整个Flink它的一个架构的一个体系或者说是一个工作原理工作的一个流程图

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Flink 的架构组成与作业提交执行流程，包括 JobClient、JobManager 和 TaskManager 三个核心组件及其交互关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：1.4 Flink架构
- 内容：Flink在运行中主要有三个组件组成，JobClient、JobManager 和 TaskManager。
- 图表：工作原理图（Actor 提交 Flink 程序 → JobClient → JobManager → TaskManager，以及 JobManager 定时汇报 Task 状态）。
- 图表：作业提交流程图（包含两个 TaskManager 和一个 JobManager，展示 Task Slot、Memory & I/O Manager、Network Manager、Actor System 等组件）。

画面2：
- 图表：作业提交流程图（展示 TaskManager 内部结构，包括 Task Slot、Memory & I/O Manager、Network Manager、Actor System，以及 Data Streams 和 Task Status 等）。

画面3：
- 图表：作业提交流程图（展示 Flink Program、Client、JobManager 之间的交互，包括 Program Dataflow、Optimizer / Graph Builder、Dataflow graph、Actor System、Submit job (send dataflow)、Cancel/update job 等）。

画面4：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面5：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。
- 文本：Program Code：我们编写的 Flink 应用程序代码。
- 文本：Job Client：Job Client 不是 Flink 程序执行的内部部分，但它是任务执行的起点。Job Client 负责接受用户的程序代码，然后创建数据流，将数据流提交给 Job Manager 以进一步执行。执行完成后，Job Client 将结果返回给用户。

画面6：
- 文本：Job Manager：主进程（也称为作业管理器）协调和管理程序的执行。它的主要职责包括安排任务，管理 checkpoint，故障恢复等。机器集群中至少要有一个 master，master 负责调度 task，协调 checkpoints 和容灾。高可用设置的话可以有多个 master，但要保证一个是 leader，其他是 standby；Job Manager 包含 Actor system, Scheduler, Check pointing 三个重要的组件。
- 文本：Task Manager：从 Job Manager 处接收需要部署的 Task，Task Manager 是在 JVM 中的一个或多个线程中执行任务的工作节点。任务执行的并行性由每个 Task Manager 上可用的任务槽决定。每个任务代表分配给任务槽的一组资源。例如，如果 Task Manager 有四个插槽，那么它可以为每个插槽分配 25% 的内存。可以在任意一个插槽中运行一个或多个线程。同一插槽中的线程共享相同的 JVM。同一 JVM 中的任意事务 TCP 连接和心跳消息。Task Manager 的一个 Slot 代表一个可用线程，该线程具有固定的内存，注意 Slot 只对内存隔离，没有对 CPU 隔离。默认情况下，Flink 允许子任务共享 Slot，即使它们是不同 task 的 subtask，只要它们来自相同的 job。这种共享可以有更好的资源利用率。
- 标题：1.5 安装配置

画面7：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面8：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面9：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面10：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面11：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面12：
- 图表：作业提交流程图（与画面3相同，展示 Flink Program、Client、JobManager 之间的交互）。

画面13：
- 标题：1.4 Flink架构
- 内容：Flink在运行中主要有三个组件组成，JobClient、JobManager 和 TaskManager。
- 图表：工作原理图（Actor 提交 Flink 程序 → JobClient → JobManager → TaskManager，以及 JobManager 定时汇报 Task 状态）。
- 图表：作业提交流程图（包含两个 TaskManager 和一个 JobManager，展示 Task Slot、Memory & I/O Manager、Network Manager、Actor System 等组件）。

