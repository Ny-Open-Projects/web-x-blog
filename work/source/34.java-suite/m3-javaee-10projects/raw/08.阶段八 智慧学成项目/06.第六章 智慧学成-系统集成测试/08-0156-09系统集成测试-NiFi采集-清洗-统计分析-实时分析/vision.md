# 画面线理解：09系统集成测试-NiFi采集-清洗-统计分析-实时分析

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\09系统集成测试-NiFi采集-清洗-统计分析-实时分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:24, 00:35, 00:43, 01:07, 01:13, 01:18, 01:24, 01:32, 02:02, 02:04, 02:07, 02:09, 02:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:14:23

1) 这一组画面整体在讲什么（一句话）：
演示在 NiFi 平台上构建实时数据采集、清洗与分析流程，并通过 Spark 实时计算处理数据，最终将结果写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: NiFi 界面，显示“今日访问量”、“新增用户量”、“今日购买量”三个监控面板，下方有一个“维度实时分析进程”处理器，数据均为 0。
画面 2: NiFi 界面，与画面 1 几乎相同，仅鼠标位置不同。
画面 3: 显示 RadioView Community v1.7.0 界面，左侧为数据库列表（xc-online 下的 db1 到 db15），右侧为数据表结构预览。
画面 4: RadioView Community 界面，数据库列表中选中了 db11，右侧显示了该表的结构。
画面 5: NiFi 界面，显示“课程访问量 ToKafka 实时”和“2.课程访问量-实时统计分析”两个处理器，数据量开始有变化。
画面 6: NiFi 界面，三个监控面板数据量增加，下方“维度实时分析进程”处理器数据仍为 0。
画面 7: 浏览器地址栏输入 "xc-online-spark:8080"，搜索结果中显示 Spark Master 和 Worker 地址。
画面 8: Spark Master 界面，显示运行中的 3 个应用（RealTimeBuy, RealTimeNewUser, RealTimeVisit）和已完成的 24 个应用。
画面 9: NiFi 界面，三个监控面板数据量继续增加。
画面 10: NiFi 界面，三个监控面板数据量继续增加，下方“维度实时分析进程”处理器数据仍为 0。
画面 11: NiFi 界面，两个处理器数据量增加，显示“课程访问量 ToKafka 实时”处理器的 Queued 为 4,239。
画面 12: NiFi 界面，显示“0.数据生产-新增用户-ToMySQL”和“1.数据消费-新增用户-Mysql-ToKafka-实时采集”两个处理器，数据量为 0。
画面 13: NiFi 界面，空白画布，无处理器。
画面 14: Typora 文档，标题为“6.2 NiFi采集-清洗-统计分析”，包含 PS1 和 PS2 两部分说明，PS2 中包含 SQL 语句用于清空数据库表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 14 中的 SQL 语句：
```
# es中的数据使用es-head界面查询，web 地址：http://xc-online:9100/
# Hbase的数据需要使用base shell 删除，删除命令如下：
disable "LearningOnlineDetail"
drop "LearningOnlineDetail"

PS2：NiFi调度执行前业务数据表的数据库表，以便验证数据处理结果，清空脚本如下：
truncate table agency_amount_month_biz;
truncate table agency_amount_week_biz;
truncate table agency_sale_month_biz;
truncate table agency_user_month_biz;
truncate table agency_user_week_biz;
truncate table course_buy_biz;
truncate table course_hot_month_biz;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14 中的 PPT 标题为“6.2 NiFi采集-清洗-统计分析”，表格数据包含 PS1 和 PS2 两部分说明，PS2 中包含 SQL 语句。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
