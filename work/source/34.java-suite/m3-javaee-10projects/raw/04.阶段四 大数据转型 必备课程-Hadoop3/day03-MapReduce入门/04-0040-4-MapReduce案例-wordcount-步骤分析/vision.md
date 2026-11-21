# 画面线理解：4-MapReduce案例-wordcount-步骤分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\4-MapReduce案例-wordcount-步骤分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 02:15, 05:36, 10:11, 10:39, 12:14, 13:49, 14:03, 15:57, 17:42, 19:00, 20:06, 20:56, 21:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:40:39

1) 这一组画面整体在讲什么（一句话）：
讲解 Hadoop MapReduce 的 WordCount 示例，通过图示说明从输入文件到 Map、Shuffle、Reduce 阶段的数据处理流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 MapReduce 的整体流程图，说明 Map 阶段分为 2 个步骤，Shuffle 阶段分为 4 个步骤，Reduce 阶段分为 2 个步骤。
画面 2: 展示了源文件 a.txt 的内容，包含 "hello.world"、"hello.hadoop"、"world.hdfs"、"hadoop.java" 四行文本。
画面 3: 展示了 TextInputFormat 将源文件按行分割成 Key-Value 对，Key 为行号（0, 11, 23, 33），Value 为对应行内容。
画面 4: 展示了 Map 阶段，将 K1 V1 转换为 K2 V2，其中 K2 为单词，V2 为 1。
画面 5: 展示了 Map 阶段的输出，K2 V2 表格中单词 "hello"、"world"、"hadoop"、"hdfs" 各出现一次。
画面 6: 展示了 Shuffle 阶段的四个步骤：分区、排序、规约、分组。
画面 7: 展示了 Shuffle 阶段的输出，K2 V2 表格中单词 "hello"、"world"、"hadoop"、"hdfs" 各对应一个 <1,1>。
画面 8: 展示了 Shuffle 阶段的输出，K2 V2 表格中单词 "hello"、"world"、"hadoop"、"hdfs" 各对应一个 <1,1>。
画面 9: 展示了 Reduce 阶段，将 K2 V2 转换为 K3 V3，其中 K3 为单词，V3 为出现次数。
画面 10: 展示了 WordCount 的需求和第一步：创建一个新的文件。
画面 11: 展示了 MapReduce 的完整流程图，包括 Map、Shuffle、Reduce 阶段。
画面 12: 展示了 Reduce 阶段的输出，K3 V3 表格中单词 "hello" 出现 2 次，"world" 出现 2 次，"hadoop" 出现 3 次，"hdfs" 出现 1 次。
画面 13: 展示了 MapReduce 的完整流程图，包括 Map、Shuffle、Reduce 阶段。
画面 14: 展示了 MapReduce 的完整流程图，包括 Map、Shuffle、Reduce 阶段，最后输出到 TextInputFormat。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
