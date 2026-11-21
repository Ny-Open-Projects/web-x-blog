# 16-Hive的基本操作-表结构修改和数据加载

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\16-Hive的基本操作-表结构修改和数据加载【海量资源尽在 ubkz.com】.mp4
- 时长 4分18秒（音频 258s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来看修改表操作修改表呢就是对一些表结构进行一些修改我们先看第一个对表进行重命名这个重命名呢和我们mycircle里边差不多就altar table一个old name然后呢rename to一个新的名字这里边呢比如说呢我们可以来一个比如说altar tablescal4呢rename to scal5
[00:29] 可以把Score4呢除名为Score5我们来试一下把这个复制来放在这个位置我看我现在有没有Score4有一个没有Score4那我们再换一个比如说我们可以把这个STU4变成一个STU5好走这时候我们来再收Table4这个时候呢我们就拿到了这个STU5好接下来我们再看一个
[01:03] 查看表结构这个我们刚才演示过DSE我就不演示了还有个添加列比如说呢我有三列我可以新添加一个列那这个叫ADD columns后边跟上你要添加的列这是添加列简单了解一下用的不多好还有一个叫更新列这个更新列呢其实呢相当于啊给这个列呢更新一个类型你比如说呢这个地方叫清洁
[01:32] 然后column然后把这个呢这个列呢改成一个什么呢改成一个int类型这个是将这个列呢这个列的名字呢改成这个名字然后呢这个类型呢是int这个用的也比较少还有一个删除表删除表是dropdrop table然后后面跟上表的名字OK这是更改表那接下来呢还有一个项表中加载数据这个我们也做过我们再看一下首先呢
[02:02] 比如说我将分区表中的插入数据那这里面我先创你一个表创你一个表OK那这个表呢它的结构呢是一个scoreOK把score的表结构复制到score3里面去那接下来呢插入数据insert intoscore3然后这个里面一个分区指定一个分区字段然后呢后面跟上它的一个值这种用的呢非常少因为什么呢因为这种呢画的它的效率非常低
[02:32] 还有呢我们真实去做数据分析的时候我们的数据都是来自外部而这种呢基本上不用还有呢通过这种查询的方式呢插入数据这个呢其实就是我们呢可以通过一个什么呢通过一个load的方式加载数据你比如说呢我们这个地方呢有一个load data这个local表示从本地加载把这个文件呢通过覆盖的方式加在这个表里边而且呢这个地方还可以指定一个分区
[03:02] 你要去加在了哪个分区里边这个是partention最后一个是通过查询的方式这种方式用的比较多比如说你创建一个scal4我们来做一下这个吧把这个复制一下OK那这个复制scal的一个表结构然后我去插入数据插入数据的话那么这个分区我指定是2018-06它的数据来自哪里呢来自这个表把这个表的数据查出来之后
[03:33] 我要去把它覆盖到这个表里面去来我们来做一下这个事好拿过来拿过来之后直接在这里走一下稍等它又开始执行这个MapReduce我们来等待吧好执行完了执行完之后呢我们刚才呢向这个Skos里边呢查了数据那我们来查询一下Skos SlidesceneFrom Skos好我们来看一下这里边是不是已经有数据了这些数据呢
[04:06] 都是从思考里边查询出来的好那么这个就是它的一个表的一个修改还有呢表的一个数据加赛OK那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲Hive表的修改操作，包括重命名、增加/修改列信息、删除表以及加载数据。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

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
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面4：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面5：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面6：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

画面7：
- 展示了Hive表修改章节（1.6. 修改表）。
- 重命名基本语法：alter table old_table_name rename to new_table_name;
- 示例：alter table score4 rename to score5;
- 展示了“增加/修改列信息”下的“查询表结构”（desc scores;）和“添加列”（alter table score5 add columns (mycol string, myscu string);）。
- 展示了“更新列”（alter table score5 change column myscu mysconew int;）。
- 展示了“删除表”（drop table scores;）和“Hive表中加载数据”（create table score like score; insert into table score partition(month='201807') values ('001','002','100');）。

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
Hive> show tables;
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
Hive> alter table stu4 rename to stu5;

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
子标题：重命名、增加/修改列信息、删除表、Hive表中加载数据。
子标题：重命名基本语法：alter table old_table_name rename to new_table_name;
子标题：示例：alter table score4 rename to score5;
子标题：增加/修改列信息：
- 查询表结构：desc scores;
- 添加列：alter table score5 add columns (mycol string, myscu string);
- 查询表结构：desc scores;
- 更新列：alter table score5 change column myscu mysconew int;
子标题：删除表：drop table scores;
子标题：Hive表中加载数据：
- 直接向

