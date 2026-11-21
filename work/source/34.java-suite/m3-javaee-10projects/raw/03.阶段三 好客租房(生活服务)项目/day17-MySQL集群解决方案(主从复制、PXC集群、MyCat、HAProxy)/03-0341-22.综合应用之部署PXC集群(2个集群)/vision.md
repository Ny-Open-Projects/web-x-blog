# 画面线理解：22.综合应用之部署PXC集群（2个集群）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\22.综合应用之部署PXC集群（2个集群）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:39, 01:08, 01:43, 02:11, 02:44, 03:10, 03:31, 04:20, 04:47, 05:50, 06:43, 07:03, 07:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:42:12

1) 这一组画面整体在讲什么（一句话）：
部署一个由四个节点组成的PXC（Percona XtraDB Cluster）集群，包括创建数据卷、网络、拉取镜像、启动容器并验证集群状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PXC集群部署文档，包含集群一和集群二的节点配置表，以及创建数据卷的Docker命令。
画面2：文档中集群一和集群二的节点配置表，以及创建数据卷的Docker命令。
画面3：终端显示PXC容器已启动，执行了docker ps命令查看容器状态。
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
#创建数据卷（存储路径：/var/lib/docker/volumes）
1 docker volume create haoke-v1
2 docker volume create haoke-v2
3 docker volume create haoke-v3
4 docker volume create haoke-v4
#拉取镜像
5 docker pull percona/percona-xtradb-cluster:5.7
```

画面4：
```
#创建网络
11 docker network create --subnet=172.30.0.0/24 pxc-network
#创建容器
15 docker create -p 13306:3306 -v haoke-v1:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node1 --net=pxc-network --ip=172.30.0.2 pxc
#第二节点（增加了CLUSTER_JOIN参数）
18 docker create -p 13307:3306 -v haoke-v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node2 --net=pxc-network --ip=172.30.0.3 pxc
```

画面5：
```
#第三节点（增加了CLUSTER_JOIN参数）
24 docker create -p 13308:3306 -v haoke-v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node3 --net=pxc-network --ip=172.30.0.4 pxc
#第四节点（增加了CLUSTER_JOIN参数）
27 docker create -p 13309:3306 -v haoke-v4:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node4 --net=pxc-network --ip=172.30.0.5 pxc
#启动
28 docker start pxc_node1 && docker logs -f pxc_node1
30 docker start pxc_node3 && docker logs -f pxc_node3
32 docker start pxc_node4 && docker logs -f pxc_node4
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
