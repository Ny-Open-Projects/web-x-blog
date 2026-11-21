# 画面线理解：06.MySQL集群部署之部署MS集群(主从复制)

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\06.MySQL集群部署之部署MS集群(主从复制)【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:44, 01:39, 02:04, 03:03, 03:45, 04:19, 05:02, 05:28, 05:43, 06:34, 07:08, 08:40, 09:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:49:38

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Docker 环境中部署 MySQL 主从复制集群，包括创建节点、配置 my.cnf、启动服务及配置主从同步。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于部署 MySQL 集群的代码，包括创建 pxc_node1、pxc_node2、pxc_node3、pxc_node4 的 docker create 命令，以及启动节点的 docker start 命令。
画面2：展示 Typora 文档中关于部署 MySQL Master 节点的代码，包括创建 ms_node1 的 docker create 命令和启动命令，以及创建用户和授权的 SQL 语句。
画面3：在 SSH 终端中执行 mkdir 和 cd 命令，进入 /data/mysql/haoke/master01/conf/ 目录，准备配置文件。
画面4：展示 Typora 文档中关于配置 Master 节点的 my.cnf 内容，包括 server-id、log_bin、sql_mode 等参数，并显示了创建用户和授权的 SQL 语句。
画面5：展示 Typora 文档中关于配置 Master 节点的 my.cnf 内容，包括 server-id、log_bin、sql_mode 等参数，并显示了创建用户和授权的 SQL 语句。
画面6：展示 Typora 文档中关于部署 MySQL 集群的代码，包括创建 pxc_node1、pxc_node2、pxc_node3、pxc_node4 的 docker create 命令，以及启动节点的 docker start 命令。
画面7：在 SSH 终端中执行 mkdir 和 cd 命令，进入 /data/mysql/haoke/slave01/conf/ 目录，准备配置文件。
画面8：展示 Typora 文档中关于部署 MySQL Slave 节点的代码，包括 CHANGE MASTER TO 设置主节点信息的 SQL 语句。
画面9：在 SSH 终端中执行 docker create 命令创建 ms_node2，然后执行 docker start 命令启动，但因容器不存在而失败，随后执行 docker rm 命令删除容器。
画面10：在 SSH 终端中显示 MySQL 服务启动日志，表明服务已准备好接受连接。
画面11：在 Navicat Premium 中连接到 MySQL 服务器，显示了 CHANGE MASTER TO 语句的 SQL 编辑器界面。
画面12：展示 Typora 文档中关于部署 mycat 的代码，包括设置 master 相关信息的 SQL 语句。
画面13：在 Navicat Premium 中连接到 MySQL 服务器，显示了数据库结构，包括 mysql、information_schema、performance_schema、sys 等系统库。
画面14：展示 Typora 文档中关于部署 mycat 的代码，包括设置 master 相关信息的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
#第二节点（增加了 CLUSTER_JOIN 参数）
docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node2 -e CLUSTER_JOIN=pxc_node1 -net pxc_network --ip=172.30.0.3 pxc

#第三节点
docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node3 -net pxc_network --ip=172.30.0.4 pxc

#第四节点
docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node4 -e CLUSTER_JOIN=pxc_node3 -net pxc_network --ip=172.30.0.5 pxc

#启动
docker start pxc_node1 && docker logs -f pxc_node1
docker start pxc_node2 && docker logs -f pxc_node2
docker start pxc_node3 && docker logs -f pxc_node3
docker start pxc_node4 && docker logs -f pxc_node4

#查看集群节点
show status like 'wsrep_cluster%';
```

画面2：
```bash
#master
mkdir /data/mysql/haoke/master01/conf -p
vim my.cnf

#输入如下内容
[mysqld]
log-bin=mysql-bin #开启二进制日志
server-id=1 #服务id，不可重复
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO
,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

#创建容器
docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
docker start ms_node1 && docker logs -f ms_node1

#创建同步账户以及授权
create user 'itcast'@'%' identified by 'itcast';
grant replication slave on *.* to 'itcast'@'%';
flush privileges;

#查看master状态
show master status;
```

画面3：
```bash
root@itcast03:# mkdir /data/mysql/haoke/master01/conf -p
root@itcast03:# cd /data/mysql/haoke/master01/conf/
root@itcast03:conf# ll
total 12
drwxr-xr-x 2 root root 4896 Feb 26 22:44 ./
drwxr-xr-x 3 root root 4896 Feb 26 22:43 ../
-rw-r--r-- 1 root root 169 Feb 26 22:44 my.cnf
```

画面4：
```bash
#输入如下内容
[mysqld]
log-bin=mysql-bin #开启二进制日志
server-id=1 #服务id，不可重复
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO
,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

#创建容器
docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
docker start ms_node1 && docker logs -f ms_node1

#创建同步账户以及授权
create user 'itcast'@'%' identified by 'itcast';
grant replication slave on *.* to 'itcast'@'%';
flush privileges;

#查看master状态
show master status;
```

画面5：
```bash
#输入如下内容
[mysqld]
log-bin=mysql-bin #开启二进制日志
server-id=1 #服务id，不可重复
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO
,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

#创建容器
docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
docker start ms_node1 && docker logs -f ms_node1

#创建同步账户以及授权
create user 'itcast'@'%' identified by 'itcast';
grant replication slave on *.* to 'itcast'@'%';
flush privileges;

#查看master状态
show master status;
```

画面6：
```bash
#第二节点（增加了 CLUSTER_JOIN 参数）
docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node2 -e CLUSTER_JOIN=pxc_node1 -net pxc_network --ip=172.30.0.3 pxc

#第三节点
docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node3 -net pxc_network --ip=172.30.0.4 pxc

#第四节点
docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node4 -e CLUSTER_JOIN=pxc_node3 -net pxc_network --ip=172.30
