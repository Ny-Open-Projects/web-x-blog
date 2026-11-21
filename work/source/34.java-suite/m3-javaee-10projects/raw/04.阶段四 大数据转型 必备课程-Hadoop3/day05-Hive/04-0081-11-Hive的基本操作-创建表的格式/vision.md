# 画面线理解：11-Hive的基本操作-创建表的格式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\11-Hive的基本操作-创建表的格式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:30, 03:32, 04:20, 05:21, 05:30, 05:45, 06:13, 06:29, 07:04, 07:21, 07:37, 07:58, 08:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:03:41

1) 这一组画面整体在讲什么（一句话）：
讲解Hive创建数据库表的语法、表属性（分区、分桶、存储格式等）及通过Hive Shell进行实际操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示Hive创建数据库表的语法结构，高亮显示了CREATE TABLE语句的完整语法。
- 代码块内容：
  ```
  CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name
  ([col_name data_type [COMMENT col_comment], ...]
  [COMMENT table_comment]
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
  [CLUSTERED BY (col_name, col_name, ...) INTO num_buckets BUCKETS]
  [SORTED BY (col_name [ASC|DESC], ...) ]
  ROW FORMAT row_format
  STORED AS file_format
  [LOCATION hdfs_path]
  ```
- 说明文字：
  1. CREATE TABLE 创建一个指定名字的表。如果相同名字的表已经存在，则抛出异常；用户可以用 IF NOT EXISTS 选项来忽略这个异常。
  2. EXTERNAL 关键字可以让用户创建一个外部表，在建表的同时指定一个指向实际数据的路径（LOCATION），Hive 创建内部表时，会将数据移动到数据仓库指向的路径；若创建外部表，仅记录数据所在的路径，不对数据的位置做任何改变。在删除的时候，内部的元数据和数据会一起被删除，而外部表只删除元数据，不删除数据。
  3. LIKE 允许用户复制现有的表结构，但是不复制数据。
  4. ROW FORMAT DELIMITED FIELDS TERMINATED BY char MAP KEYS TERMINATED BY char | SERDE serde_name [WITH SERDEPROPERTIES (property_name=property_value, property_name=property_value, ...)]
  5. STORED AS SEQUENCEFILE | TEXTFILE | RCFILE
  6. PARTITIONED BY
  7. SORTED BY
  8. ROW FORMAT
  9. CLUSTERED BY

画面2：
- 继续展示Hive创建表语法的说明部分，高亮显示了第4点“ROW FORMAT DELIMITED...”。
- 说明文字：
  4. ROW FORMAT DELIMITED FIELDS TERMINATED BY char MAP KEYS TERMINATED BY char | SERDE serde_name [WITH SERDEPROPERTIES (property_name=property_value, property_name=property_value, ...)]
  用户在建表的时候可以自定义 SerDe 或者使用自带的 SerDe。如果没有指定 ROW FORMAT 或者 ROW FORMAT DELIMITED，将会使用自带的 SerDe。在建表的时候，用户还需要为表指定列的同时也会指定自定义的 SerDe，Hive 通过 SerDe 确定具体的列的数据。

画面3：
- 继续展示Hive创建表语法的说明部分，高亮显示了第5点“STORED AS SEQUENCEFILE | TEXTFILE | RCFILE”。
- 说明文字：
  5. STORED AS SEQUENCEFILE | TEXTFILE | RCFILE
  如果文件数据是纯文本，可以使用 STORED AS TEXTFILE。如果数据需要压缩，使用 STORED AS SEQUENCEFILE。

画面4：
- 展示Hive表的分区（PARTITIONED BY）、排序（SORTED BY）和分桶（CLUSTERED BY）概念的说明。
- 说明文字：
  6. PARTITIONED BY
  分区。一个表可以拥有一个或者多个分区，每个分区以文件夹的形式单独存在表文件夹的目录下。
  7. SORTED BY
  排序
  8. ROW FORMAT
  9. CLUSTERED BY
  对于每一个表（table）或者分区，Hive可以进一步组织成桶，也就是描述更为细粒度的数据范围划分。Hive也是针对某一列进行桶的组织。Hive采用对列进行哈希，然后根据以桶的个数来决定该记录存放在哪个桶当中。
  把表（或者分区）组织成桶（Bucket）有两个理由：
  （1）获得更高的查询处理效率。桶为添加上了额外的结构，Hive在处理有些查询时能利用这个结构。具体而言，连接两个在（包含连接列的）相同列划分了桶的表，可以使用 Map 端连接（Map-side join）高效地实现。比如JOIN操作。对于JOIN操作两个表有一个相同的列，如果对这两个表都进行了桶操作。那么将保存相同列值的桶进行JOIN操作就可以，可以大大减少JOIN的数据。
  （2）使取样（sampling）更高效。在处理大规模数据集时，在开发和修改查询的阶段，如果能在数据集的一小部分数据上进行运行查询，会带来很多方便。

画面5：
- 展示Hive建表体验的代码示例，同时显示了两个终端窗口，一个为SecureCRT，另一个为Hive Shell。
- 代码块内容：
  ```
  use myhive;
  create table stu(id int,name string);
  insert into stu values ("1","zhangsan");
  select * from stu;
  ```
- 窗口标题：
  - SecureCRT：f4j:/imp/StaticLoggerBinder.class
  - Hive Shell：hive> show databases;

画面6：
- 展示Hive Shell执行命令的输出，显示了Hive会话初始化信息和数据库列表。
- 输出内容：
  ```
  Logging initialized using configuration in jar:file:/export/servers/apache-hive-3.1.1-bin/lib/hive-common-3.1.1.jar!/hive-log4j2.properties Async: true
  Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. spark) or using Hive 1.X releases.
  Hive Session ID = f25c7cd3-d7c2-4e74-ad4b-8876a239a/dd
  hive> show databases;
  OK
  default
  myhive
  mytest2
  Time taken: 0.776 seconds, Fetched: 3 row(s)
  ```

画面7：
- 展示Hive Shell中执行“use myhive;”和“create table stu(id int,name string);”命令后的输出。
- 输出内容：
  ```
  hive> use myhive;
  OK
  Time taken: 0.034 seconds
  hive> create table stu(id int,name string);
  OK
  Time taken: 0.755 seconds
  hive>
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第2点各画面的代码块和输出内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
