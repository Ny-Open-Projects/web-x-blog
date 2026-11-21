# 17-课程分析-课程购买量-使用NiFi将业务数据从数据仓库同步到MySQL

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\17-课程分析-课程购买量-使用NiFi将业务数据从数据仓库同步到MySQL_【海量资源尽在 666java.com】.mp4
- 时长 4分21秒（音频 262s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢,咱们已经通过统计分析,将最终的统计结果保存到了咱们的数据仓库中。
[00:08] 接下来呢,就是使用NiFi调度,将咱们数据仓库中的数据同步到MySQL,然后呢,为咱们业务报表系统提供那个基础数据。
[00:20] 这个呢,是咱们业务报表系统的一个表结构。
[00:24] 这个呢,在咱们前边已经导入,这个地方展现一下就是,
[00:30] 和咱们数据仓库的一个数据对比和咱们数据仓库对比的话这里就少了一个咱们来切到HUE来看一下这里呢少了一个就是少了的是分区数据就是年月日的一个分区这里呢DataInfo和Counter就是一样的少的是年月日的分区因为呢咱们报表系统展示的时候我展示什么值我就拿什么值就行了它需要的值呢
[01:01] 只有这两项咱们使用NiFi调度的时候也是指在数据仓库中获取这两项值咱们来到咱们MySQL来看一下这里是咱们MySQL已经导入好的一个数据结构这目前是没有数据的NiFi调度咱们的流程和之前课程访问量的流程是一样的这里咱们就直接导入代码进行一个测试咱们来切到NiFi
[01:32] 这里呢咱们是离线分析课程购买量的数据在这里呢上传模板选择咱们选择咱们hi5to mycircle的这个调度源码然后上传上传成功之后呢还是用添加模板的方式将刚上传的数据刚上传的调度呢给添加进来这里呢就是咱们NiFi使用NiFi将数据仓库中的数据
[02:05] 同步到MySQL的调度这里有两个感叹号是咱们需要配置的右键进行一个配置这里Hive的链接直接启用即可MySQL的配置咱们这里是需要将它的密码给配置上的一定不要忘记配置了密码是123456配置完成之后点击启用即可好启用完成之后Close这时候咱们就可以进行一个集成测试了不是集成测试
[02:39] 进行一个同步测试了直接呢在空白处将点击此大将整个处理器组给启动起来这里呢可以看到put circle呢已经有数据了咱们来这里刷新一下走起这里呢可以看到已经有61条数据进入这个时候呢咱们业务的买色后咱们业务的买色后有了数据之后呢咱们就可以来到咱们的报表系统进行一个查看咱们报表系统呢
[03:09] 端口是4000咱们呢来访问咱们的报表系统由于咱们呢之前呢已经已经将咱们的系统都启动好了而且呢也是搭建好了咱们呢直接进行一个数据的查看就行了前边呢咱们是查看了客能防药量的这里呢咱们这还是客能防药量的接下来呢咱们是客能购买量的
[03:33] 这里呢按周课程购买量呢咱们按月进行一个展示然后呢按年进行一个展示到此呢咱们回到文档到此呢咱们课程购买量就是流程上就基本上已经完成了这里呢还少一个调度这里少的调度呢就是咱们使用NiFi来进行数据清洗的一个调度使用NiFi进行一个数据清洗统计分析的一个调度这个呢
[04:04] 交给后边进行一个讲解咱们本视频的内容呢就是使用NiFi调度呢将害物中的数据同步到MySQL就是将咱们数据仓库中的数据呢同步到MySQL好本节呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 将 Hive 中的业务数据同步到 MySQL 数据库，并展示相关的表结构和数据流程。

2) 按时间顺序列出每张画面的要点：
画面1: 在 Hue 的 Table Browser 中查看 Hive 表 course_buy_biz 的数据样本，包含 date_info、count、biz_years、biz_months、biz_days 等字段。
画面2: 展示 PPT 页面，标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。
画面3: 展示 PPT 页面，标题为“2.6.1 业务表结构”，展示创建表的 SQL 语句；标题为“2.6.2 NiFi调度流程”，展示数据流向和 NiFi 流程图。
画面4: 在 NiFi 界面中展示一个包含三个处理器的流程图，分别是 demo、维度、高层分析。
画面5: 在 NiFi 界面中，弹出“Upload Template”窗口，准备上传 XML 配置文件。
画面6: 在 NiFi 界面中，展示一个包含两个处理器的流程图，分别是“数据生产-课程购买量ToMySQL”和“数据消费-课程购买量MySQL-To-Hive”。
画面7: 在 NiFi 界面中，展示“3、落地业务库：课程购买量-Hive-To-Mysql Configuration”配置窗口。
画面8: 在 NiFi 界面中，展示“Configure Controller Service”窗口，配置 MySQL 数据库连接参数。
画面9: 在 NiFi 界面中，展示“SelectHiveQL”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面10: 在 NiFi 界面中，展示“ConvertAvroToJSON”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面11: 展示一个业务数据看板页面，包含今日访问量、新增用户量、今日购买量等指标。
画面12: 展示 PPT 页面，标题为“2.6.3 NiFi调度代码”，展示 NiFi 流程的 XML 代码路径。
画面13: 在 NiFi 界面中，展示“SelectHiveQL”、“SplitJson”和“PutSQL”三个处理器的连接关系。
画面14: 展示 PPT 页面，标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2: CREATE TABLE 'course_buy_biz' (
'date_info' date NOT NULL,
'count' int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
画面3: CREATE TABLE 'course_buy_biz' (
'date_info' date NOT NULL,
'count' int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
画面3: 数据流向为：Hive → MySQL，使用的NiFi处理流向为：SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。
画面8: Database Connection URL: jdbc:mysql://xc-online:8088/business...
Database Driver Class Name: com.mysql.cj.jdbc.Driver
Database Driver Location(s): /root/mysql-connector-java-8.0.16.jar
Database User: root
Password: (No value set)
Max Wait Time: 500 mills
Max Total Connections: 8
Minimum Idle Connections: 0
Max Idle Connections: 8
Max Connection Lifetime: -1
Time Between Eviction Runs: -1
Minimum Eviction Idle Time: 10 mins
画面12: nifi 流程的 XML 代码路径：/课程购买量-Hive-To-Mysql.xml

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2: 标题为“2.6 业务数据Hive到MySQL”，内容说明需要将 Hive 数据同步到 MySQL，并展示创建表的 SQL 语句。
画面3: 标题为“2.6.1 业务表结构”，展示创建表的 SQL 语句；标题为“2.6.2 NiFi调度流程”，展示数据流向和 NiFi 流程图。
画面12: 标题为“2.6.3 NiFi调度代码”，展示 NiFi 流程的 XML 代码路径。
画面3: 数据流向为：Hive → MySQL，使用的NiFi处理流向为：SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。
画面3: NiFi 流程图中，SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → PutSQL。

5) 无。

