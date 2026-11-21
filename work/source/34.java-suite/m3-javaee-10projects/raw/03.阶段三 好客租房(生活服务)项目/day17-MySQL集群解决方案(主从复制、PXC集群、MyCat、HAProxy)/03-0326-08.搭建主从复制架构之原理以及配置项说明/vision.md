# 画面线理解：08.搭建主从复制架构之原理以及配置项说明

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\08.搭建主从复制架构之原理以及配置项说明【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:22, 02:09, 03:58, 04:46, 04:47, 05:20, 06:32, 06:41, 06:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:33:08

1) 这一组画面整体在讲什么（一句话）：
讲解 MySQL 主从复制架构的搭建原理、主库和从库的配置文件（my.conf）内容及创建同步用户的 SQL 命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 标题：3.1、主从复制原理。
- 内容：展示主从复制架构图，包括 Master 和 Slave 服务器，以及 IO thread、SQL thread、Binary log、Relay log 等组件及其数据流向。
- 文本说明：mysql(主库master)从(给slave)复制的原理：master将数据变更记录到二进制日志(binary log)中，也就是配置文件log_bin指定的文件(这些记录叫做二进制日志事件，binary log events)；slave将master的binary log events拷贝到它的中继日志(relay log)；slave重做中继日志中的事件，将改变反映到自己的数据(数据重演)。

画面 2：
- 标题：3.2、主库配置文件my.conf。
- 内容：展示主库配置文件中的关键配置项。
- 代码：
  #开启主从复制，主库的配置
  log-bin = mysql-bin
  #指定主库serverid
  server-id=1
  #指定同步的数据库，如果不指定则同步全部数据库
  binlog-do-db=my_test
  #执行SQL语句查询状态
  SHOW MASTER STATUS

画面 3：
- 标题：3.3、在主库创建同步用户。
- 内容：展示在主库创建用于同步的 MySQL 用户的 SQL 命令。
- 代码：
  #授权用户'slave01'使用123456密码登录mysql
  grant replication slave on *.* to 'slave01'@'127.0.0.1' identified by '123456';
  #刷新配置
  flush privileges;

画面 4：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;

画面 5：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;

画面 6：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;

画面 7：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;

画面 8：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;

画面 9：
- 标题：3.4、从库配置文件my.conf。
- 内容：展示从库配置文件中的关键配置项。
- 代码：
  #指定server-id，只要不重复即可，从库也只有这一个配置，其他都在SQL语句中操作
  server-id=2
  #以下执行SQL：
  CHANGE MASTER TO
  master_host='127.0.0.1',
  master_user='slave01',
  master_password='123456',
  master_port=3306,
  master_log_file='mysql-bin.000006',
  master_log_pos=1120;
