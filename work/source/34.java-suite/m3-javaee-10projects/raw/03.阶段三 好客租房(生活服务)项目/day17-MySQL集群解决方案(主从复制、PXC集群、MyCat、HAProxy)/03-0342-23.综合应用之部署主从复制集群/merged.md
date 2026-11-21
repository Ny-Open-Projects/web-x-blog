# 23.综合应用之部署主从复制集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\23.综合应用之部署主从复制集群【海量资源尽在 ubkz.com】.mp4
- 时长 5分46秒（音频 347s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续接下来呢我们前面的我们是不是已经部署了PX集群那么也就意味着我们这个位置是不是就已经搞定了接下来我们来去部署一个主虫这样的一个节点或者这样的一个集群那我们来看一下部署主虫那么首先呢我们在Date的这个目录下面创建一个MySQL然后呢创建一个Hawk Master01那么把这个目录呢我们先创建出来然后呢我们去进入到这个目录中
[00:27] 那么这个操作跟我们前面操作非常的类似然后创建两个目录然后去做一个授权OK然后我们去进入到我们的config目录下面我们去创建一个mideconfig我们去创建一个mideconfig然后我们把配置文件内容拷贝过来到这拷贝一下
[00:54] 然后这个是我们的一个二进日志然后这个是我们的服务的ID好搞定保存退出然后我们接着继续往下面看创建我们的一个容器创建容器这个容器它的端口是2336我们数据库的服务是端口是2336走好容器就创建成功了然后我们可以把它先跑起来master01这个叫packender好客master01
[01:23] 那么等待它的一个启动那么下面我们是不是可以去连接一下它那么我们再来创建一个连接那么这个就叫什么呢就叫192.168.1.118更我们的一个后刻然后呢mastermaster然后呢01那么它的端口就是23306对吧你看它的端口是不是就233看一下在这个位置可以看到是23306没有问题
[01:54] 然后这个他IP地址然后是一个这前面加一个2,23306密码也是root好那么我们来测试一下连接ok没有问题那么这个我们是不是就搞定了对吧好那么接着我们继续往下面看下面我们要创建一个同步的账户这个操作前面我们也执行过那么我们就不做过的解释了走好这个就搞定了下面我们来查看一下我们的master的一个状态走
[02:23] 那么状态呢ok没有问题是他好那么接下来呢我们就来看一下看一下我们的sleeve的一个创建那么我们依然的去创建这样的一个目录那么我们去进入到我们的sleeve01这个目录下面然后呢去创建这两个目录date和config然后呢做一个授权好然后呢我们再进入到这config下面去创建一个这个my.config文件
[02:51] 然后我们把下面内容拷贝过来那么要注意这个ID不能和我们前面这个ID不能重复那么扫拷一个东西就上面的它把它拷贝一下然后我们去到这个位置来搞定然后把这个注释我们就拿掉好保存退出那么这个就搞定了那么接下来我们来创建我们的这个Sleeve这个容器它的端口是23307
[03:20] 好那么创建好了然后呢我们把它呢启动起来那么这样的话呢我们就可以再来去创建我们的一个连接了那么我们再来创建一个啊他就叫什么呢192.168.1.18-hawk-什么呢slive01-23307然后呢IP地址呢就是他然后呢端口呢是23307密码呢是root
[03:50] 然后创建一个连接ok没有问题好搞定那么接下来我们是不是就给他来设置相关的一些我们的master信息对吧然后到这个里面我们来创建一个查询到这然后这个是18然后这个是23306没有问题然后注意这个是不是有点问题那么文件名要拷贝一下拷贝他到这个里面来往这一丢然后我们再来看一下这个位置是758
[04:18] 然后呢改成758没有问题走好那么下面呢我们是不是就可以去start去启动了启动什么呢sleeve哎哎ok那么我们去启动我们的一个呃这个同步那么接下来呢我们来查看一下它的一个状态啊那么我们就往下面来吧那么查看它的一个状态那么状态中呢我们会发现那么
[04:42] 它的两个如果两个这个IO两个这个RAN1呢一个IO一个Circle呢它都为yes的话那就代表着这个组成配置已经是OK了好那么下面呢我们就来做一个测试那我们在我们的这个下面还是创建一个数据库也是叫浩克然后呢制服级呢同样的也是这个U8好那么现在呢这个浩克就创建好了这个里面有没有呢看一下它也有
[05:12] 然后我们在这个里面创建一张表那么还是用这个还是使用我们在Circle的形式做一个创建创建一个什么呢AD这张表就是我们广告那张表好来看一下这个表就创建成功了那么来刷新一下有没有这张表呢有然后这个里面有没有这张表呢也有OK好嘞那么这样的话我们这个组从复制是不是也搞定了OK那么也就意味着我们架构中的什么呢这一块是不是就已经搞定了
[05:41] 好那么关于这个部署这个祖从父子的一个集群呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

#创建数据卷（存储路径：/var/lib/Docker/volumes）
1 Docker volume create haoke-v1
2 Docker volume create haoke-v2
3 Docker volume create haoke-v3
4 Docker volume create haoke-v4

#拉取镜像
5 Docker pull percona/percona-xtradb-cluster:5.7
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
11 Docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 Docker start percona.haoke-master01 && Docker logs -f percona.haoke-master01
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
11 Docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 Docker start percona.haoke-master01 && Docker logs -f percona.haoke-master01
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
root@itcast02:conf# Docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
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
11 Docker create --name percona.haoke-master01 -v /data/mysql/haoke/master01/data:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 23306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
12 Docker start percona.haoke-master01 && Docker logs -f percona.haoke-master01
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

