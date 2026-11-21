# 画面线理解：11.搭建主从复制架构之主从复制的3种模式

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\11.搭建主从复制架构之主从复制的3种模式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:11, 00:38, 02:46, 05:55, 06:05, 06:32, 06:52, 07:26, 07:40, 07:49, 08:06, 08:37, 09:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:35:35

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 部署 MySQL 主从复制环境，并配置 binlog 格式为 ROW。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：在 Typora 编辑器中查看“3.7. 主从复制模式”章节，其中显示了 `show global variables like 'binlog%'` 的查询结果，`binlog_format` 的值为 `ROW`。
- 画面序号：1

画面 2：
- 内容：在 Typora 编辑器中显示了用于创建从库容器的 Docker 命令，包括 `docker create` 和 `docker start` 命令，以及设置从库连接主库的 SQL 语句 `CHANGE MASTER TO`。
- 画面序号：2

画面 3：
- 内容：在 Typora 编辑器中显示了用于创建主库用户和权限的 SQL 语句，以及检查主库状态的命令 `show master status`。
- 画面序号：3

画面 4：
- 内容：在 Navicat Premium 中连接到主库（192.168.1.18:3306），执行 `show global variables like 'binlog%'` 查询，结果显示 `binlog_format` 为 `ROW`。
- 画面序号：4

画面 5：
- 内容：在 Xshell 终端中显示了 MySQL 服务启动的日志，包括版本号、端口、插件状态等信息。
- 画面序号：5

画面 6：
- 内容：在 Xshell 终端中，用户切换到 `slave01` 目录，并列出目录内容，显示了 `conf` 和 `data` 文件夹。
- 画面序号：6

画面 7：
- 内容：在 Xshell 终端中，用户进入 `conf` 目录，编辑 `my.cnf` 文件，并执行 `docker restart percona-master01` 命令。
- 画面序号：7

画面 8：
- 内容：在 Typora 编辑器中显示了修改主库配置的命令，以及 `show global variables like 'binlog%'` 的查询结果，`binlog_format` 的值为 `MIXED`。
- 画面序号：8

画面 9：
- 内容：在 Typora 编辑器中显示了用于创建主库容器的 Docker 命令，包括 `docker create` 和 `docker start` 命令。
- 画面序号：9

画面 10：
- 内容：在 Navicat Premium 中连接到从库（192.168.1.18:3307），但未执行任何操作。
- 画面序号：10

画面 11：
- 内容：在 Navicat Premium 中连接到从库（192.168.1.18:3307），但未执行任何操作。
- 画面序号：11

画面 12：
- 内容：在 Navicat Premium 中连接到从库（192.168.1.18:3307），执行 `show global variables like 'binlog%'` 和 `show master status` 命令，结果显示 `Binlog_Do_DB` 为 `my_test`，`File` 为 `mysql-bin.000005`。
- 画面序号：12

画面 13：
- 内容：在 Navicat Premium 中连接到从库（192.168.1.18:3307），执行 `SELECT * FROM tb_user LIMIT 1,1000` 查询，结果显示了 `id` 和 `name` 字段。
- 画面序号：13

画面 14：
- 内容：在 Typora 编辑器中显示了“3.7. 主从复制模式”章节，其中显示了 `show global variables like 'binlog%'` 的查询结果，`binlog_format` 的值为 `ROW`，并附有文字说明 MySQL 提供的三种 binlog 格式：STATEMENT、ROW、MIXED。
- 画面序号：14

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```sql
show global variables like 'binlog%';
```

画面 2：
```sql
#输入如下内容
[mysqld]
server-id=3
sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'

#创建容器
docker create --name percona-slave01 -v /data/mysql/slave01/data:/var/lib/mysql -v /data/mysql/slave01/conf:/etc/mysql.cnf -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
docker start percona-slave01 && docker logs -f percona-slave01

#设置master相关信息
CHANGE MASTER TO
master_host='192.168.1.18',
master_user='itcast',
master_password='itcast',
master_port=3306,
master_log_file='mysql-bin.000002',
master_log_pos=648;

#启动同步
start slave;

#查看master状态
show slave status;
```

画面 3：
```sql
#创建同步用户以及授权
create user 'itcast'@'%' identified by 'itcast';
grant replication slave on *.* to 'itcast'@'%';
flush privileges;

#查看master状态
show master status;

#查看二进制日志相关的配置项
show global variables like 'binlog%';

#查看server相关的配置项
show global variables like 'server%';
```

画面 4：
```sql
show global variables like 'binlog%';
```

画面 5：
```text
2019-02-03T15:57:53.127763Z [Note] InnoDB: 96 redo rollback segment(s) found. 96 redo rollback segment(s) are active.
2019-02-03T15:57:53.129413Z [Note] InnoDB: 32 non-redo rollback segment(s) are active.
2019-02-03T15:57:53.131335Z [Note] InnoDB: Waiting for purge to start
2019-02-03T15:57:53.131857Z [Note] InnoDB: log sequence number 11904342
2019-02-03T15:57:53.135834Z [Note] InnoDB: Plugin 'FEDERATED' is disabled.
2019-02-03T15:57:53.185742Z [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2019-02-03T15:57:53.186042Z [Note] InnoDB: Found ca.pem, server-cert.pem and server-key.pem in data directory
2019-02-03T15:57:53.190134Z [Note] InnoDB: Skipping generation of SSL certificates as certificate files are present in data directory.
2019-02-03T15:57:53.190180Z [Note] InnoDB: CA certificate ca.pem is self signed.
2019-02-03T15:57:53.190966Z [Note] InnoDB: Server hostname (bind-address): '*' port: 3306
2019-02-03T15:57:53.191041Z [Note] InnoDB: IPv6 is available.
2019-02-03T15:57:53.191041Z [Note] InnoDB: Server socket created on IP: '::'
2019-02-03T15:57:53.203727Z [Note] InnoDB: Event Scheduler: Loaded 0 events
2019-02-03T15:57:53.203922Z [Note] InnoDB: mysqld: ready for connections
Version: 5.7.23-23
socket: /var/lib/mysql/mysql.sock
port: 3306
Percona Server (GPL
