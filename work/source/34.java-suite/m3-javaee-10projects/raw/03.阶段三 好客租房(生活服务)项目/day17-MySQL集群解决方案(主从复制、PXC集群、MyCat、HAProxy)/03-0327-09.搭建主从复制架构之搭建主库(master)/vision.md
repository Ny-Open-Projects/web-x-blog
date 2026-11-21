# 画面线理解：09.搭建主从复制架构之搭建主库（master）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\09.搭建主从复制架构之搭建主库（master）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:46, 01:18, 01:41, 03:01, 03:21, 03:34, 03:50, 05:20, 05:33, 06:05, 06:31, 07:08, 07:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:33:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中通过 Docker 部署并配置一个 MySQL 主库（master），包括创建目录、配置文件、启动容器及验证配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 连接到远程服务器，终端提示符为 root@itcast02:~#，左侧显示 /data 目录结构。
画面 2: 在终端中执行 mkdir /data/mysql/master01 创建目录失败，然后执行 cd /data/mysql/master01 进入目录。
画面 3: 显示 Typora 文档中关于“搭建主库”的步骤，包含创建目录、配置文件、输入内容、启动容器等指令。
画面 4: 在终端中输入并执行了 MySQL 配置文件内容，包括 log-bin 和 server-id。
画面 5: 在 /data/mysql/master01 目录下创建 conf 子目录，执行 chmod 777 * -R 命令，然后进入 conf 目录并创建 my.cnf 文件。
画面 6: 在 conf 目录下编辑 my.cnf 文件，然后执行 docker create 命令创建 MySQL 容器。
画面 7: 执行 docker start 命令启动容器，并在终端中查看 MySQL 初始化日志，确认服务已启动。
画面 8: 切换到 Windows 桌面，显示 Navicat Premium 软件的启动界面。
画面 9: 在 Navicat Premium 中连接到 MySQL 服务器（192.168.1.18:3306），并查看 mysql 数据库结构。
画面 10: 显示 Typora 文档中关于“创建同步用户以及授权”的内容，包括 create user、grant replication slave 和 flush privileges 语句。
画面 11: 在 Typora 文档中，显示了因 SQL 模式设置导致的错误提示，以及需要修改 my.cnf 文件的建议。
画面 12: 在终端中执行 docker logs 命令查看容器日志，确认 MySQL 服务已成功启动并监听 3306 端口。
画面 13: 在 Typora 文档中，显示了“master 状态”部分，包含 show master status 和 show global variables like 'binlog%' 等 SQL 语句。
画面 14: 在 Typora 文档中，显示了执行 show global variables like 'binlog%' 后的变量列表，包括 binlog_format、binlog_group_commit_sync 等参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```text
#创建目录
1 mkdir /data/mysql/master01
2 cd /data/mysql/master01
3 mkdir conf data
4 chmod 777 * -R
#创建配置文件
5 cd /data/mysql/master01/conf
6 vim my.cnf
#输入以下内容
7 [mysqld]
8 log-bin=mysql-bin #开启二进制日志
9 server-id=1 #服务id，不可重复
#创建容器
10 docker create --name percona-master01 -v /data/mysql/master01/data:/var/lib/mysql -v /data/mysql/master01/conf:/etc/my.cnf.d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
11 docker start percona-master01 && docker logs -f percona-master01
```

画面 5:
```text
root@itcast02:master01# mkdir conf data
root@itcast02:master01# ll
total 16
drwxr-x 4 root root 4096 Feb 3 23:47 ./
drwxr-x 3 root root 4096 Feb 3 23:47 ../
drwxr-x 2 root root 4096 Feb 3 23:47 conf/
drwxr-x 2 root root 4096 Feb 3 23:47 data/
root@itcast02:master01# chmod 777 * -R
root@itcast02:master01# cd conf/
root@itcast02:conf# ll
total 8
drwxr-x 4 root root 4096 Feb 3 23:47 ./
drwxr-x 3 root root 4096 Feb 3 23:47 ../
root@itcast02:conf# vim my.cnf
```

画面 6:
```text
root@itcast02:conf# docker create --name percona-master01 -v /data/mysql/master01/data:/var/lib/mysql -v /data/mysql/master01/conf:/etc/my.cnf.d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
4b04206b547c37f02d109d068f38c00372175fd2110594a1ce38366034b1f
root@itcast02:conf# docker start percona-master01 && docker logs -f percona-master01
percona-master01
```

画面 10:
```text
#创建同步用户以及授权
23 create user 'itcast'@'%' identified by 'itcast';
24 grant replication slave on *.* to 'itcast'@'%';
25 flush privileges;
#出现 [Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and implicit sorting behavior is disabled. 解决方案，在 my.cnf 配置文件中设置
sql_mode = STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```

画面 13:
```text
#查看 master 状态
29 show master status;
30 show global variables like 'binlog%';
31 show global variables like 'server%';
```

画面 14:
```text
show global variables like 'binlog%';
Variable name	Value
binlog_cache_size	12780
binlog_checksum	CRC32
binlog_direct_non_trans_write	OFF
binlog_format	MIXED
binlog_group_commit_sync	0
binlog_group_commit_sync	0
binlog_max_flush_queue	0
binlog_max_flush_queue	0
binlog_row_image	FULL
binlog_rows_query_log	OFF
binlog_stmt_cache_size	12780
binlog_transaction_depth	2000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“3.5. 搭建主库”，左侧目录结构显示了课程大纲，包括“系统架构和数据库的部署方案”、“主从复制”、“从库配置”等章节。
画面 10: PPT 标题为“3.5. 搭建主库”，左侧目录结构显示了课程大纲，包括“系统架构和数据库的部署方案”、“主从复制”、“从库配置”等章节。
画面 13: PPT 标题为“master 状态”，包含“File”、“Position”、“Binlog_Do_DB”、“Binlog_Ignore_DB”、“Executed_Gtid_Set”等列。
画面 14: PPT 标题为“show global variables like 'binlog%'”，包含“Variable name”和“Value”两列，列出多个 binlog 相关变量及其值。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
