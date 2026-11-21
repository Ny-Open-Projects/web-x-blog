# 画面线理解：05-课程分析-课程购买量-测试NiFi采集MySQL

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\05-课程分析-课程购买量-测试NiFi采集MySQL_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 02:02, 04:10, 04:53, 05:46, 07:16, 08:13, 08:53, 09:15, 10:39, 11:06, 12:07, 12:46, 13:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:01:30

1) 这一组画面整体在讲如何通过 Nifi 实现 MySQL 到 Hive 的数据同步，并演示了数据更新操作及在 Hive 中遇到的错误排查。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示 Nifi 流程图，说明启动处理组需确认 hadoop、mysql、hive 正常运行。图中显示了从 MySQL Reader 到 Hive Writer 的数据流，以及一个名为 "PutHiveQL" 的处理器。

画面2：
要点：展示在 Hive 中查询数据的结果，以及用于更新数据的 SQL 语句。
SQL 语句：
UPDATE `xc_order`.`xc_orders`
SET
`initial_price` = 0.01,
`price` = 9999.99,
`start_time` = '2018-04-05 19:32:33',
`end_time` = '2018-04-05 21:32:33',
`details` = '{"itemId":"402be5816bcf7f4016bcf8b7c6000","itemNum":1,"itemPrice":0.01,"orderId":"29916098202216"}',
`order_number` = '29916098202216';

画面3：
要点：展示 Hue 的 Table Browser 界面，列出 data_course 数据库下的多个表，包括 course_buy_biz、course_buy_fact、course_orders_source 等。

画面4：
要点：在 Hue 的 Table Browser 中，展示 course_orders_source 表的数据样本，包含 order_number、price、status、order_time 等字段。

画面5：
要点：在 Navicat Premium 中查看 MySQL 数据库 xc_order 的 xc_orders 表，显示了包含 order_number、price、start_time、end_time、details 等字段的数据记录。

画面6：
要点：展示在 Hive 中执行 UPDATE 语句后，Hive 日志报错，提示无法更新表，原因是 Hive 发现表在 HDFS 上没有对应的目录。错误信息为：Failed to update Hive table... Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.mr.MapRedTask。

画面7：
要点：展示 Hue 的 Table Browser 界面，与画面3类似，但未显示具体表数据。

画面8：
要点：展示 Nifi 流程图，显示从 MySQL Reader 到 Hive Writer 的数据流，其中 Hive Writer 处理器显示已成功写入 0 行数据。

画面9：
要点：展示在 Xshell 中连接到名为 "xc_docker" 的远程服务器，显示 Ubuntu 18.04.3 LTS 系统信息，包括 IP 地址、内存使用率等。

画面10：
要点：在 Xshell 中查看 Hive 日志文件，显示了多个日志文件（hive.log、hive.log.2019-11-13、hive.log.2019-11-14、operation_logs），并提示无法加载 native-hadoop 库。

画面11：
要点：展示 Nifi 流程图，显示从 MySQL Reader 到 Hive Writer 的数据流，其中 Hive Writer 处理器显示已成功写入 0 行数据。

画面12：
要点：在 Xshell 中查看 Hive 日志文件，显示了多个日志文件（hive.log、hive.log.2019-11-13、hive.log.2019-11-14、operation_logs），并提示无法加载 native-hadoop 库。

画面13：
要点：展示 Nifi 流程图，显示从 MySQL Reader 到 Hive Writer 的数据流，其中 Hive Writer 处理器显示已成功写入 0 行数据。

画面14：
要点：展示 Nifi 流程图，说明启动处理组需确认 hadoop、mysql、hive 正常运行。图中显示了从 MySQL Reader 到 Hive Writer 的数据流，以及一个名为 "PutHiveQL" 的处理器。
