# 23-网站流量日志分析-hive表数据分析和导出

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\23-网站流量日志分析-hive表数据分析和导出【海量资源尽在 ubkz.com】.mp4
- 时长 6分52秒（音频 413s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 再将数据导入到Hive之后接下来呢其实在Hive表里面呢对数据进行统计分析根据呢我们的需求去写相应的类Circle指令这部分呢因为时间的关系我们不能呢把每一个需求的分析呢都给大家去讲到位这里边呢我只能给大家提供一些资料来看我们这个在这个资料里边有一个有一个网络日志分析脚本代码
[00:29] 在这里边有一个叫什么呢Hive Circle好从我们的这个第四个一直到我们的这个第八个这里边全是基于Hive的一个分析比如说我们点开第四个好点开在这里我们来看这里边呢是一系列的分析的过程比如说咱们看看最简单的吧比如说我们来求每一个小时它的PVS什么叫PVS呢PV就是一个Page View
[01:00] 那么PVS就是每一个小时那么它的一个访问次数就是我们页面的访问次数在这里呢我们可以用Select Counting来统计然后呢统计完之后呢后边有一个叫什么Goal By根据呢我们的小时来分组这个呢就可以求出每个小时它的访问的一个PV量还有呢比如说还可以求什么呢按照这个统计每个小时呢来来访的一个URL产生的PV量等等
[01:30] 这些都是一些统计的一些类似的指令好那么这些呢大家下去可以自己去详细的看一下OK一直到我们的到最后有个Hive的集联求和都是对Hive的一个统计分析好这一块呢我们就先说到这里那么统计分析完之后接下来去进行哪一步呢我们来回到这个教案来看一下那么统计完分析完之后呢我们要将统计后的数据呢导出
[01:59] 因为统计后的数据呢很多都是存在我们的HDFS上所以说呢我们需要将HDFS的数据呢导入到mycircle然后导入到mycircle之后呢便于下一步的一个这个结果的一个展示那怎么导出呢来还是回到我刚才提供的这个资料里面在这里边有一个叫什么呢要scope的导出结果在这里边呢我们有一个脚本我们来看一下打开了这个脚本
[02:27] 这个脚本呢就是实现一个scope的一个数据的一个导出就是将数据从HDFS上导入到我们的mycircle数据库里边好这些呢是一些条件判断获取当前的时间然后呢获取完之后呢这里边用了这么一个命令export来导出连接了我们的一个数据库用密合密码它是自动获取因为这里边呢这些呢参数
[02:57] 它都可以去拿到拿到之后呢通过这么一个脚本的执行就可以将HDFS数据呢导到我们的MindCircle里面去那么导到哪里呢我们来看一下在我的这个MindCircle在我Windows的MindCircle里边有一个WeblogView这里边有两张表这些表数据呢就是从HDFS导过来的这是比如说这个是AVGPV这是一个平均每天的平均访问量页面的访问量这个
[03:26] flow number是每天的页面的访问信息OK 这个导出来了好 那么大家看从我们预处理一直到数据的导出它其实是一系列的流程我们再看以前的这个图来看我们刚才说导出到mycircle那么从flow收集一直到导到mycircle这一系列的流程其实需要有一个人来调度这个就是阿兹卡班这个阿兹卡班
[03:54] 它可以将这一切的流程写成一个脚本写成一些任务然后放在阿兹卡班上它给我们去调度所以说呢这里边还涉及到阿兹卡班的一个操作来我们回到这个资料里边在这个资料里边呢我给大家提供了一个阿兹卡班的一个调度脚本我们来看一下这里边一共有五个脚本五个脚本这五个脚本呢就是将我们刚才讲过的所有的操作写成一个任务
[04:22] 然后把它打包打包成一个zip包只要我把这个放在我们的阿兹卡班上它就能够自动运行那我们分别来看一下这些教步吧第一个一教步我们来看一下在这个里边呢它干了什么事呢我们来看它其实呢执行了一个加包执行了我们的预处理也就是我们数据清晰阶段的一个加包这里边有个类叫weblog pre process其实这个就是我们的第一个Mapper deals
[04:52] 咱们再看第二个第二个呢第二个其实执行的是第二个myproduce在这个地方呢它还写了一个dependency等于1这个表示什么意思呢表示我依赖于第一个脚步好还有第三个脚步第三个脚步呢它呢依赖于第二个它也执行一个myproduce好了第四个脚步第四个脚步的话呢它是执行一个脚本叫4.sh它依赖于第三个那这个是干嘛的吗
[05:22] 我来看看4.sh点开你会发现4.sh呢其实是干了这么一件事其实呢这个地方有一个叫load data它其实将我们生成的模型数据呢表数据呢导入到我们对应的表里面去导入到Hive表里面去这个是导入Hive仓库的一个脚本OK我们来执行它导入之后呢我们就进入5.job5.job呢它其实
[05:50] 用Hive-f来执行一个circle一个脚本它呢依赖于第四个脚我们来看这个5.circle这个5.circle干了什么事呢它其实就是在分析我们的Hive的数据对我们Hive的数据进行分析比如说统计呢一天的访问量一个小时的访问量还有呢计算每天的PPS等等这个就是我刚才给大家说的Hive的数据分析也就是写类circle好那么这个有了之后呢
[06:20] 我们可以把这些教科呢统一打成包打成包之后呢我们直接把它放在我们的阿兹卡班上我们就可以调度而且可以定时调度OK这是我们的阿兹卡班好回到我们刚才这个图也就是说这个图里边我们基本上的所有知识点都给大家讲到了只有最后一个就是如何将我们查询出来的结果或者分析出来的结果展示到我们的页面上
[06:48] 还通过外放呢可以展示到页面上这个地方我们来讲一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
#目标Hive表
ods_weblog_origin="weblog.ods_weblog_origin"
ods_click_pageviews="weblog.ods_click_pageviews"
ods_click_stream_visit="weblog.ods_click_stream_visit"
#导入数据到weblog.ods_weblog_origin
HQL_origin="load data inpah "$log_pre_output" overwrite into table $ods_weblog_origin partition(datestr='$day_0)'"
echo $HQL_origin
/export/servers/Hive-1.1.0-cdh5.14.0/bin/Hive -e "$HQL_origin"
#导入点击流模型pageviews数据到
HQL_pvs="load data inpah "$pageView" overwrite into table $ods_click_pageviews partition(datestr='$day_0)'"
echo $HQL_pvs
/export/servers/Hive-1.1.0-cdh5.14.0/bin/Hive -e "$HQL_pvs"
#导入点击流模型visit数据到
HQL_vst="load data inpah "$visit" overwrite into table $ods_click_stream_visit partition(datestr='$day_0)'"
echo $HQL_vst
/export/servers/Hive-1.1.0-cdh5.14.0/bin/Hive -e "$HQL_vst"
```

画面 12:
```bash
#!/bin/bash
export JAVA_HOME=/export/servers/JDK 8.0_141
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:${PATH}
#set Hadoop env
export HADOOP_HOME=/export/servers/Hadoop-2.6.0-cdh5.14.0
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

