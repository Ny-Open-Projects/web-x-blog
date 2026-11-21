# 13-Hive的基本操作-创建外部表

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\13-Hive的基本操作-创建外部表【海量资源尽在 ubkz.com】.mp4
- 时长 12分44秒（音频 765s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在学习完内部表之后接下来我们来学习外部表那么刚才我们说过内部表和外部表最大的区别是什么呢内部表呢当我们在删除这个表的时候呢不仅会删除它的原数据而且呢会删除表本身的数据而外部表呢在删除的时候它只会删除原数据刚才呢我们创建了一些内部表比如说我把它删除一下我们来看一下这个效果好在这里呢
[00:29] 我们来show一个table4好在这里呢我刚才创建了很多表比如说在stu3这张表我们来看看它有没有数据select新from stu3好这里边有两行数据那么这个表的数据在哪里呢我们可以打开我们的hdfs在这里呢在应该是在user下面有一个叫hivehive下面有一个warehouse那么我们用的数据库是myhive
[01:01] 我们进来好进来之后呢我们找STU3你发现这里有文件这个文件呢其实就是我们的表数据那当我删除这个STU3的时候这个文件也会随着删除来我们来看一下好在这里我来删除这张表怎么删呢drop table然后呢后面跟上STU3走好删完之后呢我们再看HDFS刷新
[01:31] 好你会发现他说这个目录已经不存在了我们再进来看一下在userhivewarehouse然后呢myhive你发现stu3已经不存在了说明什么意思呢说明内部表在删的时候他会将原数据和表本身的数据呢全部删除那接下来我们再学习外部表外部表呢他和内部表是不一样的
[02:00] 我们来看外表一个特点那么外部表是这样的一般我们建完这个表之后我们这个数据一般是从外部加载过来的而加载过来的这个数据我们的外部表认为它不会独自占用这份数据而是可以和其他表共享这份数据所以说我们在删的时候它不会把这个数据真正的删除那它有什么用场景呢我们来看
[02:29] 比如说我们在应用中比如说有时候一个网站每天要收到网站的一些日志信息它会定期的写到我们的HDFS上那么我们需要在日志的基础上做一些大量的统计分析那么我们做分析可能别人也会做分析那么在做分析的时候这颗数据本来就是应该大家是共享的所以说这个时候为了避免某一个人在删的时候
[02:59] 我们的原始数据删掉我们一般采用外部表来存储OK那么接下来我们来看它的一个案例那创建外部表呢其实和创建内部表差不多在创建外部表的时候呢我们只需要加个关键字这个关键字呢叫external比如说呢这里就创建了一个teacher表一个老师表OK然后呢它有两个字段后面呢横分隔幅呢是杠T又创建了一个学生表
[03:28] 有四个字段那么接下来呢我们把这两张表呢分别来创建一下我们来看我们把这个呢直接复制过来先创建一个T-shirt表好在这里回车已经创建成功再创建一个学生表拿过来这个表创建完之后呢我们是不是需要给这个外部表添加点数据啊那么怎么给外部表添加数据呢我们需要使用一个命令这个命令叫
[04:02] load data impasseOK这个load data impasse呢中间还有个local对吧这个local可以加也可以不加我们来先说一下如果加了这个local表示我在给这个表添加数据的时候呢我可以将本地的一个文件挺好是一个文件作为表的原数据比如说呢我这里一个文件叫stu.csv这个csv这种格式呢
[04:30] 你就认为呢它就像一个Excel表格我们从数据库导出数导出文件的时候呢我们就可以导成CSV我们也可以把CSV文件呢导到Excel中它就类似一个表格我们可以把这个表格文件呢加载给这个表OK那我们接下来就做了做了一个事情那么要做这个事情呢我们得先有这个CSV文件在我的这个在我的桌面里边呢有一个叫测试数据我们可以看
[05:00] 这里边就有一个stu.csv还有一个teacher.csv这样我们先把这两个文件上传到我们的服务器上好 稍等我在这里在这里的话呢我可以在Service下面我们来新建一个目录这个目录叫haveData4来 我们来统一下然后呢把我们的这个文件呢统一上传到这个目录来找到这里一个测试数据teacher和这个
[05:31] 好上传完之后呢接下来我们就可以调用刚才这个命令load datalocal impasse表示我要将本地的这个目录下面的这个文件我要加载到我们的这张表里边去好我来直接复制这个命令我们呢可以在在这个这个命令行里边注意一定要在这个Hive命令行来直接运行
[05:58] 我已经有了这个目录对吧而且里边已经有这个文件我的表也已经有了走回车好他这个地方呢他报了一个错误他说什么呢我们来看一下他说呢这个地方他这个地方应该是写错了没有这个文件他说这个文件不存在我看我写目录是不是写错了have data store我们来看来看看这里
[06:28] 我把它放错位置了我应该放到haveData4里面去那这样我move一下move student.csv然后呢放到haveData4这个目录再move一下这个teacher.csv好teacher好把它放进去好这样的话呢我们的haveData4里面已经有了这两个文件那我们再来好再来运行OK好这样子就没问题没问题之后我要告诉大家我们这张表已经有数据了
[07:01] 这个表的数据呢就是这个文件的数据那这个文件长什么样子呢我们来打开一下这个文件来看一下好teacher.csv我们来点开你看这里边呢是不是就类似一个表格那好了你表的一个数据也就是这些数据也就相当于呢我们现在有了一个文件我们现在有文件那么我们做了这么一个操作之后呢就相当于把这个文件呢
[07:28] 放在对应的这个表的目录下面然后呢在这个文件和这个表之间呢有一个映射关系那比如说我在查询的时候呢你看我来查询select星from student这个表已经有数据了走你会发现是不是已经查出来了那这个文件放在哪里去呢我们可以找一下它应该是放在我们的稍等我们的这个student这个目录你看是不是有文件这个文件就已经和这个表
[07:58] 产生了一个映射关系好那这个呢你可以认为就是原数据信息那么还有一个特点的话呢比如说我现在把这个student这个表删除了drop table student我来删除我们说过对于外部表来讲当你删原数据的时候呢当你删表的时候只是把原数据删掉而我们表真实的内容呢并没有删我们来看一下好我删完了删完之后再刷新你会发现这个文件还在这里
[08:27] 这个目录也并没有变那你说我在查的时候还能查到吗我们来查一下你会发现已经查不到了他说这个表已经不存在了实际上他的目录结构并没有消失当我呢再去做一件事情当我再把这个表创建一下你看我再把这个丢掉的表创建一下走我再来查你会发现又能查到了所以说这个表呢其实只是一个外壳真实的数据并没有丢
[08:55] 好这是一个特点这是外部表的特点那么大家在创建这个表的时候呢一定要注意这个地方呢我们的行分格符是钢T是因为呢你这个CS文件你的分格符也是钢T它一定要对应起来OK这是一种加载方式那我们接下来继续除了呢有这么一个加载方式之外呢还有另外一个就是后面加个overwrite这个overwrite和上面的区别是什么呢上面呢加载完之后呢
[09:25] 我们的表呢它的数据就是这里边的数据而下面这个呢overwrite表示我覆盖我会将这个文件的数据呢将以前原数据进行覆盖啊这是做个覆盖操作就是加overwrite所以说你运行这个OK运行这个之后呢有时候呢可以将原数据做一个覆盖操作OK这是这个那么除了这种加载方式之外呢我们还有另外一种加载方式我们刚才呢说呢这个地方可以加local也可以不加
[09:54] 如果你加了local表示从我的一个本地也就是我们Linux一个主机的本地去加载如果你把这个local去掉那么表示呢是从HDFS上去加载那我们来看一下那怎么做呢我们这里呢有一个步骤这个步骤的意思说呢你呢先在HDFS上建一个目录叫haveData4然后呢把teacher的scsv这个文件呢上传到HDFS上
[10:23] 然后再利用loadDataImpass注意前面没有加local那么我们可以把这个文件把这个文件的数据呢加在了这张表那我们来做一下直接把这个复制一下来我们来看我们注意这个执行的时候要在外边好先去建一个目录haveData4稍等好这个警告呢不用管它好接下来我们再看下一个我们呢把这个teacher的CSV呢加在了这个
[10:54] 这个上传到这里面去Teacher的CSV应该正好是在我当前目录走一下好上传上传到我们HDFS这个目录我们来检查一下在根目录下边有个haveData4好haveData4有个Teacher的CSV好有了这个之后呢FBG我们需要给我们的Teacher这张表也就是我们刚才showTables这边有一张表Teacher我们要给它加载数据
[11:25] 怎么加载呢我们来看下面这个命令叫load data in path这么一个命令这个注意没有加local表示我从hdfs上把这个文件加载给这张表来走加载完之后我们再来查询一下我们再来查询一下我们的teacher你会发现它已经有数据了这个也是另外一种加载方式同时呢大家会发现一个神奇的现象
[11:58] 当我把这个做完之后呢你再看Hive data4下面它已经没有这个文件了没有这个teacher csv了它跑哪里去呢它已经跑到我表目录下面就是在userhive warehouse在这里呢有一个myhive数据库有个teacher已经跑这里来了所以说呢它做的是剪切啊它做的是剪切也就是说这种方式它做的是剪切如果说呢我从本地加local
[12:27] 这种方式加载注意它其实将本地的一个文件复制到我们表的目录下面它是不一样的OK那么这个就是外部表的一个创建规则OK关于外表的创建呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建外部表并从本地文件系统和HDFS文件系统加载数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Hive执行完一个MapReduce任务后的日志，接着执行了创建表stu4和删除表student的命令。
画面2：在Hadoop Web UI中浏览HDFS目录，路径为/user/Hive/warehouse/myhive.db/stu3，显示一个名为000000_0的文件。
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
Hive> create table stu4 like stu2;
Hive> drop table student;
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
Hive> drop table stu3;
Hive> create external table teacher (t_id string,t_name string) row format delimited fields terminated by '\t';
Hive> create external table student (s_id string,s_name string,s_birth string ,s_sex string) row format delimited fields terminated by '\t';
Hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
Hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
```
画面8：
```
Hive> load data local inpath '/export/servers/hivedatas/student.csv' into table student;
Hive> select * from student;
```
画面9：
```
Hive> select * from student;
Hive> create external table student (s_id string,s_name string,s_birth string ,s_sex string) row format delimited fields terminated by '\t';
Hive> select * from student;
```
画面11：
```
[root@node03 servers]# mkdir hivedatas
[root@node03 servers]# rz -E
Transferring student.csv...
Transferring techer.csv...
[root@node03 servers]# ls
apache-Hive-3.1.1-bin  JDK 8.0_141  techer.csv
Hive sql  student.csv  ZooKeeper-3.4.9
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

