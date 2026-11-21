# 画面线理解：14-MapReduce运行机制-Reduce阶段

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\14-MapReduce运行机制-Reduce阶段【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:08, 00:12, 00:22, 04:45, 06:37, 07:51, 07:55, 08:01, 08:09, 08:44, 09:03, 09:31, 09:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:49:33

1) 这一组画面整体在讲什么（一句话）：
讲解 MapReduce 框架中 Shuffle 阶段的数据流转过程，包括 Map 端的排序、合并与 Reduce 端的缓冲、溢写、排序和最终写入 HDFS 的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 MapReduce Shuffle 阶段的详细流程图，包括 Map 端的环形缓冲区、溢写、排序、合并，以及 Reduce 端的缓冲区、溢写、排序和写入 HDFS。
- 文本内容提到：当数据量超过 80MB 时，会触发溢写（spill）和排序，然后合并（Merge）形成中间文件。
- 配置表：mapreduce.task.io.sort.mb 默认值 100，解释为“设置环形缓冲区的内存大小”；mapreduce.map.spill.percent 默认值 0.8，解释为“设置溢写的比例”；mapreduce.cluster.local.dir 默认值 $HADOOP_TMP_DIR/mapred/local，解释为“写入数据目录”。

画面 2：
- 展示了 Map 阶段的 Shuffle 流程图，包括环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map的shuffle阶段”和“Map阶段”。

画面 3：
- 展示了 Map 阶段的 Shuffle 流程图，与画面 2 类似，但更聚焦于“合并:Merge”和“中间文件”的部分。
- 文本内容提到：合并与溢写时，会生成临时文件，如果 Mapper 输出结果有多个临时文件，Reduce 会合并。

画面 4：
- 展示了 Map 阶段的 Shuffle 流程图，聚焦于“合并:Merge”和“中间文件”的部分。
- 标注了“Map的shuffle阶段”和“Map阶段”。

画面 5：
- 展示了 Reduce 阶段的流程图，包括 Reduce 缓冲区、溢写、排序、中间文件、ReduceTask 和 HDFS。
- 标注了“Reduce阶段”。

画面 6：
- 展示了 Reduce 阶段的流程图，包括 Reduce 缓冲区、溢写、排序、中间文件、ReduceTask 和 HDFS。
- 标注了“Reduce阶段”。

画面 7：
- 展示了 Reduce 阶段的流程图，包括 Reduce 缓冲区、溢写、排序、中间文件、ReduceTask 和 HDFS。
- 标注了“Reduce阶段”。

画面 8：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

画面 9：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

画面 10：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

画面 11：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

画面 12：
- 展示了 Reduce 阶段的流程图，包括 Reduce 缓冲区、溢写、排序、中间文件、ReduceTask 和 HDFS。
- 标注了“Reduce阶段”。

画面 13：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

画面 14：
- 展示了 Map 阶段的 Shuffle 流程图，包括 MapTask、分区、环形缓冲区、溢写、排序、合并、中间文件等步骤。
- 标注了“Map处理阶段”、“Map的shuffle阶段”和“Map阶段”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
配置表：
| 配置 | 默认值 | 解释 |
| --- | --- | --- |
| mapreduce.task.io.sort.mb | 100 | 设置环形缓冲区的内存大小 |
| mapreduce.map.spill.percent | 0.8 | 设置溢写的比例 |
| mapreduce.cluster.local.dir | $hadoop.tmp.dir/mapred/local | 写入数据目录 |

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- PPT 标题：MapReduce Shuffle 阶段
- 架构图结构：
  - Map 端：环形缓冲区 → 溢出:spill → 排序 → 小文件 → 合并:Merge → 中间文件 → Reduce 端
  - Reduce 端：Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：
  | 配置 | 默认值 | 解释 |
  | --- | --- | --- |
  | mapreduce.task.io.sort.mb | 100 | 设置环形缓冲区的内存大小 |
  | mapreduce.map.spill.percent | 0.8 | 设置溢写的比例 |
  | mapreduce.cluster.local.dir | $hadoop.tmp.dir/mapred/local | 写入数据目录 |

画面 2：
- PPT 标题：Map 阶段
- 架构图结构：
  - 环形缓冲区 → 溢出:spill → 排序 → 小文件 → 合并:Merge → 中间文件 → Reduce 端
  - Reduce 端：Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 3：
- PPT 标题：Map 阶段
- 架构图结构：
  - 合并:Merge → 中间文件 → Reduce 端
  - Reduce 端：Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 4：
- PPT 标题：Map 阶段
- 架构图结构：
  - 合并:Merge → 中间文件 → Reduce 端
  - Reduce 端：Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 5：
- PPT 标题：Reduce 阶段
- 架构图结构：
  - Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 6：
- PPT 标题：Reduce 阶段
- 架构图结构：
  - Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 7：
- PPT 标题：Reduce 阶段
- 架构图结构：
  - Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 8：
- PPT 标题：Map 处理阶段
- 架构图结构：
  - MapTask → 分区:Partition → 环形缓冲区 → 溢出:spill → 排序 → 小文件 → 合并:Merge → 中间文件 → Reduce 端
  - Reduce 端：Reduce 缓冲区 → spill:溢写 → 小文件 → 排序/分组 → 中间文件 → ReduceTask → HDFS
- 表格数据：无

画面 9：
- PPT 标题：Map 处理阶段
- 架构图结构：
  - MapTask → 分区:Partition → 环形缓冲区 → 溢出:spill → 排序 → 小文件 → 合并:
