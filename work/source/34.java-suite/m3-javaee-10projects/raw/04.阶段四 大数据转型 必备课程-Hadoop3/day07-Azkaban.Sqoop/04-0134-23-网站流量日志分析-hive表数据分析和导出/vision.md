# 画面线理解：23-网站流量日志分析-hive表数据分析和导出

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\23-网站流量日志分析-hive表数据分析和导出【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:22, 01:35, 01:53, 02:25, 02:37, 02:56, 03:10, 04:35, 05:15, 05:29, 05:46, 06:02, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:25:22

1) 这一组画面整体在讲什么（一句话）：
演示如何通过编写 SQL 脚本和 Shell 脚本，对网站日志数据进行多维度统计分析，并通过 Sqoop 导出数据到 Hive 表中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示文件夹内容，包含多个 .job 文件、.sql 文件、.zip 文件和 .jar 文件，用于网站日志分析任务。
画面 2: 显示 SQL 脚本，包含创建和插入表的语句，用于计算每日 PV 总量。
画面 3: 显示 SQL 脚本，包含创建和插入表的语句，用于计算按用户 IP 统计的 PV。
画面 4: 显示 PPT 页面，标题为“四、模块开发---统计分析”，子标题为“1.1 多维度统计 PV 总量”，并展示 SQL 语句示例。
画面 5: 显示文件夹内容，包含名为 “sqoop_export.sh” 的脚本文件。
画面 6: 显示 Sqoop 导出脚本，包含获取日期、设置变量和执行 Sqoop 命令。
画面 7: 显示 Sqoop 导出脚本，包含获取日期、设置变量和执行 Sqoop 命令，其中变量部分有高亮。
画面 8: 显示数据库管理工具界面，执行了 GRANT 和 TRUNCATE 语句，并显示了表数据。
画面 9: 显示文件夹内容，鼠标悬停在 “1.job” 文件上，准备编辑。
画面 10: 显示一个空的 .job 文件，内容为 Type、Command 和 Dependencies 的定义。
画面 11: 显示 Hive 数据导入脚本，包含将数据导入到不同 Hive 表的命令。
画面 12: 显示 Shell 脚本，用于设置 Java 和 Hadoop 环境变量，并获取日期信息。
画面 13: 显示 SQL 脚本，包含创建和插入表的语句，用于统计每小时各来源 URL 的 PV。
画面 14: 显示文件夹内容，底部任务栏显示了两个“网站日志分析”窗口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```sql
--第一种方式：直接在ods_weblog_detail单表上进行查询
1.1.1 计算该处理批次（一天）中的各小时pvs
drop table if exists dw_pvs_everyhour_oneday;
create table if not exists dw_pvs_everyhour_oneday(month string,day string,hour string,pvs bigint) partitioned by (datestr string) row format delimited fields terminated by '\001' stored as textfile;
insert into table dw_pvs_everyhour_oneday partition(datestr='20130918')
select a.month as month,a.day as day,a.hour as hour,count(*) as pvs from ods_weblog_detail a
where a.datestr='20130918' group by a.month,a.day,a.hour;

--计算每天的pvs
drop table if exists dw_pvs_everyday;
create table if not exists dw_pvs_everyday(pvs bigint,month string,day string);
insert into table dw_pvs_everyday select count(*) as pvs,a.month as month,a.day as day from ods_weblog_detail a
group by a.month,a.day;

1.1.2 第二种方式：与时间维表关联查询
--维度：日
drop table dw_pvs_everyday;
create table dw_pvs_everyday(pvs bigint,month string,day string);
insert into table dw_pvs_everyday
select count(*) as pvs,a.month as month,a.day as day from ods_weblog_detail a
group by a.month,a.day;
```

画面 3:
```sql
drop table dw_avgpv_user_everyday;
create table dw_avgpv_user_everyday(
day string,
avgpv string);
insert into table dw_avgpv_user_everyday
select '20130918',sum(b.pvs)/count(b.remote_addr)
from (
select remote_addr,count(1) as pvs from ods_weblog_detail where datestr='20130918'
group by remote_addr
) b;
```

画面 6:
```bash
#!/bin/bash
if [ $# -eq 1 ]
then
cur_date=date --date="$1" +%Y-%m-%d
else
cur_date=date -d'1 day' +%Y-%m-%d
fi
echo "cur_date:"$cur_date
year='date --date=$cur_date +%Y'
month='date --date=$cur_date +%m'
day='date --date=$cur_date +%d'
table_name=""
hadoop_dir=/user/rd/bi_dm/app_user_experience_d/year=$year/month=$month/day=$day
mysql_db_pwd=biall_pwd2015
mysql_db_name=bi_tag_all
echo 'sqoop start'
$SQOOP_HOME/bin/sqoop export \
--connect "jdbc:mysql://hadoop03:3306/biclick" \
--username $mysql_db_name \
--password $mysql_db_pwd \
--table $table_name \
--columns $table_columns \
--fields-terminated-by '\001'
```

画面 7:
```bash
echo "cur_date:"$cur_date
year='date --date=$cur_date +%Y'
month='date --date=$cur_date +%m'
day='date --date=$cur_date +%d'
table_name=""
table_columns=""
hadoop_dir=/user/rd/bi_dm/app_user_experience_d/year=$year/month=$month/day=$day
mysql_db_pwd=biall_pwd2015
mysql_db_name=bi_tag_all
echo 'sqoop start'
$SQOOP_HOME/bin/sqoop export \
--connect "jdbc:mysql://hadoop03:3306/biclick" \
--username $mysql_db_name \
--password $mysql_db_pwd \
--table $table_name \
--columns $table_columns \
--fields-terminated-by '\001'
```

画面 11:
```bash
#!/bin/bash
#目标hive表
ods_weblog_origin="weblog.ods_weblog_origin"
ods_click_pageviews="weblog.ods_click_pageviews"
ods_click_stream_visit="weblog.ods_click_stream_visit"
#导入数据到weblog.ods_weblog_origin
HQL_origin="load data inpah "$log_pre_output" overwrite into table $ods_weblog_origin partition(datestr='$day_0)'"
echo $HQL_origin
/export/servers/hive-1.1.0-cdh5.14.0/bin/hive -e "$HQL_origin"
#导入点击流模型pageviews数据到
HQL_pvs="load data inpah "$pageView" overwrite into table $ods_click_pageviews partition(datestr='$day_0)'"
echo $HQL_pvs
/export/servers/hive-1.1.0-cdh5.14.0/bin/hive -e "$HQL_pvs"
#导入点击流模型visit数据到
HQL_vst="load data inpah "$visit" overwrite into table $ods_click_stream_visit partition(datestr='$day_0)'"
echo $HQL_vst
/export/servers/hive-1.1.0-cdh5.14.0/bin/hive -e "$HQL_vst"
```

画面 12:
```bash
#!/bin/bash
export JAVA_HOME=/export/servers/jdk1.8.0_141
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:${PATH}
#set hadoop env
export HADOOP_HOME=/export/servers/hadoop-2.6.0-cdh5.14.0
export PATH=${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}
#获取时间信息
day01=date -d'1 day' +%Y%m%d
year01=date --date=$day01 +%Y
```

画面 13:
```sql
drop table if exists dw_pvs_everyhour_oneday;
create table if not exists dw_pvs_everyhour_oneday(month string,day string,hour string,pvs bigint) partitioned by (datestr string) row format delimited fields terminated by '\001' stored as textfile;
insert into table dw_pvs_everyhour_oneday partition(datestr='20130918')
select a.month as month,a.day as day,a.hour as hour,count(*) as pvs from ods_weblog_detail a
where a.datestr='20130918' group by a.month,a.day,a.hour;

--计算每天的pvs
drop table if exists dw_pvs_everyday;
create table if not exists dw_pvs_everyday(pvs bigint,month string,day string);
insert into table dw_pvs_everyday select count(*) as pvs,a.month as month,a.day as day from ods_weblog_detail a
group by a.month,a.day;

-- 统计每小时各来访url产生的pv数，并查询存储在：{dw_pvs_referer_everyhour
