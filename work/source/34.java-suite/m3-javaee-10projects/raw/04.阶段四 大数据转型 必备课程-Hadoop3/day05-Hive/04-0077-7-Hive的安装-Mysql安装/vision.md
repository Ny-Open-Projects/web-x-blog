# 画面线理解：7-Hive的安装-Mysql安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\7-Hive的安装-Mysql安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:19, 01:25, 01:38, 02:17, 02:32, 02:46, 02:59, 03:22, 03:42, 04:10, 04:24, 04:37, 04:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:40:48

1) 这一组画面整体在讲什么（一句话）：
演示在 Linux 服务器上安装 Hive 3.1.1 及其依赖的 MySQL 数据库环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 文档中“2.5 Hive 的安装”章节，内容包括 Hive 下载地址、安装步骤（上传并解压安装包、安装 MySQL）。
- 文档中列出的命令：
  cd /export/software/
  tar zxvf apache-hive-3.1.1-bin.tar.gz -C /export/software/
- 文档中列出的 MySQL 安装命令：
  yum install mysql mysql-server mysql-devel
  /etc/init.d/mysql start

画面 2：
- 展示了 Hive 安装包解压后目录下的部分 JAR 文件列表，包括 flatabuffers、arrow-memory、netty-buffer、hadoop-bundle、hive-metastore、commons-collections、commons-pool、antlr-runtime、derby、datanucleus-core、datanucleus-rdbms 等。

画面 3：
- 展示了在服务器上切换目录至 /servers/，并进入 Hive 安装目录的命令：
  [root@node03 software]# cd ../servers/
  [root@node03 servers]# cd apache-hive-3.1.1-bin/

画面 4：
- 展示了 Typora 文档中“2.5 Hive 的安装”章节，内容包括 Hive 下载地址、安装步骤（上传并解压安装包、安装 MySQL）。
- 文档中列出的 MySQL 安装命令：
  yum install mysql mysql-server mysql-devel
  /etc/init.d/mysql start

画面 5：
- 展示了在服务器上执行 yum 安装 MySQL 及其依赖包的命令：
  [root@node03 apache-hive-3.1.1-bin]# yum install mysql mysql-server mysql-devel

画面 6：
- 展示了 yum 安装过程中的事务摘要：
  Transaction Summary
  Install  11 Package(s)
  Upgrade  4 Package(s)
  Total download size: 12 M
  Is this ok [y/N]: y

画面 7：
- 展示了 yum 安装完成后，系统提示“Complete!”，并显示已安装的 MySQL 相关包及更新的依赖包列表，包括 mysql、mysql-devel、mysql-server、keyutils-libs-devel、libcom_err、libsepol-devel、perl-DBD-MySQL、krb5-devel、libselinux-devel、openssl-devel、libss 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
cd /export/software/
tar zxvf apache-hive-3.1.1-bin.tar.gz -C /export/software/
yum install mysql mysql-server mysql-devel
/etc/init.d/mysql start

画面 2：
apache-hive-3.1.1-bin/lib/flatabuffers-1.2.0-3f79e055.jar
apache-hive-3.1.1-bin/lib/arrow-memory-0.8.0.jar
apache-hive-3.1.1-bin/lib/netty-buffer-4.1.17.Final.jar
apache-hive-3.1.1-bin/lib/netty-common-4.1.17.Final.jar
apache-hive-3.1.1-bin/lib/hppc-0.7.2.jar
apache-hive-3.1.1-bin/lib/opencv-2.3.jar
apache-hive-3.1.1-bin/lib/parquet-hadoop-bundle-1.10.0.jar
apache-hive-3.1.1-bin/lib/hive-metastore-3.1.1.jar
apache-hive-3.1.1-bin/lib/hive-standalone-metastore-3.1.1.jar
apache-hive-3.1.1-bin/lib/bonecp-0.8.0.RELEASE.jar
apache-hive-3.1.1-bin/lib/HikariCP-2.6.1.jar
apache-hive-3.1.1-bin/lib/commons-collections-3.2.2.jar
apache-hive-3.1.1-bin/lib/commons-collections-3.2.2.jar
apache-hive-3.1.1-bin/lib/commons-pool-1.5.4.jar
apache-hive-3.1.1-bin/lib/antlr-runtime-3.5.2.jar
apache-hive-3.1.1-bin/lib/derby-10.14.1.0.jar
apache-hive-3.1.1-bin/lib/datanucleus-api-jdo-4.2.4.jar
apache-hive-3.1.1-bin/lib/datanucleus-core-4.1.17.jar
apache-hive-3.1.1-bin/lib/datanucleus-rdbms-4.1.19.jar

画面 3：
[root@node03 software]# cd ../servers/
[root@node03 servers]# cd apache-hive-3.1.1-bin/

画面 4：
yum install mysql mysql-server mysql-devel
/etc/init.d/mysql start

画面 5：
[root@node03 apache-hive-3.1.1-bin]# yum install mysql mysql-server mysql-devel

画面 6：
Transaction Summary
Install  11 Package(s)
Upgrade  4 Package(s)
Total download size: 12 M
Is this ok [y/N]: y

画面 7：
Verifying : e2fsprogs-1.41.12-23.el6.x86_64
Verifying : libcom_err-1.41.12-23.el6.x86_64
Verifying : libsepol-1.41.12-23.el6.x86_64
Verifying : e2fsprogs-libs-1.41.12-23.el6.x86_64
Verifying : libcom_err-1.41.12-23.el6.x86_64
Verifying : libsepol-1.41.12-23.el6.x86_64
Verifying : e2fsprogs-libs-1.41.12-23.el6.x86_64
Installed:
mysql.x86_64 0:5.1.73-8.el6_8
mysql-devel.x86_64 0:5.1.73-8.el6_8
mysql-server.x86_64 0:5.1.73-8.el6_8
Dependency Installed:
keyutils-libs-devel.x86_64 0:1.4-5.el6
libcom_err.x86_64 0:1.41-12-24.el6
libsepol-devel.x86_64 0:2.0.41-4.el6
perl-DBD-MySQL.x86_64 0:4.013-3.el6
krb5-devel.x86_64 0:1.10.3-65.el6
libselinux-devel.x86_64 0:2.0.94-7.el6
openssl-devel.x86_64 0:1.0.1e-57.el6
libss.x86_64 0:1.41.12-24.el6
Dependency Updated:
e2fsprogs.x86_64 0:1.41.12-24.el6
e2fsprogs-libs.x86_64 0:1.41.12-24.el6
libcom_err.x86_64 0:1.41.12-24.el6
libss.x86_64 0:1.41.12-24.el6

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
