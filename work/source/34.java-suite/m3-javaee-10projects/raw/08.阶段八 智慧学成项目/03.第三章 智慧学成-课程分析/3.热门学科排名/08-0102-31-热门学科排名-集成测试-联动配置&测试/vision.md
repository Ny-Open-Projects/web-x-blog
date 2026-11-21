# 画面线理解：31-热门学科排名-集成测试-联动配置&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\31-热门学科排名-集成测试-联动配置&测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:02, 01:37, 02:25, 03:10, 03:48, 04:07, 04:30, 04:53, 06:25, 07:45, 08:44, 09:23, 10:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:34:27

1) 这一组画面整体在讲什么（一句话）：
演示如何在 NiFi 中配置数据流，实现从 MySQL 到 Hive 的数据同步，并展示相关配置和 SQL 操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 NiFi 界面，包含三个处理器：用户需求-Mysql-To-Hive、数据清洗分析-热门学科排名、热业业务-热门学科排名-Hive-To-Mysql，均处于未处理状态。
画面 2: 显示 NiFi 流程图，包含多个处理器（如 subject learn count by week biz、subject sales volume by month biz）和连接关系，鼠标悬停显示处理器属性。
画面 3: 显示 NiFi 流程图，鼠标悬停在 "subject sales volume by month biz" 处，显示其属性，同时右下角有 "WaitForNextGroupProcessor" 处理器。
画面 4: 显示 "Add Controller Service" 对话框，其中 "Controller Service Name" 为 "CouchbaseMapCacheClient"，"Bundle" 为 "org.apache.nifi - nifi-couchbase-nar"。
画面 5: 显示 "Add Port" 对话框，用于添加端口。
画面 6: 显示 NiFi 流程图，包含 "SelectLineOfS"、"SplitJson"、"EvaluateJsonPath" 和 "PutSQL" 处理器，鼠标悬停显示属性。
画面 7: 显示 NiFi 流程图，包含两个处理器：热门学科排名-Hive-To-Mysql 和 热门学科排名-Hive-To-Mysql，均处于未处理状态。
画面 8: 显示 "Add Port" 对话框，用于添加端口。
画面 9: 显示 NiFi 流程图，包含两个处理器：热门学科排名-Hive-To-Mysql 和 热门学科排名-Hive-To-Mysql，均处于未处理状态。
画面 10: 显示 Navicat Premium 界面，连接到 MySQL 数据库，显示 "business" 数据库下的表列表，包括 subject_amount_month_biz、subject_user_week_biz 等。
画面 11: 显示 Navicat Premium 界面，显示 "business" 数据库下的表列表，包括 subject_amount_month_biz、subject_user_week_biz 等。
画面 12: 显示 NiFi 流程图，包含多个处理器（如 subject learn count by week biz、subject sales volume by month biz）和连接关系，鼠标悬停显示处理器属性。
画面 13: 显示 NiFi 流程图，鼠标悬停在 "subject-sales-volume-by-month-biz" 处理器上，显示其属性。
画面 14: 显示 PDF 文档页面，标题为 "3.7.4 热门学科排名-整体流程"，包含 "3.7.4.1 联动配置" 和 "3.7.4.2 整体流程" 两个小节，以及 "整体流程代码" 的占位符。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
