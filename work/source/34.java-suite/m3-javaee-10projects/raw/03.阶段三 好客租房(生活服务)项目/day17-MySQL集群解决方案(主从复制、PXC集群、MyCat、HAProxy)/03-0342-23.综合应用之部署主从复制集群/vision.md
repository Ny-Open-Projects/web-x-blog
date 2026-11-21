# 画面线理解：23.综合应用之部署主从复制集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\23.综合应用之部署主从复制集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:29, 00:41, 01:04, 01:21, 02:08, 02:32, 02:44, 03:00, 03:22, 04:01, 04:53, 05:18, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:43:10

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Percona XtraDB Cluster 的主从复制集群，包括创建目录、配置文件、启动容器及验证复制状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“7.2. 部署PXC集群”的内容，包含集群一和集群二的节点、端口、容器名称和数据卷配置表，以及创建数据卷的 Docker 命令。
画面2：展示 Typora 文档中“7.3. 部署主从复制集群”的“master”部分，列出创建目录、配置文件、输入配置内容和创建容器的命令。
画面3：同画面2，但光标在“#创建配置文件”行附近。
画面4：同画面2，光标在“#创建容器”命令行附近。
画面5：终端窗口显示在主机上执行创建目录、配置文件、创建容器并启动的命令，以及容器初始化数据库的日志。
画面6：同画面2，光标在“#创建容器”命令行附近。
画面7：终端窗口显示 MySQL 服务启动成功后的日志，包括版本号、端口、SSL 证书警告等。
画面8：终端窗口显示在主机上为 slave01 创建目录和配置文件的命令。
画面9：终端窗口显示编辑 slave01 的 my.cnf 配置文件，内容为 sql_mode 设置。
画面10：展示 Typora 文档中“slave”部分，列出创建目录、配置文件、输入配置内容、创建容器、启动容器和设置 master 相关信息的命令。
画面11：Navicat Premium 连接界面，显示已连接到 slave01 的数据库，列出多个数据库和表。
画面12：展示 Typora 文档中“#启动同步”和“#查看 slave 状态”的命令，以及下方显示“Relay_Master_Log_File”、“Slave_IO_Running”、“Slave_SQL_Running”均为“Yes”的状态框。
画面13：展示“新建数据库”对话框，数据库名为“haoke”，字符集为“UTF-8 Unicode”。
画面14：展示 Typora 文档中“7.3. 部署主从复制集群”的“master”部分，光标在“#创建目录”命令行附近。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
• 虚拟数据保存到PXC分片中，其余数据保存到主从架构中

7.2. 部署PXC集群

集群一：
节点	端口	容器名称	数据卷
node1	13306	pxc_node1	haoke-v1
node2	13307	pxc_node2	haoke-v2

集群二：
节点	端口	容器名称	数据卷
node3	13308	pxc_node3	haoke-v3
node4	13309	pxc_node4	haoke-v4

#创建数据卷（存储路径：/var/lib/docker/volumes）
1 docker volume create haoke-v1
2 docker volume create haoke-v2
3 docker volume create haoke-v3
4 docker volume create haoke-v4

#拉取镜像
5 docker pull percona/percona-xtradb-cluster:5.7
```

画面2：
```
7.3. 部署主从复制集群
master：
#创建目录
1 mkdir /data/mysql/haoke/master01 -p
2 cd /data/mysql/haoke/master01
3 mkdir conf data
4 chmod 777 * -R
#创建配置文件
5 cd /data/mysql/haoke/master01/conf
6 vim my.cnf
#输入如下内容
7 [mysqld]
8 log-bin=mysql-bin #开启二进制日志
9 server-id=1 #服务id，不可重复
10 sql_mode= STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
#创建容器
11 docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 docker start percona.haoke-master01 && docker logs -f percona.haoke-master01
#创建普通用户以及授权
13 create user 'itcast'@'%' identified by 'itcast';
14 grant replication slave on *,* to 'itcast'@'%';
15 flush privileges;
#查看master状态
16 show master status;
```

画面4：
```
#创建目录
1 mkdir /data/mysql/haoke/master01 -p
2 cd /data/mysql/haoke/master01
3 mkdir conf data
4 chmod 777 * -R
#创建配置文件
5 cd /data/mysql/haoke/master01/conf
6 vim my.cnf
#输入如下内容
7 [mysqld]
8 log-bin=mysql-bin #开启二进制日志
9 server-id=1 #服务id，不可重复
10 sql_mode= STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
#创建容器
11 docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 docker start percona.haoke-master01 && docker logs -f percona.haoke-master01
#创建普通用户以及授权
13 create user 'itcast'@'%' identified by 'itcast';
14 grant replication slave on *,* to 'itcast'@'%';
15 flush privileges;
#查看master状态
16 show master status;
```

画面5：
```
root@itcast02:volumes# mkdir /data/mysql/haoke/master01 -p
root@itcast02:master01# cd /data/mysql/haoke/master01
root@itcast02:master01# chmod 777 * -R
root@itcast02:conf# docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
percona.haoke-master01
Initializing database
2019-02-04T03:19:59.419661Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use
--explicit_defaults_for_timestamp option for documentation for more details.
```

画面6：
```
#创建目录
1 mkdir /data/mysql/haoke/master01 -p
2 cd /data/mysql/haoke/master01
3 mkdir conf data
4 chmod 777 * -R
#创建配置文件
5 cd /data/mysql/haoke/master01/conf
6 vim my.cnf
#输入如下内容
7 [mysqld]
8 log-bin=mysql-bin #开启二进制日志
9 server-id=1 #服务id，不可重复
10 sql_mode= STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
#创建容器
11 docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 docker start percona.haoke-master01 && docker logs -f percona.haoke-master01
#创建普通用户以及授权
13 create user 'itcast'@'%' identified by 'itcast';
14 grant replication slave on *,* to 'itcast'@'%';
15 flush privileges;
#查看master状态
16 show master status;
```

画面7：
```
InnoDB: 32 non-redo rollback segment(s) are active.
InnoDB: Waiting for purge to start
InnoDB: Percona XtraDB (http://www.percona.com) 5.7.23-23 started;
log sequence number 11904408
[Note] Plugin 'FEDERATED' is disabled.
InnoDB: Buffer pool(s) load completed at 190204
