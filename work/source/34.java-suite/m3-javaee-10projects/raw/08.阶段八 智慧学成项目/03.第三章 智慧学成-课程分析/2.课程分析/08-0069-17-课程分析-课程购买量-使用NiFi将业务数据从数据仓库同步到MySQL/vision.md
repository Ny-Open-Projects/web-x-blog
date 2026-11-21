# 画面线理解：17-课程分析-课程购买量-使用NiFi将业务数据从数据仓库同步到MySQL

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\17-课程分析-课程购买量-使用NiFi将业务数据从数据仓库同步到MySQL_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:37, 00:48, 01:18, 01:31, 01:42, 01:54, 02:09, 02:21, 02:35, 03:07, 03:19, 03:45, 04:04, 04:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:08:52

1) 这一组画面整体在讲如何使用 NiFi 将 Hive 中的业务数据同步到 MySQL 数据库，并展示相关的表结构和数据流程。

2) 按时间顺序列出每张画面的要点：
画面1: 在 Hue 的 Table Browser 中查看 Hive 表 course_buy_biz 的数据样本，包含 date_info、count、biz_years、biz_months、biz_days 等字段。
画面2: 展示 PPT 页面，标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。
画面3: 展示 PPT 页面，标题为“2.6.1 业务表结构”，展示创建表的 SQL 语句；标题为“2.6.2 NiFi调度流程”，展示数据流向和 NiFi 流程图。
画面4: 在 NiFi 界面中展示一个包含三个处理器的流程图，分别是 demo、维度、高层分析。
画面5: 在 NiFi 界面中，弹出“Upload Template”窗口，准备上传 XML 配置文件。
画面6: 在 NiFi 界面中，展示一个包含两个处理器的流程图，分别是“数据生产-课程购买量ToMySQL”和“数据消费-课程购买量MySQL-To-Hive”。
画面7: 在 NiFi 界面中，展示“3、落地业务库：课程购买量-Hive-To-Mysql Configuration”配置窗口。
画面8: 在 NiFi 界面中，展示“Configure Controller Service”窗口，配置 MySQL 数据库连接参数。
画面9: 在 NiFi 界面中，展示“SelectHiveQL”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面10: 在 NiFi 界面中，展示“ConvertAvroToJSON”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面11: 展示一个业务数据看板页面，包含今日访问量、新增用户量、今日购买量等指标。
画面12: 展示 PPT 页面，标题为“2.6.3 NiFi调度代码”，展示 NiFi 流程的 XML 代码路径。
画面13: 在 NiFi 界面中，展示“SelectHiveQL”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面14: 展示 PPT 页面，标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2: CREATE TABLE 'course_buy_biz' (
'date_info' date NOT NULL,
'count' int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
画面3: CREATE TABLE 'course_buy_biz' (
'date_info' date NOT NULL,
'count' int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
画面3: 数据流向为：Hive → MySQL，使用的NiFi处理流向为：SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。
画面8: Database Connection URL: jdbc:mysql://xc-online:8088/business...
Database Driver Class Name: com.mysql.cj.jdbc.Driver
Database Driver Location(s): /root/mysql-connector-java-8.0.16.jar
Database User: root
Password: (No value set)
Max Wait Time: 500 mills
Max Total Connections: 8
Minimum Idle Connections: 0
Max Idle Connections: 8
Max Connection Lifetime: -1
Time Between Eviction Runs: -1
Minimum Eviction Idle Time: 10 mins
画面12: nifi 流程的 XML 代码路径：/课程购买量-Hive-To-Mysql.xml

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2: 标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。
画面3: 标题为“2.6.1 业务表结构”，展示创建表的 SQL 语句；标题为“2.6.2 NiFi调度流程”，展示数据流向和 NiFi 流程图。
画面12: 标题为“2.6.3 NiFi调度代码”，展示 NiFi 流程的 XML 代码路径。
画面3: 数据流向为：Hive → MySQL，使用的NiFi处理流向为：SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。
画面3: NiFi 流程图中，SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。

5) 无。
