# 15-Hive的基本操作-创建分桶表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\15-Hive的基本操作-创建分桶表【海量资源尽在 ubkz.com】.mp4
- 时长 8分35秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习分同表刚才呢我们学过分区表分区表呢是分文件夹而这里的分同表呢是分文件比如说呢一个文件夹下面的文件过大那这个时候呢我们需要将一个文件拆分成多个文件那这个时候就需要用分同表那分同表怎么创建呢我们来看一下要去创建分同表呢首先呢
[00:28] 需要去开启Hive的一个分统功能那怎么去开启呢这里有一个设置叫SetHiveInforcePacketingOK然后等于True我们要去做这一个设置来我们来看一下把这个呢先开启在这里我们需要做个开启稍等我们来去开启Hive功能来稍等我们再把这个刚才这个呢把这句话粘贴复制一下好拿过来
[01:00] 然后在这里好这里呢我们可以先去把这个等于处呢先去掉如果说直接呢去执行这么一个set命令它呢会查看它默认的一个值来我们来加个分号走你看它说呢这个地方呢它说没有被定义我们加一个处稍等我们等于处走好那这个时候呢就开启了一个分统功能好那么接下来还要做一件事情我们要设置reduce的个数
[01:29] 那这里呢很多很多同学很奇怪为什么要设置Reduce的个数呢是这样的分统表示分成多个文件它凭什么能够分成多个文件呢它其实内部呢就是走的是我们之前MapReduce中的一个分区那我们MapReduce分区的时候我们是不是也要设置Reduce的个数那这里也是一样的我们来做一个设置就SetMapReduceJobReduce来我们呢把这个复制一下好
[01:59] 在这里我们来看一下把等于3去掉我们来看默认值这里默认值是-1-1表示Reduce的个数是不限制的这里的话我们为了测试我们设置一个固定的值比如说设置成3也就是三个Reduce那么意味着以后分统之后最多产生三个文件回车这个时候我们就设置完了设置完了之后接下来我们来继续我们来创建一个分统表
[02:29] 创建分头表你会发现前边和以前一样那还有一个问题呢在后面呢我们有一个什么呢叫cluster by这个cluster by呢它其实就实现了一个分统那么分统的话呢这个地方需要指定一个分统的字段这个分统的字段呢必须是你前面已经存在的一个字段这个你可以理解成呢按照哪一个字段分统
[02:56] 也就是我们MAP REDUCE中按照哪一个哪一个什么呢哪一个K2进行了一个分区那这个地方呢它怎么分呢它其实用这个我们以前这个叫Hashi Partner它会和Hashi Partner呢然后呢对这个Reduce个数去磨不是去磨去磨之后呢它就会存放在不同的Reduce上然后呢去存放在不同的文件中
[03:24] 这个和以前是一样的OK那后面的一个int这个地方是3这个就叫buckets这个是什么意思呢就说我分完桶之后呢我把这些文件呢放在三个桶里边其实就放在三个文件里边而后面呢是一个行的分割服OK我们把这个呢拿过来我们来运行一下好在这里走回车好这个时候我们就创建一个分桶表重点是这个按照哪一个字段分桶
[03:54] 把它放在几个桶里边好 这是一个核心那么分完桶之后呢注意这个表呢我们需要给这张表加载数据那么给这张表呢添加数据的时候呢不能用我们之前这个load data为什么呢因为呢给这个分同表加载数据的时候它要走map reduce所以说呢我们需要怎么办呢我们需要去先建一个中间表先建一个中间表然后我给中间表呢添加数据
[04:23] 中间表添加完数据呢我再通过中间表给我们的分同表添加数据所以说呢我先添加个cos common这个中间表来我们来看一下在这里这个叫cos common走这个完了之后呢回到我们讲义在这里呢我给分同表添加数据不是给分同表给这个中间表添加数据这个cos.csv我有没有这个文件呢
[04:53] 我们来看一下有没有在export Service have data在这里有一个我看这里是一个是一个什么cost的CFV还没有没有的话我给它上传一下再还是在我这个测试数据里边在这个地方一个叫cost的CFV你可以把这里的所有数据一次性全部上传OK好上传之后呢我们就有这个数据了我们给刚才这个中间表
[05:24] 给他添加数据好在这里走不是在这里去执行啊在这个have的命令行中好走那这样的话我们的这个中间面就有数据了有了数据之后呢接下来我们该给分同表添加数据怎么添加呢我们用一个命令叫insert overwrite这个insert overwrite呢你看insert overwrite tablecause这个cause是不是就是我们的分同表然后呢怎么给他添加数据呢
[05:52] 我去查询另外一张表另外一张表就是中间表然后Cluster By按照CAD来分统也就是说把这个表查完之后按照CAD来分统把这个结果放到这个表里边去OK那么这个时候我们就可以把它添加数据我们来做一下好 稍等我们放在这个位置来 执行一下走稍等它需要去走MapReduce
[06:22] 所以说呢这个过程呢会有点漫长也就是说我们给分统表添加数据必须走MapReduce那么要走MapReduce必须有中间表我们先要将数据放在中间表里边然后呢去查询中间表查完之后呢我们来进行一个分统然后分统之后呢然后我们把这个数据呢添加到这个分统表里边去OK这是它的一个过程那我们稍等一下好
[06:51] 这个map呢百分百你看它这个地方reduce的个数是三个好reduce呢你看百分之三十三一个reduce执行完了然后六十七接下来再等好马上执行完好你看刚才呢我们执行的是state一也就是第一个map reduce你看接下来呢它又一个state二那接下来还有一个state应该是一个state三那么它终于执行完了执行完之后呢
[07:24] 接下来我们来看一个效果那么我们给这个分同表添加完数据之后我们来打开HDFS打开HDFS在HDFS里边我们来找到这个表在user havemore than warehouse然后myhive db我们找到这个cause这是一个分同表如果不出意外的话这个表里边应该有三个文件你看是不是有三个文件这三个文件其实就是我们刚把我们
[07:53] 那个这个什么呢这个cost.csv里边的文件呢拆分成三个拆分成三个我们可以点开可以随便点开看一个稍等这里边呢这个数据你看稍等好你看了这里边有一个数据03英语03OK这是其中的一个文件OK这个时候呢我们的分头表的作用就体现出来了它可以将一个大的文件呢分成多个小文件OK
[08:28] 这是一个分同表的一个基本创建那么关于分同表的基本操作呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hive 中使用分桶表（bucketed table）和普通表（regular table）进行数据建模与加载，包括设置分桶参数、创建表结构、加载数据及通过 insert overwrite 方式插入数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 文档中关于“1.5. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set Hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 文档底部提示“创建普通表”并展示另一段 SQL：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 2：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了查询结果（36 行数据）和执行时间（2.664 秒）。
- 命令行中显示了设置分桶参数的语句：
  Hive> set Hive.enforce.bucketing=true;
- 后续执行了创建表语句：
  Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 显示了创建普通表语句：
  Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 3：
- 展示了 Typora 文档中关于“1.3. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set Hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';

画面 4：
- 展示了 Typora 文档中关于“1.5. 分桶表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  set Hive.enforce.bucketing=true;
  set mapreduce.job.reduces=3;
  create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
- 文档中新增了“创建普通表”语句：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
- 文档中新增了“普通表中加载数据”语句：
  load data local inpath '/export/servers/hivedatas/course.csv' into table course_common;

画面 5：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了执行创建分桶表和普通表的命令及结果：
  Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
  Time taken: 0.305 seconds
  Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
  Time taken: 0.08 seconds

画面 6：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 显示了执行创建分桶表和普通表的命令及结果：
  Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
  Time taken: 0.305 seconds
  Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
  Time taken: 0.08 seconds

画面 7：
- 展示了 Typora 文档中关于“1.6. 修改表”的章节内容。
- 文档中包含以下 Hive SQL 语句：
  create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
- 文档中新增了“通过 insert overwrite table course select * from course_common cluster by(c_id);”语句，用于将普通表数据插入分桶表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
set Hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 2：
Hive> set Hive.enforce.bucketing=true;
Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';

画面 3：
set Hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';

画面 4：
set Hive.enforce.bucketing=true;
set mapreduce.job.reduces=3;
create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
load data local inpath '/export/servers/hivedatas/course.csv' into table course_common;

画面 5：
Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
Time taken: 0.305 seconds
Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
Time taken: 0.08 seconds

画面 6：
Hive> create table course (c_id string,c_name string,t_id string) clustered by(c_id) into 3 buckets row format delimited fields terminated by '\t';
Time taken: 0.305 seconds
Hive> create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
Time taken: 0.08 seconds

画面 7：
create table course_common (c_id string,c_name string,t_id string) row format delimited fields terminated by '\t';
通过 insert overwrite table course select * from course_common cluster by(c_id);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

