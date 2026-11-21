# 22.综合应用之部署PXC集群（2个集群）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\22.综合应用之部署PXC集群（2个集群）【海量资源尽在 ubkz.com】.mp4
- 时长 7分38秒（音频 458s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来部署我们的PXC集群那么我们要部署两个集群一个是集群一,一个是集群二集群一呢,是13306和13307这两个我们刚刚是不是已经部署好了,对吧?
[00:12] 哎,OK,那么我们来检查一下刚刚的这个呢,它已经OK了,有三个这个节点那么我们这个里面呢,有一个数据库,也有一个表那我们把这个表呢,先删除掉因为我们呢,前面说过,在PXC集群中呢我们所存储的是房源的数据所以呢,我们把这个广告这个表呢,我们先删除掉
[00:30] 删除然后下面所对应的他们的肯定也就全部都删除掉了对吧没有了然后检查一下那么这个也就被删除了刷新一下ok没有问题好那么接下来我们来部署我们的第二个节点第二个集群那么第二个集群所在用的端口是13308和13309ok好那么我们先把这个这样我们我们这样吧我们把这个容器我们就重新再创建一下
[00:56] 那么我们把它就先停止掉那么目前跑的有三个容器那么我们把它先stop掉那么PXNode1Node2然后Node3把它删掉把它stop掉然后再把它remote掉不remote也可以那么如果你想把它删除也OK没有问题那么把它停止掉然后我就把它删掉如果我们需要的话再去做一个创建remoteok好嘞
[01:25] 然后我们来看一下他们四个节点每一个都是他们有一个数据有这样的一个数据数据区那么我们把这四个给他就创建出来创建出来OK好那么然后我们下面去做我们的一个集群的一个搭建那么首先创建这个网络这个网络我们本身就有所以就不再创建了然后我们这个是第一个集群这个节点13306
[01:52] 拷贝过来那么要注意的是呢在这个位置呢我们可以看到它的一个指定的一个这个目录挂载呢是浩克v1ok然后呢我们去执行好这第一个就搞定那么第二个呢添加了一个classclusterjoin这样的一个参数那么这个是13307搞定然后呢这个是集群1就搞定了那么下面看集群2那我把这个集群2它的端口呢是13308
[02:19] 然后呢他的这个数据券呢是浩克V3哎OK好然后呢我们把它呢就拷贝过来到这然后呢创建没有问题然后呢这个呢是我们第二个集群中的第二个这个节点那么是V4哎OK好那么就创建OK了好那么下面我们先来做一个启动要注意的是每一个集群先启动什么呢第一个这个节点那我们把这个第一个跑起来走那么等待他的一个执行
[02:48] 好那么现在呢就跑起来了我们来测试一下啊那么我们进入到我们这个3306这个里面来那么来我们就这样吧把这个连接的先关掉啊也是13306和13307是1和2这个没有问题这个没有问题这个有点问题我们来检查一下啊这个是啊这个我们还没有启动那么我们只是启动了一个对吧只是启动了一个好那我们来启动我们的第二个这个节点把第二个节点呢也跑起来
[03:16] 那么等到第一个节点启动完成之后呢我们才能够去启动第二个这个节点那么我们来尝试的去打开一下看是否能够打开呢走那么还不能够打开那么还没有完全的启动起来那我们来看一下等待它的一个启动那我们再来测试一下
[03:34] 还不行那我们稍微等一下好我们看到了第二个节点呢它就已经跑起来了那么也就可以打开了啊ok好没有问题那么接下来呢我们来启动我们的第二个这个集群先把第二个集群中的第一个这个节点呢先跑起来走那么然后呢我们来创建一个连接啊那么我们呃这么来玩吧我们再来创建一个呃叫做192.1681.18然后呢横杠
[04:01] 然后呢我们来个new pxc-2加个2然后来一个node1然后呢我们来看一下这个呢把它就拷贝过来然后呢它的端口呢是13308对吧我们简单一下啊它的这个是13308这个是13309然后呢密码呢也是root测试一下没有问题好那么现在呢这个就ok了那么接下来呢我们就可以把
[04:32] 这个第二个集群中的第二个这个节点也跑起来了那么到这个位置来跑一下走好那么我们等待它的一个启动那么启动之后呢我们可以查看它集群的一个数量啊那么我们先进入我们的第一个这个集群就是这个node这个px1啊这个里面我们去查看一下它的一个集群的一个节点数量你会发现数量呢是不是等于2啊没有问题ok的好那么我们来等待它的一个启动
[05:01] 那么我们需要稍微等一下集群二中的第一个这个节点搞定了我们这样我们来创建一个连接就是我连接到第二个这个节点1681.18-newpxc2下面的node2然后它的端口这个Ibd整的是它端口是1330913309然后密码的同样也是root然后能联接测试一下没有问题连接成功了
[05:30] OK好那么我们在这个里面呢也去做一个查询查询它的一个这个就是节点的一个数量啊咱们把这个的拷贝过来然后在这个里面去做一个知情走那么你会发现节点数量的也是二没有问题好这样的话呢我们是不是已经分别呢把两个这个集群一和集群二全部都已经跑起来了那么跑起来之后呢我们就去创建一个数据库叫浩克这个数据库啊那我们在这个里面出来做一个创建创建数据库叫浩克
[06:00] 然后它的制服级我们把它设置为是一个U8我们来设置一下U8搞定好那么这个里面就搞定了那么这个里面就有没有刷新一下有那么这个里面有没有注意来看一下它肯定没有因为这两个是两个集群对不对所以在这个里面也需要再创建一个数据库叫浩克然后制服级叫做什么UTF8然后保存然后这个里面保存来刷新一下好这样的话我们是不是就已经
[06:29] 在两个集群中把这个数据库都创建好了接下来呢我们来创建这个表那么把这个房源表拷贝过来创建一下Ctrl C我们还是进入到这个里面吧来执行一下那么这个里面呢走那么这个表就OK了没有选中数据库这个是我们要选中它再去做一个执行到这个里面走执行这样的话就OK了然后呢这个表我们检查一下有
[06:59] 那么这个里面有没有表呢有没有问题把它呢就折起来然后呢进入到第一个这个集群里面呢没有这个表那么我们来去创建一个这个表搞定那么刷新一下再刷新一下表已经就有了
[07:14] 然后下面这个有没有来看一下他同样做了个同步也有了ok没有任何问题好那么到这里我们是不是就已经完成了一个我们的PXC的一个集群并且我们创建了数据库以及这个表那么一会儿我们是不是就可以去操作真正的数据去做一个测试了ok好那么关于这个部署两个集群的一个PXC集群那么就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
部署一个由四个节点组成的PXC（Percona XtraDB Cluster）集群，包括创建数据卷、网络、拉取镜像、启动容器并验证集群状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PXC集群部署文档，包含集群一和集群二的节点配置表，以及创建数据卷的Docker命令。
画面2：文档中集群一和集群二的节点配置表，以及创建数据卷的Docker命令。
画面3：终端显示PXC容器已启动，执行了Docker ps命令查看容器状态。
画面4：文档中展示创建网络和启动第一个节点的Docker命令。
画面5：文档中展示创建第二个节点的Docker命令，包含CLUSTER_JOIN参数。
画面6：终端执行创建数据卷和启动三个PXC节点的Docker命令。
画面7：终端显示PXC服务启动日志，包括版本信息和集群初始化状态。
画面8：终端显示PXC集群状态转移日志，从JOINER到SYNCD。
画面9：文档中展示启动第三个节点的Docker命令。
画面10：终端显示PXC集群状态转移日志，从JOINER到SYNCD。
画面11：Navicat界面显示PXC集群的架构图，包含多个节点和数据卷。
画面12：Navicat界面显示PXC集群的状态信息，包括集群ID、大小、状态等。
画面13：Navicat界面显示PXC集群的数据库结构。
画面14：文档中展示创建房屋资源表的SQL语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
• 部署了2个PXC集群节点，作为2个Mycat分片，每个PXC集群中有2个节点，作为数据的同步存储
• 部署了1个主从复制集群
• 序列号数据存储到PXC分片中，其余数据保存到主从架构中
7.2、部署PXC集群
集群一：
节点    端口    容器名称    数据卷
node1    13306    pxc_node1    haoke-v1
node2    13307    pxc_node2    haoke-v2
集群二：
节点    端口    容器名称    数据卷
node3    13308    pxc_node3    haoke-v3
node4    13309    pxc_node4    haoke-v4
#创建数据卷（存储路径：/var/lib/Docker/volumes）
1 Docker volume create haoke-v1
2 Docker volume create haoke-v2
3 Docker volume create haoke-v3
4 Docker volume create haoke-v4
#拉取镜像
5 Docker pull percona/percona-xtradb-cluster:5.7
```

画面4：
```
#创建网络
11 Docker network create --subnet=172.30.0.0/24 pxc-network
#创建容器
15 Docker create -p 13306:3306 -v haoke-v1:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node1 --net=pxc-network --ip=172.30.0.2 pxc
#第二节点（增加了CLUSTER_JOIN参数）
18 Docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node2 --net=pxc-network --ip=172.30.0.3 pxc
```

画面5：
```
#第三节点（增加了CLUSTER_JOIN参数）
24 Docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node3 --net=pxc-network --ip=172.30.0.4 pxc
#第四节点（增加了CLUSTER_JOIN参数）
27 Docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node4 --net=pxc-network --ip=172.30.0.5 pxc
#启动
28 Docker start pxc_node1 && Docker logs -f pxc_node1
30 Docker start pxc_node3 && Docker logs -f pxc_node3
32 Docker start pxc_node4 && Docker logs -f pxc_node4
#查看集群状态
35 show status like 'wsrep_cluster%';
```

画面14：
```
CREATE TABLE `tb_house_resources` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL COMMENT '房源标题',
  `estate_id` bigint(20) DEFAULT NULL COMMENT '楼盘id',
  `building_num` varchar(5) DEFAULT NULL COMMENT '楼号',
  `building_unit` varchar(5) DEFAULT NULL COMMENT '单元号',
  `building_floor_num` varchar(5) DEFAULT NULL COMMENT '楼层号',
  `rent` int(11) DEFAULT NULL COMMENT '租金',
  `rent_method` tinyint(1) DEFAULT NULL COMMENT '租借方式：1-整租，2-合租',
  `house_type` varchar(25) DEFAULT NULL COMMENT '户型：2室1厅1卫',
  `covered_area` varchar(10) DEFAULT NULL COMMENT '建筑面积',
  `use_area` varchar(10) DEFAULT NULL COMMENT '使用面积',
  `orientation` varchar(2) DEFAULT NULL COMMENT '朝向：东、南、西、北',
  `decoration` tinyint(1) DEFAULT NULL COMMENT '装修：1-精装，2-简装，3-毛坯',
  `facilities` varchar(20) DEFAULT NULL COMMENT '设施：1-电梯，2-空调，3-暖气',
  `pic` varchar(1000) DEFAULT NULL COMMENT '图片',
  `pic_desc` varchar(200) DEFAULT NULL COMMENT '联系人',
  `contact` varchar(11) DEFAULT NULL COMMENT '手机号',
  `mobile` varchar(11) DEFAULT NULL COMMENT '手机',
  `payment_method` tinyint(1) DEFAULT NULL COMMENT '支付方式：1-付一押一，2-付三押一，3-付四押二',
  `house_status` tinyint(1) DEFAULT NULL COMMENT '状态：1-在售，2-已售，3-已租',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `delete_flag` tinyint(1) DEFAULT '0' COMMENT '删除标识：0-未删除，1-已删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11：
架构图：包含多个节点，每个节点指向一个数据卷，节点之间通过网络连接。
表格数据：无。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

