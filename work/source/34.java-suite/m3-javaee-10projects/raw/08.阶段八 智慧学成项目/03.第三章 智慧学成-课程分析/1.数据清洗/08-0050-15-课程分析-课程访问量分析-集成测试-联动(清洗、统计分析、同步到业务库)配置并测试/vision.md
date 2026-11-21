# 画面线理解：15-课程分析-课程访问量分析-集成测试-联动（清洗、统计分析、同步到业务库）配置并测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\15-课程分析-课程访问量分析-集成测试-联动（清洗、统计分析、同步到业务库）配置并测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:41, 01:50, 03:01, 03:34, 04:12, 05:13, 06:06, 06:39, 07:31, 08:39, 09:14, 09:50, 10:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:57:39

1) 这一组画面整体在讲如何使用 NiFi 构建一个数据流程，实现从生成模拟数据、处理、到写入 MySQL 数据库的完整链路，并涉及控制器服务的配置与 Hive 数据的同步。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程文档，标题为“1.3.5 课程访问量-整体流程”，子标题“1.3.5.1 联动配置”，内容说明使用 WaitForNextGroupProcessor 实现两个处理器组的联动。
画面 2: NiFi 流程图，包含 GenerateFlowFile、visit-to-process、visit-to-fact 三个处理器，数据流向从 GenerateFlowFile 到 visit-to-process，再到 visit-to-fact。
画面 3: NiFi 流程图，新增 WaitForNextGroupProcessor 处理器，连接在 visit-to-fact 后，用于等待另一个处理器组完成。
画面 4: NiFi 流程图，WaitForNextGroupProcessor 的配置显示其等待另一个处理器组完成。
画面 5: NiFi 流程图，显示数据从 GenerateFlowFile 经过 visit-to-process 和 visit-to-fact 处理后，流向 Out。
画面 6: NiFi 控制器服务配置界面，显示“Enable Controller Service”弹窗，服务为 DistributedMapCacheServer，作用域为 Service only。
画面 7: NiFi 流程图，新增 SelectHiveQL 和 PutSQL 处理器，用于从 Hive 读取数据并写入 MySQL。
画面 8: NiFi 流程图，显示数据从 GenerateFlowFile 经过 visit-to-process 和 visit-to-fact 处理后，流向 Out。
画面 9: Hue 文件浏览器界面，显示数据表列表，包含 course_visit_bit、course_visit_fact 等表。
画面 10: NiFi 流程图，显示数据从 GenerateFlowFile 经过 visit-to-process 和 visit-to-fact 处理后，流向 Out。
画面 11: NiFi 流程图，显示数据从 GenerateFlowFile 经过 visit-to-process 和 visit-to-fact 处理后，流向 Out。
画面 12: Hue 查询界面，显示 SQL 查询结果，查询语句为 SELECT * FROM course_visit_fact。
画面 13: NiFi 控制器服务配置界面，显示 DistributedMapCacheServer 已启用。
画面 14: 课程文档，标题为“1.3.5.2 整体流程代码”，下方有代码结构图，显示“课程访问量整体流程.vn1”文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1: 无代码或配置。
画面 2: 无代码或配置。
画面 3: 无代码或配置。
画面 4: 无代码或配置。
画面 5: 无代码或配置。
画面 6: 无代码或配置。
画面 7: 无代码或配置。
画面 8: 无代码或配置。
画面 9: 无代码或配置。
画面 10: 无代码或配置。
画面 11: 无代码或配置。
画面 12: SQL 查询语句：
```sql
CREATE TABLE `course_visit_fact` (
  `course_visit_fact_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `course_id` bigint(20) DEFAULT NULL,
  `visit_time` datetime DEFAULT NULL,
  `visit_days` int(11) DEFAULT NULL,
  `visit_type` varchar(255) DEFAULT NULL,
  `visit_source` varchar(255) DEFAULT NULL,
  `visit_ip` varchar(255) DEFAULT NULL,
  `visit_user_id` bigint(20) DEFAULT NULL,
  `visit_user_name` varchar(255) DEFAULT NULL,
  `visit_user_type` varchar(255) DEFAULT NULL,
  `visit_user_source` varchar(255) DEFAULT NULL,
  `visit_user_status` varchar(255) DEFAULT NULL,
  `visit_user_login_time` datetime DEFAULT NULL,
  `visit_user_login_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source` varchar(255) DEFAULT NULL,
  `visit_user_login_type` varchar(255) DEFAULT NULL,
  `visit_user_login_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type` varchar(255) DEFAULT NULL,
  `visit_user_login_source_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type_ip_status_type
