# 画面线理解：13-Hive的基本操作-创建外部表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\13-Hive的基本操作-创建外部表【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:29, 03:40, 04:01, 05:38, 06:54, 07:21, 08:03, 08:50, 09:17, 10:43, 11:09, 11:57, 12:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:11:27

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建外部表并从本地文件系统和HDFS文件系统加载数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Hive执行完一个MapReduce任务后的日志，接着执行了创建表stu4和删除表student的命令。
画面2：在Hadoop Web UI中浏览HDFS目录，路径为/user/hive/warehouse/myhive.db/stu3，显示一个名为000000_0的文件。
画面3：展示Notebook中的Hive操作案例，包括创建外部表teacher和student的SQL语句，以及加载数据的命令。
画面4：Notebook中高亮显示创建student表的SQL语句。
画面5：Notebook中显示加载数据的SQL语句，并提示从HDFS文件系统向表中加载数据。
画面6：在SecureCRT中执行Hive命令，先删除表stu3，然后创建teacher和student表，接着尝试加载本地数据，但因路径错误失败。
画面7：在Excel中显示student.csv文件的内容，包含学生姓名、出生日期和性别。
画面8：在SecureCRT中成功加载本地数据到student表，并查询显示了8行数据。
画面9：在SecureCRT中查询student表，因表不存在报错，然后创建student表并再次查询成功。
画面10：Notebook中高亮显示加载数据的SQL语句。
画面11：在SecureCRT中执行命令，将student.csv和techer.csv文件移动到hivedatas目录，并创建HDFS目录。
画面12：在Hadoop Web UI中浏览HDFS根目录，显示多个文件和目录。
画面13：在Hadoop Web UI中浏览/hivedatas目录，显示techer.csv文件。
画面14：Notebook中显示从HDFS文件系统向表中加载数据的命令，包括cd、hdfs dfs -mkdir -p、hdfs dfs -put和load data inpath命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
hive> create table stu4 like stu2;
hive> drop table student;
```
画面3：
```
create external table teacher (t_id string,t_name string) row format delimited fields terminated by '\t';
create external table student (s_id string,s_name string,s_birth string ,s_sex string) row format delimited fields terminated by '\t';
load data local inpath '/export/servers/hivedatas/student.csv' into table student;
load data local inpath '/export/servers/hivedatas/student.csv' overwrite into table student;
```
画面6：
```
hive> drop table stu3;
hive> create external table teacher (t_id string,t_name string) row format delimited fields terminated by '\t';
hive> create external table student (s_id string,s_name string,s_birth string ,s_sex string) row format delimited fields terminated by '\t';
hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
```
画面8：
```
hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
hive> select * from student;
```
画面9：
```
hive> select * from student;
hive> create external table student (s_id string,s_name string,s_birth string ,s_sex string) row format delimited fields terminated by '\t';
hive> select * from student;
```
画面11：
```
[root@node03 servers]# mkdir hivedatas
[root@node03 servers]# rz -E
Transferring student.csv...
Transferring techer.csv...
[root@node03 servers]# ls
apache-hive-3.1.1-bin  jdk1.8.0_141  techer.csv
hive sql  student.csv  zookeeper-3.4.9
[root@node03 servers]# mv student.csv hivedatas/
[root@node03 servers]# mv techer.csv hivedatas/
[root@node03 servers]# cd hivedatas
[root@node03 hivedatas]# hdfs dfs -mkdir -p /hivedatas
```
画面14：
```
cd /export/servers/hivedatas
hdfs dfs -mkdir -p /hivedatas
hdfs dfs -put techer.csv /hivedatas/
load data inpath '/hivedatas/techer.csv' into table teacher;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3、4、5、10、14：PPT标题为“操作案例”，子标题为“分别创建老师与学生外表表，并向表中加载数据”。
画面3、4、5、10、14：PPT中包含“创建老师表”、“创建学生表”、“加载数据”、“加载数据并覆盖已有数据”、“从hdfs文件系统向表中加载数据”等小标题。
画面14：PPT中包含“1.4 分区表”标题，内容为“在大数据中，常用的一种数据表就是分区表，我们可以把大的文件切割分成一个的文件，这样每次操作一个”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
