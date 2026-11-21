# 02.使用Docker安装MySQL

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\02.使用Docker安装MySQL【海量资源尽在 ubkz.com】.mp4
- 时长 10分21秒（音频 622s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来通过这个Docker来进行安装我们的MySQL那么前面我们说过,我们这个项目呢,底层呢,所使用的数据库呢,我们使用的是MySQL数据库那么我们也知道,MySQL数据库呢,它是一个非常优秀的一个开源的数据库而这个MySQL呢,又会有很多的一些衍生版本那么什么叫做衍生版呢?
[00:25] 那么简单的给大家来解释一下就是我们知道MySQL它本身是不是开源的那么就会有一些这个个人或者说组织或者说一些企业然后呢会基于MySQL的这个源码的基础之上呢结合自身的一些业务然后呢做一些这种改进然后呢就会形成有很多的一些这个版本那么在众多的这个衍生版本中啊那么有一个版本呢叫做Prayer Counter
[00:51] 那么这个呢是相对比较知名的这样的一个衍生版那么它的性能呢做的也是非常好的也对原生的一个MySQL做了很大的一个改进所以呢我们在本套课程中呢我们选用这个Payakana作为我们的一个MySQL的一个数据库来做一个使用当然了有同学可能会有一个疑惑就是说老师我们是不是要去学习一个新的一个数据库Payakana呢是不是我们会有一些
[01:20] 这个学习的成本那么其实并没有因为这个衍生版它只是在底层做了一些改进那么在使用层面来讲的话和我们使用原本的这个MySQL没有任何的区别这一点大家一定要注意所以说我们不会额外增加太多的这个学习成本基本上也就没有什么学习成本那么如果你本身对MySQL比较熟悉的话
[01:44] 那么并且我们这种部署的形式我们采用的是Docker这种形式容器化这种形式就做一个部署OK那么下面我们来看一下那么什么是这个Prior Candle那么给大家来简单的介绍一下来看一下那Prior Candle是MySQL数据库服务器进行了一个改进在功能和性能上叫MySQL的有显著的一个提升那么你可以看到是不是有性能方面有很大的提升OK
[02:13] 所以说所以说我们在选择这个MySQL的时候我们尽可能的去选择它的一些衍生版然后呢去得到更高的这样的一个性能啊哎OK你看他说该版本呢这个提升了啊高负载情况下的inoDB的一个性能我们知道这个inoDB是不是MySQL下面最常用也就是它现在的一个默认的一个传输引擎啊
[02:37] 包括为DBA提供了一些非常有用的性能的诊断工具等等也就是说它比官方的MySQL是不是有很大的性能提升功能方面也有了一些提升OK那么需要大家注意的是Private Counter Server只是包含了MySQL服务器的版本并没有对MySQL的一些这种客户端
[03:00] 一些GUI这些工具做一些改进并没有做改进所以说当然了我们一般来讲我们只需要他的服务端是不是就可以了ok那么你客户端就会使用他官方提供的客户端就可以了或者说我们会使用一些第三方的客户端来做一些使用那么这个是他的一个官网大家如果感兴趣的话可以去到官网去阅读一下去查看一下他相关的信息ok
[03:29] 好 那么这个就是对于Precana的一个简单的一个介绍好 那么下面我们对它做一个部署做一个安装那么我们采用这个Dark的形式那么我们先得去拉取这个镜像那么通过这个命令是不是破一个Precana冒号5.7.23那么也就是说我们所采用的Precana的版本是5.7.23这个版本
[03:54] OK那么他所对应的MySQL的版本那就5.7这个版本跟他一样的OK那我们来看一下其实我在这个位置是不是已经已经把这个Procanner5.7.23这个版本是不是已经拉取到我的一个本地镜像文件是不是已经拉取下来了好那么接下来我就需要给他创建一个容器这个镜像我就不给大家演示了那么大家在联网的状态下
[04:20] 通过输入这个命令我相信他跟我拉到的这个镜像是一样的哎呀OK好那么我们接下来创建一个这个容器我们把这个内容来靠一下然后呢我们来打开一个文件先把它丢到这个里面来我们先来看一下这个命令那么通过这个不要有回车啊不要有回车哎OK那我们来看一下那么Docker Creator是不是去创建一个容器
[04:48] 然后杠杠内模是不是指定我们这个容器的名字叫PairCanner然后呢杠V注意这个杠V呢是指的是我们的做一个这个数据文件的一个映射那么前面的这个呢是指的我们在外面的这个机器就是我外部的这个机器它的一个目录然后呢映射到
[05:08] 这个数据库里面的一个文件的一个这个目录啊做一个这样的一个映射啊做一个映射那么也就是说在容器的内部是不是当容器内部往这个目录下面去写内容的时候它会自动是不是会写到这个目录下面来那么也就是说我们是不是把这个数据和我们的一个容器做一个分离这个大家一定要理解啊就是说
[05:32] 我们可以看到现在啊就是说这个是我们的整个的一个服务器对吧然后在服务器的内部呢又有这样的一个容器又有个我们这个Docker这个容器对不对这个容器是不是仅仅是运行着我们的一个镜像对吧但是在这个容器中它要不断的是不是有一些数据的产生但是我们不能把这个数据是不是写到容器的内部而是需要把这个容器把这个数据呢写到容器的外部所以我们通过这种方式
[06:00] 通过这种方式对吧那么这个是不是就是我们外部的某一个这个目录然后呢后面的这个呢是容器内的一个目录那么它呢就代表的是它然后呢我们的容器往这个里面去写内容的时候其实它就会映射的写到这个里面来那么同样的一个目录在这哎OK就这样的一个意思啊然后后面呢看一下这样的一个参数叫杠P是不是指定一个端口的一个映射
[06:27] 前面这个是目录的映射后面这个是一个端口的映射ok好那我来看一下这么更硬的是设置它的一些环境变量就是容器内部的一个环境变量那么设置我mycircle root的一个密码是密码就是root密码就是root然后后面指定的是我们这个镜像ok好那么下面我们把这个mini call过来来运行一下看一下效果大了在运行之前我们先来检查一下这个目录就是我们本地的目录
[06:56] 那么LL查看一下LL把这个贴过来查看一下那么其实我们可以发现这个下面本身是不是有内容那么因为之前的我安装过我这个mysock所以呢这样我把这个目录给它删除掉把这个目录删掉好那么再去查看一下那么这个目录显然是不是就不存在了好那么我接下来呢就把它呢去创建这样的一个容器
[07:21] 好那么我们可以看到这个容器是不是已经创建好了那么创建好之后我是不是就可以把它启动起来那么我先来看一下刚刚的这个目录有没有生成这个目录是不是并没有生成因为我们只是创建了容器还没有去运行容器所以这个目录并不会创建好那么接下来我们来去启动我们这个容器是不是叫Project CanerC-O-N-A
[07:47] 然后我们来启动这个容器好那么我们发现这个容器它已经启动了我们来查看一下ps来看一下那么我们可以看到在这个位置这个PriorityKana5.7.23这个容器它已经启动了并且它可以看到它的一个端口的一个映射那么我们是不是可以来检查一下那么这个目录下面有没有内容ok你发现这个目录是不是也就
[08:11] 自动创建好了对吧这个里面就是我们其实如果我们对MySQL它的一些底层的这个文件比较熟悉的话那我们其实可以看到这个呢本身就是MySQL的一个数据库的一个存储文件的一个目录对不对OK好那么到这儿呢我们就已经把这个MySQL呢就安装好了那么我们接下来我们来测试一下我们是否能够通过远程的工具去连接到它
[08:36] 然后我们来打开一个工具这个工具我写过叫NeoCAD这个工具打开看一下那么通过这个工具我们来测试一下那么在这创建一个连接这样我把这个连接删除掉然后我们来新建一个连接叫MySQL的连接那么这个连接名就是跟我的这个IP地址一样就可以了那么叫什么来看一下
[09:01] 就叫172.16.55.185然后呢他主机地址呢也是这个地址然后他的密码呢是3306然后呢注意root用户名还是root密码我们是不是通过刚刚的一个环境变量是不是设置了他的一个这个密码是root所以呢我们在这个位置给他去填一个什么呢填一个这个root
[09:27] 然后点击连接做一个测试可以发现是不是已经连接成功了我们点击确定OK好那么可以看到是不是我们已经成功的连接到我们这个数据库OK好那么我们继续往下面看是不是通过我们
[09:44] 这样的一个创建容器然后呢我们去启动容器那我们这个数据库是不是已经部署完成了所以说使用这个Docker的部署是非常简单的啊OK那么刚刚我们是不是对这个参数是不是也给大家做了一些这个
[09:58] 解释ok好那么到他就连接成功了那么我们现在是不是就已经为我们后面的是不是做了一个准备对吧那么我们数据库已经有了那么下面我们是不是就可以进入数据库来做一些我们的开发了ok好那么关于使用Docker来安装部署MySQL或者说安装部署Project Kena衍生版我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
使用 Docker 容器化方式部署 Percona 版本的 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档内容，介绍 Percona 是 MySQL 的增强版本，采用 Docker 部署。列出 Docker 拉取和创建容器的命令：Docker pull percona:5.7.23 和 Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23。
画面 2: 在终端中执行 Docker stop percona 和 Docker rm percona 停止并删除容器。接着执行 Docker ps -a 查看容器状态，显示 percona 容器已停止。执行 Docker images 查看镜像列表，包含 ZooKeeper:3.5 和 percona:5.7.23。
画面 3: 展示 PDF 文档内容，详细解释 Docker 创建容器命令的参数：-name、-v、-p、-e。
画面 4: 终端中执行 Docker stop percona 和 Docker rm percona 停止并删除容器。执行 Docker ps -a 查看容器状态，显示 percona 容器已停止。执行 Docker images 查看镜像列表，包含 ZooKeeper:3.5 和 percona:5.7.23。
画面 5: 终端中执行 Docker stop percona 和 Docker rm percona 停止并删除容器。执行 Docker ps -a 查看容器状态，显示 percona 容器已停止。执行 Docker images 查看镜像列表，包含 ZooKeeper:3.5 和 percona:5.7.23。
画面 6: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示目录为空。
画面 7: 在 EdiPlus 编辑器中，显示创建容器的命令：Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23。
画面 8: 在终端中执行 rm -rf /data/mysql-data 删除目录，提示目录不存在。接着执行 Docker create 命令创建容器，然后执行 Docker start percona 启动容器。
画面 9: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示 MySQL 相关文件和目录，如 mysql、performance_schema、sys 等。
画面 10: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示 MySQL 相关文件和目录，如 mysql、performance_schema、sys 等。
画面 11: 展示文件资源管理器，显示 Navicat Premium 的安装文件夹，包含 Navicat Premium 的可执行文件。
画面 12: 展示 PDF 文档内容，详细解释 Docker 创建容器命令的参数：-name、-v、-p、-e。
画面 13: 展示 PDF 文档内容，显示连接属性窗口，主机地址为 172.16.55.185，端口为 3306。
画面 14: 展示 PDF 文档内容，介绍 Percona 是 MySQL 的增强版本，采用 Docker 部署。列出 Docker 拉取和创建容器的命令：Docker pull percona:5.7.23。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
#镜像地址：https://hub.Docker.com/_/percona/
#拉取镜像
Docker pull percona:5.7.23
#创建容器
Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#参数解释
--name percona 指定容器的名称
-v /data/mysql-data:/var/lib/mysql 将主机目录/data/mysql-data挂载到容器的/var/lib/mysql上
-p 3306:3306 设置端口映射，主机端口是3306，容器内部端口3306
-e MYSQL_ROOT_PASSWORD=root 设置容器参数，设置root用户的密码为root
percona:5.7.23 镜像名:版本
#启动容器
Docker start percona

画面 3:
#镜像地址：https://hub.Docker.com/_/percona/
#拉取镜像
Docker pull percona:5.7.23
#创建容器
Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#参数解释
--name percona 指定容器的名称
-v /data/mysql-data:/var/lib/mysql 将主机目录/data/mysql-data挂载到容器的/var/lib/mysql上
-p 3306:3306 设置端口映射，主机端口是3306，容器内部端口3306
-e MYSQL_ROOT_PASSWORD=root 设置容器参数，设置root用户的密码为root
percona:5.7.23 镜像名:版本
#启动容器
Docker start percona

画面 7:
Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

画面 8:
root@bitcast:~# rm -rf /data/mysql-data
ls: cannot access '/data/mysql-data': No such file or directory
root@bitcast:~# Docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
a801fcb82204ff995391a5u16f3b5d1cc7f4bchce1c2325b7b7612d2416
root@bitcast:~# Docker start percona

画面 9:
root@bitcast:~# ls -l /data/mysql-data
total 192324
drwxr-x--- 2 999 999 4096 Nov 15 11:46 ./
drwxr-x--- 2 999 999 4096 Nov 15 11:46 ../
-rw-r----- 1 999 999 56 Nov 7 17:52 auto.cnf
-rw-r----- 1 999 999 1680 Nov 7 17:52 ca-key.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 ca.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 client-cert.pem
-rw-r----- 1 999 999 1339 Nov 7 17:52 client-key.pem
-rw-r----- 1 999 999 79631776 Nov 15 11:46 ibdata1
-rw-r----- 1 999 999 50331648 Nov 15 11:46 ib_logfile0
-rw-r----- 1 999 999 50331648 Nov 15 11:46 ib_logfile1
-rw-r----- 1 999 999 1676 Nov 7 17:52 mysql/
-rw-r----- 1 999 999 1676 Nov 7 17:52 performance_schema/
-rw-r----- 1 999 999 452 Nov 7 17:52 private_key.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 public_key.pem
-rw-r----- 1 999 999 1676 Nov 7 17:52 server-cert.pem
-rw-r----- 1 999 999 1676 Nov 7 17:52 server-key.pem
-rw-r----- 1 999 999 12288 Nov 7 17:52 sys/
-rw-r----- 1 999 999 12288 Nov 15 11:4

