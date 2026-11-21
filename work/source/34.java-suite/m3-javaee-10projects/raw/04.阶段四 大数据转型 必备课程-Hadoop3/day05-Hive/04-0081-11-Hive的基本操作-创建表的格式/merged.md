# 11-Hive的基本操作-创建表的格式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\11-Hive的基本操作-创建表的格式【海量资源尽在 ubkz.com】.mp4
- 时长 8分15秒（音频 495s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习表的一个创建这个创建表的语法在这里这个语法比较多我们来看一下首先是create关键字后面呢这个中框号里边的external这个中框号呢表示这个关键字可以有也可以没有如果加上呢external表示创建的是外部表否则呢创建的是内部表那关于什么是外部表什么是内部表我们后面呢再给大家说
[00:29] 好后面呢这个地方呢是判断这个表是否存在哎如果说不存在我在创建这个可以避免出错这是第一个那接下来呢是每一列的一些呢这个类型还有每一列的名字OK这是他的一个啊每一个字段每一个列他的一些信息那接下来呢这个comment呢表示一些注释这个注释呢默认是不能使用中文的好接下来还有一个partention的by
[00:59] 这个呢是分区是我们创建表的分区注意这个分区啊和我们这个在myproduce的分区不太一样这里的分区呢其实是分文件夹我分多少个区呢它就会产生多少个文件夹这个不太一样还有个clusterby这个clusterby是干嘛呢clusterby呢是来分统什么叫分统呢其实分统呢在这里是分文件
[01:28] 这个有点了这个分统呢有点类似于我们myproduce中的分区啊这个下面呢有文详细的文的介绍我们先看一下还有一个叫sorted by这个是呢实现一个排序还有一个raw format这个地方呢实现一个字段的一个分割符比如说呢我可以将一个文件映射成一张表那你这个文件每个字段用的什么分割符在这里可以指定OK那么
[01:57] 接下来还有一个stored as这个表示你这个表存储的文件格式文件的格式文件的类型location这个表示我们创建的表指定它的存储位置OK这是它的一个创建表的信息那接下来我们再分别看一下它这里边一些文字描述accurate table创建一个表指定表的名字如果相同的表已经存在了再抛一场
[02:26] 我们可以使用这个if not exist来去忽略这个选项好那个internal呢表示我要创建一个web表也就是这个关键字所谓的web表呢你可以简单的理解如果创建的是web表那么我在删除表的时候呢删除表的时候web表在删除表的时候它只删除原数据不会删除真实的数据如果我们创建的是一个内部表那么在删除表的时候呢
[02:56] 内部表的数据呢和这个原数据呢和真实的数据一起删除也就是说外部表其实更安全一点而内部表呢删了之后呢我们的所有数据全部跟着删除大家可以简单的先了解一下那这里边还有个关键字呢叫like这个like呢是我们在创建表的时候呢我们可以加上这个关键字我们可以将一个已经存在的表的结构呢给它复制过来但是呢不会复制真实的数据
[03:25] OK这个RuleFormatDelimit这个表示行的一个分格符OK这个分格符也很重要还有一个叫ThirdBy这个地方呢它主要是指定的一个文件的一个数据类型文件的数据类型那比如说呢我们可以使用一个叫TestFileTestFile那如果要实现压缩呢我们可以去这个指定一个叫SecondFileOK这是它一个存储类型还有一个就是PartentionBy这个呢
[03:55] 就是我刚才说的分区那这个分区呢就是一个表呢可以拥有多个分区而每个分区呢它都是以文件夹的形式单独存在这个这个每一个目录下面OK它是以文件夹的形式存储的还有一个叫SortedBy这个呢实现一个排序排序OK那么这个RowFormat呢指定分格符而这个ClassBar呢实现一个分统
[04:23] 实验一个分统那这个分统呢其实是划分文件那么咱在这里呢有两个东西一个是分区一个是分统你可以怎么理解呢就是说如果我的数据量很大的话呢那么我这个时候呢一个文件存起来会造成单个文件过大那这个时候呢我们可以采用分统分统的话呢将这个数据拆翻成多个文件但是如果你有文件太多的话呢我们还要去分文件夹也就是分区
[04:52] 把它再拆分OK这是它的一个它的一个机制好那么接下来我们来创建一个表其实这个表呢我们已经创建过了比如说这个SlowDec.us.myhive用这个表创建一张表然后呢插入一点数据然后来查询我们来做一下吧首先呢这个地方呢大家注意创建表的时候呢如果前面没有加external表示创建的是一个内部表好我们来在这里呢
[05:22] 我们来创建一张表在这里创建一个学生表我直接把这个复制一下在这里我们去用哪个表用have用myhave我们来use一下myhave走加个分号我们来创建这个表稍等好创建成功创建成功之后我们在这里边添加一行数据大家注意我们现在操作的其实是数据仓库
[05:52] 那么在后期呢我们主要是做分析查询的对于这个表的一些增删改呢很少去做但是这里呢我们可以做一个测试像这里边添加一条数据稍等这个添加数据呢是非常消耗时间的消耗时间的所以说我们要稍等这个就添加完了添加完之后呢我们来查询一下好查询一下这个select新formstu和我们的mycircle一样的走稍等好那这个时候呢
[06:22] 我们来看没有查到数据没有查到数据是刚才这个地方呢应该是报错了报错了之后我们来看一下他说这个地方呢检查这个时间应该还是时间同步问题这个有时候呢我把这个机子呢把这个虚拟机呢进行一个挂起可能时间呢没有更新我再更新一下这个时间那我们来更新一下在这个第一台机子呢我们在这里CrawlTable然后呢-1我们把这个呢
[06:53] 来运行一下好 稍等好 拿过来来测一下来 走一下然后第二个我们也来走一下来 再运行好 第三个我们也来更新一下第三个呢在这个位置我们来更新一下走稍等我们来把这句话呢粘贴进来走好 也没有问题好 时间更新完了之后我们再来再来运行一下来 再叉热一下稍等
[07:31] 这个时间有点慢因为它插入的时候它要走这个map reduce再启动map再启动reduce已经插完了插完之后我们来查一下select from stu好稍等这个数据就查出来了说明我们这个数据是没问题的大家注意我们以后尽量避免在我们的数据仓库中进行数据的一些更改你看它这个map reduce都在启动它是非常消耗时间的而且
[08:03] 我们数据仓库的数据呢主要是用于分析而很少对它做改动OK这是我们一个简单的一个表的一个创建和数据的插入那这样我们先呢停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  - Hive Shell：Hive> show databases;

画面6：
- 展示Hive Shell执行命令的输出，显示了Hive会话初始化信息和数据库列表。
- 输出内容：
  ```
  Logging initialized using configuration in jar:file:/export/servers/apache-Hive-3.1.1-bin/lib/Hive-common-3.1.1.jar!/Hive-log4j2.properties Async: true
  Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. Spark) or using Hive 1.X releases.
  Hive Session ID = f25c7cd3-d7c2-4e74-ad4b-8876a239a/dd
  Hive> show databases;
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
  Hive> use myhive;
  OK
  Time taken: 0.034 seconds
  Hive> create table stu(id int,name string);
  OK
  Time taken: 0.755 seconds
  Hive>
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第2点各画面的代码块和输出内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

