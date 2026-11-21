# 画面线理解：05系统集成测试-NiFi采集-清洗-统计分析-即时查询

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\05系统集成测试-NiFi采集-清洗-统计分析-即时查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:22, 02:07, 02:47, 03:35, 03:54, 04:28, 05:02, 05:20, 05:30, 05:55, 06:21, 07:19, 08:16, 08:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:11:20

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 NiFi 流处理数据，将用户学习数据从 HDFS 读取、转换、清洗后写入 Elasticsearch，并通过 Spark 进行实时分析，最终在 Elasticsearch 中展示结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Elasticsearch 集群状态为黄色（5 of 10），索引 "demo" 有 3 个文档，节点 V76BrIv 有 4 个分片。
画面 2: NiFi 界面，显示两个处理流：1. 数据生产-用户学习(在线学习)ToHDFS；2. 数据清洗统计-用户学习。
画面 3: NiFi 界面，显示数据流处理组件：从 "ExecuteScript" 开始，经过 "ConvertAvroToJSON"、"ReplaceText"、"EvaluateJsonPath"，最终写入 "PutHDFS"。
画面 4: NiFi 界面，显示 "InstantQueryStepToHiveAndES" 组件，其 In 和 Out 字段均为 0 字节。
画面 5: Spark Master 界面，显示 1 个 Worker，1 个正在运行的应用 "InstantQueryStepToHive"。
画面 6: Spark Master 界面，显示 1 个 Worker，0 个正在运行的应用，3 个已完成的应用。
画面 7: Elasticsearch 界面，显示集群状态为黄色（5 of 10），索引 "demo" 有 3 个文档。
画面 8: Elasticsearch 界面，显示索引 "learning_course_online_detail" 的数据，包含字段如 user_name, date_info, id, name, age。
画面 9: NiFi 界面，显示数据流处理组件：从 "获取用户id、课程id、视频id" 开始，经过 "ConvertAvroToJSON"、"ReplaceText"、"EvaluateJsonPath"，最终写入 "PutHDFS"。
画面 10: Elasticsearch 界面，显示索引 "learning_course_online_detail" 的数据，包含字段如 user_name, date_info, id, name, age。
画面 11: Hue Table Browser 界面，显示表 "learning_course_online_dwm" 的数据，包含字段如 learning_course_online_dwm.course_id, learning_course_online_dwm.course_name。
画面 12: Xshell 终端界面，显示连接到服务器 "xc-online-1"。
画面 13: Xshell 终端界面，显示执行命令 `select * from learning_online_detail limit 10;`，并输出了 10 条记录，包含字段如 learning_online_detail.course_id, learning_online_detail.course_name。
画面 14: NiFi 界面，显示处理流 "demo"，其 In 字段有 2 个记录，Out 字段为 0。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13 的 SQL 命令：
```sql
select * from learning_online_detail limit 10;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
