# 画面线理解：14-Hive的基本操作-创建分区表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\14-Hive的基本操作-创建分区表【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:46, 02:00, 02:12, 03:47, 04:20, 05:03, 05:18, 06:02, 06:46, 06:59, 07:28, 08:15, 08:43, 09:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:14:59

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建分区表、加载数据到分区表、查询多分区数据以及管理分区（添加和删除）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Hive客户端界面，讲解分区表概念，显示创建分区表语句：create table score(s_id string,c_id string, s_score int) partitioned by (month string) row format delimited fields terminated by '\t';
画面2：同画面1，鼠标悬停在代码上，无新增要点。
画面3：显示HDFS浏览器界面，路径为/user/hive/warehouse/myhive.db/teacher，展示teacher.csv文件。
画面4：显示SQLyog数据库管理工具界面，左侧为数据库结构，右侧为查询编辑器，无具体操作。
画面5：SecureCRT终端中，执行rz命令上传文件，显示传输进度。
画面6：HDFS浏览器界面，路径为/user，为空目录。
画面7：Windows资源管理器，显示本地文件夹，包含score.csv等文件。
画面8：SecureCRT终端中，执行Hive命令创建表score和score2，加载数据到分区。
画面9：Hive客户端界面，展示加载数据到多分区表的SQL语句。
画面10：HDFS浏览器界面，路径为/user/hive/warehouse/myhive.db，显示score、score2等目录。
画面11：Hive客户端界面，展示查看分区、添加分区和删除分区的SQL语句。
画面12：SecureCRT终端中，执行Hive查询语句，显示查询结果。
画面13：同画面12，无新增要点。
画面14：Hive客户端界面，展示创建分区表语句和加载数据到分区表的SQL语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
create table score(s_id string,c_id string, s_score int) partitioned by (month string) row format delimited fields terminated by '\t';

画面8：
hive> create table score(s_id string,c_id string, s_score int) partitioned by (month string) row format delimited fields terminated by '\t';
Time taken: 0.123 seconds
OK
hive> create table score2 (s_id string,c_id string, s_score int) partitioned by (year string,month string,day string) row format delimited fields terminated by '\t';
Time taken: 0.062 seconds
OK
hive> load data local inpath '/export/servers/hivedatas/score.csv' into table score partition (month='201806');
Loading data to table myhive.score partition (month='201806')
OK
Time taken: 0.383 seconds
hive> load data local inpath '/export/servers/hivedatas/score.csv' into table score partition (month='201807');
Loading data to table myhive.score partition (month='201807')
OK
Time taken: 0.337 seconds

画面9：
load data local inpath '/export/servers/hivedatas/score.csv' into table score2 partition(year='2018',month='06',day='01');

画面11：
show partitions score;
alter table score add partition(month='201805');
alter table score drop partition(month = '201806');

画面12：
Time taken: 0.289 seconds, Fetched: 18 row(s)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1.4 分区表”，内容包括“创建分区表语法”、“创建一个表带多个分区”、“加载数据到分区表中”、“加载数据到多个分区表中”、“多分区表联合查询（使用 union all）”、“查看分区”、“添加一个分区”、“删除分区”。
画面9：PPT标题为“加载数据到多个分区表中”，内容包括“load data local inpath '/export/servers/hivedatas/score.csv' into table score2 partition(year='2018',month='06',day='01');”。
画面11：PPT标题为“查看分区”、“添加一个分区”、“删除分区”，内容包括“show partitions score;”、“alter table score add partition(month='201805');”、“alter table score drop partition(month = '201806');”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
