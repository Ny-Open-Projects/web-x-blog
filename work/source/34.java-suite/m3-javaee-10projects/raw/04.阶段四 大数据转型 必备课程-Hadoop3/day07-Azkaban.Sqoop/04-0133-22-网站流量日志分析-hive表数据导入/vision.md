# 画面线理解：22-网站流量日志分析-hive表数据导入

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\22-网站流量日志分析-hive表数据导入【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:08, 02:07, 02:44, 03:19, 04:15, 05:14, 05:58, 07:04, 07:39, 08:20, 09:55, 10:32, 11:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:22:23

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建日志分析相关的数据表，并将本地数据加载到Hive表中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT中“网站日志分析系统”的架构图，包含Nginx、HDFS、MapReduce、Hive、Sqoop和MySQL等组件。
画面2：在Notepad++中展示创建Hive表的SQL语句，用于创建ods_weblog_origin表。
画面3：在SecureCRT中执行Hive命令，创建ods_weblog_origin表。
画面4：在SecureCRT中执行Hive命令，创建ods_click_stream_visit表。
画面5：在SecureCRT中执行Hive命令，创建ods_click_pageviews表。
画面6：在Windows资源管理器中，右键点击“part-r-00000”文件，准备进行操作。
画面7：在Notepad++中展示HDFS命令和Hive本地模式配置，用于准备数据导入。
画面8：在Notepad++中展示HDFS命令和Hive本地模式配置，用于准备数据导入。
画面9：展示Windows桌面，包含“黑马程序员”和“博学谷”的标志。
画面10：在Windows桌面，右键点击“part-r-00000”文件，准备进行操作。
画面11：在Windows资源管理器中，展示“1-HiveSQL”文件夹下的多个SQL文件。
画面12：在SecureCRT中执行Hive命令，加载本地数据到ods_weblog_origin表，并尝试查询。
画面13：在SecureCRT中执行Hive命令，加载本地数据到ods_click_pageviews表，并查询。
画面14：展示PPT中“网站日志分析系统”的架构图，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
drop table if exists ods_weblog_origin;
create table ods_weblog_origin(
valid string,
remote_addr string,
remote_user string,
time_local string,
request string,
status string,
body_bytes_sent string,
http_referer string,
http_user_agent string,
partitioned by (datestr string)
row format delimited
fields terminated by '\001';

画面3：
hive> create table ods_weblog_origin(
> valid string,
> remote_addr string,
> remote_user string,
> time_local string,
> request string,
> status string,
> body_bytes_sent string,
> http_referer string,
> http_user_agent string,
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面4：
hive> create table ods_click_stream_visit(
> session string,
> remote_addr string,
> inTime string,
> outTime string,
> inPage string,
> outPage string,
> referral string,
> pageVisits int)
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面5：
hive> create table ods_click_pageviews(
> session string,
> remote_addr string,
> time_local string,
> request string,
> visit_step string,
> page_staylong string,
> http_referer string,
> http_user_agent string,
> body_bytes_sent string,
> status string,
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面7：
hdfs dfs -mkdir -p /weblog/preprocessed
hdfs dfs -mkdir -p /weblog/clickstream/pageviews
hdfs dfs -mkdir -p /weblog/clickstream/visits
hdfs dfs -mkdir -p /weblog/dim_time
hdfs dfs -put part-m-00000 /weblog/preprocessed
hdfs dfs -put part-r-00000 /weblog/clickstream/pageviews
hdfs dfs -put part-r-00000 /weblog/clickstream/visits
hdfs dfs -put dim_time.dat.txt /weblog/dim_time
设置hive本地模式运行
set hive.exec.mode.local.auto=true;

画面12：
hive> load data local inpath '/export/servers/weblogdatas/weblog_origin' overwrite into table ods_weblog_origin partition(datestr='20130918');
hive> show tables;
OK
ods_click_pageviews
ods_click_stream_visit
ods_weblog_origin
Time taken: 0.386 seconds, Fetched: 3 row(s)
hive> select * from ods_weblog_roigin limit 10;
FAILED: SemanticException [Error 10001]: Line 1:14 Table not found 'ods_weblog_roigin'
hive> select * from ods_weblog_origin limit 10;

画面13：
hive> load data local inpath '/export/servers/weblogdatas/pageView' overwrite into table ods_click_pageviews partition(datestr='20130918');
OK
Time taken: 2.104 seconds
hive> show tables;
OK
ods_click_pageviews
ods_click_stream_visit
ods_weblog_origin
Time taken: 0.386 seconds, Fetched: 3 row(s)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面14：
标题：大数据平台 网站日志分析系统
架构图结构：
- 三个Nginx实例（分别标注为“Nginx”、“Nginx”、“Nginx”）指向HDFS。
- HDFS指向MapReduce。
- MapReduce指向Hive。
- Hive指向Sqoop。
- Sqoop指向MySQL。
- MySQL指向Web展现。
- 一个“任务调度”组件指向MapReduce。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
