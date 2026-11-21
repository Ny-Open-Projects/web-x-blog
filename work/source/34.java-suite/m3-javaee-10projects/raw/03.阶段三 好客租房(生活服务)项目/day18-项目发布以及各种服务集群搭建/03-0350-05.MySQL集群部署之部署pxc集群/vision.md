# 画面线理解：05.MySQL集群部署之部署pxc集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\05.MySQL集群部署之部署pxc集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:10, 01:43, 02:06, 02:27, 02:52, 04:23, 05:27, 05:56, 06:20, 06:40, 07:37, 10:23, 10:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:48:47

1) 这一组画面整体在讲什么（一句话）：
部署 Percona XtraDB Cluster (PXC) 集群，包括创建数据卷、拉取镜像、创建网络和启动多个节点。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 2: 在 SSH 终端中执行 `docker volume create haoke-v5` 和 `docker volume create haoke-v6`，并列出本地卷。
画面 3: 在 SSH 终端中列出 Docker 镜像，显示了 Hyperledger Fabric、Kibana、Elasticsearch 等镜像。
画面 4: 在 SSH 终端中列出 Docker 镜像，显示了 Zookeeper、Percona、Elasticsearch、Redis、MongoDB、Hyperledger Fabric 等镜像。
画面 5: 在 SSH 终端中列出 Docker 镜像，显示了 Kibana、Elasticsearch、Percona、Redis、MongoDB、Hyperledger Fabric 等镜像。
画面 6: 在 SSH 终端中执行 `docker network ls`，并显示了网络列表，包括 `bridge`、`host`、`none`、`pxc-network` 等。
画面 7: 在 SSH 终端中执行 `docker network ls`，并显示了网络列表，包括 `bridge`、`host`、`none`、`pxc-network` 等。
画面 8: 在 SSH 终端中执行 `docker create` 命令，创建多个 PXC 节点，包括 `pxc_node1`、`pxc_node2`、`pxc_node3`、`pxc_node4`。
画面 9: 在 SSH 终端中执行 `docker start pxc_node1 & docker logs -f pxc_node1`，并显示了 PXC 节点的启动日志。
画面 10: 在 SSH 终端中执行 `docker start pxc_node1 & docker logs -f pxc_node1`，并显示了 PXC 节点的启动日志。
画面 11: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 12: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。
画面 13: 在 Navicat Premium 中显示数据库连接，连接到 `192.168.1.18 pxc node03`，并显示了 `test` 数据库。
画面 14: 显示 Typora 文档，内容为部署 PXC 集群的步骤，包括创建数据卷、拉取镜像、创建网络等命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
#创建数据卷（存储路径：/var/lib/docker/volumes）
1 docker volume create haoke-v1
2 docker volume create haoke-v2
3 docker volume create haoke-v3
4 docker volume create haoke-v4
5 docker volume create haoke-v5
6 docker volume create haoke-v6

#拉取镜像
10 docker pull percona/percona-xtradb-cluster:5.7
11 docker tag percona/percona-xtradb-cluster:5.7 pxc

#创建网络
15 docker network create --subnet=172.30.0.0/24 pxc-network
```

画面 2:
```bash
docker volume create haoke-v5
docker volume create haoke-v6
docker volume ls
```

画面 3:
```bash
latest	b023f9be0771	11 months ago	187MB
x86_64-1.1.0	b023f9be0771	11 months ago	187MB
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-ca
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyperledger/fabric-peer
hyperledger/fabric-javaenv
hyperledger/fabric-cenv
hyperledger/fabric-zookeeper
hyperledger/fabric-kafka
hyperledger/fabric-couchdb
hyperledger/fabric-bases
hyperledger/fabric-tools
hyperledger/fabric-orderer
hyper
