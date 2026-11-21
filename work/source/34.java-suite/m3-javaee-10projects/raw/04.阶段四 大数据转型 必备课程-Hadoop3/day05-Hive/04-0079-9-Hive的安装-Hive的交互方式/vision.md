# 画面线理解：9-Hive的安装-Hive的交互方式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\9-Hive的安装-Hive的交互方式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:06, 01:41, 03:02, 03:42, 04:25, 04:41, 05:08, 05:25, 05:39, 06:17, 06:41, 06:57, 07:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:53:41

1) 这一组画面整体在讲什么（一句话）：
演示如何通过命令行和 SQL 脚本两种方式在 Hive 中创建数据库和表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Notepad++ 编辑器中的 Hive 交互方式文档，包含两种交互方式：
  第一种交互方式：bin/hive
  第二种交互方式：使用 sql 语句或者 sql 脚本进行交互
- 文档中提供了创建数据库的命令：
  create database if not exists myhive;
- 文档中提供了通过 SQL 脚本创建数据库的命令：
  cd /export/servers/apache-hive-3.1.1-bin
  bin/hive -e "create database if not exists mytest;"

画面2：
- 展示了 Notepad++ 编辑器中的 Hive 交互方式文档，内容与画面1相同。
- 文档中提供了通过 SQL 脚本创建数据库并创建表的命令：
  cd /export/servers/apache-hive-3.1.1-bin
  vim hive.sql
  create database if not exists mytest;
  use mytest;
  create table stu (id int, name string);

画面3：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了以下命令：
  hive> show databases;
  hive> create database if not exists myhive;
  hive> show databases;
  hive> use myhive;

画面4：
- 展示了 SQLyog Ultimate 的“连接 MySQL 主机”对话框。
- 对话框中显示了连接信息：
  MySQL 主机地址：192.168.174.120
- 对话框提示：“You have changed your connection details. Click OK to save changes.”

画面5：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了以下命令：
  hive> create table t_test(id int, name string);
  hive> show tables;
  hive> exit;

画面6：
- 展示了 SecureCRT 中的终端界面。
- 执行了命令：
  bin/hive -e "create database if not exists myhive;"
- 输出了 SLF4J 日志绑定信息。

画面7：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了命令：
  hive> show databases;
- 输出了数据库列表：
  default
  myhive
- 当前 Hive 会话 ID：ab13d01a-b9ba-4bf4-abe9-ff4bea22b0d

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cd /export/servers/apache-hive-3.1.1-bin
bin/hive
create database if not exists myhive;
cd /export/servers/apache-hive-3.1.1-bin
bin/hive -e "create database if not exists mytest;"

画面2：
cd /export/servers/apache-hive-3.1.1-bin
vim hive.sql
create database if not exists mytest;
use mytest;
create table stu (id int, name string);

画面3：
hive> show databases;
hive> create database if not exists myhive;
hive> show databases;
hive> use myhive;

画面5：
hive> create table t_test(id int, name string);
hive> show tables;
hive> exit;

画面6：
bin/hive -e "create database if not exists myhive;"

画面7：
hive> show databases;
default
myhive

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
