# 画面线理解：10-sqoop入门介绍

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\10-sqoop入门介绍【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:14, 00:58, 02:25, 02:27, 02:36, 02:44, 04:24, 04:25, 04:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:29:35

1) 这一组画面整体在讲什么（一句话）：
讲解 Sqoop 数据迁移工具的概述、架构对比及任务调度配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示大数据处理架构图，包含日志文件、业务数据、外部数据通过 Flume 采集、Sqoop 导入进入 HDFS 和 HBase，经预处理（清洗过滤、日志分析、分类合并）、Hive 仓库（操作数据、数据仓库、数据集市）、机器学习（mahout）最终输出到报表系统，任务调度由 Azkaban 控制。
画面2：PPT 页面标题为“4. sqoop数据迁移”，子标题“4.1、概述”，内容说明 Sqoop 是 Apache 下一款用于 Hadoop 和关系数据库服务器之间传送数据的工具，支持导入数据（MySQL、Oracle 导入到 HDFS、HIVE、HBASE）和导出数据（从 Hadoop 文件系统导出到关系数据库 mysql）。
画面3：与画面2内容相同，仅滚动位置略有不同。
画面4：PPT 页面标题为“4.2、sqoop1与sqoop2架构对比”，子标题“sqoop1架构”，展示 sqoop1 架构图。
画面5：与画面4内容相同，仅滚动位置略有不同。
画面6：展示 sqoop1 架构图，包含 command、Sqoop、Map Task、HDFS/HBase/Hive 等组件。
画面7：PPT 页面标题为“4.2、sqoop1与sqoop2架构对比”，子标题“sqoop2架构”，展示 sqoop2 架构图。
画面8：PPT 页面标题为“4.1、概述”，内容包含任务调度配置示例：
0 1 2 3 * 每天凌晨一点钟执行这个任务
0 2 3 4 * 每隔两个小时定时执行这个任务
0 3 4 5 * 每天晚上九点半定时执行这个任务
画面9：与画面2内容相同，仅滚动位置略有不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8 中的配置代码：
0 1 2 3 * 每天凌晨一点钟执行这个任务
0 2 3 4 * 每隔两个小时定时执行这个任务
0 3 4 5 * 每天晚上九点半定时执行这个任务

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2、3、4、5、7、8、9：PPT 标题为“4. sqoop数据迁移”，子标题“4.1、概述”，内容说明 Sqoop 是 Apache 下一款用于 Hadoop 和关系数据库服务器之间传送数据的工具，支持导入数据（MySQL、Oracle 导入到 HDFS、HIVE、HBASE）和导出数据（从 Hadoop 文件系统导出到关系数据库 mysql）。
画面4、5：PPT 标题为“4.2、sqoop1与sqoop2架构对比”，子标题“sqoop1架构”，展示 sqoop1 架构图。
画面7：PPT 标题为“4.2、sqoop1与sqoop2架构对比”，子标题“sqoop2架构”，展示 sqoop2 架构图。
画面6：架构图结构：
- command → Sqoop → Map Task → HDFS/HBase/Hive
- CLI → Sqoop Client → Sqoop Server → Metadata Repository → Hadoop
- Sqoop Server → REST、UI、Connectors
- Hadoop → Map Task → Reduce Task → HDFS/HBase/Hive

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
