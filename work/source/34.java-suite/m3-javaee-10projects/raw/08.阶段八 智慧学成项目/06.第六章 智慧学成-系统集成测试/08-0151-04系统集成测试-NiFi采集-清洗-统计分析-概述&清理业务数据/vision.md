# 画面线理解：04系统集成测试-NiFi采集-清洗-统计分析-概述&清理业务数据

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\04系统集成测试-NiFi采集-清洗-统计分析-概述&清理业务数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:49, 01:52, 02:06, 02:14, 02:51, 02:58, 03:09, 03:15, 03:23, 03:28, 03:35, 03:40, 03:44, 03:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:10:51

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
