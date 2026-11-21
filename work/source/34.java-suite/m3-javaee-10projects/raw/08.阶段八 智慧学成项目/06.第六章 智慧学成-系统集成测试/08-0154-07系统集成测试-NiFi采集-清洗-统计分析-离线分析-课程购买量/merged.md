# 07系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程购买量

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\07系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程购买量_【海量资源尽在 666java.com】.mp4
- 时长 6分17秒（音频 377s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前面已经测试了离线分析中的课程缓量,按照这个步骤进行了一个测试,接下来测试离线分析中的课程购买量,咱们来切换来看,这是课程购买量的处理系组,咱们来切换到这个处理系组,课程购买量的数据采集是来自于MySQL,这里这是咱们采集MySQL的处理系组,可以把它先给起来,
[00:33] 采集买色后呢是需要有用户的行为数据产生的这里咱们正常生产环境正常的一个采集呢是用户有购买行为产生那个订单数据订单数据呢咱们通过这个处理系统呢把它给采集过来但是咱们现在这个学生在天这个系统呢咱们是没没办法进行演示这个整个流程的因为咱们只有一个静态页面
[01:02] 所以说呢咱们这个地方也是使用NiFi进行一个数据的一个生产咱们可以把这个处理器都给启开这里呢是之前咱们测试的时候遗留的一些数据其实呢咱们整个处理器这个地方只启它就行了因为这个处理器这个对列里面还有9000多条数据咱们把它给启动了就行启动完成之后呢这个地方它就在生产了可以看到这个地方就在生产数据了
[01:37] 我把它给停了这个地方呢还不能这样使用因为咱们之前的话这个测试那个日期不一定是什么呀这个日期不一定就是正确的咱们生产数据这个地方要生产的是啥要生产正确的这个日期的所以说呢把它给对列给清了对列清掉之后呢咱们重新进行来跑这个数据如果你在测试的时候也可能会遇到这样一个问题对列里边有数据我又不想跑整个流程
[02:07] 你确认生成那个对链这个数据呢是可以用的就可以只起最后一个处理器处理器就行了但是如果你不确定那个数据是可以用的就把对链里边这个数据全清了然后呢咱们把它给重新启动好这个时候呢可以看到数据已经在进行一个保存操作了已经2000多条了2000多条呢基本上够咱们用了因为咱们这个地方生产这个数据呢也是
[02:40] 1-60天的咱们购买量呢少一点就行这个时候呢咱们已经得到了这个当天那个购买量你说我显我觉得这个地方那个数据呢比较少我这个时候就可以只启动这一个处理器把对链里边这个数据呢给消耗了因为我确定这个数据呢是就是刚生成的是正确的这个时候就可以只启动一个可以看到现在已经多少啊将近4000条了好已经4000多条了就可以把它给停下来
[03:11] 这是咱们生产数据这个停下来之后呢咱们来看采集是否把所有的数据都给保存完了这个时候可以看到对列里边这个地方对列还有数据它还没处理到这个里边也就是说这个处理完成之后put害物这个地方保存成功就说明咱们这个地方采集这个刚才生产那个数据通过采集就完全获取到了这个呢因为保存的害物中它需要相关的计算
[03:46] 没有买Circle那么快这个地方呢也已经成功了咱们把它给停了停止完成之后呢接下来就是咱们统计分析的一个操作这个地方呢走起启动它接下来呢再启动咱们的落地的用户走这个时候呢可以看到试试表正在进行一个清洗咱们来刷新可以看到试试表正在执行好接下来呢已经到了中间表
[04:21] 稍息走,中间表正在进行,这个呢,等待它执行完成即可,好,已经呢,到了这个地方,已经到了咱们统计这个,到BIZ落地的业务库这个SPARK的一个统计分析,可以看到已经到BIZ,这个地方呢,等待它到它,等待它到下一个处理器组,咱们呢,在这个地方等就行了,也可以呢,把数据库给切过来,
[05:12] 这个和咱们这个防御量是一样的咱们只把咱们页入报表系统的页入表给清了咱们这个地方统计分析这个地方落地到这个数据仓库中这个清洗并没有把它给数据仓库中那个BIZ这个并没有把它给清理掉它没有清理掉的话也就是说咱们在这一步保存的时候它会把所有的数据都给拿过来所有的数据都给拿过来了
[05:43] 也是为了报表的一个展示就是最终报表展示的时候它这个效果相对来说比较好咱们来刷新因为这个地方可以看到它已经保存完成保存完成之后呢咱们就可以进行这个时候刷新就有数据了咱们来看1216有吗可以看到1216的购买量是52OK咱们切回问答到此呢咱们离线分析的课程购买量
[06:12] 按照咱们这个步骤操作就完成了视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 NiFi 中构建数据采集、清洗和统计分析流程，并通过 Spark 处理数据，最终写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 NiFi 界面，三个处理器的监控面板，分别显示“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的队列状态，其中“读取数据源”处理器的队列中有 32,983 字节数据。
画面 2: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“ExecuteScript”、“SplitJson”、“ConvertJSONToSON”、“ReplaceText”、“EvaluateJsonPath”、“PutSQL”等处理器，展示数据处理流程。
画面 3: 显示 NiFi 界面，弹出“Empty Queue”对话框，提示“10,000 FlowFiles (312.5 KB) were removed from the queue”。
画面 4: 显示 NiFi 界面，弹出“Empty Queue”确认对话框，提示“Are you sure you want to empty this queue? All FlowFiles waiting at the time of the request will be removed.”，并提供“CANCEL”和“EMPTY”按钮。
画面 5: 显示 NiFi 界面，弹出“Empty Queue”确认对话框，提示“Are you sure you want to empty this queue? All FlowFiles waiting at the time of the request will be removed.”，并提供“CANCEL”和“EMPTY”按钮。
画面 6: 显示 NiFi 界面，数据流图，包含“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的监控面板，显示“读取数据源”处理器的队列中有 0 字节数据。
画面 7: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 8: 显示 Spark Master 界面，显示 Spark 集群状态，包括“URL”、“REST URL”、“Alive Workers”、“Memory in use”、“Applications”、“Status”等信息，以及“Workers”和“Running Applications”、“Completed Applications”列表。
画面 9: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 10: 显示 NiFi 界面，数据流图，包含“GenerateFlowFile”、“CourseBuyProcessToWM”、“CourseBuyProcessByDay”、“WaitForNextGroupProcessor”等处理器，展示数据处理流程。
画面 11: 显示 Navicat Premium 界面，连接到“xc-online-mysql”数据库，显示“business”数据库下的表结构，包括“agency_amount_month_biz”、“agency_amount_week_biz”、“agency_sale_month_biz”、“agency_sale_week_biz”、“agency_user_month_biz”、“agency_user_week_biz”、“course_buy_biz”、“course_hot_month_biz”、“course_hot_week_biz”、“course_sale_biz”、“course_user_month_biz”、“course_user_week_biz”、“subject_amount_month_biz”、“subject_amount_week_biz”、“subject_sale_month_biz”、“subject_sale_week_biz”、“subject_user_month_biz”、“subject_user_week_biz”等表。
画面 12: 显示 NiFi 界面，数据流图，包含“读取数据源”、“读取数据源”和“写入 MySQL”三个处理器的监控面板，显示“读取数据源”处理器的队列中有 0 字节数据。
画面 13: 显示 NiFi 界面，处理器详细信息面板，显示“Hive Database Connection Pooling Service”、“HiveQL Pre-Query”、“HiveQL Select Query”、“Fetch Size”、“Max Rows Per Flow File”、“Maximum Number of Fragments”、“Output Format”、“Normalize Table/Column Names”、“CSV Header”、“Alternate CSV Header”、“CSV Delimiter”、“CSV Quote”、“PRM Format”等属性及其值。
画面 14: 显示 Typora 文档，标题为“6.2 NiFi采集-清洗-统计分析”，内容包括“1. 数据采集：使用NiFi生成数据的方式进行采集，根据指标进行，生成一定的数据后停止即可”、“2. 数据清洗统计分析：执行Spark程序占用资源较多也是根据指标这个进行”、“3. 清洗业务数据和步骤驱动，自动触发”、“PS1：清理即时查询的数据，es中索引表及Hbase存储的完整数据”、“PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：”以及清空表的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 14 中的 SQL 语句：
```
# es中的索引使用es-head管理页面删除，web 址：http://xc-online:9100/
disable "LearningOnlineDetail"
drop "LearningOnlineDetail"

PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：
truncate table agency_amount_month_biz;
truncate table agency_amount_week_biz;
truncate table agency_sale_month_biz;
truncate table agency_user_month_biz;
truncate table agency_user_week_biz;
truncate table course_buy_biz;
truncate table course_hot_month_biz;
truncate table course_hot_week_biz;
truncate table course_sale_biz;
truncate table course_user_month_biz;
truncate table course_user_week_biz;
truncate table subject_amount_month_biz;
truncate table subject_amount_week_biz;
truncate table subject_sale_month_biz;
truncate table subject_sale_week_biz;
truncate table subject_user_month_biz;
truncate table subject_user_week_biz;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14 中的 PPT 标题为“6.2 NiFi采集-清洗-统计分析”，内容包括：
- 1. 数据采集：使用NiFi生成数据的方式进行采集，根据指标进行，生成一定的数据后停止即可
- 2. 数据清洗统计分析：执行Spark程序占用资源较多也是根据指标这个进行
- 3. 清洗业务数据和步骤驱动，自动触发
- PS1：清理即时查询的数据，es中索引表及Hbase存储的完整数据
- PS2：NiFi调度执行前业务表系统的数据库表清空，以便验证数据处理结果，清空脚本如下：
  - truncate table agency_amount_month_biz;
  - truncate table agency_amount_week_biz;
  - truncate table agency_sale_month_biz;
  - truncate table agency_user_month_biz;
  - truncate table agency_user_week_biz;
  - truncate table course_buy_biz;
  - truncate table course_hot_month_biz;
  - truncate table course_hot_week_biz;
  - truncate table course_sale_biz;
  - truncate table course_user_month_biz;
  - truncate table course_user_week_biz;
  - truncate table subject_amount_month_biz;
  - truncate table subject_amount_week_biz;
  - truncate table subject_sale_month_biz;
  - truncate table subject_sale_week_biz;
  - truncate table subject_user_month_biz;
  - truncate table subject_user_week_biz;

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

