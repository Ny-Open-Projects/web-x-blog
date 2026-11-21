# 11.搭建主从复制架构之主从复制的3种模式

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\11.搭建主从复制架构之主从复制的3种模式【海量资源尽在 ubkz.com】.mp4
- 时长 9分11秒（音频 551s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下主从复制的模式啊那么首先呢我们先来去做这样的一个执行那么我们还得去找一下前面的一个命令啊在前面的有这样的一个命令我们去查看主的一个相关这个二进制啊相关的配置项那么我们找到我们这个主然后呢点击这个新建一个查询走那么在这个相关二进制配置项中啊有一项的比较重要是在这个位置
[00:30] 我们的一个binlog的一个format然后呢它呢是一个raw这个代表什么意思呢我们来看一下它其实代表的是我们的一个组从复制的一个模式啊我们来看一下那么在我们的这个mycircle中啊它提供了有三种模式可选大家默认使用的是raw啊这种模式这个是什么意思呢我们来看一下第一种模式呢它是叫基于circle语句啊这样的一个复制
[00:58] 把它称之为叫做SBR第二种叫做基于行的复制叫做RBR然后还有一种叫做混合模式叫MBR那么它所对应的三个配置项的三个指的是这样的也叫statement然后叫做row还有叫mixed这三个项这三个项分别代表什么意思我们一一来讲一下那么首先我们来看一下第一个叫做什么呢SBR就是我们去根据基于社会语句的一个这样的一个记录
[01:26] 那么也就是说我们的每一条每一条这个会修改数据的语句呢都会被记录到二进制的一个日子文件中那么这种方式有没有优缺点呢有那么我们来看一下它的优缺点那么首先第一个先来看优点优点就是我们并不需要去记录每一条Circle语句和每一行数据的变化这个代表什么意思大家想一下你比如说我现在呢有一个这个update的操作比如说update
[01:56] 一个某一个值然后的条件是Value比如说年龄大于20岁的这样的一个条件那么这个条件更新的可能会涉及到有100个用户的数据的一个更新那么但是我们仅仅记录到日志文件中的时候只需要记录一条语句就可以了你不需要去记录这20条数据它的一个变化
[02:19] 所以说呢这个就是它的一个优点它减少了一个日志啊减少日志也节省了我们这个IO提升了这个性能那么这个是它的一个优点它有没有缺点呢同样它也是有缺点的我们来看一下那么在某些这个特殊的情况下面会导致我们的数据不一致那么什么时候会导致数据不一致呢比如说我们使用一些函数的时候是不一致的你比如说啊我们来举个例子
[02:46] 比如说呢我们看一下这样的一个语句比如说来一个叫做select什么呢比如说就有一个那么这个是我们的一个语句对不对那么我来查询一下这个是我当前的一个这个时间但是呢大家可以想一下
[03:02] 那么如果我仅仅在日志文件中呢我记录了这样的一个语句那么我这个语句如果去同步了我重顾的话他是不是也是去记录这样的语句啊那么显然呢我的主顾所执行这个语句得到的一个结果跟我的重顾所执行这个语句得到的结果是不一样的所以说呢那么我们可能在
[03:24] 这样的一些情况下面就会导致我们这个数据呢它是不一致的啊所以这个呢就是我们这个SBR这种模式的一个最大的一个缺点那么就是我们使用了函数的时候啊就会导致数据的不一致这个问题还是比较严重的那么第二种模式叫肉模式这种模式是默认的模式什么意思呢就是说不记录每条社会语句的一个它的一个社会语句而是说去记录了哪些数据
[03:52] 被修改了并且修改成什么样子了他所记录的是你的数据的修改并不是搜狗语句那么这种情况下面那么就不会因为我们使用了一些函数而导致我们数据不一致这样的问题这个问题是不存在的但是呢大家可以想一下那么
[04:13] 这个是他的一个优点他解决了前面的问题对不对那么他有没有缺点呢同样他也是有缺点的那么他的缺点呢就是他会产生什么大量的我们这个日志啊大量的日志数据那么尤其是在什么时候呢比如说再举个例子比如说当我们去更新一张表的时候比如刚刚我所举的那个例子那么我如果去修改年龄大于20岁的一些这个值的时候
[04:39] 那么我可能会涉及到有100个用户那么对于第一种模式你只需要记录一条语句就可以了但第二条模式呢你需要记录100条这个数据因为它所记录的是每一条数据的一个变化
[04:54] 这个大家能够理解吗OK所以说在我们特殊情况下面它会导致我们日志文件的一个数量的一个暴增比如说更新表比如说一个全量表的全表的更新的时候这个日志肯定是个大量的对吧所以你会发现无论是SBR还是RBR各有各的优缺点对不对各有个优缺点那么这样的话就会出现什么出现第三种这个模式叫做MIC的模式就是混合模式什么叫MIC的模式呢
[05:22] 他是将我们前面的SBR和RBR做一个混合然后呢我们MySQL去根据我们的一个SQL语气来判断我们是采用我们的一个SBR保存还是采用的RBR做一个保存所以说呢这种模式相对而言是不是就会比较的灵活和比较的一个合理OK所以说在这给出大家一个建议建议使用MIC的这种模式好那我们来看一下
[05:51] 这种模式怎么样去做一个配置呢配置非常简单只需要去找到我们的一个配置项那么我还是要回到cd点点回去进入到这个下面的有一个master然后呢进入到config下面的我们打开这个配置内容然后呢把它丢到下面就可以了那么指定它的一个值是mixed然后呢保存退出那么接下来呢我们去把它做一个重启restart叫precender
[06:19] 然后呢master01然后呢我们去直接重启吧就不去查看日志了那么等待他的一个重启重启成功之后呢那就OK了好那么重新重启之后呢我们就来查看一下他的一个这个值是多少那么OK我们等待他重启完成了
[06:38] 然后那么去做一个查询查询它的一个相关的配置项那么你会发现在这个位置我们是不是已经把它改成什么呢mixed这种模式了这个也是我们所建议使用的一种模式ok好那么我们来看一下那么最终是不是就会这样的一个效果当然了当我们去做一些我们数据更新的时候或者说我们去添加数据的时候没有任何问题张三李是来一个网五保存那么进入到我们3307这个里面刷新那么数据是不是
[07:07] 现在我们数据是否没有去同步过来网络没有同步过来那么这样的话我们是不是需要可能是我们刚刚我们在重启之后它的一个同步的一个内容发生了变化我们可以来查看一下那么我们去找到前面我们主库中的一个配置我们来查看一下它的一个must的一个状态那么我们到这个位置来那么查看它的一个must状态
[07:33] 那么是有这么多些内容那我们给我们的重库呢再去做一些这个把它的这个就是同步的信心的去做一下这个调整那么进入到这个重库里面咱们把这个内容拷贝过来那么这样吧我们先给它stop掉stop然后呢slave然后呢先把它停止然后呢我们再去什么呢再去修改它的一个这样的一个值那么要修改的内容呢还是去回到我们的
[08:02] 这个配置的内容能把它呢拷贝过来然后它的位置啊我们从这个495开始去做一个同步哎ok然后呢这样的话就搞定了然后呢我们再去做一个start start来一个sleepok好然后呢我们去做一个启动这样的话就可以了下面呢我们也可以去查看它的一个这个状态啊这个状态呢应该呢就可以去完成一个数据的一个同步了那我们来看一下
[08:31] 那么有两个关键的位置是不是有两个这个yes都搞定了好那么我们接下来再来去这个位置来刷新一下这个里面没有问题但是到这个里面来看一下网我是不是就来了ok好那么我们来看再来添加一个有没有问题再来一个造6然后保存然后到这个里面来刷新一下来看一下是不是就没有任何问题了
[08:54] OK好那么这样的话呢我们是不是就已经成功的去将我们的这个组从复制的模式由原有的这个zo这种模式改为什么呢mix模式这也是我们所推荐使用的一种模式OK好那么关于这个组从复制的一个模式那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 部署 MySQL 主从复制环境，并配置 binlog 格式为 ROW。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：在 Typora 编辑器中查看“3.7. 主从复制模式”章节，其中显示了 `show global variables like 'binlog%'` 的查询结果，`binlog_format` 的值为 `ROW`。
- 画面序号：1

画面 2：
- 内容：在 Typora 编辑器中显示了用于创建从库容器的 Docker 命令，包括 `Docker create` 和 `Docker start` 命令，以及设置从库连接主库的 SQL 语句 `CHANGE MASTER TO`。
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
- 内容：在 Xshell 终端中，用户进入 `conf` 目录，编辑 `my.cnf` 文件，并执行 `Docker restart percona-master01` 命令。
- 画面序号：7

画面 8：
- 内容：在 Typora 编辑器中显示了修改主库配置的命令，以及 `show global variables like 'binlog%'` 的查询结果，`binlog_format` 的值为 `MIXED`。
- 画面序号：8

画面 9：
- 内容：在 Typora 编辑器中显示了用于创建主库容器的 Docker 命令，包括 `Docker create` 和 `Docker start` 命令。
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
Docker create --name percona-slave01 -v /data/mysql/slave01/data:/var/lib/mysql -v /data/mysql/slave01/conf:/etc/mysql.cnf -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
Docker start percona-slave01 && Docker logs -f percona-slave01

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

