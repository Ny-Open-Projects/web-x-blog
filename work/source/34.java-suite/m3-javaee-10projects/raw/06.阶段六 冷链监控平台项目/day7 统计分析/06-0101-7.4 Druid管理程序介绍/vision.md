# 画面线理解：7.4 Druid管理程序介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.4 Druid管理程序介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:25, 02:11, 02:38, 02:40, 02:50, 03:07, 03:12, 03:16, 03:22, 03:32, 03:36, 03:42, 03:56, 04:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:40:42

1) 这一组画面整体在讲什么（一句话）：
演示 Apache Druid 的统一控制台界面，包括数据源管理、数据段查看、任务监控、中间管理器状态和 SQL 查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Druid 控制台的“Load data”页面，提示用户指定原始数据位置，提供 HTTP(s)、AWS S3、Google Cloud Storage、Local disk 等选项。
画面 2: 切换到“DataSources”页面，显示一个名为 “all_device_message” 的数据源，状态为“Fully available”，保留策略为 “loadby(period)(P100), dropby(period)(P300)”，压缩策略为“None”，大小 36.37 MB，行数 444,097。
画面 3: 切换到“Segments”页面，显示空的段列表。
画面 4: 在“Segments”页面中，显示了多个数据段，数据源均为 “all_device_message”，时间范围从 2019-12-05T00:00:00.000Z 到 2019-12-04T16:00:00.000Z，版本从 1 到 11，行数从 161 到 336。
画面 5: 切换到“Tasks”页面，显示空的任务列表。
画面 6: 切换到“Data servers”页面，显示“Supervisors”部分，主机为 “172.17.0.143:8091”，使用率为 1/3，上次完成任务时间为 2019-12-05T04:11:39.629Z。
画面 7: 在“Data servers”页面中，显示了另一个主机 “172.17.0.143:8093”，数据源为 “default_liter”，大小 36.37 MB，容量 300.00 GB，使用率 0.0%，队列为空。
画面 8: 在“Data servers”页面中，显示了主机 “172.17.0.143:8093” 的详细信息，数据源为 “default_liter”，大小 36.37 MB，容量 300.00 GB，使用率 0.0%，队列为空。
画面 9: 切换到“Query”页面，SQL 编辑器为空。
画面 10: 在“Query”页面中，输入 SQL 语句：`select * from all_device_message`。
画面 11: 在“Query”页面中，SQL 语句为：`select * from all_device_message limit 30`。
画面 12: 执行 SQL 查询后，显示查询结果，包含字段如 `line`, `companyname`, `curtime`, `hotcode`, `hostid`, `hostname`, `housecode`, `houseid`, `hum`, `humslat`, `lat`, `lon` 等，数据行数为 10。
画面 13: 切换回“Load data”页面，提示用户指定原始数据位置。
画面 14: 切换回“Query”页面，SQL 编辑器为空。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 10: `select * from all_device_message`
画面 11: `select * from all_device_message limit 30`
画面 12: 查询结果中的字段包括：
```
line
companyname
curtime
hotcode
hostid
hostname
housecode
houseid
hum
humslat
lat
lon
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
