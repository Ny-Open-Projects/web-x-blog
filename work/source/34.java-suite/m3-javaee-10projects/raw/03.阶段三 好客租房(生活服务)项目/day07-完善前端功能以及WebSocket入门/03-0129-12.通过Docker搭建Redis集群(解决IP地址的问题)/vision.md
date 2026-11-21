# 画面线理解：12.通过Docker搭建Redis集群（解决IP地址的问题）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\12.通过Docker搭建Redis集群（解决IP地址的问题）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:09, 02:40, 02:59, 04:12, 04:27, 04:36, 04:50, 04:58, 05:15, 05:45, 05:56, 06:30, 06:37, 06:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:25:51

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 创建并配置 Redis 集群，包括容器网络模式选择、容器启动、集群初始化和节点验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，讲解 Docker 网络类型，包括 None、Container、Host 和 Bridge 模式。
画面2：展示 PPT 图形，说明容器内 eth0 网卡与主机 eth0 网卡共享 IP 地址 10.0.7.197。
画面3：展示 EditPlus 编辑器中的 Docker 命令，用于创建和启动三个 Redis 容器节点。
画面4：展示 PDF 文档内容，列出用于查看容器 IP、删除容器、清理数据目录和进入容器执行集群创建命令的步骤。
画面5：展示 PDF 文档内容，列出删除容器和清理数据目录的命令。
画面6：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面7：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面8：展示 PDF 文档内容，列出启动容器、进入容器执行操作和主机 IP 地址 172.16.55.185 的说明。
画面9：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面10：展示 Xshell 终端，执行 docker start 启动容器，然后进入 redis-node01 容器执行 redis-cli 命令创建集群。
画面11：展示 Xshell 终端，显示集群创建过程，包括槽位分配、配置确认和节点加入。
画面12：展示 PDF 文档内容，列出启动容器、进入容器执行操作和主机 IP 地址 172.16.55.185 的说明。
画面13：展示 Xshell 终端，执行 redis-cli 命令查看集群节点信息。
画面14：展示 PDF 文档内容，列出查看集群信息的命令，同时终端显示了集群节点的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```
docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf
docker start redis-node01 redis-node02 redis-node03
docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
redis-cli --cluster create 172.16.55.185:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
docker create --name redis-node01 -net host -v /data/redis-data/node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
docker create --name redis-node02 -net host -v /data/redis-data/node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面4：
```
docker inspect redis-node01 -> 172.17.0.4
docker inspect redis-node02 -> 172.17.0.5
docker inspect redis-node03 -> 172.17.0.6

#删除容器
docker stop redis-node01 redis-node02 redis-node03
docker rm redis-node01 redis-node02 redis-node03
rm -rf /data/redis-data

#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.4:6379 172.17.0.5:6379 172.17.0.6:6379 --cluster-replicas 0
```

画面5：
```
#删除容器
docker stop redis-node01 redis-node02 redis-node03
docker rm redis-node01 redis-node02 redis-node03
rm -rf /data/redis-data

#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.4:6379 172.17.0.5:6379 172.17.0.6:6379 --cluster-replicas 0
```

画面6：
```
docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面7：
```
docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面8：
```
#启动容器
docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
docker exec -it redis-node01 /bin/bash

172.16.55.185是主机的ip地址
```

画面9：
```
docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面10：
```
root@itcast:~# docker start redis-node01 redis-node02 redis-node03
redis-node01
redis-node02
redis-node03
root@itcast:~# docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.16.55.185:6379 172.16.55.185:6380 172.16.55.185:6381 --cluster-replicas 0
```

画面11：
```
>>> Performing hash slots allocation on 3 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
M: 544e237d0cb57ab921e7f1e6ca4b980a3fc7b 172.16.55.185:6380
slots:[0-5460] (5461 slots) master
slots:[5461-10922] (5461 slots) master
slots:[10923-16383] (5461 slots) master
Can I set the above configuration? (type 'yes' to accept) : yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
```

画面12：
```
#启动容器
docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
docker exec -it redis-node01 /bin/bash

172.16.55.185是主机的ip地址
```

画面13：
```
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
>>> Performing Cluster Check (using node 172.16.55.185:6379)
M: d59f1dd9
