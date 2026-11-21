# 04系统集成测试-NiFi采集-清洗-统计分析-概述&清理业务数据

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\04系统集成测试-NiFi采集-清洗-统计分析-概述&清理业务数据_【海量资源尽在 666java.com】.mp4
- 时长 4分26秒（音频 267s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,接下来呢,就使用NiFi对数据进行采集,清洗以及统计分析。
[00:08] 咱们这里呢,按步骤进行操作。
[00:11] 第一步呢,就是数据采集。
[00:14] 这里呢,咱们各个指标都需要进行数据的采集。
[00:18] 由于指标比较多呢,咱们也是逐个进行采集,生成一定量的数据呢,就停止计划。
[00:26] 数据采集完成之后呢,咱们进行清...
[00:30] 清洗统计分析的这个调度这个时候呢Spark程序呢是占用资源比较多的咱们首先对离线分析以及及时查询进行处理最后呢咱们来做实时分析的这个调度落地到业务库呢咱们是和清洗统计分析呢是联动的这个呢主要是针对离线分析来说这个是自动出发的咱们把清洗统计分析只要启动起来之后
[01:00] 和落地业务库一起起来,上面的清洗统计完成之后,落地业务库会自动出发。
[01:07] 这是咱们使用NiFi进行模拟生产环境,就是企业中的生产环境,调度咱们这里的一个测试流程。
[01:17] 但是在测试开始之前,咱们数据,就是最终业务报表系统要使用的数据,是有一些脏数据的,就是咱们之前测试遗留的一个数据。
[01:30] 这里需要将数据进行清理首先就是ES中的数据和HBase中的数据ES咱们使用ES header进行一个删除咱们先把数据给删除了然后再执行上面的采集和清晰统计分析的一个操作这里来切换到咱们的ES header这是咱们上面的一个锁点数据把它给删除掉好
[02:04] 删除成功之后呢,咱们接着呢是删除HBase的数据HBase呢是需要登录HBase的share,咱们呢这里使用终端来切换到咱们这个HBase的容器好,已经切换进来,咱们呢来切换到HBase的BML这里呢使用HBase share来切换到这个HBase的share中
[02:40] 这个时候你可以看到这里边现在有两张表咱们呢把咱们这个智慧学成的这个业务数据把它给清掉先禁用禁用完成之后呢再把它给照顾掉再删除好完成之后呢咱们可以再使用list进行查看这个时候呢你可以看到表只有一个了就说明咱们删除已经成功了这个删除呢是咱们针对
[03:13] 及时查询的一个数据的一个清理咱们离线分析呢这个地方用了大量的这个mycircle的表咱们呢这里统一的一个脚本是清理咱们页面报表系统mycircle中的这个数据的这里呢内部cat已经打开这里呢是有数据的咱们呢就用一张一个circle把它给全部给处理掉OK它显示已经执行完成咱们来刷一下这里边应该已经没有数据了
[03:43] 好,数据呢已经完成了咱们来切回温呢咱们呢已经对奈飞、采集、数据清洗还有统计分析前置工作已经做完接下来呢咱们就是根据步骤进行一个调度这个根据步骤调度呢咱们就给下一个视频本视频呢咱们主要是对采集、清洗还有统计分析进行了一个概述以及呢清理了咱们之前程序的一个
[04:15] 运行的数据然后呢保证咱们的这个数据库以及呢HBase和ES中这个数据是空的好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Nifi中配置数据采集流程，并通过清空HBase和MySQL表来验证数据处理结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Nifi流程界面，包含三个处理器：1. 数据采集（读取HDFS数据）、2. 数据清洗（处理数据）、3. 数据写入（写入MySQL）。处理器间通过“From: Out”和“To: Input”连接。
画面2：展示Elasticsearch的Kibana界面，显示索引“learning_online_detail”和“demo”的文档数量，状态为“yellow”。
画面3：展示Typora文档，标题为“6.2 NiFi采集-清洗-统计分析”，内容包含步骤说明和PS1、PS2说明，其中PS2包含清空HBase表的SQL语句。
画面4：展示Xshell终端，连接到Nifi服务器，显示当前目录为“/opt/cdh5.14.0s”，准备执行命令。
画面5：Xshell终端中执行了“cd /opt/cdh5.14.0s”和“/opt/cdh5.14.0s/bin/hbase shell”命令，进入HBase Shell。
画面6：在HBase Shell中执行“list”命令，列出表“LearningOnlineDetail”和“demo”。
画面7：在HBase Shell中执行“disable 'LearningOnlineDetail'”命令，禁用表。
画面8：在HBase Shell中执行“drop 'LearningOnlineDetail'”命令，删除表。
画面9：在HBase Shell中执行“list”命令，确认表已删除。
画面10：展示Navicat Premium界面，连接到MySQL数据库“xc-online-mysql”，显示“business”数据库中的表列表。
画面11：在Navicat Premium中，选中“subject_sale_week.biz”表，准备执行SQL语句。
画面12：在Navicat Premium中，选中“subject_sale_week.biz”表，准备执行SQL语句。
画面13：在Navicat Premium中，选中“subject_sale_week.biz”表，准备执行SQL语句。
画面14：展示Typora文档，标题为“6.2 NiFi采集-清洗-统计分析”，内容包含步骤说明和PS1、PS2说明，其中PS2包含清空HBase表的SQL语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3、8、9、14中的SQL语句：
PS2: NiFi调度执行前将业务报表系统的数据库清空，以便验证数据处理结果，清空脚本如下：
truncate table agency_amount_month.biz;
truncate table agency_amount_week.biz;
truncate table agency_sale_month.biz;
truncate table agency_sale_week.biz;
truncate table agency_user_month.biz;
truncate table agency_user_week.biz;
truncate table course_buy.biz;
truncate table course_hot_week.biz;
truncate table course_visit.biz;
truncate table platform_offline.biz;
truncate table subject_amount_month.biz;
truncate table subject_amount_week.biz;
truncate table subject_sale_month.biz;
truncate table subject_sale_week.biz;
truncate table subject_user_month.biz;
truncate table subject_user_week.biz;

画面5、6、7中的命令：
cd /opt/cdh5.14.0s
/opt/cdh5.14.0s/bin/hbase shell
list
disable "LearningOnlineDetail"
drop "LearningOnlineDetail"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3、14中的PPT标题：
6.2 NiFi采集-清洗-统计分析

画面3、14中的步骤说明：
1. 数据采集：使用NiFi生产数据的方式进行采集，根据指标这个进行，生成一定量的数据后停止即可。
2. 数据清洗统计调度：执行Spark程序时占用资源较多也是根据指标这个进行。
3. 落地业务库和数据驱动，自动触发。

画面3、14中的PS1说明：
PS1：清理即时查询数据，es中索引数据及hbase存储的完整数据

画面3、14中的PS2说明：
PS2：NiFi调度执行前将业务报表系统的数据库清空，以便验证数据处理结果，清空脚本如下：

画面1中的流程图结构：
1. 数据采集（读取HDFS数据） → 2. 数据清洗（处理数据） → 3. 数据写入（写入MySQL）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

