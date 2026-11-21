# 画面线理解：13-实时分析-新增用户量-概述&数据采集

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\13-实时分析-新增用户量-概述&数据采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:51, 01:16, 01:34, 01:51, 02:31, 03:06, 03:25, 03:55, 04:04, 04:36, 05:02, 05:30, 05:52, 06:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:45:10

1) 这一组画面整体在讲如何使用 NiFi 实时采集 MySQL 中的用户数据，并通过过滤和路由写入 Kafka。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程大纲，当前章节为“3.1 数据采集”，子章节“3.1.1 NiFi采集流程”，并附带 NiFi 流程图，图中包含 CaptureChangeMySQL、Insert、EvaluateAttribute、PublishKafka 等组件。
画面2：在 NiFi 界面中弹出“Add Process Group”对话框，输入名称“新用户”后点击 ADD。
画面3：新建的 Process Group 界面为空白画布。
画面4：在 NiFi 界面中，已添加两个处理器：左侧为“0.数据生产-新增用户ToMySQL”，右侧为“1.数据采集-新增用户-Mysql-ToKafka实时采集”。
画面5：NiFi 流程图中，CaptureChangeMySQL 组件的输出连接到 Insert 组件，Insert 组件的输出连接到 EvaluateAttribute 组件，EvaluateAttribute 组件的输出连接到 PublishKafka 组件。
画面6：NiFi 流程图中，EvaluateAttribute 组件的输出连接到 PublishKafka 组件，同时 Insert 组件的输出连接到 EvaluateAttribute 组件。
画面7：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面8：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面9：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面10：在 NiFi 界面中，弹出“Empty Queue”对话框，提示“274,164 FlowFiles (203.06 MB) were removed from the queue”。
画面11：在 Navicat Premium 中，显示 MySQL 数据库“xc_online”的“xc_user”表，其中包含多条用户记录。
画面12：在 Navicat Premium 中，选中“xc_user”表中的一条记录，点击“删除”按钮。
画面13：在 Navicat Premium 中，选中“xc_user”表中的一条记录，点击“删除”按钮。
画面14：在 NiFi 界面中，显示“3.1.2 NiF调度过滤指定数据库和表配置”页面，配置处理器的属性中，“Database”为“xc_user”，“Table Name”为“xc_user”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面7：
Known Brokers: xc-online-kafka:9092
Topic Name: NEW_USER
Client Name: publish_course_buy

画面14：
Database: xc_user
Table Name: xc_user

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“3 新增用户量”，子标题为“3.1 数据采集”，并附带 NiFi 流程图，图中包含 CaptureChangeMySQL、Insert、EvaluateAttribute、PublishKafka 等组件。
画面5：NiFi 流程图中，CaptureChangeMySQL 组件的输出连接到 Insert 组件，Insert 组件的输出连接到 EvaluateAttribute 组件，EvaluateAttribute 组件的输出连接到 PublishKafka 组件。
画面6：NiFi 流程图中，EvaluateAttribute 组件的输出连接到 PublishKafka 组件，同时 Insert 组件的输出连接到 EvaluateAttribute 组件。
画面14：PPT 标题为“3.1.2 NiF调度过滤指定数据库和表配置”，并附带配置处理器的属性表，表中包含“Database”和“Table Name”字段。

5) 无。
