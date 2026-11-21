# 画面线理解：5-Azkaban-two_server模式-安装1

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\5-Azkaban-two_server模式-安装1【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:47, 01:22, 01:48, 02:22, 03:03, 03:48, 04:34, 05:21, 06:06, 07:08, 07:55, 08:57, 09:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:17:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下为 Azkaban 3.5.1.0 版本准备数据库、解压软件包并生成相关配置文件，为后续服务安装做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 当前页面是课程 PPT，标题为“2.3 Azkaban 两个服务模式安装与使用”。
- 当前章节为“Step 1: 数据库准备”。
- 展示了 Azkaban 数据库安装目录下的 SQL 文件列表，其中 `create-all-sql-0.1.0-SNAPSHOT.sql` 文件被高亮选中。
- 提示文字：“Step 1: 数据库准备 进入mysql的客户端执行以下命令”。

画面 2：
- PPT 内容继续展示“Step 1: 数据库准备”和“Step 2: 解压软件包”。
- “Step 1”部分列出在 mysql 客户端执行的 SQL 命令：
  CREATE DATABASE azkaban;
  CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  flush privileges;
  use azkaban;
  source /export/software/create-all-sql-0.1.0-SNAPSHOT.sql;
- “Step 2”部分列出“解压软件安装包”，并具体到“解压 azkaban-web-server”。

画面 3：
- PPT 内容与画面 2 相同，仅鼠标光标位置不同。

画面 4：
- 展示了在 SecureCRT 中执行 SQL 命令的终端界面。
- 命令执行结果：
  mysql> CREATE DATABASE azkaban;
  Query OK, 1 row affected (0.00 sec)
  mysql> CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  Query OK, 0 rows affected (0.02 sec)
  mysql> GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  Query OK, 0 rows affected (0.01 sec)
  mysql> flush privileges;
  Query OK, 0 rows affected (0.00 sec)
  mysql> use azkaban;
  Database changed
  mysql>

画面 5：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-3.5.1.0。
- 执行了命令：cd azkaban-exec-server/。
- 列出了 azkaban-exec-server 目录下的文件和子目录，包括 build.gradle、src、az-core、az-examples 等。

画面 6：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-db。
- 执行了命令：cp create-all-sql-0.1.0-SNAPSHOT.sql /export/software/。
- 列出了 azkaban-db 目录下的 SQL 文件列表。

画面 7：
- 展示了在 SecureCRT 中的终端界面。
- 显示了 SQL 命令执行后的结果，均为“Query OK, 0 rows affected (0.00 sec)”或“Query OK, 0 rows affected (0.01 sec)”。

画面 8：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-db。
- 执行了命令：cd ..。
- 列出了 azkaban-db 目录下的 SQL 文件列表。

画面 9：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-exec-server。
- 执行了命令：cd distributions/。
- 执行了命令：cp azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz /export/software/。
- 列出了 distributions 目录下的文件。

画面 10：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-web-server。
- 执行了命令：cd distributions/。
- 执行了命令：cp azkaban-web-server-0.1.0-SNAPSHOT.tar.gz /export/software/。
- 列出了 /export/software/ 目录下的文件，包括 azkaban-web-server-0.1.0-SNAPSHOT.tar.gz。

画面 11：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/software。
- 执行了命令：mv azkaban-web-server-0.1.0-SNAPSHOT/ azkaban-web-server-3.5.1.0。
- 列出了 /servers/ 目录下的文件，包括 apache-flume-1.8.0-bin、azkaban-3.5.1.0、azkaban-exec-server-3.5.1.0 等。

画面 12：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /servers。
- 执行了命令：cd /export/servers/azkaban-web-server-3.5.1.0。
- 列出了 /export/servers/azkaban-web-server-3.5.1.0 目录下的文件。

画面 13：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/servers/azkaban-web-server-3.5.1.0。
- 执行了命令：keytool -keystore keystore -alias jetty -genkey -keyalg RSA。
- 系统提示输入密码和组织信息。

画面 14：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/servers/azkaban-web-server-3.5.1.0。
- 系统提示确认组织信息，用户输入“yes”。
- 系统提示输入密钥库密码，用户输入“RETURN”。
- 系统提示“Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?”，用户输入“yes”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
- 无代码或配置。

画面 2：
- SQL 命令：
  CREATE DATABASE azkaban;
  CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  flush privileges;
  use azkaban;
  source /export/software/create-all-sql-0.1.0-SNAPSHOT.sql;

画面 4：
- SQL 命令：
  mysql> CREATE DATABASE azkaban;
  Query OK, 1 row affected (0.00 sec)
  mysql> CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  Query OK, 0 rows affected (0.02 sec)
  mysql> GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  Query OK, 0 rows affected (0.01 sec)
  mysql> flush privileges;
  Query OK, 0 rows affected (0.00 sec)
  mysql> use azkaban;
  Database changed
  mysql>

画面 5：
- 命令：
  [root@node03 azkaban-3.5.1.0]# cd azkaban-exec-server/
  [root@node03 azkaban-exec-server]# ls
  build.gradle  src
  az-core/
  az-examples/
  az-exec-util/
  az-flow-trigger-dependency-plugin/
  az-flow-trigger-dependency-type/
  az-hadoop-jobtype-plugin/
  az-hdfs-viewer/
  az-intellis-style.xml
  az-jobsummary/
  azkaban-common/
  azkaban-db/
  azkaban-exec-server/
  azkaban-hadoop-security-plugin/
  azkaban-solo-server/
  azkaban-web-server/
  az-reportal/

画面 6：
- 命令：
  [root@node03 azkaban-db]# cp create-all-sql-0.1.0-SNAPSHOT.sql /export/software/
  [root@node03 azkaban-db]#

画面 7：
- 无代码或配置。

画面 8：
- 命令：
  [root@node03 azkaban-db]# cd ..
  [root@node03 azkaban-db]#

画面 9：
- 命令：
  [root@node03 azkaban-exec-server]# cd distributions/
  [root@node03 distributions]# cp azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz /export/software/
  [root@node03 distributions]#

画面 10：
- 命令：
  [root@node03 az
