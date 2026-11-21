# 画面线理解：18.PXC集群之部署安装以及测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\18.PXC集群之部署安装以及测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:51, 02:22, 02:42, 03:26, 04:06, 04:44, 06:55, 08:27, 09:59, 10:57, 11:52, 12:19, 12:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:40:08

1) 这一组画面整体在讲如何使用 Docker 部署一个三节点的 Percona XtraDB Cluster（PXC）。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PXC 架构图，包含应用系统、proxy、中间件、PXC 节点和 MySQL。
画面2: 显示 Docker 命令列表，终端提示符为 root@itcast02:bin#。
画面3: 展示部署安装部分，列出节点信息（node1, node2），并显示创建网络和创建容器的命令。
画面4: 在终端中执行 docker volume create 命令，创建 v1、v2、v3 三个卷，并列出 /var/lib/docker/volumes 目录内容。
画面5: 在终端中执行 docker pull 命令拉取 percona/percona-xtradb-cluster:5.7 镜像，并显示镜像列表。
画面6: 在终端中执行 docker tag 命令，将拉取的镜像重命名为 pxc。
画面7: 展示部署安装的代码，包含创建卷、拉取镜像、重命名镜像、创建网络、创建第一个节点和第二个节点的命令。
画面8: 在终端中执行 docker network create 命令创建网络，然后执行 docker create 命令创建第二个节点，但提示网络已存在。
画面9: 在 Navicat Premium 中配置连接到 192.168.1.18-pxc-node1，端口 3306，用户名 root。
画面10: 在终端中查看 MySQL 日志，显示 PXC 集群启动过程，包括 SST 完成、JOINER 加入集群、同步完成等。
画面11: 在 Navicat Premium 中连接到 192.168.1.18-newpxc-node1，显示数据库结构。
画面12: 在 Navicat Premium 中连接到 192.168.1.18-newpxc-node2，显示数据库结构。
画面13: 在 Navicat Premium 中连接到 192.168.1.18-newpxc-node3，显示数据库结构。
画面14: 展示集群说明，包含数据表结构和数据记录。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
```
#创建卷
docker volume create v1
docker volume create v2
docker volume create v3

#拉取镜像
docker pull percona/percona-xtradb-cluster:5.7

#重命名
docker tag percona/percona-xtradb-cluster:5.7 pxc

#创建网络
docker network create --subnet=172.30.0.0/24 pxc-network

#第一节点
docker create -p 13306:3306 -v v1:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node1 --net=pxc-network --ip=172.30.0.2 pxc

#第二节点（增加了CLUSTER_JOIN参数）
docker create -p 13307:3306 -v v2:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node2 --net=pxc-network --ip=172.30.0.3 pxc

#第三节点（增加了CLUSTER_JOIN参数）
docker create -p 13308:3306 -v v3:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --name=pxc_node3 --net=pxc-network --ip=172.30.0.4 pxc

#查看节点状态
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: PPT 标题为“6.2、架构”，架构图包含应用系统、proxy、中间件、PXC 节点和 MySQL。
画面3: PPT 标题为“6.3、部署安装”，表格包含节点、端口、容器名称和数据卷。
画面14: PPT 标题为“6.5、集群的说明”，表格包含数据记录。

5) 无。
