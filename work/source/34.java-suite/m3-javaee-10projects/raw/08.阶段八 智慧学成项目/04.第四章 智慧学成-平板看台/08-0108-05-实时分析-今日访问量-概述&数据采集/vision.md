# 画面线理解：05-实时分析-今日访问量-概述&数据采集

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\05-实时分析-今日访问量-概述&数据采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:19, 02:09, 02:15, 02:31, 03:07, 03:13, 03:15, 03:20, 03:25, 03:29, 03:34, 04:02, 04:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:38:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在学成在线平台设置学习兴趣，并通过终端操作Kafka集群来消费“访问量”主题数据，用于后续的实时分析。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“4 部署”章节，列出软件环境要求：Jdk: 1.8, nginx: 1.6, hadoop: 2.6.5, kafka: 2.2.0, - kafka-connect (配置参考: Kafka-Connector使用文档), zookeeper: 3.4.5。
画面2：展示“4.4.1 负载均衡启动”部分，说明buried.jar服务的启动方式：java -jar buried.jar，并列出三个服务的IP和端口：172.16.0.161:12100, 172.16.0.162:12100, 172.16.0.163:12100。
画面3：展示学成在线平台“设置学习兴趣”页面，用户可选择前端、Java、大数据、安卓、iOS、PHP等方向的技能标签。
画面4：展示学成在线平台首页，包含“来~用语言撩遍全宇宙”的宣传语和课程分类导航。
画面5：展示终端窗口，执行命令进入Kafka容器：docker exec -it xc-online-kafka bash，并列出Kafka目录下的脚本文件。
画面6：终端窗口中执行命令进入Kafka目录并列出脚本文件，准备消费数据。
画面7：学成在线平台页面，显示“我的课程表”弹窗，列出“继续学习 程序语言设计”等课程。
画面8：学成在线平台页面，显示“我的课程表”弹窗，列出“继续学习 程序语言设计”等课程。
画面9：终端窗口中列出Kafka脚本文件，准备消费数据。
画面10：学成在线平台页面，显示“PHP基础视频”课程的“环境搭建”、“函数”、“文件”、“正则”等模块。
画面11：学成在线平台“设置学习兴趣”页面，用户可选择前端、Java、大数据、安卓、iOS、PHP等方向的技能标签。
画面12：学成在线平台“设置学习兴趣”页面，用户可选择前端、Java、大数据、安卓、iOS、PHP等方向的技能标签。
画面13：展示课程文档“2 今日访问量”章节，列出“2.1 数据采集”和“2.2 统计分析”部分，其中“2.1 数据采集”参考“第二章 ETL 采集博访问量数据”，并给出查看Kafka中指定topic数据的命令：# 模拟消费查看topic数据.sh /Kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic visit_topic。
画面14：终端窗口中执行命令消费Kafka主题数据，输出结果包含IP地址、浏览器信息等，如：102.168.0.5, 102.168.0.5, 102.168.0.5。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
Jdk: 1.8
nginx: 1.6
hadoop: 2.6.5
kafka: 2.2.0
- kafka-connect (配置参考: Kafka-Connector使用文档)
zookeeper: 3.4.5

画面2：
java -jar buried.jar
# 采集服务buried
172.16.0.161:12100
172.16.0.162:12100
172.16.0.163:12100

画面5：
docker exec -it xc-online-kafka bash
/root
[root@xc-online-kafka opt]# ls
[root@xc-online-kafka opt]# cd kafka
kafka_2.11-2.2.0/bin
[root@xc-online-kafka bin]# ls

画面6：
[root@xc-online-kafka bin]# ls
connect-distributed.sh
kafka-console-consumer.sh
kafka-console-producer.sh
kafka-consumer-groups.sh
kafka-delegation-tokens.sh
kafka-delete-records.sh
kafka-dump-log.sh
kafka-log-darsh.sh
kafka-mirror-maker.sh
kafka-preferred-replica-election.sh
kafka-producer-perf-test.sh
kafka-reassign-partitions.sh
kafka-replica-verification.sh
kafka-run-class.sh
kafka-server-start.sh
kafka-server-stop.sh
kafka-streams-application-reset.sh
kafka-toools.sh
kafka-verifiable-producer.sh
kafka-verify.sh
kafka-zookeeper.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell.sh
kafka-zookeeper-security-migration.sh
kafka-zookeeper-server-start.sh
kafka-zookeeper-server-stop.sh
kafka-zookeeper-shell
