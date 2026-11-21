# 22-网站流量日志分析-hive表数据导入

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\22-网站流量日志分析-hive表数据导入【海量资源尽在 ubkz.com】.mp4
- 时长 11分43秒（音频 704s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 经过了三个myproduce的一个处理我们得到了一些预处理的数据并且得到了我们想要的一些表模型那接下来呢我们就把这些已经分析好的表模型数据导入到Hive仓库以便于呢我们进行下一步的处理那怎么去导入呢来回到我的这个资料里面在资料里面呢这里有个文件夹这里边呢是我们这个流量分析中一些脚本和一些配置代码我们来看这里边
[00:29] 一共有这么多步咱们先看第一步我们要使用HiveHive里面呢又分为很多步我们先进行最简单的这个我们来建表然后呢再把数据呢导入到这个表里面去我们先看第一个ODS层表的一个创建打开好打开之后呢我们需要呢建三张表第一张呢是我们的原始数据表第二张呢是我们的PageView表
[00:59] 第三张呢是我们的visit表分别对应我们的三个表模型来我们先看这个原始表这个原始表呢其实就是我们做一个数据清洗之后呢对应的一个表表模型在哪里去创建呢我们需要来到我们的Hive里面去来我们来连一下在这里我们进入了xpod servicehivehive我们来看一下xpod serviceapache Hive
[01:31] 好进来之后呢我们先去进到Hive这个命令行走一下稍等进来之后呢我们依次创建了三张表因为只有创建表之后呢我们才能导入数据好这个地方是drop table也就是如果这个表已经存在了我们可以把它删掉这个表是不存在的我直接复制创建表这个地方创建表叫ods weblog origin那这个地方呢它的表的字段呢
[02:01] 其实和我们预处理之后它的字段是对应起来的来我们来粘贴一下好回车稍等好我们就创建了第一个原始数据表接下来再创建第二个创建一个pageview表来我们来创建一个走回车再创建第三个visit表好在这里粘贴走那么这时候我们来看一下我们来说一下这个地方我做错了一件事情
[02:38] 我这地方并没有选择我们对应的数据库DAT BISES这样子这个表呢应该是创建的默认的default下面去了这样子我呢选择一个数据库这样我们再创建一个数据库create database然后呢后边写个weblog我们再创建一个数据库use weblog那么这样子我们只能把刚才这个表呢再重新创建一下分别来创建一下
[03:10] 第一个接下来快速的做一下第二个好再来第三个创建完了创建完之后我们来输入一下table4这里边有三张表这三张表依次对应什么呢我们回到我们的这个数据里边依次就对应在这里data里边有三个output第一个output呢是第一个myproduce一个输出这个呢其实就对应我们的原始表而第二个呢output呢
[03:50] 其实就对应我们的一个配置view表而第三个呢这个里边呢就是对应我们的visit表好那么这三张表创建成功了创建成功之后呢接下来我们需要给这三张表的导入数据怎么导入呢我们来看在这里呢在这个资料里面呢有一个项目脚本加配置代码进来我们接下来进入这里的第二步数据的导入数据导入怎么导入数据呢
[04:18] 我们需要在HDFS上创建一些目录然后创建完这些目录之后我们把这些我们刚才生成的一些文件放在对应的目录就可以了好了 我来做一下这个事情首先我们需要在HDFS上创建对应的目录我们来做一下稍等把这个再打开一下我们来创建对应的目录在这里我们再打开个页面稍等
[04:54] 回程然后呢这个地方我们直接来运行吧好在这里边创建一个weblogpreparepaste走这是创建第一个好接下来我们再把剩余的也创建一下第二个好第二个创建一个pageview然后接下来第三个拿过来第三个然后呢第四个都创建一下嗯粘了两次创建一下好创建完了好创建完了之后呢接下来我们来看
[05:48] 我们还需要将我们生成的三个文件分别上传到对应的目录下面上传到对应的目录下面之后我们再去把这个数据加在表里面或者是这样这种方式你也可以不用或者还有种方式你可以把我们的三个文件放到Export Service在这个下面建个WeblogDataS这个目录然后把我的文件分别放在这里OK那这样我们就用这种这种方式非常简单我们可以在Export Service下面
[06:17] 分别创建一个目录这个目录叫weblogdata4那我来做这个是这个简单一点我们make make there好在这里创建这么一个目录进到export Service下面一个webdata4我们需要将呢三个输出的文件上传到这个目录来我们来找一下那么刚才呢我们在这个里边有一个资料资料里边有一个data我要把这三个输出文件
[06:47] 分别放在桌面上这个地方呢我们给它重命名一下这个地方重命名为什么名字呢我们来看一下它这个原始数据叫weblog orange那我们给它重命名一下这个名字就叫weblog orangeOK这是这个文件那接下来呢咱们再看第二个这个output2呢这里边这个文件我们也给它粘一下好这个名字命名为什么呢
[07:16] 回到这个位置来看第二个呢叫配置v那我们也改成配置v好 重名配置v再看第三个第三个呢重名名为visit我们也是把它拷出来走一下把它第三个这个地方拷到我们的桌面上那这地方呢是visit好 visit这个就没有问题了我们打开看一下吧看会不会好 这个没错好 这个没错之后呢我们需要把这三个文件
[07:50] 分别上传到我们的export 34webdata4这个来我们来看我们只需要呢把它们都上传到这个目录在桌面上找一下这三个文件这个这个还有这个添加好走稍等上传成功上传成功接下来呢我们来看这个地方再找到我刚才这个地方在资料里边配置文件找到这个好我们来导入数据
[08:23] 怎么导入呢我们来运行这三条命令第一条load data localimpass这个表示把这个文件的数据呢导入到我们的这张表里边而且这里边有个分区分区呢这个数字呢是一个日期OK导入导入完之后呢我们来看一下我们把这句话呢把这行呢复制一下好复制完之后我们来运行运行的话呢在Hive中运行在Hive中运行走
[08:55] 这句话啊稍等让他去加载已经加载成功加载成功之后呢那么我们这个表中已经有数据了我们来show table 3一下应该是这个orange这个表我们来查这个表里边有没有数据清号fromods-weblog-originok这个数位查数据的时候不要直接这样子回车应该加个limit因为这个数据量特别大
[09:26] 如果你不加limit的话呢它会造成呢这个屏幕呢一直在刷因为数据量太大了我来显示前十条走稍等一下它报一个错我这个名字是不是写错了weblogoriginods它说呢表不存在weblog表明写错了orange写错了稍等origin走
[09:56] 我们来查前10条看能不能查出来发现这个10条数据已经查出来了因为这个数据量比较大所以说呢它这个显示的格式可能不太好看好那么咱们导完第一个之后咱们接下来把剩余两张表的数据也导过来按照这个步骤那接下来我们导入这个也比较简单我们的数据呢也是在Export Service这个是PageView表粘贴走它也在导入好那么我们来看这个PageView
[10:27] 来查一下这个表这个表呢叫什么名字呢show table 4是这个配置viewselect from粘一下然后limit 10走好这个也查出来了好查出来之后呢咱们再导第三个好这个地方呢是visit应该是一个我们来看一下这个是一个visit表看有没有导错OK没有这是visit表我们也把它导进来
[11:00] 好在这里执行稍等好我们来查一些visit表这个地方show tables我们来查这个ods select from然后呢这个地方是ods visit一定要加limit是好数据也倒过来到此为止呢我们把这三张三个表模型的数据呢已经成功的导入了我们还有表里边好那么到这个位置的话呢相当于
[11:31] 看我们的图相当于我们这个Hive就做完了做完之后呢我们还需要对这个Hive中的数据呢进行一些分析OK关于导入Hive表呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建日志分析相关的数据表，并将本地数据加载到Hive表中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT中“网站日志分析系统”的架构图，包含Nginx、HDFS、MapReduce、Hive、Sqoop和MySQL等组件。
画面2：在Notepad++中展示创建Hive表的SQL语句，用于创建ods_weblog_origin表。
画面3：在SecureCRT中执行Hive命令，创建ods_weblog_origin表。
画面4：在SecureCRT中执行Hive命令，创建ods_click_stream_visit表。
画面5：在SecureCRT中执行Hive命令，创建ods_click_pageviews表。
画面6：在Windows资源管理器中，右键点击“part-r-00000”文件，准备进行操作。
画面7：在Notepad++中展示HDFS命令和Hive本地模式配置，用于准备数据导入。
画面8：在Notepad++中展示HDFS命令和Hive本地模式配置，用于准备数据导入。
画面9：展示Windows桌面，包含“黑马程序员”和“博学谷”的标志。
画面10：在Windows桌面，右键点击“part-r-00000”文件，准备进行操作。
画面11：在Windows资源管理器中，展示“1-HiveSQL”文件夹下的多个SQL文件。
画面12：在SecureCRT中执行Hive命令，加载本地数据到ods_weblog_origin表，并尝试查询。
画面13：在SecureCRT中执行Hive命令，加载本地数据到ods_click_pageviews表，并查询。
画面14：展示PPT中“网站日志分析系统”的架构图，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
drop table if exists ods_weblog_origin;
create table ods_weblog_origin(
valid string,
remote_addr string,
remote_user string,
time_local string,
request string,
status string,
body_bytes_sent string,
http_referer string,
http_user_agent string,
partitioned by (datestr string)
row format delimited
fields terminated by '\001';

画面3：
Hive> create table ods_weblog_origin(
> valid string,
> remote_addr string,
> remote_user string,
> time_local string,
> request string,
> status string,
> body_bytes_sent string,
> http_referer string,
> http_user_agent string,
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面4：
Hive> create table ods_click_stream_visit(
> session string,
> remote_addr string,
> inTime string,
> outTime string,
> inPage string,
> outPage string,
> referral string,
> pageVisits int)
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面5：
Hive> create table ods_click_pageviews(
> session string,
> remote_addr string,
> time_local string,
> request string,
> visit_step string,
> page_staylong string,
> http_referer string,
> http_user_agent string,
> body_bytes_sent string,
> status string,
> partitioned by (datestr string)
> row format delimited
> fields terminated by '\001';

画面7：
hdfs dfs -mkdir -p /weblog/preprocessed
hdfs dfs -mkdir -p /weblog/clickstream/pageviews
hdfs dfs -mkdir -p /weblog/clickstream/visits
hdfs dfs -mkdir -p /weblog/dim_time
hdfs dfs -put part-m-00000 /weblog/preprocessed
hdfs dfs -put part-r-00000 /weblog/clickstream/pageviews
hdfs dfs -put part-r-00000 /weblog/clickstream/visits
hdfs dfs -put dim_time.dat.txt /weblog/dim_time
设置Hive本地模式运行
set Hive.exec.mode.local.auto=true;

画面12：
Hive> load data local inpath '/export/servers/weblogdatas/weblog_origin' overwrite into table ods_weblog_origin partition(datestr='20130918');
Hive> show tables;
OK
ods_click_pageviews
ods_click_stream_visit
ods_weblog_origin
Time taken: 0.386 seconds, Fetched: 3 row(s)
Hive> select * from ods_weblog_roigin limit 10;
FAILED: SemanticException [Error 10001]: Line 1:14 Table not found 'ods_weblog_roigin'
Hive> select * from ods_weblog_origin limit 10;

画面13：
Hive> load data local inpath '/export/servers/weblogdatas/pageView' overwrite into table ods_click_pageviews partition(datestr='20130918');
OK
Time taken: 2.104 seconds
Hive> show tables;
OK
ods_click_pageviews
ods_click_stream_visit
ods_weblog_origin
Time taken: 0.386 seconds, Fetched: 3 row(s)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面14：
标题：大数据平台 网站日志分析系统
架构图结构：
- 三个Nginx实例（分别标注为“Nginx”、“Nginx”、“Nginx”）指向HDFS。
- HDFS指向MapReduce。
- MapReduce指向Hive。
- Hive指向Sqoop。
- Sqoop指向MySQL。
- MySQL指向Web展现。
- 一个“任务调度”组件指向MapReduce。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

