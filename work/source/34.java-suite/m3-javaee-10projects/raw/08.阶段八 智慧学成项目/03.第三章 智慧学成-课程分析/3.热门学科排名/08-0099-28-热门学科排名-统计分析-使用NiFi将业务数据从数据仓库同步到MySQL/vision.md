# 画面线理解：28-热门学科排名-统计分析-使用NiFi将业务数据从数据仓库同步到MySQL

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\28-热门学科排名-统计分析-使用NiFi将业务数据从数据仓库同步到MySQL_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:57, 01:44, 02:11, 02:29, 03:01, 03:22, 03:38, 04:05, 04:23, 04:44, 05:11, 05:36, 06:00, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:32:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在Nifi中配置Hive到MySQL的数据同步流程，包括业务表结构定义、Nifi流程设计、Controller Service配置及最终数据验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了Typora文档中“3.6.1.1 业务表结构”部分，内容为“经过上面一系列的清洗 → 统计分析，数据已经经过APP层，这个时候还需要最后一步，把数据同步到MySQL 供业务使用。课程访问量业务表结构如下：”
- 代码块内容：
  -- 在导入学员在线业务数据时，business数据表已导入
  CREATE TABLE `subject_sale_week.biz` (
  `course_category_dim_id` varchar(255) NOT NULL,
  `course_category_name` varchar(255) DEFAULT NULL,
  `sale_num` int(11) NOT NULL,
  `sale_percent` float(11,4) DEFAULT NULL,
  `sale_info` varchar(255) DEFAULT NULL,
  `date_info` varchar(255) DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面2：
- 展示了Typora文档中“3.6.5 销售额-周”部分，内容与画面1相同，但标题不同。
- 代码块内容：
  -- 在导入学员在线业务数据时，business数据表已导入
  CREATE TABLE `subject_amount_week.biz` (
  `course_category_dim_id` varchar(255) NOT NULL,
  `course_category_name` varchar(255) DEFAULT NULL,
  `sale_amount` float(11,4) NOT NULL,
  `amount_percent` float(11,4) DEFAULT NULL,
  `date_info` varchar(255) DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面3：
- 展示了Nifi流程界面，包含两个处理器：左侧为“数据生产-用户流量-ToMySQL”，右侧为“数据消费-用户流量-ToHive-实时采集”。
- 两个处理器的“Queued”、“In”、“Read/Write”、“Out”等指标均为0。

画面4：
- 展示了Nifi流程界面，包含四个处理器：
  - 左上角：“热门学科排名-用户流量-ToMySQL”
  - 左下角：“热门学科学生人数(实时)-用户流量-ToMySQL”
  - 右上角：“热门学科排名-月-Hive-To-MySQL”
  - 右下角：“热门学科学生人数(实时)-月-Hive-To-MySQL”
- 所有处理器的“Queued”、“In”、“Read/Write”、“Out”等指标均为0。

画面5：
- 展示了Nifi中“热门学科排名-周-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-hive- | Enabled | 热门学科排名-周-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Disabled | 热门学科排名-周-Hive-To-MySQL |

画面6：
- 展示了Nifi中“热门学科排名-月-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-hive- | Enabled | 热门学科排名-月-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Disabled | 热门学科排名-月-Hive-To-MySQL |

画面7：
- 展示了Nifi中“热门学科排名-月-Hive-To-MySQL”流程的“Configure Controller Service”对话框。
- 属性配置：
  - Database Connection URL: jdbc:mysql://xc-online.mysql/3306/business...
  - Database Driver Class Name: com.mysql.cj.jdbc.Driver
  - Database Driver Location(s): /opt/mysql-connector-java-8.0.16.jar
  - Database User: root
  - Password: No value set
  - Max Wait Time: 500 mille
  - Max Total Connections: 8
  - Validation query: No value set
  - Minimum idle connections: 0
  - Max idle connections: 8
  - Max Connection Lifetime: -1
  - Time Between Eviction Runs: 10 mins
  - Minimum Eviction Life Time: 10 mins

画面8：
- 展示了Nifi中“热门学科排名-月-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-hive- | Enabled | 热门学科排名-月-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Enabled | 热门学科排名-月-Hive-To-MySQL |

画面9：
- 展示了Nifi中“热门学科学生人数(选课)-月-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-hive- | Enabled | 热门学科学生人数(选课)-月-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Enabled | 热门学科学生人数(选课)-月-Hive-To-MySQL |

画面10：
- 展示了Nifi流程界面，包含两个处理器：
  - 左侧：“热门学科学生人数(实时)-用户流量-ToMySQL”
  - 右侧：“热门学科学生人数(实时)-月-Hive-To-MySQL”
- 两个处理器的“Queued”、“In”、“Read/Write”、“Out”等指标均为0。

画面11：
- 展示了Nifi流程界面，包含三个处理器：
  - 左上角：“EvaluateJsonPath”处理器，其“Read/Write”为14.1 KB / 8 bytes。
  - 左下角：“PostSQL”处理器，其“Read/Write”为0 bytes / 0 bytes。
  - 右侧：“EvaluateJsonPath”处理器，其“Read/Write”为11.4 KB / 1.7 KB。
- 三个处理器的“Queued”、“In”、“Out”等指标均为0。

画面12：
- 展示了Navicat Premium中“xc-online-mysql”数据库的表结构。
- 表列表：
  - agency_amount_month.biz
  - agency_amount_week.biz
  - agency_sale_month.biz
  - agency_sale_week.biz
  - agency_user_month.biz
  - agency_user_week.biz
  - course_buy.biz
  - course_hot_month.biz
  - course_hot_week.biz
  - course_wish.biz
  - platform_offline.biz
  - subject_amount_month.biz
  - subject_amount_week.biz
  - subject_category_month.biz
  - subject_category_week.biz
  - subject_sale_month.biz
  - subject_sale_week.biz
  - subject_user_month.biz
  - subject_user_week.biz

画面13：
- 展示了Navicat Premium中“xc-online-mysql”数据库的表结构。
- 表列表：
  - agency_amount_month.biz
  - agency_amount_week.biz
  - agency_sale_month.biz
  - agency_sale_week.biz
  - agency_user_month.biz
  - agency_user_week.biz
  - course_buy.biz
  - course_hot_month.biz
  - course_hot_week.biz
  - course_wish.biz
  - platform_offline.biz
  - subject_amount_month.biz
  - subject_amount_week.biz
  - subject_category_month.biz
  - subject_category_week.biz
  - subject_sale_month.biz
  - subject_sale_week.biz
  - subject_user_month.biz
  -
