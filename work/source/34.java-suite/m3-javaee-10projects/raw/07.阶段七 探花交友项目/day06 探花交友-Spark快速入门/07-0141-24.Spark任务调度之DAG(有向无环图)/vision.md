# 画面线理解：24.Spark任务调度之DAG（有向无环图）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\24.Spark任务调度之DAG（有向无环图）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:47, 01:17, 01:18, 01:19, 01:37, 01:50, 02:22, 02:54, 03:25, 03:57, 04:29, 04:39, 04:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:33:24

1) 这一组画面整体在讲 Spark 中 RDD 的依赖关系（窄依赖与宽依赖）及其对 DAG 阶段划分的影响。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 DAG（有向无环图）的概念，说明 RDD 通过一系列转换形成 DAG，其依赖关系被划分为不同 Stage。图示为 Stage 1，包含 A、B、G 三个节点，B 节点为 groupBy，G 节点为 join。
画面 2: 与画面 1 相同，但对文本“Stage”进行了高亮。
画面 3: 与画面 1 相同，但高亮了“Stage”。
画面 4: 展示了窄依赖（Narrow Dependencies）和宽依赖（Wide Dependencies）的对比图。窄依赖包括 map、filter、union；宽依赖包括 groupByKey 和 join with inputs not co-partitioned。
画面 5: 与画面 4 相同，但标题为“6.4.1、RDD的依赖关系”。
画面 6: 与画面 4 相同，但标题为“6.4.1、RDD的依赖关系”。
画面 7: 展示了任务调度流程图，图中包含 Stage 1、Stage 2、Stage 3，以及 RDD Objects、DAGScheduler、TaskScheduler、Worker 等组件。
画面 8: 与画面 7 相同。
画面 9: 与画面 7 相同。
画面 10: 与画面 7 相同。
画面 11: 在图中 Stage 1 的节点 A 和 G 上添加了红色框。
画面 12: 与画面 11 相同。
画面 13: 弹出 MySQL Installer 的初始化窗口，标题为“Start Initialization”，内容为“MySQL Installer is running in Community mode...”。
画面 14: 与画面 7 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
- PPT 标题：
  - 画面 1: “6.4.2、DAG”
  - 画面 4: “6.4.1、RDD的依赖关系”
  - 画面 7: “6.4.3、任务调度流程”
- 架构图/流程图结构：
  - 画面 1: Stage 1 包含节点 A、B、G。A 指向 B，B 指向 G。
  - 画面 4: 左侧“Narrow Dependencies”部分，map、filter、union 节点指向下方的 RDD 节点。右侧“Wide Dependencies”部分，groupByKey 和 join with inputs not co-partitioned 节点指向下方的 RDD 节点。
  - 画面 7: Stage 1 包含节点 A、B、G。A 指向 B，B 指向 G。Stage 2 包含节点 C、D、E、F。C 指向 D，D 指向 F，E 指向 F。Stage 3 包含节点 G。F 指向 G。图下方列出组件：RDD Objects、DAGScheduler、TaskScheduler、Worker。
- 表格数据：
  无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
