# 画面线理解：4.5 Flink架构原理

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.5 Flink架构原理_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 02:02, 02:03, 02:05, 03:18, 03:19, 03:23, 03:24, 03:26, 03:43, 03:46, 03:48, 03:49, 03:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:13:08

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
