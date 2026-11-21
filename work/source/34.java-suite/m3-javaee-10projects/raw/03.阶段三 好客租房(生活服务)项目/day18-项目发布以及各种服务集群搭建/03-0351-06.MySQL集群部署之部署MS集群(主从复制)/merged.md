# 06.MySQL集群部署之部署MS集群(主从复制)

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\06.MySQL集群部署之部署MS集群(主从复制)【海量资源尽在 ubkz.com】.mp4
- 时长 9分20秒（音频 560s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来部署MS架构就是我们的主从架构那么主从架构呢按照前面我们的规划来讲的话那我们需要在我们的19这个机器上面去做一个执行好那么我们来看一下那么首先呢需要去创建一个目录那么这个目录下面呢主要呢是需要放置我们的配置文件哎OK好那我们先把这个目录呢创建出来那么在这创建
[00:26] 然后我们进入到这个目录叫date下面的mycircle然后下面的浩克mast01config下面然后VM创建一个my.cnf这是我们的一个配置文件那么走那么我们把这个配置文件的内容去拷贝过来那么有这么多内容然后网上一贴然后我把这个就删掉注释就删掉OK
[00:57] 那么这个服务ID呢我们就保持为1就可以了保存退出那么现在呢我们是不是就有了这样的一个配置文件了卖点config这样的一个配置文件那么接下来呢我们需要创建一个容器那么这个容器呢我们是需要去给它去指定一个我们的一个这个数据券这个呢我们刚刚已经创建好了然后呢去指向了这个目录然后呢我们需要去指定一个config的一个配置那么由于我们要指定配置文件嘛
[01:27] 然后呢我们指定一个端口是13310啊这个端口那么映射道是3306那么后面的这个呢就是指定root的一个密码同样的也是rootok好那么我们来创建这个容器我们来尝试试一下走那么这个容器呢就发现它已经创建好了那么接下来呢我们就可以去把这个容器呢就先跑起来那么我们去启动它然后呢去等待它的一个启动
[01:54] 好那么到这里呢我们这个服务呢就跑起来了那么跑起来之后呢我们需要去登录到这个服务呢去给他去创建一些用户啊那么所以呢我们在我们Networkit的下面呢我们再来去去添加几个这个连接那么我们这样吧还是做复制吧复制这样会快一些那么复制一个连接那么名字呢我们这个就不叫PXC了那我们就叫这个MS啊这种架构然后它是我们的一个这个master对吧
[02:24] master01然后呢它的一个端口呢刚刚我们看到它呢是13310那么我们把这个端口改成13310密码呢不变那么连接测试一下那么这个是有问题的我们刚刚连到是这个19那么这个并没有修改那么我们把这个呢118也改成这个19那么我们再来测试一下发现没有问题连接成功了好那么连接成功之后呢我们要创建一个查询
[02:52] 然后在创建查询中呢我们要去执行下面的这个内容啊那么我们把它先拷贝过来那么这个呢我们是创建一个这个用户对吧那么这样我们把这个IDCast呢我们就改成浩克吧不要用IDCast了浩克然后呢这个呢就用这个浩克然后呢这个也改成浩克这样的一个语句那么我们把它呢同样的也拷贝过来然后呢去做一个这样的一个执行走
[03:19] 那么现在呢就这个用户呢就创建好了那么这个用户主要是用于我们的这个数据的一个复制对吧好那么下面我们可以来查看一下我们这个组的这个状态啊就是设为一个master这样的一个状态那么这两个信息我们一会要用到啊这个大家应该是比较熟悉了哎OK好那么我们组的就已经搞定了下面我们来看一下我们的这个重节点那么这个重节点呢同样的也是在我们的19这个服务器上面去做一个执行
[03:49] 好那我们来看一下那么找到我们这个虫那么同样的也去也去创建啊这样的一个目录那么这个不叫CD这个叫MakeDR去创建这样的一个目录好那么我们进入到我们这个配置文件然后呢就我们这个控制台然后呢我们再进入它叫DataMyCircle然后下面Hawk然后呢Slave01然后呢Config
[04:16] 然后呢我们再来创建这个配置文件到这那么配置文件中的内容呢我们再来做一下这个拷贝把这个内容呢就拷贝过来到这然后呢我们把这个serve id呢改成这个2这个呢要保持这个不相同啊就可以了保持它的唯一性好那么接下来呢我们再来创建这个容器啊创建这个容器那么这个容器呢
[04:44] 就是它的一个端口音色呢是13311啊这个端口去做一个音色啊就可以了好那么把这个呢拷贝过来当然了你也需要去指定这个配置文件啊的目录啊刚刚我们看到已经在这个位置呢就指定了那么下面呢我们就需要把我们这个服务呢就跑起来那我们来看一下这个呢是node2那么大家会发现啊这个名字是跟我们前面写的是不一样的叫mxnode2
[05:14] 这块我们可能没有去做一个调整那么这样我们就把它调一下吧我们先把刚刚我们创建这个啊给它删除掉remote就它把它删掉好那么删掉之后呢我们重新来创建一个这个容器啊我们去创建一个它这样那么呃这样的话呢我们名字呢就变成这个ms node2了然后呢我们再去做一个start启动那么再去查看日志啊这样的话就没有问题了那我们等待它的一个启动
[05:41] 好那么到这里呢这个服务呢就已经跑起来了那么跑起来之后呢我们还是需要去再次连接到它啊那么我们再去把它呢复制一个连接然后呢这个就叫Sleeve01Sleeve01然后呢这个19然后呢这个是11那么改成11连接测试一下没有问题OK好那么这个是我们的这个Sleeve那么在这个里面呢我们再来去创建一个查询
[06:11] 然后呢我们把下面这个命令拷贝过来要注意的是这个命令呢里面的XXX内容啊需要我们自己做一个调整那我们的地址呢是191681.19啊这个机器然后呢用户名呢是浩克啊刚刚我们修改成这个浩克了那么他的密码呢同样呢我们看一下啊密码呢刚刚我们是不是已经去掉了密码呢其实就是这个浩克也是这个浩克然后呢这个端口呢是
[06:38] 刚刚呢我们可以看到他的端口呢是13310没有问题是对的然后呢这个文件啊就是我们的这个日志的这个文件那么就是他那么把它拷贝过来然后呢位置呢是741然后呢我们把这个呢就拷贝到这哎OK好搞定走那么这样的话呢我们must相关的一些信息呢就已经配置好了那配置好之后呢我们去启动啊我们的这个sleep然后呢让他去做一个开始做同步
[07:08] 那么接下来呢我们可以去查看一下我们这个slave的一个状态啊那么来看一下那么在这个呢我们其实讲过就是说看两个关键点那么是不是就是这两个那种啊那么他们两个都为yes的话那就代表着我们这个主虫呢就搞定了那么接下来呢我们就可以来测试一下啊测试一下看这个主虫究竟啊ok了没有那么回到主这个里面来那么在这个位置呢我们创建个数据库比如说就叫test
[07:35] 然后呢制服级呢我们还是使用这个u8作为我们那个制服级那么我们来看一下这个里面有没有去创建好这个test呢ok没有问题然后呢我们在这个里面呢创建一张表那么这个表呢呃在这创建一张表那么这个表呢我们呃这个字段叫id然后呢叫bigint然后呢是主件然后呢只增长再添加一个字段叫name然后呢5x然后呢100
[08:05] 保存然后呢tb然后呢bt然后呢我们点击这个确定好那么下面我们来看一下在下面的我们这个虫这个里面中啊那么它有没有创建这张表呢你发现也是有表的对不对那么在这个里面再来测试一下那么比如说我叫这个王我保存一下那么没有问题那么到这个里面再来看一下有没有数据呢你发现也是没有也是ok同样是有数据的啊那么这样的话就说明我们主虫是不是就已经
[08:33] 搭建是OK了没有任何问题好那我们就把这个test这个库呢就删掉吧然后呢刷新一下这个里面同样它也就被删掉了那么在前面呢我们测试这个PXC的时候啊那么没有把这个删除掉因为我保留的并没有任何用啊所以把它就删掉就好了然后可能有两个问题是不是我们刚刚这个服务停掉了还是怎么样的啊我们检查一下
[08:59] 那么在这个里面呢去查看一下正在运行的啊没有也是有的啊没有问题那么有可能是我这个工具的这个问题啊等待他响应就好了OK好那么到这里呢我们其实就已经完成了我们这个MS的这样的一个集群的一个搭建啊OK好那么关于这个MS集群的搭建呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Docker 环境中部署 MySQL 主从复制集群，包括创建节点、配置 my.cnf、启动服务及配置主从同步。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于部署 MySQL 集群的代码，包括创建 pxc_node1、pxc_node2、pxc_node3、pxc_node4 的 Docker create 命令，以及启动节点的 Docker start 命令。
画面2：展示 Typora 文档中关于部署 MySQL Master 节点的代码，包括创建 ms_node1 的 Docker create 命令和启动命令，以及创建用户和授权的 SQL 语句。
画面3：在 SSH 终端中执行 mkdir 和 cd 命令，进入 /data/mysql/haoke/master01/conf/ 目录，准备配置文件。
画面4：展示 Typora 文档中关于配置 Master 节点的 my.cnf 内容，包括 server-id、log_bin、sql_mode 等参数，并显示了创建用户和授权的 SQL 语句。
画面5：展示 Typora 文档中关于配置 Master 节点的 my.cnf 内容，包括 server-id、log_bin、sql_mode 等参数，并显示了创建用户和授权的 SQL 语句。
画面6：展示 Typora 文档中关于部署 MySQL 集群的代码，包括创建 pxc_node1、pxc_node2、pxc_node3、pxc_node4 的 Docker create 命令，以及启动节点的 Docker start 命令。
画面7：在 SSH 终端中执行 mkdir 和 cd 命令，进入 /data/mysql/haoke/slave01/conf/ 目录，准备配置文件。
画面8：展示 Typora 文档中关于部署 MySQL Slave 节点的代码，包括 CHANGE MASTER TO 设置主节点信息的 SQL 语句。
画面9：在 SSH 终端中执行 Docker create 命令创建 ms_node2，然后执行 Docker start 命令启动，但因容器不存在而失败，随后执行 Docker rm 命令删除容器。
画面10：在 SSH 终端中显示 MySQL 服务启动日志，表明服务已准备好接受连接。
画面11：在 Navicat Premium 中连接到 MySQL 服务器，显示了 CHANGE MASTER TO 语句的 SQL 编辑器界面。
画面12：展示 Typora 文档中关于部署 mycat 的代码，包括设置 master 相关信息的 SQL 语句。
画面13：在 Navicat Premium 中连接到 MySQL 服务器，显示了数据库结构，包括 mysql、information_schema、performance_schema、sys 等系统库。
画面14：展示 Typora 文档中关于部署 mycat 的代码，包括设置 master 相关信息的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
#第二节点（增加了 CLUSTER_JOIN 参数）
Docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node2 -e CLUSTER_JOIN=pxc_node1 -net pxc_network --ip=172.30.0.3 pxc

#第三节点
Docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node3 -net pxc_network --ip=172.30.0.4 pxc

#第四节点
Docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node4 -e CLUSTER_JOIN=pxc_node3 -net pxc_network --ip=172.30.0.5 pxc

#启动
Docker start pxc_node1 && Docker logs -f pxc_node1
Docker start pxc_node2 && Docker logs -f pxc_node2
Docker start pxc_node3 && Docker logs -f pxc_node3
Docker start pxc_node4 && Docker logs -f pxc_node4

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
Docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
Docker start ms_node1 && Docker logs -f ms_node1

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
Docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
Docker start ms_node1 && Docker logs -f ms_node1

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
Docker create --name ms_node1 -v haoke-v5:/var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf.d -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
Docker start ms_node1 && Docker logs -f ms_node1

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
Docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node2 -e CLUSTER_JOIN=pxc_node1 -net pxc_network --ip=172.30.0.3 pxc

#第三节点
Docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node3 -net pxc_network --ip=172.30.0.4 pxc

#第四节点
Docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc -name=pxc_node4 -e CLUSTER_JOIN=pxc_node3 -net pxc_network --ip=172.30

