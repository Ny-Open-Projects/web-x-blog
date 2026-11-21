# 画面线理解：29-热门学科排名-集成测试-配置NiFi调度数据清洗分析任务

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\29-热门学科排名-集成测试-配置NiFi调度数据清洗分析任务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:10, 01:36, 01:58, 02:10, 02:25, 02:43, 04:11, 04:54, 05:12, 05:26, 05:41, 06:09, 06:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:33:29

1) 这一组画面整体在讲如何配置和部署 Nifi 流程以实现数据采集、清洗和分析，并通过脚本和配置文件控制数据流向。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了文档中关于“3.7.2.2 调度脚本”的说明，其中提到“热门学科排名脚本共7个，脚本在资料中的路径如下”，并附有目录结构图，图中显示了“nifi”目录下“script”子目录包含的7个脚本文件。
画面2: 展示了“script”目录下的7个脚本文件列表，文件名包括：subject_learn_num_by_month.biz.sh, subject_sales_by_month.biz.sh, subject_sales_volume_by_month.biz.sh, subject_learn_num_by_week.biz.sh, subject_sales_by_week.biz.sh, subject_sales_volume_by_week.biz.sh, user_learn_source_to_fact.sh。
画面3: 展示了IDE中“application.properties”文件，其中配置了“useingCluster=true”，并说明“true-集群模式，false-local模式，不配置默认为false”。
画面4: 展示了Nifi界面，包含三个数据流组件：“0.数据生产:用户表选ToMySQL”、“1.数据采集:用户表选Mysql To Hive实时采集”、“3.落地业务表:热门学科排名Hive To Mysql”，并显示了各组件的队列和读写状态。
画面5: 展示了Nifi界面，组件“0.数据生产:用户表选ToMySQL”和“1.数据采集:用户表选Mysql To Hive实时采集”被选中，组件“3.落地业务表:热门学科排名Hive To Mysql”未被选中。
画面6: 展示了Nifi界面，显示了多个数据流组件及其连接关系，包括“subject_learn_num_by_month.biz.sh”、“subject_sales_by_month.biz.sh”等脚本对应的组件。
画面7: 展示了WinSCP界面，显示了本地和远程服务器的文件夹结构。
画面8: 展示了终端界面，执行了“cd /opt/tmps”、“ls”、“cd /opt”、“cd /opt/nifi”、“bash”等命令，以及“hadoop hive mysql connector java 8.0.16.jar nifi 1.0.2 run sdk spark tmp venv”等命令。
画面9: 展示了IDE中“application.properties”文件，其中配置了“useingCluster=true”，并说明“true-集群模式，false-local模式，不配置默认为false”。
画面10: 展示了IDE中“application.properties”文件，其中配置了“useingCluster=true”，并说明“true-集群模式，false-local模式，不配置默认为false”。
画面11: 展示了IDE中“application.properties”文件，其中配置了“useingCluster=true”，并说明“true-集群模式，false-local模式，不配置默认为false”。
画面12: 展示了终端界面，显示了Ubuntu系统信息，包括系统负载、磁盘使用率、内存使用率、进程数、用户登录信息、IP地址等。
画面13: 展示了终端界面，执行了“cd /opt/tmps”、“ls”、“cd /opt”、“cd /opt/nifi”、“bash”等命令，以及“hadoop hive mysql connector java 8.0.16.jar nifi 1.0.2 run sdk spark tmp venv”等命令。
画面14: 展示了文档中关于“3.7.2.2 调度脚本”的说明，其中提到“热门学科排名脚本共7个，脚本在资料中的路径如下”，并附有目录结构图，图中显示了“nifi”目录下“script”子目录包含的7个脚本文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1: 无代码或配置。
画面2: 无代码或配置。
画面3: useingCluster=true
画面4: 无代码或配置。
画面5: 无代码或配置。
画面6: 无代码或配置。
画面7: 无代码或配置。
画面8: cd /opt/tmps
ls
cd /opt
cd /opt/nifi
bash
hadoop hive mysql connector java 8.0.16.jar nifi 1.0.2 run sdk spark tmp venv
画面9: useingCluster=true
画面10: useingCluster=true
画面11: useingCluster=true
画面12: 无代码或配置。
画面13: cd /opt/tmps
ls
cd /opt
cd /opt/nifi
bash
hadoop hive mysql connector java 8.0.16.jar nifi 1.0.2 run sdk spark tmp venv
画面14: 无代码或配置。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 标题为“3.7.2.2 调度脚本”，内容为“热门学科排名脚本共7个，脚本在资料中的路径如下”，并附有目录结构图，图中显示了“nifi”目录下“script”子目录包含的7个脚本文件。
画面4: 无PPT标题，但有Nifi界面，包含三个数据流组件：“0.数据生产:用户表选ToMySQL”、“1.数据采集:用户表选Mysql To Hive实时采集”、“3.落地业务表:热门学科排名Hive To Mysql”，并显示了各组件的队列和读写状态。
画面5: 无PPT标题，但有Nifi界面，组件“0.数据生产:用户表选ToMySQL”和“1.数据采集:用户表选Mysql To Hive实时采集”被选中，组件“3.落地业务表:热门学科排名Hive To Mysql”未被选中。
画面6: 无PPT标题，但有Nifi界面，显示了多个数据流组件及其连接关系，包括“subject_learn_num_by_month.biz.sh”、“subject_sales_by_month.biz.sh”等脚本对应的组件。
画面14: 标题为“3.7.2.2 调度脚本”，内容为“热门学科排名脚本共7个，脚本在资料中的路径如下”，并附有目录结构图，图中显示了“nifi”目录下“script”子目录包含的7个脚本文件。

5) 无。
