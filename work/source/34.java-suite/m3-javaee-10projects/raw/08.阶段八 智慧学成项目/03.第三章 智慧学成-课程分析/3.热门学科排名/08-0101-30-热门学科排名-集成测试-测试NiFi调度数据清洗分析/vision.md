# 画面线理解：30-热门学科排名-集成测试-测试NiFi调度数据清洗分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\30-热门学科排名-集成测试-测试NiFi调度数据清洗分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:54, 01:11, 01:26, 01:43, 01:57, 02:28, 03:09, 03:51, 04:12, 04:34, 04:48, 05:11, 05:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:33:57

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 NiFi 流处理系统将用户行为数据从 MySQL 同步到 Hive，并通过 Spark 进行数据聚合分析，最终将结果写入 MySQL。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 NiFi 流处理界面，包含三个处理节点：0. 数据生产（用户表从 MySQL 同步）、1. 数据采集（用户表从 MySQL 同步至 Hive）、2. 数据清洗分析（热门学科排名）、3. 落地业务表（热门学科排名写入 MySQL）。每个节点显示了队列、读写、处理时间等指标。
画面 2: Hue 文件浏览器，路径为 /user/hive/external/data_subject，显示了多个业务数据文件，如 subject_amount_month_biz、subject_sale_week_biz 等。
画面 3: Hue 文件浏览器，鼠标悬停在 subject_amount_month_biz 文件上。
画面 4: Hue 文件浏览器，鼠标悬停在文件列表上方。
画面 5: Hue 文件浏览器，鼠标悬停在 subject_amount_month_biz 文件上。
画面 6: Hue 文件浏览器，路径为 /user/hive/external/data_course，显示了课程相关的数据文件，如 course_buy_biz、course_study_fact 等。
画面 7: NiFi 流处理界面，显示了数据处理流程，包括从 MySQL 读取数据、写入 Hive、进行数据清洗和聚合分析，最终写入 MySQL。
画面 8: Hue 文件浏览器，路径为 /user/hive/external/data_course/learning_course_fact，显示该目录为空。
画面 9: Hue 文件浏览器，鼠标悬停在 /user/hive/external/data_course 路径上。
画面 10: Hue 文件浏览器，路径为 /user/hive/external/data_subject/subject_amount_week_biz，显示了 years2019 文件夹。
画面 11: Spark Master 界面，显示了 Spark 集群状态，包括 Worker 节点信息和已完成的应用程序列表，如 SubjectLearnNumByWeekBiz、SubjectSalesByMonthBiz 等。
画面 12: Hue 文件浏览器，路径为 /user/hive/external/data_subject/subject_sale_week_biz，显示了 years2019 文件夹。
画面 13: NiFi 流处理界面，显示了数据处理流程，包括从 MySQL 读取数据、写入 Hive、进行数据清洗和聚合分析，最终写入 MySQL。
画面 14: NiFi 流处理界面，显示了三个处理节点：0. 数据生产（用户表从 MySQL 同步）、1. 数据采集（用户表从 MySQL 同步至 Hive）、2. 数据清洗分析（热门学科排名）、3. 落地业务表（热门学科排名写入 MySQL）。每个节点显示了队列、读写、处理时间等指标。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
