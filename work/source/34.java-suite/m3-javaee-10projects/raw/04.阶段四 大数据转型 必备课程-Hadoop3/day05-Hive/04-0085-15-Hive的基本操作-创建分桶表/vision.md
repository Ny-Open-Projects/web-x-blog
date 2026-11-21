# 画面线理解：15-Hive的基本操作-创建分桶表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\15-Hive的基本操作-创建分桶表【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:26, 03:45, 04:20, 04:37, 04:52, 05:20, 05:31, 06:18, 07:05, 07:13, 07:38, 08:06, 08:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:21:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hive 中使用分桶表（bucketed table）和普通表（regular table）进行数据建模与加载，包括设置分桶参数、创建表结构、加载数据及通过 insert overwrite 方式插入数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 文档中关于“1.5. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 文档底部提示“创建普通表”并展示另一段 SQL：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 2：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了查询结果（36 行数据）和执行时间（2.664 秒）。
- 命令行中显示了设置分桶参数的语句：
  hive> set hive.enforce.bucketing=true;
- 后续执行了创建表语句：
  hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 显示了创建普通表语句：
  hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 3：
- 展示了 Typora 文档中关于“1.3. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';

画面 4：
- 展示了 Typora 文档中关于“1.5. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 文档中新增了“创建普通表”语句：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
- 文档中新增了“普通表中加载数据”语句：
  load data local inpath '/export/servers/hivedatas/course.csv' into table course_common;

画面 5：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了执行创建分桶表和普通表的命令及结果：
  hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
  Time taken: 0.305 seconds
  hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
  Time taken: 0.08 seconds

画面 6：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了执行创建分桶表和普通表的命令及结果：
  hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
  Time taken: 0.305 seconds
  hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
  Time taken: 0.08 seconds

画面 7：
- 展示了 Typora 文档中关于“1.6. 修改表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
- 文档中新增了“通过 insert overwrite table course select * from course_common cluster by(c_id);”语句，用于将普通表数据插入分桶表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
set hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 2：
hive> set hive.enforce.bucketing=true;
hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 3：
set hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';

画面 4：
set hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
load data local inpath '/export/servers/hivedatas/course.csv' into table course_common;

画面 5：
hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
Time taken: 0.305 seconds
hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
Time taken: 0.08 seconds

画面 6：
hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
Time taken: 0.305 seconds
hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
Time taken: 0.08 seconds

画面 7：
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
通过 insert overwrite table course select * from course_common cluster by(c_id);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
