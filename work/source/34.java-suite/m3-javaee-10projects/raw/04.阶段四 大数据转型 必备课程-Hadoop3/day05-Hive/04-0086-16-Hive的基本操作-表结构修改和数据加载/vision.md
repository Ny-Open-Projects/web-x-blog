# 画面线理解：16-Hive的基本操作-表结构修改和数据加载

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\16-Hive的基本操作-表结构修改和数据加载【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:36, 00:52, 01:07, 01:21, 01:55, 02:00, 02:29, 02:50, 03:17, 03:22, 03:44, 03:50, 04:11, 04:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:28:32

1) 这一组画面整体在讲Hive表的修改操作，包括重命名、增加/修改列信息、删除表以及加载数据。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面2：
- 展示了在SecureCRT中执行Hive命令的终端界面。
- 执行了show tables;，列出当前数据库中的表。
- 执行了alter table stu4 rename to stu5;，将表stu4重命名为stu5。

画面3：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面4：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面5：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面6：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面7：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

画面2：
hive> show tables;
course
score_common
score
score2
stu2
student
stu4
t_test
teacher
techer
hive> alter table stu4 rename to stu5;

画面3：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

画面4：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

画面5：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

画面6：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

画面7：
alter table old_table_name rename to new_table_name;
alter table score4 rename to score5;
desc scores;
alter table score5 add columns (mycol string, myscu string);
alter table score5 change column myscu mysconew int;
drop table scores;
create table score like score;
insert into table score partition(month='201807') values ('001','002','100');

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：1.6. 修改表
子标题：重命名、增加/修改列信息、删除表、hive表中加载数据。
子标题：重命名基本语法：alter table old_table_name rename to new_table_name;
子标题：示例：alter table score4 rename to score5;
子标题：增加/修改列信息：
- 查询表结构：desc scores;
- 添加列：alter table score5 add columns (mycol string, myscu string);
- 查询表结构：desc scores;
- 更新列：alter table score5 change column myscu mysconew int;
子标题：删除表：drop table scores;
子标题：hive表中加载数据：
- 直接向
