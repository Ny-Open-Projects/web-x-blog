# 05.MySQL集群部署之部署pxc集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\05.MySQL集群部署之部署pxc集群【海量资源尽在 ubkz.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来具体实施啊MySQL的集群那么首先呢我们先来部署的是PXC集群那么首先我们去创建这个数据券那么因为我们要去存储数据那么我们要创建的有六个这个数据券那么六个数据券呢我们回头看一下我们的一个规划那么其中呢有四个有四个的是在18这个机器那么有两个呢是在19这个机器
[00:28] 那么我们先把这四个先创建出来那么也就是说这个V1到V4那么它呢在18这台机器那么V5和V6呢是在19这个机器那么我们把这个来拷贝一下那么打开这个18这个机器我们去做一个创建OK好那么四个这个数据券呢就创建好了那么我们可以来查看一下然后呢我们去多了一个key
[00:53] 然后通过LS查看那么目前是不是有四个这个数据卷接下来呢我们把这个五和六呢我们在这个19这个机器上面去做一个创建那么依然我们通过这个命令呢去做一个查看那么可以看到是不是有两个这个数据卷好那么接下来呢去拉取这个镜像那么这个呢应该在我们的这个机器上面是存在的我们去执行一下
[01:20] 那么去执行它去做一个拉取那么这个镜像是存在的没有问题那么19存在吗查看一下这个里面也这个不存在那么让它去拉取一下就好了那么我们来看一下把它呢这个去做一个打一个tag做打一个tag就是PXC方便我们去做一个使用那么其实我们可以看一下在18上面应该是有那么查看一下镜像就知道了那么在这个里面我们来看一下有没有PXC呢
[01:48] 找一下那么PXC你发现是有在这对吧已经有这个PXCOK好那么我们到这个里面来查看一下Docker然后呢我们Images然后呢去查看一下在这个里面呢它有没有有一个叫做PXC的有没有没有吧因为刚刚我们那个5.7的这个Packender是不是去下载下来对吧然后呢我们去给它重新去打一个这个Tag在19上面去打一个这个Tag
[02:17] 那么这样的话呢它就会有了一个PXC这样的一个这个镜像了那么可以看到就是它啊OK好那么我们使用它呢就可以去呃构建我们的PXC集群了好那么我们接着继续往下面看那么接下来呢我们来看一下那么我们要需要创建网络啊除了创建网络那么我们把这个网络呢我们去查看一下那么我们先到这个18里面去查看一下
[02:44] 那么通过这个Docker然后呢Network去查看那么我们可以LS查看一下那么目前呢我们看一下啊我们要创建的这个呢是一个PXC这个Network那么我们目前有没有这个网络呢检查一下是不是已经有这个网络啊所以我们就不需要创建了啊那么19呢它呢不创建这个PXC集群那么我们就不用去创建这个网络了OK好那么接下来呢我们来创建这四个这个节点那么也就两个集群
[03:14] 那我们来看一下这个创建创建我们这个容器的这个命令那么在这个里面呢我们去create去创建一个容器那么这个它的一个这个端口的映射那么前面说过是从这个13306然后到13070809这是前四个这个节点那么这个它数据券的一个挂载数据券的一个挂载OK好没有问题然后这个设置它的
[03:42] root用户的这个密码是root然后呢集群的名字呢是pxc然后呢它的容器的名字呢是pxc node1然后呢网络呢是pxc network这个这个要和我们上面这个要一致啊然后呢指定一个IP地址这个是0.2这个是0.30.40.5哎OK没有问题好那么接下来呢我们把它呢创建出来
[04:09] 第一个我们的这个容器那么是在这个18这个机器上面去做一个执行那么同学们在执行的时候呢一定要看清楚这个机器呢再去做一个执行以免出错那么我们去把它执行一下那么OK这个容器呢就创建好了那么下面呢我们把这个第二个这个节点去创建那么要注意的是在第二个节点中是我们添加了一个叫做
[04:35] cluster join就是加入这个集群的这样的一个参数那么我们加入的是pxc node1也就是说这个参数指向的呢其实就是他哎ok好嘞好那么我们把它呢去来拷贝一下那么到这个里面去做一个执行好嘞那么第二个容器是不是就创建好了那么第二个容器创建好其实这个这两个容器它就能够组建一个集群哎ok好那么接着继续往下面看那我们把
[05:03] 第二个这个集群的第一个这个节点也创建出来然后呢走好创建好了那么下面我们把这个第二个集群的第二个节点呢也创建出来同理呢在第二个节点中呢他所指向的这个集群啊集群这个名字呢其实也是前面所指向的这个名字啊OK好那么我们把它呢卡背过来然后呢到这走
[05:27] 好那么到这里呢我们这个容器呢就创建好了那么我们可以来查看一下啊目前呢我们拥有的有四个这个容器就是PXCNode1到这个Node4啊四个容器那么接下来呢我们来启动啊来启动那么首先我们来启动第一个这个节点那么启动它那么它启动之后呢我们才能够去启动我们的这个第一个集群的第二个这个节点哎OK那么等待它的一个启动
[05:57] 那么我们可以看到他呢正在做一些初始化的一些这个操作那么我们稍微等待一下好那么我们可以看到目前呢这个他正在做一个启动那么稍微等一下他应该就能够启动起来了那我就Ctrl C结束掉啊然后呢我会把这个第二个这个节点呢也跑起来那么把它跑起来同样的我们去
[06:24] 去跑这个第二个集群的第一个这个节点那么要注意每一个集群的第一个这个节点呢你要等待它完全跑起来之后呢再去启动它的其他的节点那么这个呢我们稍微也等一下好那么到这里呢第二个集群的第一个节点呢它就跑起来了那么接下来呢我们把这个第二个集群的第二个节点呢也给它跑起来那么它呢就会加入这个集群中那么接下来呢我们就可以来测试一下
[06:52] 看这两个集群是否是可用的哎OK好嘞好那么我们就来测试一下啊就来测试一下那么我们首先呢先去做一个连接那么在这个里面呢我们去呃新建啊咱们这样那么我们在这个位置吧呃我们应该是新建一个组吧那么这个我们就叫一个部署哎OK那么在这个里面我们创建一个my circle的一个连接
[07:19] 那么它的IP地址是192.168然后我们这个是1.18然后这个PXC然后-Node01这个节点那么它的IP地址就是这个IP地址那么它的端口我们回过来看一下它的端口是不是就是13306那么13306那么root用户的密码也是root用户连接OK连接成功了
[07:45] 那么这个第一个这个就搞定那么我们是不是需要去创建啊多个呀那么我们可以把这个呢去复制一下那么复制这个就是02然后呢这个呢是133013307啊1307测试连接一下没有问题好那么我们再来复制一个那么再来复制一个呢就叫这个node0啊node03然后呢它呢就是13308然后呢测试一下
[08:15] 没有问题好那么这个也搞定那我们再来复制一个那么这个就是node04然后呢这个是13309密码呢同样也是root然后呢去连接测试一下没有问题那么四个节点就搞定了那么前面两个呢这两个呢是一个集群对吧那我们可以来看一下那么在这个里面那么由于他们是做一个强移性同步的那么我们可以做一个测试比如说我创建一个数据库比如说我叫test
[08:42] 随便写一个叫test那么制服级呢我们选择用U8创建一下那么这个里面呢这个数据库就创建好了刷新一下那么你会发现是不是同样做了一个同步那么当然在这个里面它肯定就没有了因为它们并不是一个集群那么这个里面呢我们可以创建一张表那么我们在这个里面去添加一个ID然后呢叫vginter然后呢设置为主件那么这个我们就随意去创建一张表添加一个字段比如说叫name
[09:11] 然后呢长度呢叫100保存一下叫tb然后呢t那么我们随便去创建一张表去做一个测试那么你会发现这个表创建好了那么在这个里面呢我们可以看到这个表同样也创建好了那我们在前面这个里面插入一条数据呢测试一下比如说叫张三
[09:28] 叫张三然后保存一下没有问题那么回到这个里面来查看一下同样也是有张三这个数据的没有问题那就说明我们第一个这个集群是吧OK的那我们就把这个里面的给它去删除掉好嘞那么刷新一下这个里面同样是不是也就删除了没有问题那么第一个集群就搞定了那么来看一下第二个这个集群那么第二个集群同样我们测试方法一样那么新建一个数据库比如说就叫test然后制服体呢同样的也是叫它U8
[09:58] 然后呢我们去测试一下没有问题吧然后这个里面刷新一下同样是没有问题的那么同样的创建一张表这张表呢我们还是随便去写一些东西啊比如说bigint然后呢这个组件然后呢自身找再添加一个字段比如叫name然后呢叫我差100保存然后呢tb然后呢t然后呢保存退出一下那么这样的话呢我们就可以去打开来看一下当然这个里面我们刷新一下啊
[10:26] 没有问题没有问题那么在在我们这个表里面这个表里面呢我们去插过条数据叫李四保存一下没有问题那么回到这个里面来看一下依然是有数据的没有问题那就说明我们这两个集群是不是就已经搭建OK了那么到目前为止呢我们这个部署PXC集群是不是就已经搞定了哎呀OK好那么关于我们这个PXC的集群的一个搭建那么就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
部署 Percona XtraDB Cluster (PXC) 集群，包括创建数据卷、拉取镜像、创建网络和启动多个节点。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 2: 在 SSH 终端中执行 `Docker volume create haoke-v5` 和 `Docker volume create haoke-v6`，并列出本地卷。
画面 3: 在 SSH 终端中列出 Docker 镜像，显示了 Hyperledger Fabric、Kibana、Elasticsearch 等镜像。
画面 4: 在 SSH 终端中列出 Docker 镜像，显示了 Zookeeper、Percona、Elasticsearch、Redis、MongoDB、Hyperledger Fabric 等镜像。
画面 5: 在 SSH 终端中列出 Docker 镜像，显示了 Kibana、Elasticsearch、Percona、Redis、MongoDB、Hyperledger Fabric 等镜像。
画面 6: 在 SSH 终端中执行 `Docker network ls`，并显示了网络列表，包括 `bridge`、`host`、`none`、`pxc-network` 等。
画面 7: 在 SSH 终端中执行 `Docker network ls`，并显示了网络列表，包括 `bridge`、`host`、`none`、`pxc-network` 等。
画面 8: 在 SSH 终端中执行 `Docker create` 命令，创建多个 PXC 节点，包括 `pxc_node1`、`pxc_node2`、`pxc_node3`、`pxc_node4`。
画面 9: 在 SSH 终端中执行 `Docker start pxc_node1 & Docker logs -f pxc_node1`，并显示了 PXC 节点的启动日志。
画面 10: 在 SSH 终端中执行 `Docker start pxc_node1 & Docker logs -f pxc_node1`，并显示了 PXC 节点的启动日志。
画面 11: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 12: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 13: 在 Navicat Premium 中显示数据库连接，连接到 `192.168.1.18 pxc node03`，并显示了 `test` 数据库。
画面 14: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
#创建数据卷（存储路径：/var/lib/Docker/volumes）
1 Docker volume create haoke-v1
2 Docker volume create haoke-v2
3 Docker volume create haoke-v3
4 Docker volume create haoke-v4
5 Docker volume create haoke-v5
6 Docker volume create haoke-v6

#拉取镜像
10 Docker pull percona/percona-xtradb-cluster:5.7
11 Docker tag percona/percona-xtradb-cluster:5.7 pxc

#创建网络
15 Docker network create --subnet=172.30.0.0/24 pxc-network
```

画面 2:
```bash
Docker volume create haoke-v5
Docker volume create haoke-v6
Docker volume ls
```

画面 3:
```bash
latest	b023f9be0771	11 months ago	187MB
x86_64-1.1.0	b023f9be0771	11 months ago	187MB
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-ca
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-ZooKeeper
hyperledger/fabric-Kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyper

