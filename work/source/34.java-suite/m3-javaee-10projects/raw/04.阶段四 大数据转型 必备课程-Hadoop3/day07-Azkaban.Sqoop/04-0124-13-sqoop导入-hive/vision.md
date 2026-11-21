# 画面线理解：13-sqoop导入-hive

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\13-sqoop导入-hive【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:40, 01:03, 01:35, 01:50, 02:40, 03:19, 04:06, 04:38, 04:52, 05:04, 05:53, 06:05, 06:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:36:23

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Sqoop 将 MySQL 数据库中的表数据导入到 Hive 中，并展示创建 Hive 表和查询数据的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“导入关系表到HIVE”，内容包括“第一步：拷贝jar包”和“第二步：准备hive数据库与表”，并列出相关命令。
画面2：显示终端窗口，列出 HBase 相关的 JAR 包文件名。
画面3：终端中执行命令将 hive-exec-3.1.1.jar 复制到 Sqoop 的 lib 目录下。
画面4：终端中进入 apache-hive-3.1.1-bin 目录并列出其内容。
画面5：PPT 页面，高亮显示“第二步：准备hive数据库与表”中的创建数据库命令。
画面6：PPT 页面，高亮显示创建外部表的 SQL 语句。
画面7：PPT 页面，展示“第三步：开始导入”和“第四步：hive表数据查看”的命令和查询语句。
画面8：终端中执行 Sqoop 导入命令，显示警告信息（缺少 HBase、HCatalog、Accumulo、ZooKeeper 环境变量）。
画面9：终端中执行 Hive 命令，创建数据库、使用数据库、创建外部表、查看表和查询数据。
画面10：终端中执行 Hive 查询语句，显示查询结果（5 行数据）。
画面11：PPT 页面，展示“第三步：开始导入”的命令。
画面12：终端中执行 Sqoop 导入命令，显示日志信息（HiveImport 初始化、加载数据、导入完成）。
画面13：终端中执行 Hive 查询语句，显示查询结果（5 行数据）。
画面14：PPT 页面，展示“第四步：hive表数据查看”的查询语句和“导入关系表到hive并自动创建hive表”的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cp /export/servers/apache-hive-3.1.1-bin/lib/hive-exec-3.1.1.jar
/export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/lib

画面3：
cp hive-exec-3.1.1.jar /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/lib/

画面4：
bin binary-package-licenses conf hostlog jdbc lib LICENSE NOTICE RELEASE NOTES.txt scripts

画面5：
hive (default)> create database sqoopothive;
hive (default)> use sqoopothive;
hive (sqoopothive)> create external table emp.hive(id int,name string,deg string,salary int ,dept string) row format delimited fields terminated by '\001';

画面7：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --fields-terminated-by '\001' --hive-import --hive-table sqoopothive.emp_hive --hive-overwrite --delete-target-dir -m 1

画面11：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --fields-terminated-by '\001' --hive-import --hive-table sqoopothive.emp_hive --hive-overwrite --delete-target-dir -m 1

画面14：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --hive-import --hive-database sqoopothive

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备hive数据库与表
第三步：开始导入
第四步：hive表数据查看

画面5：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备hive数据库与表
第三步：开始导入
第四步：hive表数据查看

画面7：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备hive数据库与表
第三步：开始导入
第四步：hive表数据查看

画面11：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备hive数据库与表
第三步：开始导入
第四步：hive表数据查看

画面14：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备hive数据库与表
第三步：开始导入
第四步：hive表数据查看
第五步：导入关系表到hive并自动创建hive表

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
