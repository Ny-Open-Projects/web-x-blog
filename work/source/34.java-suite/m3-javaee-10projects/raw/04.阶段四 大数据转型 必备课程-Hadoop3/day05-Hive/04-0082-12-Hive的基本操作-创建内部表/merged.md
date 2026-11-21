# 12-Hive的基本操作-创建内部表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\12-Hive的基本操作-创建内部表【海量资源尽在 666java.com】.mp4
- 时长 7分34秒（音频 454s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来继续学习Hive表的创建我们先来看一下Hive表在创建的时候可以使用的一些字段类型这个表里面列出了Hive中的一些数据类型这个数据类型和我们使用的MySQL差不多你比如说四个字节的整形是一个int而八个字节是bigint还有浮点形flat和double还有字幕串是stream
[00:30] 还有VACHA那么这个String用的比较多还有一个日期Data那么集合是Array好那么这是一些常用的数据类型接下来我们来看一个操作说要创建一个表并且指定字段之间的分隔符我们来看这么一个命令是Create Table后面跟上一个表的名字STR然后指定有两个字段一个是ID一个是Name
[00:59] 它的类型呢分别是int和stream后面呢跟了这么一串那这个呢rawformat delimited然后fuse然后这个地方有个by-t这什么意思呢这个合在一起表示啊我创建这个表的时候字段之间的分隔符呢是-t这是设置一个字段分隔符这个字段分隔符呢以后有什么意义呢比如说我们以后呢在创建一个表的时候呢我们可以直接加载一个文件
[01:29] 我只要创建这个表的时候这个分隔符和我文件本身的分隔符是一致的那它就可以直接读取文件内容把文件映射成一张表也就是说你先有这么一个概念我们后面再说这个地方还有一个start as这个表示它的存储的一个文件类型是test file还有一个location这个表示我创建这个表的时候它的一个存储的一个目录是
[01:58] 根目录下边user叫S2OK S2那接下来呢我们来去把这个表呢给大家创建一下来我把它直接复制好拿到我们在这个位置我们放在这里好直接呢回车稍等好这个就创建好好创建好之后呢接下来我们来继续我们来看一下它的一个呃信息吧我们来看它的一个信息首先呢我们来看一下在这个
[02:27] user stu2下面有没有这个表打开我们的hdfs在这个user下面你看到是不是有stu2这就是那张表那么创建完表之后我们来看再看其他操作比如说这里边还有一个关键字叫as这个就画什么意思呢就是我创建一个表是stu3那么创建这个表的时候它是这个
[02:54] 将STU2的结果呢查询出来然后呢再创建这个STU3那么这样做了之后呢它有什么效果呢就相当于STU3这个表呢既复制了STU2这个表的结构那又呢去把这个STU2的内容也一起拷贝过来相当于STU3和STU2呢长得一模一样OK我们也可以做一下那么在做之前呢我们可以先给STU2呢
[03:24] 添加点数据进来在这里我们可以添加点数据insertint然后呢这个地方呢stu2values我们来写一个比如说呢第一个是id第二个是name比如说写个jack用字幕串代号okjack我们来回车这个稍微有点慢因为呢它要走myproduce我们来稍等
[03:54] 好结束了结束了之后呢我们来查一下select新from然后st2走一下好这个里边呢就进来了我们还可以再添加一条数据比如说呢我2然后呢写个这个写个叫Tom走好我们再稍等好也结束了结束之后我们再来查一下走好有两条数据那接下来呢我们来看我们可以创建在这个地方呢我们可以创建一个studio3
[04:24] 然后呢它可以将STU2的一个结果呢查出来复制到STU3上来我们来直接把这些话复制一下来在这里我们来粘贴走稍等它也在走这个MapperDuce你看所有的操作呢它的底层都是MapperDuce那么它的它的这个速度是非常慢的好结束了结束之后呢我们可以查一下STU3
[04:53] 你会发现它的数据和STOR是不是一样所以说呢这种查询方式它既拷贝表结构又拷贝表的内容我们可以记一下就是这个地方我们可以加个注释就是复制复制表结构和表内容OK然后通过吧咱们前面补一个通过复制表结构和表内容创建表创建新表
[05:31] 有了这个之后呢咱们再看下一个这个叫create table stu4 like stu2这个和上面不一样这个呢它只是来拷贝一个表结构注意它只是来拷贝一个表结构就是我把stu2的表结构呢然后呢拷贝给stu4而并不会拷贝内容我们来看一下把这个拿过来走一下完了完了之后呢我们来看看stu4有没有内容stu4走
[06:02] 你会发现没有内容那没有内容的话呢咱们可以用咱们可以查看表的结构吧DSC STU2 4我来看一下好这个是表的结构你看它这个ID是Name类型而这个这个什么呢还有一个什么呢这个ID是Int类型而这个Name呢是一个String类型你发现表结构和我们STU2是一样的OK这是拷贝表结构好那我们来继续看
[06:31] 这里边还有一些查看表的类型呢一个详细查看叫DSC Formatted然后呢加上表的名字我们来看一下走这个可以查看它的详细信息走一下你看这里边呢这个信息就非常丰富了我这个命令在这里你看它可以查看了列的名字啊还有列的类型啊还有数据库啊你所在的数据库的名字还有呢拥有者的一个类型用户用户拥有
[07:01] 用户呢叫什么名字呢root还有创建的时间啊最后访问的时间啊等等还有呢它所在的位置啊在这个user下面st2还有呢一些这个一些表的一些其他参数OK这些呢都有这是它的一些详细信息如果说你需要去查看的话呢可以使用这个dscformatted后面盖上表的名字OK这是这个命令好那么关于这个内部表的创建呢我们就先
[07:31] 介绍到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  Hive> create table stu3 as select * from stu2;
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
  Hive> select * from stu3;
  OK
  1 jack
  2 tom
  Time taken: 0.184 seconds, Fetched: 2 row(s)
  Hive> create table stu4 like stu2;
  OK
  Hive> select * from stu4;
  OK
  Time taken: 0.187 seconds
  Hive> desc stu4;
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
  Hive> select * from stu3;
  OK
  1 jack
  2 tom
  Time taken: 0.184 seconds, Fetched: 2 row(s)
  Hive> create table stu4 like stu2;
  OK
  Hive> select * from stu4;
  OK
  Time taken: 0.187 seconds
  Hive> desc stu4;
  OK
  id
  int
  name
  string
  Time taken: 0.082 seconds, Fetched: 2 row(s)
  Hive> desc formatted stu2;
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

