# 09.搭建主从复制架构之搭建主库（master）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\09.搭建主从复制架构之搭建主库（master）【海量资源尽在 ubkz.com】.mp4
- 时长 7分54秒（音频 474s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来动手来搭建一下我们的祖宗复制啊这种架构那么首先呢我们来搭建的是我们的主库就那个must那么我们来看一下呢首先连接到我的一个虚拟机那么这个虚拟机它来币地址呢是192.168然后呢1.8这个地址然后呢我们参考我们的讲义来做一个搭建那么首先我们去把我们这个目录先创建出来
[00:27] 那么可以看到在我们的date下面有一个mycircle这样的一个目录然后我们会发现创建是失败的因为我们前面不存在mycircle目录怎么办后面是不是可以加一个-p这个参数那么就创建好了创建好之后我们去进入到这个目录中然后我们去注意进入这个目录pwd然后我们就创建两个目录一个是config一个是date
[00:54] 那么显然我们可以看到我们这个目录是master01那么可能意味着可能会有多个master对吧然后我们可以看到在这个位置是有config和date显然config是不是放我们的配置date是放我们的数据OK好那么接下来我们给它去做一个授权那么会涉及到一个Docker的一个权限的问题那么授权成777最大权限然后我们就进入到我们config这个目录
[01:22] 然后我们去创建一个我们的一个mideconfig这个配置文件那么这个配置文件的内容呢就是下面的这两个内容这个前面我们也提到过对吧然后呢第一个就是我们这个要开启这个二进制的一个日志那么后面的这个呢是指定他的一个二进制的一个日志文件的一个文件名然后呢下面这个指定的服务的ID
[01:47] 那么服务设定不可重复所以我们把它先设置为1保存退出那么我们配置文件就搞定了接下来我们来去创建我们容器那么在这个位置要注意的是那么我们首先我来看一下所需要的我们就是PriorCannot的一个镜像是5.7.23这样的一个镜像我们来看一下它的一些参数有哪些
[02:13] 那么创建这个容器指定名字呢就Burkner Master01然后呢杠V是做一个目录的挂载就是刚刚我所看到的这个date这个目录呢去挂载到容器中的one lab下面的一个mycircle这个目录还有一个呢是这个比较重要了啊就是一个杠V来指定我们config这个目录来指定到我们etc下面的my.config.d这个目录那么
[02:41] 这注意后面这个目录的是我们容器中的一个目录哎OK这一定要注意然后的杠屁呢是指定我们端口的一个映射3306到3306然后呢后面这个呢是指定我们入图用户的一个密码是入图密码OK好那我们把这个命令拷贝过来然后呢往这一贴走那么显然可以看到这个容器呢它就已经创建好了当然如果在你的机器上面啊这个镜像呢没有下载的话它呢会先做一个下载然后再去做这样的一个
[03:10] 这个创建容器哎OK好嘞好那么当我们创建好之后呢我们就可以来启动啊启动它了然后呢我们来启动一下吧启动它走那么启动我们这个容器呢并且来查看我们的一个这个日志啊那我们等待它的一个创建那么等待创建等待它的一个一些这个初始化的操作那么看到这个位置呢它就已经启动完成了
[03:39] 那么启动成功之后呢我们就需要连接到他去做一个操作那么我在这使用的呢依然是使用的我们的这个呃来不及去做为我作为我那个客户端去做一个使用那么这个呢里面有这么多集群啊这个我们最终会有这么多啊呃这样我就先创建一个吧先新建一个我们的一个呃这个主那么比如说叫my circle集群呃my circle集群二
[04:09] 放到这个里面来然后我们首先创建MySQL的一个连接这个连接叫192.168.1.18然后它是我们的一个master然后33063306这个端口然后我们把这个IP地卡背一下到这然后这个端口是3306用户名是root密码也是root然后点击连接测试走那你会发现现在也是连接成功了
[04:37] 然后点击这个确定那么我们这个的就已经连接成功了那么接下来我们需要去做一些我们的一个设置那么前面我们说过为了去实现一个主厨的一个复制那我们在我们的主库中需要去创建一个用户然后去做一个这样的一个授权那么首先我们先来先来创建一个用户那么我们把这个命令拷贝过来这个用户就创建成功了但是我会发现那么这个其实我们的命令直接成功了
[05:07] 但是后面这个显示会有点问题就是他在显示这个国外货币的时候会出现一个这个error这个是仅仅显示的问题我们这个用户其实就创建成功了其实我们可以通过这个mycircle这个库下面有个表叫做优劣表你会发现这个里面这个IDcast这个用户就已经创建成功了那么可以看到这个IDcast用户以及他的密码的就是IDcast那么接下来我们来给他做一个授权
[05:35] 做个授权那么刚刚我们所提到这个错误呢我们一会儿再来做一个解决OK那么做一个授权那么选中它去做这样的一个执行授权成功依然会有这个错误然后呢我们去刷新这个配置那么我们来看一下到这个位置来去选中它选中它去点击右键运行与选择的这个命令行那么这样的话呢就已经刷新成功了那么接下来呢我们来把这个错误解决一下这个错误怎么解决呢也是非常好解决的
[06:03] 那么只要打开我们的配置文件那么我们打开这个mide.conf一个配置文件在下面的去添加这样的一个配置那么它就不会出现这样的错误了那么保存退出然后我们把我们这个容器做一个重新做一个启动来一个restart我们等待它的启动那么启动成功之后我们再去做一些查询它就不会出现这样的错误了那么一会我们可以来测试一下那么现在它已经就启动成功了
[06:32] 那启动成功之后呢我们去刷新一下走你会发现哎那个错误是不是就没有了哎OK好嘞那么我们接着继续往下面看那么下面呢我们可以通过这个是我一个master states来去查看我们的一个master的一个状态啊走那么这个呢就是一个状态那么在这个状态的一个结果中呢要需要注意的是这两个内容比较关键啊一个就是他的一个这个
[06:57] 日志的文件一个呢就是我们的一个这个位置啊一个是文件一个位置这两个呢我们要记住然后一会儿要用到它啊大了一会儿我们可以再来查询一次啊就可以了OK好那么也可以去查看一些其他的一些这个配置项你比如说我们可以查看一下这个相关于我们二进制的一些配置项那么查看那么有大概有这么多的配置项啊也可以做一些这个查看
[07:22] 那么也可以去查看我们相关的一些server相关的一些信息那么我可以选中它去做一个查看做一个查看那么在这个里面可以看到一个关键点是不是一个server id它是等于1在前面我们的配置文件中是不是已经把它配置为是1了所以其实可以说明我们配置文件它已经生效了ok好那么到这里我们组的配置就搞定了
[07:48] 那么下面我们来看虫的配置好那么关于这个主库的一个配置我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中通过 Docker 部署并配置一个 MySQL 主库（master），包括创建目录、配置文件、启动容器及验证配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 连接到远程服务器，终端提示符为 root@itcast02:~#，左侧显示 /data 目录结构。
画面 2: 在终端中执行 mkdir /data/mysql/master01 创建目录失败，然后执行 cd /data/mysql/master01 进入目录。
画面 3: 显示 Typora 文档中关于“搭建主库”的步骤，包含创建目录、配置文件、输入内容、启动容器等指令。
画面 4: 在终端中输入并执行了 MySQL 配置文件内容，包括 log-bin 和 server-id。
画面 5: 在 /data/mysql/master01 目录下创建 conf 子目录，执行 chmod 777 * -R 命令，然后进入 conf 目录并创建 my.cnf 文件。
画面 6: 在 conf 目录下编辑 my.cnf 文件，然后执行 Docker create 命令创建 MySQL 容器。
画面 7: 执行 Docker start 命令启动容器，并在终端中查看 MySQL 初始化日志，确认服务已启动。
画面 8: 切换到 Windows 桌面，显示 Navicat Premium 软件的启动界面。
画面 9: 在 Navicat Premium 中连接到 MySQL 服务器（192.168.1.18:3306），并查看 mysql 数据库结构。
画面 10: 显示 Typora 文档中关于“创建同步用户以及授权”的内容，包括 create user、grant replication slave 和 flush privileges 语句。
画面 11: 在 Typora 文档中，显示了因 SQL 模式设置导致的错误提示，以及需要修改 my.cnf 文件的建议。
画面 12: 在终端中执行 Docker logs 命令查看容器日志，确认 MySQL 服务已成功启动并监听 3306 端口。
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
10 Docker create --name percona-master01 -v /data/mysql/master01/data:/var/lib/mysql -v /data/mysql/master01/conf:/etc/my.cnf.d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#启动
11 Docker start percona-master01 && Docker logs -f percona-master01
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
root@itcast02:conf# Docker create --name percona-master01 -v /data/mysql/master01/data:/var/lib/mysql -v /data/mysql/master01/conf:/etc/my.cnf.d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
4b04206b547c37f02d109d068f38c00372175fd2110594a1ce38366034b1f
root@itcast02:conf# Docker start percona-master01 && Docker logs -f percona-master01
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

