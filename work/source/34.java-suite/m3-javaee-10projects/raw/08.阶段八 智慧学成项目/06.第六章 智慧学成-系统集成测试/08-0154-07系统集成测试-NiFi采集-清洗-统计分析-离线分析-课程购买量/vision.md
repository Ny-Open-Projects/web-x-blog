# 画面线理解：07系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程购买量

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\07系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程购买量_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:12, 01:56, 02:08, 02:18, 03:15, 04:03, 04:20, 04:37, 05:04, 05:11, 05:25, 05:39, 06:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:12:55

1) 这一组画面整体在讲什么（一句话）：
演示在 NiFi 中构建数据采集、清洗和统计分析流程，并通过 Spark 处理数据，最终写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 NiFi 界面，三个处理器的监控面板，分别显示“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的队列状态，其中“读取数据源”处理器的队列中有 32,983 字节数据。
画面 2: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“ExecuteScript”、“SplitJson”、“ConvertJSONToSON”、“ReplaceText”、“EvaluateJsonPath”、“PutSQL”等处理器，展示数据处理流程。
画面 3: 显示 NiFi 界面，弹出“Empty Queue”对话框，提示“10,000 FlowFiles (312.5 KB) were removed from the queue”。
画面 4: 显示 NiFi 界面，弹出“Empty Queue”确认对话框，提示“Are you sure you want to empty this queue? All FlowFiles waiting at the time of the request will be removed.”，并提供“CANCEL”和“EMPTY”按钮。
画面 5: 显示 NiFi 界面，弹出“Empty Queue”确认对话框，提示“Are you sure you want to empty this queue? All FlowFiles waiting at the time of the request will be removed.”，并提供“CANCEL”和“EMPTY”按钮。
画面 6: 显示 NiFi 界面，数据流图，包含“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的监控面板，显示“读取数据源”处理器的队列中有 0 字节数据。
画面 7: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 8: 显示 Spark Master 界面，显示 Spark 集群状态，包括“URL”、“REST URL”、“Alive Workers”、“Memory in use”、“Applications”、“Status”等信息，以及“Workers”和“Running Applications”、“Completed Applications”列表。
画面 9: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 10: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 11: 显示 Navicat Premium 界面，连接到“xc-online-mysql”数据库，显示“business”数据库下的表结构，包括“agency_amount_month_biz”、“agency_amount_week_biz”、“agency_sale_month_biz”、“agency_sale_week_biz”、“agency_user_month_biz”、“agency_user_week_biz”、“course_buy_biz”、“course_hot_month_biz”、“course_hot_week_biz”、“course_sale_biz”、“course_user_month_biz”、“course_user_week_biz”、“subject_amount_month_biz”、“subject_amount_week_biz”、“subject_sale_month_biz”、“subject_sale_week_biz”、“subject_user_month_biz”、“subject_user_week_biz”等表。
画面 12: 显示 NiFi 界面，数据流图，包含“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的监控面板，显示“读取数据源”处理器的队列中有 0 字节数据。
画面 13: 显示 NiFi 界面，处理器详细信息面板，显示“Hive Database Connection Pooling Service”、“HiveQL Pre-Query”、“HiveQL Select Query”、“Fetch Size”、“Max Rows Per Flow File”、“Maximum Number of Fragments”、“Output Format”、“Normalize Table/Column Names”、“CSV Header”、“Alternate CSV Header”、“CSV Delimiter”、“CSV Quote”、“PRM Format”等属性及其值。
画面 14: 显示 Typora 文档，标题为“6.2 NiFi采集-清洗-统计分析”，内容包括“1. 数据采集：使用NiFi生成数据的方式进行采集，根据指标进行，生成一定的数据后停止即可”、“2. 数据清洗统计分析：执行Spark程序占用资源较多也是根据指标这个进行”、“3. 清洗业务数据和步骤驱动，自动触发”、“PS1：清理即时查询的数据，es中索引表及Hbase存储的完整数据”、“PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：”以及清空表的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 14 中的 SQL 语句：
```
# es中的索引使用es-head管理页面删除，web 址：http://xc-online:9100/
disable "LearningOnlineDetail"
drop "LearningOnlineDetail"

PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：
truncate table agency_amount_month_biz;
truncate table agency_amount_week_biz;
truncate table agency_sale_month_biz;
truncate table agency_user_month_biz;
truncate table agency_user_week_biz;
truncate table course_buy_biz;
truncate table course_hot_month_biz;
truncate table course_hot_week_biz;
truncate table course_sale_biz;
truncate table course_user_month_biz;
truncate table course_user_week_biz;
truncate table subject_amount_month_biz;
truncate table subject_amount_week_biz;
truncate table subject_sale_month_biz;
truncate table subject_sale_week_biz;
truncate table subject_user_month_biz;
truncate table subject_user_week_biz;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14 中的 PPT 标题为“6.2 NiFi采集-清洗-统计分析”，内容包括：
- 1. 数据采集：使用NiFi生成数据的方式进行采集，根据指标进行，生成一定的数据后停止即可
- 2. 数据清洗统计分析：执行Spark程序占用资源较多也是根据指标这个进行
- 3. 清洗业务数据和步骤驱动，自动触发
- PS1：清理即时查询的数据，es中索引表及Hbase存储的完整数据
- PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：
  - truncate table agency_amount_month_biz;
  - truncate table agency_amount_week_biz;
  - truncate table agency_sale_month_biz;
  - truncate table agency_user_month_biz;
  - truncate table agency_user_week_biz;
  - truncate table course_buy_biz;
  - truncate table course_hot_month_biz;
  - truncate table course_hot_week_biz;
  - truncate table course_sale_biz;
  - truncate table course_user_month_biz;
  - truncate table course_user_week_biz;
  - truncate table subject_amount_month_biz;
  - truncate table subject_amount_week_biz;
  - truncate table subject_sale_month_biz;
  - truncate table subject_sale_week_biz;
  - truncate table subject_user_month_biz;
  - truncate table subject_user_week_biz;

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
