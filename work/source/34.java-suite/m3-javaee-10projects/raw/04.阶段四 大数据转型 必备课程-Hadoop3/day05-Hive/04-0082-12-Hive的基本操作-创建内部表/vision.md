# 画面线理解：12-Hive的基本操作-创建内部表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\12-Hive的基本操作-创建内部表【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:42, 02:18, 02:32, 03:04, 03:55, 04:15, 04:36, 05:32, 06:02, 06:33, 06:45, 07:07, 07:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:07:43

1) 这一组画面整体在讲什么（一句话）：
演示Hive中创建表的多种方式，包括建表初体验、指定字段分隔符、根据查询结果建表、根据已有表结构建表，以及查询表结构和字段类型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：“1.2. 管理表的操作”、“建表初体验”。
- 代码示例：
  ```sql
  use myhive;
  create table stu(id int,name string);
  insert into stu values (1,'zhangsan');
  select * from stu;
  ```
- 表格：Hive建表时候的字段类型，包含原始类型（BOOLEAN, TINYINT, SMALLINT, INT, BIGINT, FLOAT, DOUBLE, STRING, VARCHAR, CHAR, BINARY, DATE, TIMESTAMP, INTERVAL）和复杂类型（ARRAY, MAP, STRUCT, UNION）及其描述和示例。

画面2：
- 表格：Hive建表时候的字段类型，继续展示复杂类型（ARRAY, MAP, STRUCT, UNION）及其描述和示例。

画面3：
- 代码示例：
  ```sql
  create table if not exists stu2(id int,name string) row format delimited fields terminated by '|' stored as textfile location '/user/stu2';
  ```

画面4：
- 网页界面：Hadoop的“Browse Directory”，显示了HDFS中的文件列表，包括a.txt, app, bigtxt.txt, export, hello.txt, input等文件。

画面5：
- 代码示例：
  ```sql
  create table stu3 as select * from stu2;
  create table stu like stu2;
  ```

画面6：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果。

画面7：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果。

画面8：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果，以及查询结果：
  ```
  OK
  1 jack
  2 tom
  Time taken: 0.128 seconds, Fetched: 2 row(s)
  hive> create table stu3 as select * from stu2;
  ```

画面9：
- 代码示例：
  ```sql
  create table stu like stu2;
  ```

画面10：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果，以及查询结果：
  ```
  Time taken: 22.964 seconds
  hive> select * from stu3;
  OK
  1 jack
  2 tom
  Time taken: 0.184 seconds, Fetched: 2 row(s)
  hive> create table stu4 like stu2;
  OK
  hive> select * from stu4;
  OK
  Time taken: 0.187 seconds
  hive> desc stu4;
  OK
  id
  int
  name
  string
  Time taken: 0.082 seconds, Fetched: 2 row(s)
  ```

画面11：
- 代码示例：
  ```sql
  desc formatted stu;
  ```
- 查询结果：
  ```
  OK
  # col_name data_type comment
  id int
  name string
  # Detailed Table Information
  Database: myhive
  OwnerType: USER
  Owner: root
  CreateTime: Tue May 07 19:30:08 CST 2019
  LastAccessTime: UNKNOWN
  Retention: 0
  Location: hdfs://node01:8020/user/stu2
  Table Type: MANAGED_TABLE
  Table Parameters:
  COLUMN_STATS_ACCURATE {"BASIC_STATS":"true","COLUMN_STATS":{"id":"true","name":"true"}}
  bucketing_version 2
  numFiles 2
  ```

画面12：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果，以及查询结果：
  ```
  Time taken: 22.964 seconds
  hive> select * from stu3;
  OK
  1 jack
  2 tom
  Time taken: 0.184 seconds, Fetched: 2 row(s)
  hive> create table stu4 like stu2;
  OK
  hive> select * from stu4;
  OK
  Time taken: 0.187 seconds
  hive> desc stu4;
  OK
  id
  int
  name
  string
  Time taken: 0.082 seconds, Fetched: 2 row(s)
  hive> desc formatted stu2;
  ```

画面13：
- 命令行界面：显示了Hadoop作业的执行日志，包括MapReduce任务的执行过程和结果，以及查询结果：
  ```
  OK
  # col_name data_type comment
  id int
  name string
  # Detailed Table Information
  Database: myhive
  OwnerType: USER
  Owner: root
  CreateTime: Tue May 07 19:30:08 CST 2019
  LastAccessTime: UNKNOWN
  Retention: 0
  Location: hdfs://node01:8020/user/stu2
  Table Type: MANAGED_TABLE
  Table Parameters:
  COLUMN_STATS_ACCURATE {"BASIC_STATS":"true","COLUMN_STATS":{"id":"true","name":"true"}}
  bucketing_version 2
  numFiles 2
  ```

画面14：
- 代码示例：
  ```sql
  create table stu like stu2;
  ```
- 查询结果：
  ```
  OK
  # col_name data_type comment
  id int
  name string
  # Detailed Table Information
  Database: myhive
  OwnerType: USER
  Owner: root
  CreateTime: Tue May 07 19:30:08 CST 2019
  LastAccessTime: UNKNOWN
  Retention: 0
  Location: hdfs://node01:8020/user/stu2
  Table Type: MANAGED_TABLE
  Table Parameters:
  COLUMN_STATS_ACCURATE {"BASIC_STATS":"true","COLUMN_STATS":{"id":"true","name":"true"}}
  bucketing_version 2
  numFiles 2
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上述要点中对应的代码和命令。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT标题：1.2. 管理表的操作、建表初体验、Hive建表时候的字段类型、创建表并指定字段之间的分隔符、根据查询结果创建表、根据已经存在的表结构创建表、查询表的类型。
- 表格数据：Hive建表时候的字段类型，包含原始类型和复杂类型及其描述和示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
