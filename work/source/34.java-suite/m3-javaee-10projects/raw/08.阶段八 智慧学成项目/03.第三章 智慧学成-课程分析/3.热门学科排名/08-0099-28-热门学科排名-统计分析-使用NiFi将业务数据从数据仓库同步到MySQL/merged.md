# 28-热门学科排名-统计分析-使用NiFi将业务数据从数据仓库同步到MySQL

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\28-热门学科排名-统计分析-使用NiFi将业务数据从数据仓库同步到MySQL_【海量资源尽在 666java.com】.mp4
- 时长 6分53秒（音频 413s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 前面呢,咱们已经对任何学科排名中的销售量销售额以及学生人数进行统计分析在每项统计分析中呢,又根据维度中的月还有周这两个级别分别进行的一个统计分析咱们呢,已经将统计分析的结果保存到数据仓库中保存到数据仓库中之后呢,咱们的业务报表系统还不能使用接下来呢,咱们就将
[00:31] 页目数据存咱们的数据仓库中保存到咱们的MySQL中这里咱们的调度方式是使用NiFi调度的方式通过本节的学习你需要掌握使用NiFi将咱们数据仓库中的页目数据同步到MySQL中这里咱们同步的页目数据是热门学科排名的相关数据下面有
[00:58] 每个业务表所对应MySQL的一个表结构这里呢这些表结构咱们已经提前的已经导入就是在咱们导入咱们学生在线业务库的时候已经将咱们business表给导入这里呢你只需要知道咱们是哪个库和咱们哪个业务相对应的即可这下面呢是调度流程调度流程呢都是一样的咱们呢
[01:27] 这里直接使用咱们的汇总代码进行一个导入进行一个调度就行了下面的这些学生人数也好销售额也好这些呢对应的表想了解的话去了解一下不想了解也没有关系咱们呢在这个调度里边已经把所有的内容都给做了咱们来切到NiFi对这个调度进行配置这里呢已经切到切换到咱们热门学科排名这个处理器组中
[01:59] 咱们首先是对模板的一个上传这里咱们是认为学科排名的Hive to MySQL就是数据仓库同步到咱们MySQL的一个调度上传成功之后使用添加模板的方式将咱们刚上传的代码给添加进来添加进来之后咱们需要对它做一个相应的配置这里有12个感叹号也就是说要配置的项还是蛮多的咱们进入咱们的处理器组
[02:28] 这个处理器组呢包含的内容就是每一项的一个调度它是单独的就是每一项指标就是销量的按周统计销量按月统计每一项都是单独进行一个调度的所以说咱们每一项都要配置这里呢就快速的进行一个配置Hive的链接咱们直接启用集合好已经启动完成MySQL呢咱们是需要配置密码的一定不要忘记配置密码密码是123456这里我复制一下
[02:59] 后边就可以直接粘贴就行配置完成之后呢一定也要把它给启用起来启用完成之后呢咱们这个算配置完成接下来呢是下一个hi5呢还是直接启用mycircle呢需要配置密码密码123456然后配置完成之后也是启用好咱们继续hi5直接启用启用完成之后呢mycircle配置密码配置完成之后呢
[03:42] 接着启用好下一个启用Hive然后MySQL配置密码配置完成之后启用MySQL的链接OK刷一下还有最后两个咱们继续配置启用Hive配置MySQL密码然后启用好咱们来配置最后一个启用Hive的链接启用完Hive的链接之后呢咱们千万不要忘记配置MySQL的密码
[04:34] 密码呢是123456配置完成之后呢点击了play然后启用启用完成之后咱们这里从数据仓库同步到买色库的任务调度呢就算配置完成了咱们呢这里直接进行一个测试启动这里呢在这个处理器组进行一个启动操作它呢会将所有的处理器组就是当前目录内的所有处理器组全部启用可以看到这里呢已经有数据了
[05:07] 有数据流动保存到了myserfone中这里呢也已经有数据流动这个地方看到数据流动呢就说明它已经保存成功了咱们来到myserfone进行查看下边的六张表就是咱们认为学科排名需要使用的六张表咱们来打开这里呢有第27周和28周的数据咱们向下拉这是之前的测试的老数据第40周的数据这应该是咱们新的数据40周和45周的每一个项都是的
[05:38] 前边呢是7月这是按月统计按月统计这是7月老数据咱们呢这是按照11月进行一个统计好数据已经进来接下来呢这是销售量按周统计第39周这也是销售量按月统计11月已经进来接下来呢是销售额这是按周统计咱们呢是第43周和第39周接下来呢是销售额按月统计咱们呢是
[06:11] 10月和11月数据已经进来之后呢咱们这个调度就算完成了咱们把它给停下来调度完成之后呢咱们回到文档这里呢咱们使用NiFi调度然后呢将数据仓库的数据同步到MySQL到此呢就配置完成咱们呢也测试完成数据已经同步到咱们的数据仓库中接下来呢视频就要停止了因为咱们这个呢业务数据存汇不到MySQL
[06:42] 配置已经完成通过学习呢一定要将这个数据存买色口从害物中就是咱们数据仓库中同步到买色口好视频到此结束

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  | Hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-Hive- | Enabled | 热门学科排名-周-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Disabled | 热门学科排名-周-Hive-To-MySQL |

画面6：
- 展示了Nifi中“热门学科排名-月-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | Hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-Hive- | Enabled | 热门学科排名-月-Hive-To-MySQL |
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
  | Hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-Hive- | Enabled | 热门学科排名-月-Hive-To-MySQL |
  | mysql连接 | DBConnectionPool 1.9.2 | org.apache.nifi-nifi-dbc- | Enabled | 热门学科排名-月-Hive-To-MySQL |

画面9：
- 展示了Nifi中“热门学科学生人数(选课)-月-Hive-To-MySQL”流程的Controller Services配置页面。
- 表格内容：
  | Name | Type | Bundle | State | Scope |
  | --- | --- | --- | --- | --- |
  | DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache- | Enabled | NIF Flow |
  | Hive连接 | hiveConnectionPool 1.9.2 | org.apache.nifi-nifi-Hive- | Enabled | 热门学科学生人数(选课)-月-Hive-To-MySQL |
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

