# 画面线理解：18-课程分析-课程购买量-集成测试-概述&NiFi调度数据清洗分析任务

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\18-课程分析-课程购买量-集成测试-概述&NiFi调度数据清洗分析任务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:39, 03:10, 04:01, 04:45, 05:32, 07:24, 09:02, 09:46, 10:07, 10:39, 11:39, 12:29, 13:07, 14:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:09:34

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Nifi 进行数据采集、清洗、转换，并通过 Spark 进行数据处理，最终将结果写入 MySQL 数据库的全流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 文档中关于“2.7.2.4 NIFI离线分析调度代码”的章节。
- 文档内容提到：使用 Nifi 广播 UDP 数据流，通过 Nifi 采集数据，到达一站式数据采集 → 数据解析 → 落地到业务库，最终形成 Nifi 离线主要部分。

画面 2：
- 展示了 Nifi 界面，其中包含三个处理节点：数据生产-离线采集-ToMySQL、数据清洗-离线采集-Mysql-ToHive、数据清洗-离线采集-Hive-ToMySQL。
- 文档内容提到：Nifi 代码较长，放在资料中，直接导入即可，路径如下：
  _ 课设资料
    _ 第3章-课程分析
      _ nifi
        _ 课程分析变量
        _ 数据清洗统计程序.exe

画面 3：
- 展示了 Nifi 界面，其中包含三个处理节点：数据生产-离线采集-ToMySQL、数据清洗-离线采集-Mysql-ToHive、数据清洗-离线采集-Hive-ToMySQL。
- 三个节点的 In/Out/Read/Write 均为 0。

画面 4：
- 展示了 WinSCP 软件界面，左侧为本地文件夹，右侧为远程服务器的 /opt/tmp 目录。
- 当前选中的是 /opt/tmp 目录。

画面 5：
- 展示了 IDEA 开发工具界面，项目结构为 xc-analysis。
- application.properties 配置文件内容：
  usingCluster=true
- Maven 项目结构中包含：xc-common-antity、xc-common-utils、xc-service-offline、src、main、resources、core-servlet、core-spring、hdfs-site.xml、hive-site.xml、xc-stream。
- Terminal 中显示了构建日志，包含多个警告信息，如：
  [WARNING] cn.itcast:xc-common-utils:1.8-SHAPSHOT requires scala version: 2.11.8
  [INFO] Includes = ["**/*.java","**/*.scala"]
  [INFO] Excludes = []

画面 6：
- 展示了 IDEA 开发工具界面，项目结构为 xc-analysis。
- application.properties 配置文件内容：
  usingCluster=true
- Maven 项目结构中包含：xc-analysis、src、main、resources、core-servlet、core-spring、hdfs-site.xml、hive-site.xml、xc-stream。
- Terminal 中显示了构建日志，包含多个警告信息，如：
  [WARNING] cn.itcast:xc-common-utils:1.8-SHAPSHOT requires scala version: 2.11.8
  [INFO] Includes = ["**/*.java","**/*.scala"]
  [INFO] Excludes = []

画面 7：
- 展示了 Nifi 界面，其中包含两个处理节点：CourseBuySourceToFact 和 CourseBuyProcessToFact。
- CourseBuySourceToFact 的 In/Out/Read/Write 均为 0。
- CourseBuyProcessToFact 的 In/Out/Read/Write 均为 0。

画面 8：
- 展示了 Hue 文件浏览器界面，弹出确认对话框，询问是否永久删除文件夹 years-2018 和 years-2019。
- 对话框中包含“取消”和“删除”按钮。

画面 9：
- 展示了 Hue 文件浏览器界面，当前路径为 /user/hive。
- 文件列表包含：.、external、warehouse。

画面 10：
- 展示了 Spark Master 界面，显示集群状态为 ALIVE。
- Workers (1)：Worker Id 为 worker-2019112004214-172.18.0.11-41259，Address 为 172.18.0.11-41259，State 为 ALIVE，Cores 为 6（8 Used），Memory 为 14.6 GB (1024.0 MB Used)。
- Running Applications (1)：Application ID 为 app-20191120030501-0004，Name 为 CourseBuyHiveToFact，Cores 为 8，Memory per Executor 为 1024.0 MB，Submitted Time 为 2019/11/22 09:08:31，User 为 root，State 为 RUNNING，Duration 为 12 s。
- Completed Applications (4)：列出四个已完成的应用程序，包括 CourseVisitProcessByDay、VisitSourceToFact、VisitProcessToFact 等。

画面 11：
- 展示了 Hue 文件浏览器界面，当前路径为 /user。
- 文件列表包含：.、hive、hue。

画面 12：
- 展示了 Hue Table Browser 界面，正在加载数据。
- 左侧 Tables 列表包含：course_buy_biz、course_buy_dim、course_buy_fact、course_hot_month_biz、course_orders_source、course_study_fact、course_user_fact、course_visit_fact、learning_course_fact、user_add_fact、user_login_fact。

画面 13：
- 展示了 Nifi 界面，其中包含两个处理节点：SelectFromHive 和 EvaluateJsonPath。
- SelectFromHive 的 In 为 0.0 bytes，Out 为 1.226 MB，Read/Write 为 0 bytes / 0 bytes，TotalTime 为 1.000000.000。
- EvaluateJsonPath 的 In 为 0.0 bytes，Out 为 0.0 bytes，Read/Write 为 0 bytes / 0 bytes，TotalTime 为 1.000000.000。

画面 14：
- 展示了 Typora 文档界面，内容为“容器 /opt/run/jars 目录，把.sh脚本上传到 /opt/run/script 目录”。
- 文档中提到 Nifi 离线调度代码，包含三个处理节点：CourseBuySourceToFact、CourseBuyProcessToFact、CourseBuyProcessToFact。
- 文档中提到 Nifi 离线调度代码，包含三个处理节点：数据清洗-DWD、数据清洗-DWM、数据统计分析。
- 文档中提到 Nifi 离线调度代码，包含三个处理节点：数据清洗-DWD、数据清洗-DWM、数据统计分析。
