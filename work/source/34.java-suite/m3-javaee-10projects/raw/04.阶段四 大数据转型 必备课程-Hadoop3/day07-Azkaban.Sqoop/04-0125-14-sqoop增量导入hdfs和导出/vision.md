# 画面线理解：14-sqoop增量导入hdfs和导出

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\14-sqoop增量导入hdfs和导出【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 03:02, 03:18, 03:39, 04:40, 05:20, 05:45, 06:15, 06:50, 07:55, 08:09, 08:43, 09:30, 09:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:00:25

1) 这一组画面整体在讲什么（一句话）：
讲解 Sqoop 的增量导入与数据导出功能，包括使用选项和 where 条件控制增量导入，以及将 HDFS 数据导出到 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 讲解 Sqoop 增量导入的概念，需要添加 'incremental', 'check-column', 和 'last-value' 选项。展示第一种增量导入命令：`bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --incremental append --check-column id --last-value 1202 -m 1 --target-dir /sqoop/increment`。
画面 2: 展示第一种增量导入命令的完整内容，强调不能加 --delete-target-dir 参数，否则会报错。
画面 3: 在 Hadoop Web UI 的 Browse Directory 页面，显示 HDFS 上 /sqoop/ 目录下存在 emp 和 emp2 两个文件。
画面 4: 在 EditPlus 编辑器中显示 HDFS 文件 part-m-00000 的内容，包含多行员工数据记录。
画面 5: 在 MySQL Workbench 中，展示 emp 表的结构和数据，其中 id 为 1204 的记录被选中。
画面 6: 展示第二种增量导入方法，使用 where 条件：`bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --where "create_time > '2018-06-17 00:00:00' and create_time < '2018-06-17 23:59:59'" --target-dir /sqoop/increment2 -m 1`。
画面 7: 在 SecureCRT 中执行 Sqoop 导入命令，显示多个警告信息，提示 HBase、HCatalog、Accumulo 和 Zookeeper 环境变量未设置。
画面 8: 在 Hadoop Web UI 中，点击文件 part-m-00000 查看文件信息，显示 Block ID、Block Pool ID、Generation Stamp、Size 和 Availability 等信息。
画面 9: 展示第二种增量导入方法的命令，同时页面标题切换到“6、Sqoop的数据导出”，开始介绍导出功能。
画面 10: 在 Hadoop Web UI 中，点击文件 part-m-00000 的右键菜单，选择“查看文件”选项。
画面 11: 展示将 HDFS 数据导出到 MySQL 的步骤，第一步是创建目标表 emp_out，SQL 语句为：`CREATE TABLE emp_out ( id INT(11) DEFAULT NULL,`。
画面 12: 在 MySQL Workbench 中执行 TRUNCATE emp_out 命令，成功清空表数据。
画面 13: 展示 Sqoop 导出命令的开始部分，弹出“导出”对话框，提示用户选择导出目标。
画面 14: 展示完整的 Sqoop 导出命令：`bin/sqoop export --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --export-dir /sqoop/increment2`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
bin/sqoop import \
--connect jdbc:mysql://192.168.1.7:3306/userdb \
--username root \
--password root \
--table emp \
--incremental append \
--check-column id \
last_value 1202 \
-m 1 \
--target-dir /sqoop/increment
```
画面 2:
```bash
bin/sqoop import \
--connect jdbc:mysql://192.168.1.7:3306/userdb \
--username root \
--password root \
--table emp \
--incremental append \
--check-column id \
last_value 1202 \
-m 1 \
--target-dir /sqoop/increment
```
画面 6:
```bash
bin/sqoop import \
--connect jdbc:mysql://192.168.1.7:3306/userdb \
--username root \
--password root \
--table emp \
--where "create_time > '2018-06-17 00:00:00' and create_time < '2018-06-17 23:59:59'" \
--target-dir /sqoop/increment2 \
-m 1
```
画面 11:
```sql
CREATE TABLE emp_out (
id INT(11) DEFAULT NULL,
```
画面 14:
```bash
bin/sqoop export \
--connect jdbc:mysql://192.168.1.7:3306/userdb \
--username root \
--password root \
--table emp \
--export-dir /sqoop/increment2
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“增量导入”，内容包括增量导入的概念、所需选项和命令示例。
画面 6: PPT 标题为“第二种增量导入通过--where条件来实现”，内容包括使用 where 条件的命令示例。
画面 9: PPT 标题为“6、Sqoop的数据导出”，内容包括导出功能的介绍。
画面 11: PPT 标题为“hdfs导出到mysql”，内容包括导出步骤和 SQL 语句。
画面 14: PPT 标题为“第二步：执行导出命令”，内容包括导出命令的示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
