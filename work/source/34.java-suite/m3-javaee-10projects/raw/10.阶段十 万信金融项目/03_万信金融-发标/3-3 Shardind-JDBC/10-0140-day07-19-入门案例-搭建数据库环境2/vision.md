# 画面线理解：day07-19-入门案例-搭建数据库环境2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-19-入门案例-搭建数据库环境2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 03:25, 04:34, 07:02, 08:14, 09:28, 09:52, 11:04, 12:06, 12:56, 13:56, 15:14, 15:43, 16:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:41:02

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 MySQL 主从复制，包括主库授权、从库安装、设置同步参数及检查链路。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示主库配置文件 [mysqld] 的内容，包含 server-id、log-bin、binlog-do-db、binlog-ignore-db 等配置项。下方有从库配置的注释。
画面2：展示主库授权命令 GRANT REPLICATION SLAVE ON *.* TO 'db_sync'@'%' IDENTIFIED BY 'db_sync';，并执行 show master status; 查看二进制日志文件和位置。
画面3：展示主库授权命令和 show master status; 的结果，与画面2内容一致。
画面4：在 Windows PowerShell 中执行 GRANT REPLICATION SLAVE... 和 FLUSH PRIVILEGES; 命令，成功后返回 Query OK。
画面5：展示从库配置文件 [mysqld] 的内容，包含 server-id、log-bin、binlog-do-db、binlog-ignore-db 等配置项。下方有从库配置的注释。
画面6：展示从库连接主库的命令 mysql -h localhost -P3307 -uroot -p123，并提示修改从库配置文件。
画面7：展示从库连接主库的命令 mysql -h localhost -P3307 -uroot -p123，并提示修改从库配置文件。
画面8：展示从库设置同步参数的命令 CHANGE MASTER TO ...，并提示执行后需重启主从服务。
画面9：展示从库设置同步参数的命令 CHANGE MASTER TO ...，并提示执行后需重启主从服务。
画面10：展示从库设置同步参数的命令 CHANGE MASTER TO ...，并提示执行后需重启主从服务。
画面11：展示从库设置同步参数的命令 CHANGE MASTER TO ...，并提示执行后需重启主从服务。
画面12：展示从库设置同步参数的命令 CHANGE MASTER TO ...，并提示执行后需重启主从服务。
画面13：展示主库的 show master status; 结果，二进制日志文件为 mysql-bin.000001，位置为 592。
画面14：展示主库的 show master status; 结果，二进制日志文件为 mysql-bin.000001，位置为 592。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
[mysqld]
log-bin = mysql-bin
server-id = 1
#设置需要同步的数据库
binlog-do-db=store_db
binlog-do-db=product_db_1
binlog-do-db=product_db_2
#排除系统库同步
binlog-ignore-db=mysql
binlog-ignore-db=information_schema
binlog-ignore-db=performance_schema

从库配置：

画面2：
#授权至主机端口
mysql -h localhost -uroot -p123
#授权从库专用账号
GRANT REPLICATION SLAVE ON *.* TO 'db_sync'@'%' IDENTIFIED BY 'db_sync';
#刷新权限
FLUSH PRIVILEGES;
#确认位置 记录下文件名及位点
show master status;

画面3：
#授权至主机端口
mysql -h localhost -uroot -p123
#授权从库专用账号
GRANT REPLICATION SLAVE ON *.* TO 'db_sync'@'%' IDENTIFIED BY 'db_sync';
#刷新权限
FLUSH PRIVILEGES;
#确认位置 记录下文件名及位点
show master status;

画面4：
mysql> GRANT REPLICATION SLAVE ON *.* TO 'db_sync'@'%' IDENTIFIED BY 'db_sync';
Query OK, 0 rows affected, 1 warning (0.08 sec)
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.05 sec)
mysql>

画面5：
[mysqld]
log-bin = mysql-bin
server-id = 1
#设置需要同步的数据库
binlog-do-db=store_db
binlog-do-db=product_db_1
binlog-do-db=product_db_2
#排除系统库同步
binlog-ignore-db=mysql
binlog-ignore-db=information_schema
binlog-ignore-db=performance_schema

从库配置：

画面6：
#切换至从库bin目录，登录从库
mysql -h localhost -P3307 -uroot -p123
#修改从库指向主库，使用上一步记录的文件名以及位点

画面7：
#切换至从库bin目录，登录从库
mysql -h localhost -P3307 -uroot -p123
#修改从库指向主库，使用上一步记录的文件名以及位点

画面8：
CHANGE MASTER TO
master_host = 'localhost',
master_user = 'db_sync',
master_password = 'db_sync',
master_log_file = 'mysql-bin.000001',
master_log_pos = 592;

画面9：
CHANGE MASTER TO
master_host = 'localhost',
master_user = 'db_sync',
master_password = 'db_sync',
master_log_file = 'mysql-bin.000001',
master_log_pos = 592;

画面10：
CHANGE MASTER TO
master_host = 'localhost',
master_user = 'db_sync',
master_password = 'db_sync',
master_log_file = 'mysql-bin.000001',
master_log_pos = 592;

画面11：
CHANGE MASTER TO
master_host = 'localhost',
master_user = 'db_sync',
master_password = 'db_sync',
master_log_file = 'mysql-bin.000001',
master_log_pos = 592;

画面12：
CHANGE MASTER TO
master_host = 'localhost',
master_user = 'db_sync',
master_password = 'db_sync',
master_log_file = 'mysql-bin.000001',
master_log_pos = 592;

画面13：
mysql> show master status;
+------------------+----------+
| File             | Position |
+------------------+----------+
| mysql-bin.000001 | 592      |
+------------------+----------+
1 row in set (0.00 sec)

画面14：
mysql> show master status;
+------------------+----------+
| File             | Position |
+------------------+----------+
| mysql-bin.000001 | 592      |
+------------------+----------+
1 row in set (0.00 sec)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2、3、6、7、8、9、10、11、12、13、14：PPT标题为“3. 设置从库向主库同步数据，并检查链路”，内容包含：
- 授权从库专用账号的命令
- show master status; 的结果
- CHANGE MASTER TO 的配置参数
- 执行命令后的操作提示（重启服务、检查状态、处理异常）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
